import random

print("Created by Kacper Jedynak\n Github:https://github.com/ToxicPL\n Linkedin: https://www.linkedin.com/in/kacper-jedynak-a5ab91200/ ")
print("----------------------------------------")
top_range = input("Type a number: ")
if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit

r_number = random.randrange(0, top_range)

while True:
    user_guess = input("Make a guess. ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        quit()

    if user_guess == r_number:
        print("You guessed it")
        break
    else:
        if user_guess > r_number:
            print("You were above the number")
        else:
            print("You were below the number")
