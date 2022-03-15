import random

def main():
   print("Howdy! What is your name?")
   player = input('<input your name> ')

   print(player, ', I am thinking of a number between 1 and 100.\nTry to guess the number!')

   correct_number = random.randint(1, 100)
   guess = 0
   attempts = 0

   while guess != correct_number:
      guess = int(input('Your guess? '))
      attempts = attempts + 1
      
      if guess > correct_number:
         print('Your guess is too high. Try again.')
      elif guess < correct_number:
         print('Your guess is too low. Try again.')

   print('Well done', player, '--- You got the correct number in', attempts, ' tries.')
   
main()