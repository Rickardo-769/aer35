# highscore.py
class HighScore:
    def __init__(self) -> None:
        self.high_score = float('inf')

    def update(self, score: int) -> None:
        if score < self.high_score:
            self.high_score = score

    def get_high_score(self) -> int:
        return self.high_score
