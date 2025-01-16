import random

print("Hello and welcome to the first Python Project : Dice Rolling Game")

#playing = True
while True:
    choice = input("Roll the Dice (y/n) ? ").lower()
    if choice == 'y':
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        print(f'({dice_one}, {dice_two})')
    elif choice == 'n':
        print("Thanks For Playing")
        break
    else:
        print("Invalid CHOICE")