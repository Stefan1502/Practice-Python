#Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.
#Extras: Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

#SOLUTION BELLOW













a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for el in a:
#     if el < 5:
#         print(el)

# new_list = []
# for el in a:
#     if el < 5:
#         new_list.append(el)
# print(new_list)

print([el for el in a if el < 5])

new_num = int(input("write a number: "))

print([el for el in a if el < new_num])