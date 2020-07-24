#Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Extras: Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
#Print out that many copies of the previous message on separate lines. 

name = input("what is your name? ")
age = input("how old are you? ")

def get_year():
    year = 2018 - int(age) + 100
    return year

sentence = f"{name}, you will turn 100 in {get_year()}"

print(sentence)

print_multiplier = input("write a number: ")

print(int(print_multiplier) * (sentence + "\n"))