import random

def roll_dice(num_rolls):
    if num_rolls <= 0:
        print("Number of rolls should be a positive integer.")
        return

    print(f"Rolling a 6-sided die {num_rolls} times:")
    for i in range(num_rolls):
        result = random.randint(1, 6)
        print(f"Roll {i + 1}: {result}")

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        try:
            num_rolls = int(input("Enter the number of rolls: "))
            roll_dice(num_rolls)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        play_again = input("Roll the dice again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for using the Dice Rolling Simulator!")

if __name__ == "__main__":
    main()
