import random
import string

print("**Password generator**")

length = int(input("Enter your password length: "))
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0987654321"
symbols = "!@#$%^&*"
characters = letters + digits + symbols
password = ""
for i in range(length):
    password += random.choice(characters)
print("Your generated password is:", password)
mypassword = input("Enter your password: ")
if mypassword == password:
    print("Welcome to Facebook")
else:
    print("Wrong password")