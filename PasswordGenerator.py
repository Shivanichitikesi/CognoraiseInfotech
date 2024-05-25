import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password length
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length should be at least 1.")
            return
    except ValueError:
        print("Please enter a valid number for the length.")
        return
    
    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
