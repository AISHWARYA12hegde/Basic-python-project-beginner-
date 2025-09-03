#the goal is to make a rolling a dice game
#get the choicefrom user
#if choice is roll the die(here its two die)
#else if its n  print thanks for playing
#else if user enters other than y or n print ivalid


import random

while True:
  choice=input("roll the dice(y/n)").lower()
  if choice== 'y' :
     die1=random.randint(1,6)
     die2=random.randint(1,6)
     print(f'({die1},{die2})')
  elif choice=='n':
     print("THANKS FOR PLAYING!")
     break
  else:
    print("INVALID")

#roll the dice(y/n) e
INVALID
#roll the dice(y/n) y
(6,2)
#roll the dice(y/n) n
THANKS FOR PLAYING!

