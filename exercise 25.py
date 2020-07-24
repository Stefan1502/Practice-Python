# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. 
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.

# As the writer of this program, you will have to choose how your program will strategically guess. 
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. 
# But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), 
# and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! 







my_list = [el for el in range(1,100)]

user_inp = "incorrect"
num_of_guesses = 0
left, right = 0, len(my_list)

while user_inp != "correct" or left > right:
    mid = (left + right) // 2
    print(mid)
    user_inp = input()

    if user_inp == "too low":
        left = mid + 1
        num_of_guesses += 1
    elif user_inp == "too high":
        right = mid - 1
        num_of_guesses += 1
        
print(num_of_guesses)


# target = 25

# def find_target(li, target):
#     left, right = 0, len(li) - 1
#     num_of_guesses = 0
#     while left <= right:
#         mid = (left + right) // 2

#         if li[mid] == target:
#             print('correct')
#             break

#         elif li[mid] < target:
#             left = mid + 1
#             num_of_guesses += 1
#         elif target < li[mid]:
#             right = mid - 1
#             num_of_guesses += 1
    
#     return num_of_guesses

# print(find_target(my_list, target))

