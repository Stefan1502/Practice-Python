# Implement a function that takes as input three variables, and returns the largest of the three. 
# Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python normally takes care of for us. 
# All you need is some variables and if statements!














def return_max(x,y,z):
    li = sorted([x,y,z])
    return li[-1]

print(return_max(1,156,55))
    