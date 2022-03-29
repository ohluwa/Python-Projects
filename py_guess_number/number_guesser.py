import random

def guesser(num):
    j = 0
    while (j < 1):
        user_guess = num
        if (user_guess == randnum):
            print("Congratulations, you guessed the correct number!")
            guessednums.append(user_guess)
            print(guessednums)
            j+= 1
            break
        if (user_guess > randnum):
            print("Your guess is too high, please try again.")
            guessednums.append(user_guess)
            guesser(int(input()))
        if (user_guess < randnum):
            print("Your guess is too low, please try again.")
            guessednums.append(user_guess)
            guesser(int(input()))
        return j

def restart(response):
    i = 0
    while(i < 1):
        if (response == "y"):
            i +=0
            break
        if (response == "n"):
            i +=1
            print("Thanks for playing.")
            exit()
        else:
            print("ERROR: Please enter Y or N.")
            restart(str(input()))
        return response

i = 0
while (i < 1):
    randnum = random.randint(1,101)
    print(randnum)
    guessednums = []
    print("Please guess a number between 1 and 100.: ")
    guesser(int(input()))
    print("Would you like to play again? Y/N")
    restart(str(input().lower()))
