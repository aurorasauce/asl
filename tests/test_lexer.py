from asl.lexer import Lexer
from asl.tokens import TokenType


def test_lexer_tokenizes_say_statement():
    tokens = Lexer('say "Hello";').tokenize()

    assert [token.type for token in tokens] == [
        TokenType.SAY,
        TokenType.STRING,
        TokenType.SEMICOLON,
        TokenType.EOF,
    ]
    assert tokens[1].lexeme == "Hello"


def test_lexer_ignores_comments():
    tokens = Lexer('# comment\nsay "Hello";').tokenize()

    assert tokens[0].type is TokenType.SAY
