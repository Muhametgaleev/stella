# Stella Type Checker

Проверка типов (тайпчекер) для языка программирования [Stella](https://fizruk.github.io/stella/).
Реализован на Python 3 с использованием ANTLR 4 для лексического и синтаксического разбора.

## Сборка и запуск через Docker

```bash
docker build -t stella-typechecker .
```

Проверка программы на Stella:

```bash
docker run -i stella-typechecker < program.stella
```

Если программа корректно типизирована, процесс завершится с кодом `0`.

При ошибке типизации в stderr выводится сообщение с кодом ошибки,
процесс завершается с ненулевым кодом.

## Запуск тестов

```bash
./run_tests.sh --docker
./run_tests.sh --docker --stage stage2
./run_tests.sh --docker --stage stage3
```
