#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
#(Hint: remember to use the user input lessons from the very first exercise)
#Extras: Keep the game going until the user types “exit” Keep track of how many guesses the user has taken, and when the game ends, print this out.

















import random

num = random.randint(1, 9)

guess = 10
attempts = 0 
    
while guess != num and guess != "exit":
    guess = int(input("guess the num: "))
    if guess < num:
        print('too low')
        attempts += 1
    elif guess > num:
        print('too high')
        attempts += 1
    elif guess == "exit":
        break
    elif guess == num:
        print('you won')
        print(f'attempts = {attempts}')
        num = random.randint(1, 9)
        attempts = 0 
