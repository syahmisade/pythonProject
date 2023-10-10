import random

def play():
    user = input("Osom sekarang!!! 'r' for rocks, 'p' for paper, 's' for scissors\n") #user choices
    computer = random.choice(['r','p','s']) #computer choices

    if user == computer:
        return 'Its a tie!'
    
    # r -> s
    # p -> r
    # s -> p

    if wins_game(user,computer):
        return 'You won!'

    return 'You lost ;('

def wins_game(player, opponent):
    #return true if the player wins
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r')\
         or (player == 's' and opponent == 'p'):
        return True

print(play())
