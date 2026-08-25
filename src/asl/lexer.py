from .tokens import Token, TokenType


class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.current = 0
        self.line = 1

    def tokenize(self) -> list[Token]:
        tokens: list[Token] = []

        while self.current < len(self.source):
            char = self.source[self.current]

            if char.isspace():
                if char == "\n":
                    self.line += 1
                self.current += 1
                continue

            if char == "#":
                self._skip_comment()
                continue

            if char == ";":
                tokens.append(Token(TokenType.SEMICOLON, ";", self.line))
                self.current += 1
                continue

            if char == '"':
                tokens.append(self._read_string())
                continue

            word = self._read_word()
            if word == "say":
                tokens.append(Token(TokenType.SAY, word, self.line))
            else:
                raise SyntaxError(
                    f"line {self.line}: unknown keyword '{word}'"
                )

        tokens.append(Token(TokenType.EOF, "", self.line))
        return tokens

    def _skip_comment(self) -> None:
        while self.current < len(self.source):
            if self.source[self.current] == "\n":
                return
            self.current += 1

    def _read_word(self) -> str:
        start = self.current

        while self.current < len(self.source):
            char = self.source[self.current]
            if char.isspace() or char in ';"#':
                break
            self.current += 1

        return self.source[start:self.current]

    def _read_string(self) -> Token:
        self.current += 1
        start = self.current

        while self.current < len(self.source):
            char = self.source[self.current]

            if char == '"':
                value = self.source[start:self.current]
                self.current += 1
                return Token(TokenType.STRING, value, self.line)

            if char == "\n":
                self.line += 1

            self.current += 1

        raise SyntaxError(f"line {self.line}: unterminated string")
