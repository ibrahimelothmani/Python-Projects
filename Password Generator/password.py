#import random
import secrets
import string


def generate_password(min_length, numbers=True, special_characters=True):    
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    print(all_characters)
   #print(random.choice(all_characters))
    print(secrets.choice(all_characters))