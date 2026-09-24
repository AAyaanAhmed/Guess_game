import random
num =random.randint(1, 50)
attempt= 0
print("the num is between 1 and 50")
while True:
    guess = int(input("your guess: "))
    attempt += 1
    if guess < num:
        print("the guess is low")
    elif guess > num:
        print("the guess is high")
    else:
        print("the guess is right, attempts:", attempt)
        break
