import random

high = 100
low = 0

total_chance = 7
used_chance = 0

number = random.randint(low,high)

print(f"\nwelcome to number guessing game. you have {total_chance} to guess number between {high} and {low}. lets start. \n")


while True :

    guess = int(input("enter your guess : "))
    used_chance += 1

    if guess == number :
        print(f"\nCorrect ! the number is {number}. you guessed it in {used_chance}. attempts.\n")
        break

    elif used_chance >= total_chance :
        print(f"sorry ! the number was {number}. better luck next time.\n")
        break

    elif guess > number :
        print("too high ! try a lower number.\n")

    elif guess < number :
        print("too low ! try a higher number.\n")

