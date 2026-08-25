from asl.ast import SayStatement, StringLiteral
from asl.evaluator import Evaluator


def test_evaluator_prints_say_statement(capsys):
    statements = [SayStatement(StringLiteral("Hello"))]

    Evaluator().evaluate(statements)

    captured = capsys.readouterr()
    assert captured.out == "AURORA: Hello\n"
