
class Feedback:
    def congratulations(self) -> str:
        return "Congratulations! You've guessed the number!"

    def hint(self, guess: int) -> str:
        if guess < self.secret_number:
            return "Too low! Try again."
        else:
            return "Too high! Try again."
