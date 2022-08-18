from art import logo
import random

def main():
    #variables
    print(logo)
    print("Welcome to the guessing number game")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard':")
        
    def game(difficulty):
        if difficulty == "easy":
            attempts = 10
        else:
            attempts = 5
        
        randomNumber = random.randint(1, 100)

        flagGame = True
        while flagGame:
            print(f"You have {attempts} attempts")
            guessNumber = int(input("Make a guess"))
            if randomNumber == guessNumber:
                print("You win")
                flagGame = False
            elif randomNumber > guessNumber:
                print("Too slow")
            else:
                print("Too high")

            attempts -= 1

            if attempts == 0:
                flagGame == False
                print("You loose")

            



    game(easy)
        

if __name__ == "__main__":
    main()
