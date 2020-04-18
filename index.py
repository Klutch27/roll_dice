import random

def roll_dice():
  min = 1
  max = 6
  print("You rolled: ", random.randrange(min, max))

def play_game(reply = None):
  if (reply == None):
    wants_to_play = input("Do you want to roll the dice? (y|n) ")
    if (wants_to_play == "y"):
      roll_dice()
      play_again()
    elif (wants_to_play == "n"):
      print("Goodbye, Seymour.")
  else:
    roll_dice()
    play_again()

def play_again():
  again = input("Do you want to roll again? (y|n) ")
  if (again == "y"):
    play_game("start")
  else:
    print("Fine, be that way.")

play_game()