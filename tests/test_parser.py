from asl.ast import SayStatement
from asl.lexer import Lexer
from asl.parser import Parser


def test_parser_creates_say_statement():
    tokens = Lexer('say "Hello";').tokenize()
    statements = Parser(tokens).parse()

    assert len(statements) == 1
    assert isinstance(statements[0], SayStatement)
    assert statements[0].expression.value == "Hello"


def test_parser_rejects_missing_semicolon():
    tokens = Lexer('say "Hello"').tokenize()

    try:
        Parser(tokens).parse()
    except SyntaxError as error:
        assert "expected ';'" in str(error)
    else:
        raise AssertionError("SyntaxError was not raised")
