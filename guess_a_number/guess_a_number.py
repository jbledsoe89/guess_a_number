
import random
import time

# Function to determine the difficulty.
def GetDifficultyMode():
    while True:
        print("Please select 'easy', 'medium', or 'hard' mode.")
        mode = input()
        if mode == "easy" or mode == "medium" or mode == "hard":
            return mode
        else:
            print("Invalid mode")
           
# Function to get starting number.
def GetCustomStartingNumber(first_number):         
    while True:
        print("Please select a starting number between 0 and 100.")
        print("Default number is: " + str(first_number))
        integer = GetIntegerOnlyInput()
        if integer >= 0 and integer <= 100:
            return integer
        else:
            print("Not cool man. Invalid number..")
            
# Function to get ending number that's higher than the starting number.                 
def GetCustomEndingNumber(first_number, second_number):                  
    while True:
        print("Please select a number between 0 and 100.")
        if second_number > first_number:
            print("Default number is: " + str(second_number))
            
        print("This number must be greater than the starting number.")
        integer = GetIntegerOnlyInput()
        if integer >= 0 and integer <= 100:
            if integer > first_number:
                return integer
            else:
                print("Don't play me. Pick a different number.")
        else:
            print("Not cool man. Invalid number..")
            
# Function to get the integer guess with validation.
def GetIntegerOnlyInput():
    while True:
        try:
            integer = int(input("Enter a number: "))
            return integer
        except ValueError:
            print("That's not an integer!")
            
# Function to get magic number.
def NextLevelIncrease(game_variables):
    first_number, second_number, level, mode = game_variables

    level = level + 1
    
    if mode == "easy":
        first_number = first_number * 2
        second_number = second_number * 2
    elif mode == "medium":
        first_number = first_number * 5
        second_number = second_number * 5
    else:
        first_number = first_number * 10
        second_number = second_number * 10       
    
    # Let's return the new values.
    return [first_number, second_number, level, mode]

# Function to print a random victory string.
def PrintRandomVictoryString():
    print(random.choice(["You got it right!!", "WoW! That's correct!", "You cheated.", "Psh. Lucky guess."]))

# Function to print a random string
def PrintRandomGuessString(guess):
    if guess == "high":   
        print(random.choice(["Lower my guy..", "Nope! Too high!", "Shooting for the moon are we?"]))
    else:
        print(random.choice(["Higher my guy..", "Nope! Too low!", "Digging a hole?"]))

# Function to print three dots in 1 second intervals.
def PrintWaitDots():
    for i in range(2):
        print(".")
        time.sleep(1)
        
# Function to increment guess count if it's under 3 guesses otherwise print you lose.
def IncrementGuessCount(game_variables, guess_count):
    
    if guess_count < 3:
        return guess_count + 1
    else:
        print("You lose!")
        print("Thanks for playing!")
        PrintWaitDots()
        # Do you want to try again?
        print("Do you want to try again? [Please type Yes or No]")
        while True:
            userInput = input()
            if userInput == "Yes" or "yes":
                main(game_variables)
            elif userInput == "No" or "no":
                print("Thanks for playing!")
                exit()
            else:
                print("Hey.. you need to select yes or no..")
                
# Main Game Function
def main(game_variables):
    
    # Let's assign each value in the list game_variables to a variable named first_number, second_number, level, and mode.
    first_number, second_number, level, mode = game_variables
    guess_count = 0
    guesses = 3 - guess_count
    
    print("----------------------------------------")
    print("Welcome to level " + str(level) + "!")
    print("You're playing on the " + mode + " difficulty mode.")
    print("Now guess a number between " + str(first_number) + " and " + str(second_number) + ".")
    if mode == "easy":
        print("The first guess is always free when it's Ez.")
    else:
        print("You have " + str(guesses) + " guesses left.")
        guesses = 3 - guess_count - 1
        
    magic_number = random.randint(first_number, second_number)
    while True:
        guess = GetIntegerOnlyInput()
        guesses = 3 - guess_count
        if guess == magic_number:
            PrintRandomVictoryString()
            PrintWaitDots()
            break
        elif guess > magic_number:
            print("----------------------------------------")
            PrintRandomGuessString("high")
            print("You only have " + str(guesses) + " guesses.")
            guess_count = IncrementGuessCount(game_variables, guess_count)            
        else:
            print("----------------------------------------")
            PrintRandomGuessString("low")
            print("You only have " + str(guesses) + " guesses.")
            guess_count = IncrementGuessCount(game_variables, guess_count)  
            
    print("Continue to next level? [Please type Yes or No]")
    while True:
        userInput = input()
        if userInput == "Yes" or "yes":
            main(NextLevelIncrease(game_variables))
        elif userInput == "No" or "no":
            print("Thanks for playing!")
            break
        else:
            print("Hey.. you need to select yes or no..")
            
# Initial Global Settings
game_variables = [1,10, 0, "easy"]
first_number, second_number, level, mode = game_variables


# Main Code
print("----------------------------------------")
print("Welcome to the ~Magic Number~ Game!")
print("Where the numbers are cheap, but entropy is forever..")
print("----------------------------------------")
PrintWaitDots()
mode = GetDifficultyMode()
PrintWaitDots()
first_number = GetCustomStartingNumber(first_number)
PrintWaitDots()
second_number = GetCustomEndingNumber(first_number, second_number)
PrintWaitDots()
game_variables = [first_number, second_number, level, mode]
main(game_variables)