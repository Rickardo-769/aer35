# number.py
import random
from config import LOWER_BOUND, UPPER_BOUND

class Number:
    def __init__(self) -> None:
        self.secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)

    def check_guess(self, guess: int) -> bool:
        return guess == self.secret_number
