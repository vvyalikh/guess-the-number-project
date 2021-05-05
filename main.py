
import random
th_number = random.randint(1, 100)
game_over = False
COUNT_HARD = 5
COUNT_EASY = 10

print('Welcome to the number guessing game!')
print("I'm thinking number from 1 to 100")
print(th_number)
difficulty = input("Please choose difficulty. Type 'hard' or 'easy':\n")

def level():
  if difficulty == "hard":
    return COUNT_HARD
  if difficulty == "easy":
    return COUNT_EASY

select_level = level() 
print(f"You have {select_level} attempts")
guess = int(input("Make a guess:\n"))

def new_game(th_number, guess, select_level):
    """checks if guess matches th_number and calculates attemts left"""
    while select_level > 0:
        if guess == th_number:
          select_level = 0
          print(f"Yes, that's right number! You win! The answer is {th_number}")    
        if guess < th_number:
          print("Too low.")
          select_level -= 1
          print(f"You have {select_level} attempts left")
          if select_level > 0:
              guess = int(input("Make a guess:\n"))
          else:
              print("Game over!")
        if guess > th_number:
          print("Too hight")
          select_level -= 1
          print(f"You have {select_level} attempts left")
          if select_level > 0:
              guess = int(input("Make a guess:\n"))
          else:
              print("Game over!")


new_game(th_number, guess, select_level)
    
      







