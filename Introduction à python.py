# -*- coding: utf-8 -*-
"""
Created on Tue May 10 13:47:27 2022

@author: Loïc
"""

########################### FONCTION NATIVE + AIDE DES FONCTIONS ###############################

print('test')

############################### ASSIGNATION DE VARIABLES #####################################

## 1. Assignons 3 variables avec une valeur numérique, une chaine de caractère et un booléen

nombre = 25
string = 'test'
booleen = True

## 2. Concaténons 2 chaines de caractères (+)

prenom = "loic"
nom = "calcagno"
print(prenom + " " + nom)


############################ LES OBJETS DE STOCKAGE DE VARIABLES ###############################

## 1. Créons une liste 

liste = ['loic', 29, True]

## 2. Créons un tuple 

tuple = ('loic', 29, True)

## 3. Créons un dictionnaire

# var = {'key':'value'}
# var = dict(key="value")

dico = dict(front = 'html', back = 'php', framework = 'laravel')


############################### LES BOUCLES CONDITIONNELLES ###############################

## 1. Une boucle if..elif..else

x = 100
if x < 100:
    print('x est inférieur à 100')
elif x > 100:
    print('x est supérieur à 100')
else:
    print('x est égal à 100')

## 2. La boucle while

x = 0
while x <5 :
    print(x)
    x += 1

## 3. La boucle for /!\ opérateur d'appartenance (in)
langages= ["php", 'r', "sql", "python"]
for elem in langages:
    print(elem)


############################### L'ECRITURE DE FONCTIONS ###############################

## 1. Créons une fonction somme avec 2 arguments

def somme(x,y):
    print("la somme vaut: ", x + y)

somme(1,5)

## 2. Créons une fonction somme utilisant un nombre **arbitraire** d'argument et utilisant 
##un tuple (* => tuple)

def somme(*args):
    s = 0
    for n in args:
        s += n 
        print("La somme vaut : ", s)
        
somme(1,5,8,3,8,92,6,48,59,48)

## 3. Créons une fonction presentation utilisant un nombre **arbitraire** d'argument et 
##utilisant un dictionnaire (** => dictionnaire)

def presentation(**kwargs):
    for key, value in kwargs.items():
        print("la clé : ", key, "/ la valeur: ", value)
        
presentation(front = 'html', back = 'php', framework = 'laravel', front2 = 'css')


############################### LA PROGRAMMATION ORIENTE OBJET ###############################


## 1. Créons une classe utilisateur prennant comme argument prénom et âge.
## Le prénom doit être visible via une méthode getter

class Utilisateur():
    def __init__(self, prenom, age):
        self.prenom = prenom
        self.age = age
        
    def getName(self):
        print("Je suis ", self.prenom)
        
moi = Utilisateur('loic', 29)
moi.getName()

## 2. Créons une classe presentation prennant comme argument prénom et âge.
## Le prénom et l'âge doit être visible via une méthode getter

class Presentation(Utilisateur):
    def getPresentation(self):
        print("Je suis ", self.prenom, "et j'ai", self.age, "ans")
        
moi2 = Presentation('loic', 29)
moi2.getPresentation()


