import secrets
import string

# Function to create a secure password of specified length (I choose default 12)
def create_pw(pw_length=12):

    # Define the character sets: letters, digits, and special characters
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Combine all characters into a single alphabet variable
    alphabet = letters + digits + special_chars

    # Initialize an empty password string and a flag for password strength
    pwd = ''
    pw_strong = False

    # Continue generating passwords until one meets the strength criteria
    while not pw_strong:
        # Generate a random password of specified length using secure random choices
        pwd = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        # Check password strength:
        # Ensure at least one special character and at least two digits
        if (any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2):
            pw_strong = True  # Set to True if criteria are met

    return pwd
# If the script is run directly, generate and print a strong password
if __name__ == '__main__':
    print(create_pw())

# Libraries: secrets provides a secure method for generating random values, which is better suited for security-sensitive applications than Python’s standard random module. string gives access to sets of characters (ascii_letters, digits, punctuation).

# Character Sets: The password uses a mix of uppercase/lowercase letters, digits, and special characters to enhance security.

# Password Strength Check: The while loop keeps generating new passwords until one includes at least one special character and two digits, ensuring the password is secure.

# Execution Check: The if __name__ == '__main__': block allows the function to be used both as a script and as an importable module.#
