from dataclasses import dataclass


@dataclass(frozen=True)
class StringLiteral:
    value: str


@dataclass(frozen=True)
class SayStatement:
    expression: StringLiteral
