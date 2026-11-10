import random
from typing import Dict, Tuple

class NumberGuessingGame:
    """An advanced object-oriented Number Guessing Game with difficulty tiers and statistics tracking."""
    
    DIFFICULTY_LEVELS: Dict[str, Tuple[int, int, int]] = {
        "1": (1, 50, 7),    # Easy: Range 1-50, 7 attempts
        "2": (1, 100, 10),  # Medium: Range 1-100, 10 attempts
        "3": (1, 500, 12)   # Hard: Range 1-500, 12 attempts
    }

    def __init__(self) -> None:
        self.total_games = 0
        self.games_won = 0
        self.best_score = float('inf')

    def display_welcome(self) -> None:
        print("=" * 55)
        print("         ADVANCED PYTHON NUMBER GUESSING GAME        ")
        print("=" * 55)

    def select_difficulty(self) -> Tuple[int, int, int]:
        print("\nSelect Difficulty Level:")
        print("1. Easy (1 - 50 | 7 Max Attempts)")
        print("2. Medium (1 - 100 | 10 Max Attempts)")
        print("3. Hard (1 - 500 | 12 Max Attempts)")
        
        while True:
            choice = input("Enter choice (1-3): ").strip()
            if choice in self.DIFFICULTY_LEVELS:
                return self.DIFFICULTY_LEVELS[choice]
            print("[ERROR] Invalid selection. Please choose 1, 2, or 3.")

    def play_round(self) -> None:
        low, high, max_attempts = self.select_difficulty()
        secret_number = random.randint(low, high)
        attempts_left = max_attempts
        current_attempts = 0

        print(f"\n[GAME START] I have selected a number between {low} and {high}.")
        print(f"You have {max_attempts} attempts to guess it. Good luck!\n")

        while attempts_left > 0:
            try:
                user_input = input(f"Attempt {current_attempts + 1}/{max_attempts} - Enter your guess: ").strip()
                guess = int(user_input)

                if guess < low or guess > high:
                    print(f"[WARNING] Out of bounds! Enter a value between {low} and {high}.\n")
                    continue

                current_attempts += 1
                attempts_left -= 1

                if guess < secret_number:
                    print(f"Hint: Too low! Attempts remaining: {attempts_left}\n")
                elif guess > secret_number:
                    print(f"Hint: Too high! Attempts remaining: {attempts_left}\n")
                else:
                    self.total_games += 1
                    self.games_won += 1
                    if current_attempts < self.best_score:
                        self.best_score = current_attempts
                    
                    print("=" * 55)
                    print(f" SUCCESS! You found the secret number {secret_number}!")
                    print(f" Statistics: Completed in {current_attempts} attempts.")
                    print("=" * 55)
                    return

            except ValueError:
                print("[ERROR] Invalid data type. Please enter a valid integer.\n")

        self.total_games += 1
        print("=" * 55)
        print(f" GAME OVER! You ran out of attempts. The secret number was {secret_number}.")
        print("=" * 55)

    def run(self) -> None:
        self.display_welcome()
        while True:
            self.play_round()
            replay = input("\nWould you like to play another round? (y/n): ").strip().lower()
            if replay != 'y':
                print(f"\n[SESSION SUMMARY] Games Played: {self.total_games} | Games Won: {self.games_won}")
                if self.best_score != float('inf'):
                    print(f"Best Performance: {self.best_score} attempts.")
                print("Thank you for playing!")
                break

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.run()