
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
    for i in range(3):
        print(".")
        time.sleep(1)
    
# Main Game Function
def main(game_variables):
    
    # Let's assign each value in the list game_variables to a variable named first_number, second_number, level, and mode.
    first_number, second_number, level, mode = game_variables
    print("----------------------------------------")
    print("Welcome to level " + str(level) + "!")
    print("Now guess a number between " + str(first_number) + " and " + str(second_number) + ".")
    magic_number = random.randint(first_number, second_number)
    while True:
        guess = GetIntegerOnlyInput()
        if guess == magic_number:
            PrintRandomVictoryString()
            break
        elif guess > magic_number:
            PrintRandomGuessString("high")
        else:
            PrintRandomGuessString("low")
            
    print("Continue to next level? [Please type Yes or No]")
    while True:
        uInput = input()
        if uInput == "Yes" or "yes":
            main(NextLevelIncrease(game_variables))
        elif uInput == "No" or "no":
            print("Thanks for playing!")
            break
        else:
            print("Hey.. you need to select yes or no..")
            
# Initial Global Settings
game_variables = [1,10, 0, "easy"]


# Main Code
print("----------------------------------------")
print("Welcome to the ~Magic Number~ Game!")
print("Where the numbers are cheap, but entropy is forever..")
print("----------------------------------------")
PrintWaitDots()
mode = GetDifficultyMode()
PrintWaitDots()
game_variables[-1] = mode
main(game_variables)