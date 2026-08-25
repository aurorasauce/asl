import argparse

from .evaluator import Evaluator
from .lexer import Lexer
from .parser import Parser


def run_file(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        source = file.read()

    tokens = Lexer(source).tokenize()
    statements = Parser(tokens).parse()
    Evaluator().evaluate(statements)


def main() -> None:
    parser = argparse.ArgumentParser(prog="asl")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("file")

    args = parser.parse_args()

    if args.command == "run":
        run_file(args.file)
