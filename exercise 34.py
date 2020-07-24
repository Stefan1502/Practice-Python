# This exercise is Part 3 of 4 of the birthday data exercise series. 
# The other exercises are: Part 1, Part 2, and Part 4.

# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. 
# In this exercise, load that JSON file from disk, extract the months of all the birthdays, 
# and count how many scientists have 
# a birthday in each month.

# Your program should output something like:

# {
# 	"May": 3,
# 	"November": 2,
# 	"December": 1
# }










import json
from collections import Counter

with open("/home/stefan/Desktop/exercises/ex33.json", "r") as f:
    data = json.load(f)

m = data.values()
m = [el.split('.')[1] for el in m]
m = Counter(m)

print(m)