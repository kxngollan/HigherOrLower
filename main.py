from data import data
import random
from replit import clear

clear()

celebrityOne = data[random.randint(0, len(data)-1)]
celebrityTwo = data[random.randint(0, len(data)-1)]
if celebrityOne == celebrityTwo:
    celebrityTwo = data[random.randint(0, len(data)-1)]

def compare(celebrityOne, celebrityTwo, choice):
    if choice == "1":
        if celebrityOne['follower_count'] > celebrityTwo['follower_count']:
            return True
        else:
            return False
    if choice == "2":
        if celebrityOne['follower_count'] < celebrityTwo['follower_count']:
            return True
        else:
            return False

playing = True

correctAnswers = 0

print("Welcome to higher or lower game.")

while playing:
    print("Tell me who you think has more instagram followers:")
    print(f"You have {correctAnswers} correct answers.")
    print(f"1. {celebrityOne['name']}, {celebrityOne['description']} from {celebrityOne['country']}")
    print("Or")
    print(f"2. {celebrityTwo['name']}, {celebrityTwo['description']} from {celebrityTwo['country']}")
    choice = input("Enter 1 or 2: ")
    correct = compare(celebrityOne, celebrityTwo, choice)
    if correct:
        correctAnswers += 1
        print("Correct!")
        celebrityOne = celebrityTwo
        celebrityTwo = data[random.randint(0, len(data)-1)]
    else:
        print(f"Wrong! Game Over!\nYou got {correctAnswers} correct")
        playing = False



print(choice)