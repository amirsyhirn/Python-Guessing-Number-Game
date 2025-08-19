import random

lowest_num = 1
highest_num = 100
guesses = 0
answer = random.randint(lowest_num, highest_num)
is_running = True

print("Guess the number!")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess <0 or guess >100 :
            print("Your guess is out of range!")
        elif guess > answer :
            print("High! Guess again")
        elif guess < answer :
            print("Low! Guess again")
        else :
            print("TING TING TING!!! CORRECT!")
            is_running = False

    else :
        print("Invalid guess!")
        print(f"Select a number between {lowest_num} and {highest_num}")