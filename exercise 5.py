#Take two lists, say for example these two: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
#Make sure your program works on two lists of different sizes.
#Extras: Randomly generate two lists to test this
#Write this in one line of Python 
















a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = [el for el in a if el in b]

print(set(new_list))

import random

def generate_random_list():
    range_ = random.randint(1, 100)
    liss = [random.randint(0, 10) for el in range(0, range_)]
    return liss

print(generate_random_list() * 2)

