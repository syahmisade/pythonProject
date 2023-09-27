import random

# More focus on the user trying to guess a number from the computer
def guess(x):
    random_number= random.randint(1, x) #this will return the random number that choosen from the computer
    guess = 0 #to make sure that the random number wil never be 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: ')) #make sure the user able to choose a number in int
        if guess < random_number: #hint if the number is too low
            print("Too low broo. Again again.") 
        elif guess > random_number: #hint if the number is too high
            print("It is too high. Again.")
    
    print(f"Yeayy, {random_number} is the correct number!") #the answer of the random_number

guess(10)