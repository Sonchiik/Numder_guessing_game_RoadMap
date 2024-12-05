import random
import time
import math


best = {1: math.inf, 2: math.inf, 3: math.inf}

def update_best_score(difficulty_level, attempts):
    if attempts < best.get(difficulty_level):
        best[difficulty_level] = attempts
        
def show_best_score():
    text = f"""
    Best score:
    Easy: {best.get(1)} attempts
    Medium: {best.get(2)} attempts
    Hard: {best.get(3)} attempts
    """
    print(text)

def game(difficulty_level):
    selected_number = random.randint(0, 100)
    number_of_attemprts = 0
    print(selected_number)
    level = {1: 10, 2: 5, 3: 3}
    while True:
        if number_of_attemprts < level.get(difficulty_level):
            start_time = time.time()
            guess = int(input("Enter your guess: "))
            number_of_attemprts += 1
            if guess == selected_number:
                elapsed_time = time.time() - start_time
                print(f"Congratulation! You guessed the correct number {selected_number} in {number_of_attemprts} attempts!\nYour took: {elapsed_time:.2f} seconds")
                update_best_score(difficulty_level, number_of_attemprts)
                show_best_score()
                break
            elif guess > selected_number:
                print(f"Incorrect! The number is less than {guess}")
            elif guess < selected_number: 
                print(f"Incorrect! The number is greater than {guess}")
        else:
            print("You lose :(")
            print(f"The correct number was {selected_number}")
            break
        
    print("\nShall we play again? 1-Yes 2-No")
    try: 
        answer = int(input("Enter your answer: "))
        if answer == 1:
            main()
        else:
            return
    except ValueError:
        print("Invalid input. Please enter a number")
    

def main():
    print("""\nPlease select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)""")
    try: 
        difficulty_level = int(input("Enter your choice (1, 2, 3): "))
        if difficulty_level in [1, 2, 3]:
            print("Let's start the game!")
            game(difficulty_level)
        else: 
            print("Incorrect choice")
    except ValueError:
        print("Invalid input. Please enter a number")


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!\n \
    I'm thinking of a number between 1 and 100 \
    ")
    main()