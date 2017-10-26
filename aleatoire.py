from garden2 import *
from random import randint

nombreAleatoire = 0


print('bonjour tout le monde')

while True :
    nombreAleatoire = randint(0, 3)
    if nombreAleatoire == 0 :
        haut()
    elif nombreAleatoire == 1 :
        bas()
    elif nombreAleatoire == 2 :
        gauche()
    elif nombreAleatoire == 3 :
        droite()
    print(ramasse())