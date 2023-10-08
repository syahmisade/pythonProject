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

# The computer will try to guess mystery number from the player
def computer_guess(x):
    low = 1
    high = x
    clue = ''

    #while loop = selagi tak dapat jawapan, selagi tu ulang
    while clue != 'c': 
        if low != high:
            guess = random.randint(low,high) #In random.randint, the low and high value cannot equal. It will give error as the outcome
        else:
            guess = low 
        clue = input(f'Is {guess} too high(H), too low(L), or correct(C)?').lower()

        #kita mahu the computer teka number instead of dia pilih2 number itu ini. We need to change the number guessing bounderies based on the hint given 
        if clue == 'h':
            high = guess - 1
        elif clue == 'l':
            low = guess + 1
    
    print(f"The computer manage to guess number, {guess}, correctly!")




#guess(10)
computer_guess(10)