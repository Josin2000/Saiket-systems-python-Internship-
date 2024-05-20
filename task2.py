import random

def guess_the_number():
    print("Welcome to  !Guess the Number Game!")
    print("I have selected a number between 1 and 100")
    print("Try to guess the number in few attempts as possible")

    
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            
            if user_guess < number_to_guess:
                print("sorry! wrong prediction")
                print("CLUE:Higher! the !number")
            elif user_guess > number_to_guess:
                print("sorry! wrong prediction")
                print("CLUE: Lower! the !number")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    guess_the_number()
