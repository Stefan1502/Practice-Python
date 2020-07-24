# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.








# Res below









with open('/home/stefan/Desktop/exercises/happynumbers.txt', 'r') as open_file:
    happy_nums = [el for el in open_file.read().split()]

with open('/home/stefan/Desktop/exercises/primenumbers.txt', 'r') as open_file:
    prime_nums = [el for el in open_file.read().split()]

print(sorted(list(set([int(el) for el in happy_nums if el in prime_nums]))))