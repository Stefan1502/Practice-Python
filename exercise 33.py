# This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 3, and Part 4.

# In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, 
# modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the 
# dictionary defined in the program.

# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, 
# and update the JSON file you have on disk with the scientist’s name. If you run the program multiple 
# times and keep adding new names, your JSON file should keep getting bigger and bigger.

#exercise oppening a file








import json

bdays = {
    "sashko": "07.06.1992",
    "igor": "08.10.1991", 
    "ana": "19.02.1990"
    }

with open("/home/stefan/Desktop/exercises/ex33.json", "w") as f:
    json.dump(bdays, f)

with open("/home/stefan/Desktop/exercises/ex33.json", "r") as f:
    data = json.load(f)

user_name = input('append to json, name: ')
user_age = input('bday: ')
user_inp = {user_name : user_age}

data.update(user_inp)

with open("/home/stefan/Desktop/exercises/ex33.json", "w") as f:
    json.dump(data, f)

with open("/home/stefan/Desktop/exercises/ex33.json", "r") as f:
    info = json.load(f)

print(info)