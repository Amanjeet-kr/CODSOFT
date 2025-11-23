import random
import string

def generate_password(length):
    # All possible characters: letters, digits, punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose 'length' characters from the 'characters'
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter desired password length: "))
        if length < 1:
            print("Length must be a positive integer.")
            return
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()