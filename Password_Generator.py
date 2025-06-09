# Password_Generator


import secrets
# using library secrets for making it cryptographically secure
import string

n = int(input("Enter number of characters"))
passwd = []
complex = input(
    "Enter EASY for easy password\n enter HARD for hard password: ")
if complex == "EASY":
    char_pool = string.ascii_letters+string.digits
elif complex == "HARD":
    char_pool = string.ascii_letters+string.digits+string.punctuation


for i in range(n):
    rand_char = secrets.choice(char_pool)
    passwd.append(rand_char)

password = "".join(passwd)
print(password)
