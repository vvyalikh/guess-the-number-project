#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
th_number = random.choice(range(1, 100))
game_over = False

print('Welcome to the number guessing game!')
print("I'm thinking number from 1 to 100")
#print(th_number)
difficulty = input("Please choose difficulty. Type 'hard' or 'easy':\n")

count_hard = 5
count_easy = 10
if difficulty == "hard":
  print(f"You have {count_hard} attempts")
  guess = int(input("Make a guess:\n"))
  while count_hard > 0:
    if guess == th_number:
      count_hard = 0
      print("Yes, that's right number! You win!")    
    if guess < th_number:
      print("Too low.")
      count_hard -= 1
      print(f"You have {count_hard} attempts left")
      if count_hard > 0:
          guess = int(input("Make a guess:\n"))
      else:
          print("Game over!")
    if guess > th_number:
      print("Too hight")
      count_hard -= 1
      print(f"You have {count_hard} attempts left")
      if count_hard > 0:
          guess = int(input("Make a guess:\n"))
      else:
          print("Game over!")

if difficulty == "easy":
  print(f"You have {count_easy} attempts")
  guess = int(input("Make a guess:\n"))
  while count_easy > 0:
    if guess == th_number:
      count_easy = 0
      print("Yes, that's right number! You win!")    
    if guess < th_number:
      print("Too low.")
      count_easy -= 1
      print(f"You have {count_easy} attempts left")
      if count_easy > 0:
          guess = int(input("Make a guess:\n"))
      else:
          print("Game over!")
    if guess > th_number:
      print("Too hight")
      count_easy -= 1
      print(f"You have {count_easy} attempts left")
      if count_easy > 0:
          guess = int(input("Make a guess:\n"))
      else:
          print("Game over!")
else:
  if count_hard == 0 or count_easy == 0:
    game_over = True
  else:
    print("Something goes wrong. Try again")    
    difficulty = input("Please choose difficulty. Type 'hard' or 'easy':\n")
    
      







