#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#Extras: Write two different functions to do this - one using a loop and constructing a list, and another using sets.







#   I
#   I
#  \ /
#   I 







def no_dup(li):
    a = []
    for i in li:
        if i not in a:
            a.append(i)
    return a

def no_dupp(li):
    return set(li)

test = [1,1,2,2,2,2,3,4,5,5,5,6,6,7]

print(no_dup(test))
print(no_dupp(test))