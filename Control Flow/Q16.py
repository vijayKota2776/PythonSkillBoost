import random
random_number = random.randint(1, 100)
user_guess = None
while user_guess != random_number:
    user_guess = int(input("Guess the number between 1 and 100: "))
    if user_guess < random_number:
        print("Too low! Try again.")
    elif user_guess > random_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! {user_guess} is the correct number!")