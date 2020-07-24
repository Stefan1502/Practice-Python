#Ask the user for a number and determine whether the number is prime or not. 
#(For those who have forgotten, a prime number is a number that has no divisors.). 



#SOLUTION BELLOW














def prim(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("not a prime num")
                break
            else:
                print("prime num")
                break

inp = int(input("number?: "))

print(prim(inp))