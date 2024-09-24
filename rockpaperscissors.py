# import random module
import random

# make options for the computer
options = ["r", "p", "s"]

# keep score
wins = 0
losses = 0

# rules
print("Welcome to Rock, Paper, Scissors. If you don't know, rock defeats scissors, which defeats paper, which defeats rock. \nWrite r for rock \nWrite p for paper\nWrite s for scissors. \nHave fun.")

# ask for number of rounds
rounds = int(input("\nHow many rounds would you like to play? \nPick an odd number. "))
remainder = rounds % 2

# make sure rounds are odd
while remainder != 1:
  rounds = int(input("\nThat wasn't an odd number. \nHow many rounds would you like to play? \nPick an odd number. "))
  remainder = rounds % 2
  if remainder == 1:
    break

# set variables used in loops and if statements
i = 0
x = 1 
tie = 0
y = 0

# start the game 
# make the game run for number of rounds chosen
while i < rounds:
# make sure the question only runs once
  if y == 0:
# take the player's choice
    choice = input("\nRock, Paper or Scissors? ").strip().lower()
# make sure the question runs again for the next round
  if y > 0:
    y -= 1
# get the computer's item (r, p, or s)
  enemy = random.choice(options)
# make sure the player types r, p, or s
  if choice == "r" or choice == "p" or choice == "s":
# run this if the computer chose r
    if enemy == "r":
# tell the user what item the computer chose
      print("\nThe enemy chose rock.")
# tell the user if they won or lost depending on their choice
      if choice == "p":
        print("You win this round.")
        wins += 1
      elif choice == "s":
        print("You lose this round.")
        losses += 1
# run this if the computer chose p
    elif enemy == "p":
# tell the user what item the computer chose
      print("\nThe enemy chose paper.")
# tell the user if they won or lost depending on their choice
      if choice == "r":
        print("You lost this round.")
        losses += 1
      elif choice == "s": 
        print("You won this round.")
        wins += 1
# run this if the computer chose s
    else:
# tell the user what item the computer chose
      print("\nThe enemy chose scissors.")
# tell the user if they won or lost depending on their choice
      if choice == "r":
        print("You won this round.")
        wins += 1
      elif choice == "p":
        print("You lost this round.")
        losses += 1
# set the conditions for a tie
    if choice == enemy:
# tell the user if it was a tie
      print("\nIt was a tie. This round doesn't count.")
# add 1 to tie so that the code doesn't count it as a round
      tie += 1
# only tell user amount of rounds/wins/losses if there's no tie
    if tie < 1:
# tell the user the round/wins/losses
      print("\nThis was round {}. You have {} wins and {} losses.".format(x, wins, losses))
# add 1 to the rounds that are shown to the user
      x += 1
# prevent an infinite loop
      i += 1
# tell the computer that the round doesn't count if there's a tie
    if tie > 0:
      tie -= 1
# if the user didn't type r, p, or s, tell them to
  else: 
    while choice  != "r" or choice != "p" or choice != "s":
      print("Write r, p, or s.")
# ask the user to make their choice after telling them
      choice = input("Rock, Paper or Scissors? ").strip().lower()
# stop the loop if they write the correct letter
      if choice == "r" or choice == "p" or choice == "s":
# add 1 to y to stop the question from being asked again
        y += 1
        break
# after the game ends, tell the player if they won or lost
  if wins > (rounds/2):
    print("\nCongratulations. You won.") 
  if losses > (rounds/2):
    print("\nCongratulations. You lost.") 
