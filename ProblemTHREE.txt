# Revision number 1 / 12/15/24
## Begin - Amran Rahim (12/15/24) 

import random
import string

# Create a list of words to be used as the dictionary
dictionary = ["password", "secret", "123456", "qwerty", "admin"]

def create_password():
    """
    Generate a random password with 8 characters, including symbols and letters.
    """
    # Choose 8 random characters from the string of letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(8))
    return password

# Initialize an empty list to store accepted passwords
accepted_passwords = []

# Keep generating passwords until 40 acceptable passwords are found
iteration = 0
while len(accepted_passwords) < 40:
    # Generate a random password
    password = create_password()
    iteration += 1
    
    # Check if the password is not in the dictionary and contains at least one special symbol
    if password not in dictionary and any(c in string.punctuation for c in password):
        accepted_passwords.append(password)

# Print the header and the list of accepted passwords
print("Accepted Passwords:")
for password in accepted_passwords:
    print(password)

# 2/15/2024
## End - Amran Rahim 