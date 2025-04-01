import random
import string

#Password generator 

# User Chooses Password length

#Generate password with upper, lower, nums, symbols

print("Welcome to Password Generator! We will compile a password using Upper/lower case letters, numbers, and symbols!")
length = int(input("How many characters would you like your password to be? "))
def pass_generator (size = length, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range (size))
   

password = pass_generator()
print(password)
