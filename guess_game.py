import random

print("Created by Kacper Jedynak\n Github:https://github.com/ToxicPL\n Linkedin: https://www.linkedin.com/in/kacper-jedynak-a5ab91200/ ")
print("----------------------------------------")

def guess_intiger(prompt):
    while True:
        intiger = input(prompt)
        if intiger.isnumeric:
            return int(intiger)

def high_nuber(promp):
    while True:
        high = input(promp)
        if high.isnumeric:
            return int(high)


high = high_nuber("Please type a number: ")

answer: int = random.randint(1 , high)
print(answer) #TODO: Testing
print("Please guess betwen 1 and {}: ".format(high))
guess = 0


while guess != answer:
    guess = guess_intiger(": ")
    if guess == 0:
        print("EXIT")
        break
    if guess == answer:
        print("You got it :)")
    if guess > answer:
        print("Please guess lower")
    elif guess < answer:
        print("Please guess higher")