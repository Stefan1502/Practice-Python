# Write a password generator in Python. Be creative with how you generate passwords 
# - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.












if __name__ == "__main__":

    import random
    import re

    low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cap = [el.upper() for el in low]
    num = ['1','2','3','4','5','6','7','8','9']
    sym = ['@','#','$','^','&','*','!','?']

    alll = low + cap + num + sym

    pwd = ''.join([random.choice(alll) for el in range(random.choice(range(5,20)))])

    print(pwd)
