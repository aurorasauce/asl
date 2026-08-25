from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    SAY = auto()
    STRING = auto()
    SEMICOLON = auto()
    EOF = auto()


@dataclass(frozen=True)
class Token:
    type: TokenType
    lexeme: str
    line: int
