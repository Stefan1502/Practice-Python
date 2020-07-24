#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
#(If you don’t know what a divisor is, it is a number that divides evenly into another number. 


















num = int(input("write a num: "))

for el in range(0, num):
    if el and num % el == 0:
        print(el)
