import random

number = random.randint(1, 100)
guess = 0
print("Random number has been generated! Guess it!")
while(number != guess):
    guess = int(input("your guess : "))
    if(number > guess):
        print("Your number is lower than the random number!\nTry Again!")
    elif(number < guess):
        print("Your number is higher than the random number!\nTry Again!")
        
print("Congratulation, You guessed it.\nThe number is", str(number))
