import sys
import os

_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
_GEN_DIR = os.path.join(_SRC_DIR, 'generated')
sys.path.insert(0, _SRC_DIR)
sys.path.insert(0, _GEN_DIR)

from antlr4 import CommonTokenStream, InputStream

try:
    from generated.stellaLexer import stellaLexer
    from generated.stellaParser import stellaParser
except ImportError:
    try:
        from stellaLexer import stellaLexer
        from stellaParser import stellaParser
    except ImportError as e:
        print(
            f"Error: Could not import generated parser. "
            f"Run 'make generate' first.\n{e}",
            file=sys.stderr
        )
        sys.exit(2)

from checker import TypeChecker
from errors import TypeCheckError

def main():
    data = sys.stdin.read()
    input_stream = InputStream(data)
    lexer = stellaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = stellaParser(stream)
    tree = parser.start_Program()

    extensions = set()
    try:
        for ext in tree.x.extensions:
            for name in ext.extensionNames:
                extensions.add(name.text)
    except AttributeError:
        pass

    checker = TypeChecker(extensions)
    try:
        checker.check_program(tree.x)
        sys.exit(0)
    except TypeCheckError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
