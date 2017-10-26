import numpy as np

# on crée un tableau a trois dimensions
P = nP.zeros(shape=(256,5,256), dtype = float)

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
    # enregistre l'état
    s = etat()
    nombreAleatoire = randint(0, 4)
    action(nombreAleatoire)
    s_prime = etat()
    a = nombreAleatoire
    P[s,a,s_prime] = P[s,a,s_prime] + 1
    
