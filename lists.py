import random

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = lowercase_letters.upper()

N = 8
password = []

# Add your code here

for i in range(N):
    if i%3 == 0:
        password.append(str(random.randint(0,9)))
    elif i%2 == 0:
        password.append(random.choice(lowercase_letters))
    else:
        password.append(random.choice(uppercase_letters))

random.shuffle(password)
password = "".join(password)

print (password)