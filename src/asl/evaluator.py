from .ast import SayStatement


class Evaluator:
    def evaluate(self, statements: list[object]) -> None:
        for statement in statements:
            if isinstance(statement, SayStatement):
                print(f"AURORA: {statement.expression.value}")
                continue

            raise RuntimeError("unknown AST node")
