# Higher_Lower_Guessing_Game
import random

def list_numbers():
  nums = []
  for x in range(10):
    num = random.randint(1, 13)
    nums.append(str(num))
    while x > 0 and (nums[x] == nums[x - 1]):
      num = random.randint(1, 13)
      nums[x] = str(num)
  return nums

def game(nums):
  for y in range(9):
    if y == 0:
      print('\nStarting number:', nums[0])
    current_number = int(nums[y])
    next_number = int(nums[y + 1])
    guess = input('Higher(H) or Lower(L)? ')
    if y == 8:
      print('\nYou won! Last number was', next_number)
      break
    if guess == 'H' and next_number > current_number:
      print('\nNext number ', next_number)
    elif guess == 'L' and next_number < current_number:
      print('\nNext number', next_number)
    elif guess == 'H' and next_number < current_number:
      print('\nYou lose. Current number:', current_number,
            ', and next the number was: ', next_number, '\nYou have got', y,
            'points out of of 10!')
      break
    elif guess == 'L' and next_number > current_number:
      print('\nYou lose. Current number: ', current_number,
            ', and the next number was: ', next_number, '\nYou have got', y,
            'points out of of 10!')
      break

if __name__ == "__main__":
  number_sequence = list_numbers()
  game(number_sequence)