print("Try the Guess number in 1 to 20")
import random

guess_number = random.randint(1, 20)

count = 0

while True:
    user_input = int(input("Enter a number: "))
    
    if user_input > guess_number:
        print("Try guessing a lower number")
        count = count + 1

    elif user_input < guess_number:
        print("Try guessing a higher number")
        count = count + 1

    else:
        print("Congratulatins! you guess the right number.\n you attemped for", count,"times")
        break
