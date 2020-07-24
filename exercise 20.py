# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search..














a = [1, 3, 5, 30, 42, 43, 500]

def check(li, num):
    mid_el = li[int(len(li) / 2)]
    if num == mid_el:
        print(f'{num} in list')
    elif num > mid_el:
        if num in li[int(len(li) / 2):len((li))]:
            print(f'{num} in list')
    elif num < mid_el:
        if num in li[:int(len(li) / 2)]:
            print(f'{num} in list')

check(a, 3)
            


