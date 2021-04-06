from pynput.keyboard import Key, Controller 
import time 
import random
import os

#Hat Typer -KermitToad
print('Starting in 7 seconds!')
time.sleep(3)
keyboard = Controller()

h = ['h', 'H']

a = ['a', 'A']

t = ['t', 'T']


loop = True

typed = 0
while loop == True:
    time.sleep(5)
    keyboard.press(random.choice(h))
    keyboard.release(random.choice(h))

    keyboard.press(random.choice(a))
    keyboard.release(random.choice(a))

    keyboard.press(random.choice(t))
    keyboard.release(random.choice(t))
    
    time.sleep(2)
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
  
    typed = typed + 1
    clear = lambda: os.system('cls')
    clear()
    print('Hat Typer -KermitToad')
    print('Hats gained: ', typed)
print('Error loop ended')







