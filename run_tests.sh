#!/usr/bin/env bash
set -uo pipefail

TESTS_REPO="https://github.com/ThatDraenGuy/stella_test_suite.git"
TESTS_DIR="tests/stella_test_suite"
STAGE="stage1"
REFRESH_TESTS=0

SKIP_EXTENSIONS="structural-patterns|letrec-bindings"
should_skip_file() {
    grep -q '#letrec-bindings' "$1" && return 0
    grep -q '#structural-patterns' "$1" && grep -q '#let-patterns' "$1" && return 0
    return 1
}

usage() {
    cat <<EOF
Usage: $0 [path/to/stella_typechecker | --docker] [--stage stage1|stage2|stage3] [--refresh-tests]

Examples:
  $0
  $0 ./build/stella_typechecker --stage stage2
  $0 --docker --stage stage3 --refresh-tests
EOF
}

tests_branch_for_stage() {
    case "$1" in
        stage3) echo "stage3" ;;
        *) echo "main" ;;
    esac
}

if [[ -t 1 ]]; then
    RED=$'\033[0;31m'
    GREEN=$'\033[0;32m'
    YELLOW=$'\033[1;33m'
    NC=$'\033[0m'
    BOLD=$'\033[1m'
else
    RED='' GREEN='' YELLOW='' NC='' BOLD=''
fi

passed=0
failed=0
skipped=0
failures=()

TYPECHECKER=""
POSITIONAL=()
while [[ $# -gt 0 ]]; do
    case "$1" in
        --docker)
            TYPECHECKER="docker run -i stella-typechecker"
            shift
            ;;
        --stage)
            [[ $# -ge 2 ]] || { echo "Missing value after --stage"; usage; exit 1; }
            STAGE="$2"
            shift 2
            ;;
        --refresh-tests)
            REFRESH_TESTS=1
            shift
            ;;
        --help|-h)
            usage
            exit 0
            ;;
        *)
            POSITIONAL+=("$1")
            shift
            ;;
    esac
done

if [[ -z "$TYPECHECKER" ]]; then
    if [[ ${#POSITIONAL[@]} -gt 0 ]]; then
        TYPECHECKER="${POSITIONAL[0]}"
    elif [[ -x "build/stella_typechecker" ]]; then
        TYPECHECKER="./build/stella_typechecker"
    else
        usage
        echo "Or build the project first so ./build/stella_typechecker exists."
        exit 1
    fi
fi

TESTS_BRANCH="$(tests_branch_for_stage "$STAGE")"

if [[ ! -d "$TESTS_DIR" ]]; then
    echo "Cloning test suite branch '$TESTS_BRANCH'..."
    git clone --depth 1 --branch "$TESTS_BRANCH" "$TESTS_REPO" "$TESTS_DIR" || exit 1
else
    current_branch="$(git -C "$TESTS_DIR" rev-parse --abbrev-ref HEAD 2>/dev/null || true)"
    if [[ "$current_branch" != "$TESTS_BRANCH" || "$REFRESH_TESTS" -eq 1 ]]; then
        echo "Switching test suite to branch '$TESTS_BRANCH'..."
        git -C "$TESTS_DIR" fetch --depth 1 origin "$TESTS_BRANCH" || exit 1
        git -C "$TESTS_DIR" checkout -B "$TESTS_BRANCH" FETCH_HEAD > /dev/null || exit 1
    fi
fi

if [[ ! -d "$TESTS_DIR/$STAGE" ]]; then
    echo "Requested stage '$STAGE' was not found in $TESTS_DIR."
    echo "If the remote test suite was updated, rerun with --refresh-tests."
    exit 1
fi

run_well_typed() {
    local dir="$1"
    local label="$2"
    [[ -d "$dir" ]] || return 0

    for f in "$dir"/*.stella "$dir"/*.stela; do
        [[ -f "$f" ]] || continue
        local name="${label}/$(basename "$f")"
        if should_skip_file "$f"; then
            printf "${YELLOW}  SKIP${NC}  %s\n" "$name"
            ((skipped++))
            continue
        fi
        local stderr_out
        stderr_out=$(mktemp)

        if $TYPECHECKER < "$f" > /dev/null 2> "$stderr_out"; then
            printf "${GREEN}  PASS${NC}  %s\n" "$name"
            ((passed++))
        else
            printf "${RED}  FAIL${NC}  %s  (expected exit 0, got non-zero)\n" "$name"
            if [[ -s "$stderr_out" ]]; then
                printf "        stderr: %s\n" "$(head -1 "$stderr_out")"
            fi
            ((failed++))
            failures+=("$name: expected well-typed (exit 0)")
        fi
        rm -f "$stderr_out"
    done
}

run_ill_typed() {
    local dir="$1"
    local label="$2"
    [[ -d "$dir" ]] || return 0

    for error_dir in "$dir"/*/; do
        [[ -d "$error_dir" ]] || continue
        local error_name
        error_name=$(basename "$error_dir")
        local expected_code="ERROR_${error_name^^}"

        for f in "$error_dir"/*.stella "$error_dir"/*.stela; do
            [[ -f "$f" ]] || continue
            local name="${label}/${error_name}/$(basename "$f")"
            if should_skip_file "$f"; then
                printf "${YELLOW}  SKIP${NC}  %s\n" "$name"
                ((skipped++))
                continue
            fi
            local stderr_out
            stderr_out=$(mktemp)

            if $TYPECHECKER < "$f" > /dev/null 2> "$stderr_out"; then
                printf "${RED}  FAIL${NC}  %s  (expected non-zero exit, got 0)\n" "$name"
                ((failed++))
                failures+=("$name: expected error $expected_code but program was accepted")
            else
                if grep -q "$expected_code" "$stderr_out"; then
                    printf "${GREEN}  PASS${NC}  %s\n" "$name"
                    ((passed++))
                else
                    local actual_code
                    actual_code=$(grep -oE 'ERROR_[A-Z_]+' "$stderr_out" | head -1)
                    printf "${RED}  FAIL${NC}  %s  (expected %s, got %s)\n" "$name" "$expected_code" "${actual_code:-<no error code>}"
                    ((failed++))
                    failures+=("$name: expected $expected_code, got ${actual_code:-<no error code>}")
                fi
            fi
            rm -f "$stderr_out"
        done
    done
}

echo ""
echo "${BOLD}=== Mandatory tests ===${NC}"
echo ""
echo "${BOLD}--- Well-typed ---${NC}"
run_well_typed "$TESTS_DIR/$STAGE/well-typed" "well-typed"

echo ""
echo "${BOLD}--- Ill-typed ---${NC}"
run_ill_typed "$TESTS_DIR/$STAGE/ill-typed" "ill-typed"

EXTRA_DIR="$TESTS_DIR/$STAGE/extra"
if [[ -d "$EXTRA_DIR" ]]; then
    echo ""
    echo "${BOLD}=== Extra extension tests ===${NC}"
    for ext_dir in "$EXTRA_DIR"/*/; do
        [[ -d "$ext_dir" ]] || continue
        ext_name=$(basename "$ext_dir")
        if [[ "$ext_name" =~ ^($SKIP_EXTENSIONS)$ ]]; then
            echo ""
            echo "${YELLOW}  SKIP${NC}  #${ext_name} (disabled)"
            ((skipped++))
            continue
        fi
        echo ""
        echo "${BOLD}--- #${ext_name} ---${NC}"
        run_well_typed "$ext_dir/well-typed" "extra/${ext_name}/well-typed"
        run_ill_typed "$ext_dir/ill-typed" "extra/${ext_name}/ill-typed"
    done
fi

echo ""
echo "${BOLD}==============================${NC}"
total=$((passed + failed))
echo -e "  ${GREEN}Passed: ${passed}${NC}  ${RED}Failed: ${failed}${NC}  Total: ${total}"

if [[ ${#failures[@]} -gt 0 ]]; then
    echo ""
    echo "${BOLD}Failed tests:${NC}"
    for f in "${failures[@]}"; do
        echo "  - $f"
    done
fi

echo ""
if [[ $failed -eq 0 ]]; then
    echo -e "${GREEN}${BOLD}All tests passed!${NC}"
    exit 0
else
    echo -e "${RED}${BOLD}Some tests failed.${NC}"
    exit 1
fi
