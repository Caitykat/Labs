#Caitlyn Trail
#10/24/25
#rps2
#Plays rock paper scissors

#imports
import random
import time

#functions
#chooses random throw for computer
def computer_move():
    c_move = random.randint(1,3)
    if c_move == 1:
        c_throw = "rock"
    if c_move == 2:
        c_throw = "paper"
    if c_move == 3:
        c_throw = "scissors"
    return c_throw

#takes input for players move !!!
def player_move():
    p_move = 0
    while p_move != 1 and p_move != 2 and p_move != 3:
        p_move = int(input("please enter 1 for rock, 2 for paper, or 3 for scissors"))
    if p_move == 1:
        p_throw = "rock"
    if p_move == 2:
        p_throw ="paper"
    if p_move == 3:
        p_throw = "scissors"
    return p_throw


#determines winner
def who_wins():
    if player_throw == "rock" and computer_throw == "rock":
        winner = "It was a draw"
    if player_throw == "rock" and computer_throw == "paper":
        winner = "Computer"
    if player_throw == "rock" and computer_throw == "scissors":
        winner = "Player"
    if player_throw == "paper" and computer_throw == "rock":
        winner = "Player"
    if player_throw == "paper" and computer_throw == "paper":
        winner = "It was a draw"
    if player_throw == "paper" and computer_throw == "scissors":
        winner = "Computer"
    if player_throw == "scissors" and computer_throw == "rock":
        winner = "Computer"
    if player_throw == "scissors" and computer_throw == "paper":
        winner = "Player"
    if player_throw == "scissors" and computer_throw == "scissors":
        winner = "It was a draw"
    return winner

#scoring
def scoring():
    tie = 0
    p_win = 0
    c_win = 0
    ifho_wins() == "It was a draw"
        
        
    

    



#play loop, will run until player says otherwise
play = "y"
while play == "y":
    computer_throw = computer_move()
    player_throw = player_move()
    result = who_wins()
    print("3...")
    time.sleep(0.5)
    print("2...")
    time.sleep(0.5)
    print("1...")
    time.sleep(0.5)
    print("THROW!!!")
    print("The winner is...")
    print(result)
    print("Current score:")
    
    play = input("play again? y/n")
