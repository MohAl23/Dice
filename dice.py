import random

while True:
     print("Rolling dice...")
     print(f"The value is" , random.randint(1,6))
     repeat = input("Roll Dice Again? 'y' for yes or 'n' for no:")
     if repeat == 'n':
         break