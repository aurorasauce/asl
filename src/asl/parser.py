from .ast import SayStatement, StringLiteral
from .tokens import Token, TokenType


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self) -> list[SayStatement]:
        statements: list[SayStatement] = []

        while not self._check(TokenType.EOF):
            statements.append(self._parse_say_statement())

        return statements

    def _parse_say_statement(self) -> SayStatement:
        self._consume(TokenType.SAY, "expected 'say'")
        string_token = self._consume(
            TokenType.STRING,
            "expected a string after 'say'",
        )
        self._consume(TokenType.SEMICOLON, "expected ';' after string")

        return SayStatement(StringLiteral(string_token.lexeme))

    def _consume(self, token_type: TokenType, message: str) -> Token:
        if self._check(token_type):
            token = self.tokens[self.current]
            self.current += 1
            return token

        token = self.tokens[self.current]
        raise SyntaxError(f"line {token.line}: {message}")

    def _check(self, token_type: TokenType) -> bool:
        return self.tokens[self.current].type == token_type
