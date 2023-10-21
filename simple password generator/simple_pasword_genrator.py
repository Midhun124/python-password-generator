import random


alphabets = ['a', 'b', 'c', 'd', 'e', 'f' , 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v' , 'w', 'x', 'y', 'z' , 'A', 'B', 'C', 'D', 'E' , 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T' , 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '[', ']', ':', ';', "'", '"', '<', '>', ',', '.', '/', '?']


print("Welcome to the Password Generator")

no_alphabets = int(input("How many alphabets to you want to generate a password ? \n"))

no_numbers = int(input("How many numbers to you want to generate a password? \n"))

no_symbols = int(input("How many symbols to you want to generate a password? \n"))

password = ""

for i in range(1 , no_alphabets + 1):

  char = random.choice(alphabets)

  password += char

for i in range(1 , no_numbers + 1):

  num = random.choice(numbers)

  password += num  

for i in range(1 , no_symbols + 1):

  sym = random.choice(symbols)

  password += sym

print("The password is : \n" + password)



