import random

secret_number = random.randint(1,100)
attempts = 0

def get_guess():
    return int(input("guess a nunber between 1 and 100:"))

guess = get_guess()

while guess != secret_number:
   #print(guess)
   attempts += 1
 
   if guess < secret_number:
       print(f"{guess} is too low")
   elif guess > secret_number:
       print(f"{guess} is too high")
   guess = get_guess()
  # print(guess)
print("Correct!")
print(f"You guessed it in {attempts + 1} attempts.")