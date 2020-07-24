# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), 
# and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

# Extras:

# Ask the user to specify the name of the output file that will be saved.

import contextlib, io

f = io.StringIO()
with contextlib.redirect_stdout(f):
    __import__("exercise 17")
prev_exs = f.getvalue()

name_the_file = input('name: ')

with open(f'/home/stefan/Desktop/exercises/{name_the_file}.txt', 'w') as open_file:
    open_file.write(prev_exs)
