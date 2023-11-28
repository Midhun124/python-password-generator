# The Hard Password generator
import random

# The list of alphabets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f' , 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v' , 'w', 'x', 'y', 'z' , 'A', 'B', 'C', 'D', 'E' , 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T' , 'U', 'V', 'W', 'X', 'Y', 'Z']

# The list of numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# The list of symbols
symbols = ['!', '@', '#', '$', '%', '&', '+', '?']

print("Welcome to the Password Generator")

# Ask the user for the total length of the password they want
password_length = int(input("What's the total length of the password you want to generate? \n"))

# Ask the user for the number of alphabets they want in their password
no_alphabets = int(input("How many alphabets to you want to generate a password ? \n"))

# Ask the user for the number of numbers they want in their password
no_numbers = int(input("How many numbers to you want to generate a password? \n"))

# Ask the user for the number of symbols they want in their password
no_symbols = int(input("How many symbols to you want to generate a password? \n"))

# Check if the total length is less than the sum of alphabets, numbers, and symbols
if password_length < no_alphabets + no_numbers + no_symbols:
    print("The total length is less than the sum of alphabets, numbers, and symbols. Please try again.")
else:
    # Initialize an empty list to store the password characters
    password_list = []

    # Generate the specified number of random alphabets and add them to the password list
    for i in range(1 , no_alphabets + 1):
        char = random.choice(alphabets)
        password_list.append(char)

    # Generate the specified number of random numbers and add them to the password list
    for i in range(1 , no_numbers + 1):
        num = random.choice(numbers)
        password_list.append(num)

    # Generate the specified number of random symbols and add them to the password list
    for i in range(1 , no_symbols + 1):
        sym = random.choice(symbols)
        password_list.append(sym)

    # If the total length of the password is greater than the sum of alphabets, numbers, and symbols, fill the rest with random alphabets
    while len(password_list) < password_length:
        char = random.choice(alphabets)
        password_list.append(char)

    # Shuffle the characters in the password list to ensure randomness
    random.shuffle(password_list)

    # Convert the password list into a string
    password = "".join(password_list)

    # Print the generated password
    print("The password is : \n" + password)
