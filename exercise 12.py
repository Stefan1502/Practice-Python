#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
#For practice, write this code inside a function.
















a = [5, 10, 15, 20, 25]

def first_last(li):
    b = [a[0], a[-1]]
    return b

print(first_last(a))