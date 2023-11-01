import random
import string

def generate_password(length, complexity):
    if complexity == "low" and length<=8:
        characters = string.ascii_letters + string.digits
    elif complexity == "medium" and length<=8:
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high" and length<=8:
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper()
    else:
        print("Invalid complexity level.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Choose complexity (low, medium, high): ")

    password = generate_password(length, complexity)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
