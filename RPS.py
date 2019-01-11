"""
This program emulates Rock-Paper-Scissors, prompt the user to select either Rock, Paper, or Scissors, instruct the computer to randomly select
either Rock, Paper or Scissors, compares the user's choice against the computer's choice, determine a winner and finally informs the user who the winner is."

Author: Franco IC
"""

print "Welcome to Rock-Paper-Scissors!"

from random import randint

options = "ROCK", "PAPER", "SCISSORS"

message = {
  "tie": "Yawn it's a tie!",
  "won": "Yay you won!",
  "lost": "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
  print "The user choice is: %s" % user_choice
  print "The computer choice is: %s" % computer_choice
  #user_choice = user_choice.upper()
  if user_choice == "ROCK" and computer_choice == "SCISSORS":
    print message["won"]
  elif user_choice == "PAPER" and computer_choice == "ROCK":
    print message["won"]
  elif user_choice == "SCISSORS" and computer_choice == "PAPER":
    print message["won"]
  elif user_choice == computer_choice:
    print message["tie"]
  else:
    print message["lost"]
    
def is_valid(param):
  if param == "ROCK" or param == "PAPER" or param == "SCISSORS":
    return True
  else:
    return False       
      
def play_RPS():
  user_choice = raw_input("Enter Rock, Paper or Scissors: ")
  user_choice = user_choice.upper()
  while not is_valid(user_choice):
    print "Wrong input"
    user_choice = raw_input("Enter Rock, Paper or Scissors: ")
    user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)
    
play_RPS()  
