# score.py
class Score:
    def __init__(self) -> None:
        self.attempts = 0

    def increment(self) -> None:
        self.attempts += 1

    def get_attempts(self) -> int:
        return self.attempts
