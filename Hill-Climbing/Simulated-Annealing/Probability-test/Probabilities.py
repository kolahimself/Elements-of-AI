import random


def main():
    x = random.random()
    if x < 0.1:
        fav = 'bats'
    elif 0.1 < x < 0.2:
        fav = 'cats'
    else:
        fav = 'dogs'
    print(f'I love {fav}')


main()

'''
Other Solution:
import random

   x = random.random()
   if x < 0.8:
      favourite = "dogs"
   elif x < 0.9:
      favourite = "cats"
   else:
      favourite = "bats"
      
   print("I love " + favourite)
'''
