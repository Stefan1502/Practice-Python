#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
#Extras: If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
















user_input = int(input("number: "))

if user_input % 4 == 0:
    print("wow")
elif user_input % 2 == 0:
    print("this number is even")
else:
    print("odd number")

num = int(input("write two nums to check if divisible, pls, ty: "))
check = int(input("second num: "))

if num % check == 0:
    print(f"{num} is divisible by {check}")
else:
    print("nope")