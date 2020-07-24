# This exercise is Part 3 of 3 of the Hangman exercise series. 
# The other exercises are: Part 1 and Part 2.

# You can start your Python journey anywhere, 
# but to finish this exercise you will have to have finished Parts 1 and 2 or use the solutions (Part 1 and Part 2).

# In this exercise, we will finish building Hangman. 
# In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

# In Part 1, we loaded a random word list and picked a word from it. 
# In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. 
# In this exercise, we have to put it all together and add logic for handling guesses.

# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

# Only let the user guess 6 times, and tell the user how many guesses they have left.



import random

with open('/home/stefan/Desktop/exercises/sowpods.txt', 'r') as f:
	words = list(f)

target = random.choice(words).strip()

hashed_w = list(len(target) * "_")
print("".join(hashed_w))
attempts = 0
guessed = []

while attempts <= 6:
    if "_" not in hashed_w:
        print('you won')
        break  
    occurence = -1
    guess = input('guess ')
    guessed.append(guess)
    attempts += 1
    for el in target:
        occurence += 1
        if el == guess.upper():
            hashed_w[occurence] = el
    print(f'attempts {"".join(guessed)}')      
    print("".join(hashed_w))
 