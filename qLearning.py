from garden2 import *
import numpy as np
from random import randint

alpha = 0.9
lamb = 0.95
s2 = 0
a= 0
r= 0

Qsa = np.zeros(shape=(256, 5),dtype=float)

def action(nombreMouvement):
    # tirer une action au hasard
    if nombreMouvement == 0 :
        # haut
        a =0
        haut()
    elif nombreMouvement == 1 :
        # bas
        a = 1
        bas()
    elif nombreMouvement == 2 :
        # gauche
        a = 2
        gauche()
    elif nombreMouvement == 3 :
        # droite
        a = 3
        droite()
    elif nombreMouvement == 4 :
        # ramasse
        a = 4
        r = ramasse()

while True :
    # enregistre
    s = etat()
    # tirage de a selon la probabilite 10 % pour le hasard
    choixAction = randint(0, 9)
    if choixAction == 0 :
        # random.choice([''])
        nombreAleatoire = randint(0, 4)
        action(nombreAleatoire)
    # la prochaine action est celle 
    else :
        # indice de l'action suivante la plus prometeuse
        if np.all(Qsa[s2,:]==0.0):
            maxA2 = randint(0,4)
        else:
            maxA2 = np.argmax(Qsa[s2,:])
        print(maxA2)
        action(maxA2)

    s2 = etat()
    print(s,a,r,s2)
    # indice de l'action suivante la plus prometeuse
    maxA2 = np.argmax(Qsa[s2,:])
    # valeur de Qsa[s2,maxA2]
    valueA2 = Qsa[s2,maxA2]
    # MAJ QSA
    Qsa[s,a] = Qsa[s,a] + alpha*(r+lamb*valueA2 - Qsa[s,a])