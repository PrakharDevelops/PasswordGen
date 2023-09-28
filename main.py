# Importing the necessary modules
import string  # Module providing various string-related functions
import random  # Module providing functions for generating random numbers and selecting random elements

if __name__ == "__main__":
    # Getting the lowercase, uppercase, digits, and punctuation characters
    sLower = string.ascii_lowercase  # Lowercase letters
    sUpper = string.ascii_uppercase  # Uppercase letters
    sDig = string.digits  # Digits (0-9)
    sPunc = string.punctuation  # Punctuation characters

    # Asking the user to input the desired password length
    pLen = input("\nEnter password length: ")

    # Error Handling: Checking if the input is a valid integer
    while not pLen.isdigit():
        print("Invalid input. Please enter an integer.")
        pLen = input("\nEnter password length:")

    # Converting the password length to an integer
    pLen = int(pLen)

    # Creating a list of characters for the password
    s = []
    s.extend(list(sLower))
    s.extend(list(sUpper))
    s.extend(list(sDig))
    s.extend(list(sPunc))

    # Shuffling the list to randomize the characters
    random.shuffle(s)
    print("Your password is:")

    # Generating and printing a random password
    # Line 27 and 28 will work the same way
    print("".join(random.sample(s, pLen)))  # Randomly samples pLen characters and joins them
    print("".join(s[0:pLen]))  # Takes the first pLen characters and joins them
