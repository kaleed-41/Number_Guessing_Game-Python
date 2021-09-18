# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

import random

#store upper bound of range
upper_value = int(input("Enter the upper bound: "))

#store lower bound of range
lower_value = int(input("Enter the lower bound: "))

# generate random number for guess
random_num = random.randint(lower_value, upper_value)

print("The random number is: " + str(random_num))

number_of_guesses = 0
max_guesses = 3
answer = 0

while number_of_guesses != max_guesses:
    answer = int(input("Guess the number: "))
    print(answer)
    if answer > random_num:
        print("Your guess is too high")
    elif answer < random_num:
        print("Your guess is too low")
    else: 
        print("You have guessed correctly")
        break
    number_of_guesses += 1    

if(number_of_guesses == max_guesses):
    print("You have reached the maximum number of guesses")
