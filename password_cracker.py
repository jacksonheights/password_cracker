# Imports the hashlib library for hashing operations
import hashlib

# Creates an empty dictionary to store username-hash pairs
user_hash_dict = {}

# Opens the "common_passwords.txt" file in read mode ("r")
with open('common_passwords.txt', 'r') as f:
    # Reads all lines from the file and splits them into a list
    common_passwords = f.read().splitlines()

# Opens the "username_hashes.txt" file in read mode ("r")
with open('username_hashes.txt', 'r') as f:
    # Reads all lines from the file and splits them into a list
    text = f.read().splitlines()

    # Loop through each line (user_hash) in the list
    for user_hash in text:
        # Splits the current user_hash string at the colon (":")
        username, hash = user_hash.split(":")

        # Adds the username and corresponding hash to the dictionary
        user_hash_dict[username] = hash

# Loop through each password in the common_passwords list
for password in common_passwords:
    # Creates a hash of the current password using SHA-256 and converts it to hexadecimal format
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Loop through each username-hash pair in the user_hash_dict
    for username, hash in user_hash_dict.items():
        # Checks if the hashed_password matches the stored hash for a username
        if hashed_password == hash:
            # If a match is found, print the username and password
            print(f'HASH FOUND\n{username}:{password}')
