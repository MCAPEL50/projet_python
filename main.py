print("Hello")
def table(n):
    for k in range(1,11):
        print(n,"* ", k, " = ", n * k)

def punition_table(m):
    for n in range(1,m+1):
        print("table de", n)
        table(n)
        print('*' * 12)

punition_table(0)

def somme(n):
    s=0
    for z in range(1,n+1):
        s=s+z
    print(s)
somme(0)

def somme_carre(n):
    s=0
    for z in range(1,n+1):
        s=s+z**2
    print(s)
somme_carre(0)

def somme_puissance(n,m):
    s=0
    for z in range(1,n+1):
        s=s+z**m
    print(s)
somme_puissance(1,2)

def somme_binaire(n):
    s=1
    for z in range(1,n+1):
        s=s+0.5**z
    print(s)
somme_binaire(0)

for c in range(5):
    print(' ' * ((11- 1- 2* c)//2) + 'M' * (1+2 * c)+ ' ' * ((11 -1 -2 * c )//2))
print('-'* 11)
for c in range(4, -1, -1):
    print(' ' * ((11- 1- 2* c)//2) + 'W' * (1+2 * c)+ ' ' * ((11 -1 -2 * c )//2))

from random import *
from math import *
d1 = randint(1,6)
d2 = randint(1,6)  
if d1>d2:
    print("le joueur 1 a gagné!")
elif d1<d2:
    print("le joueur 2 a gagné!")
elif d1==d2:
    print("même scores, partie nule")

def jeu() :
    de1 = randint(1,6)
    de2 = randint(1,6)
    if de1 > de2 :
        return 1
    elif de2 > de1 :
        return 2
    else :
        return 0
	

def frequence(n) :
    compteur = 0
    for k in range(n) :		
        if jeu() == 1 :		 
            compteur = compteur + 1	
    return compteur/n
	
	
print(frequence(10**6))
print(15/36)