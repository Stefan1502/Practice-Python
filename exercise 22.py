# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, 
# and print out the results to the screen. 
















from collections import Counter

with open('/home/stefan/Desktop/exercises/nameslist.txt', 'r') as open_file:
    all_text = open_file.read()

list_names = []
for el in all_text.split():
    list_names.append(el)

print(Counter(list_names))