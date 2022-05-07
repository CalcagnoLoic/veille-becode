# -*- coding: utf-8 -*-
########################### FONCTION NATIVE + AIDE DES FONCTIONS ###############################

print("hello world")

############################### ASSIGNATION DE VARIABLES ###############################

## 1. Assignons 3 variables avec une valeur numérique,
## une chaine et caractère et un booléen

x = 5
y = "coucou"
z = True

type(x)
type(y)
type(z)

## 2. Concaténons 2 chaines de caractères

prenom = "Loïc"
nom = "Calcagno"

print(prenom + " " + nom)

############################ LES OBJETS DE STOCKAGE DE VARIABLE S###############################

## 1. Créons une liste + print()

list = {"BeCode", 2022, True}
print(list)

## 2. Créons un tuple + print()

tuple = ("becode", 2022, True)
nom, annee, code = tuple

print(nom)
print(annee)
print(code)

## 3. Créons un dictionnaire + print()

langage = {'front':'HTML', 'back':'PHP', 'framework':'Laravel'}
langage2 = dict(front='HTML', back='PHP', framework='Laravel')

print(langage['back'])

############################### LES BOUCLES CONDITIONNELLES ###############################

## 1. Une boucle if..elif..else

x = 100

if x < 100:
    print('La variable est inférieure à 100')
elif x == 100:
    print('La variable est égale à 100')
else :
    print('La variable est supérieure à 100')
    
## 2. L'opérateur d'appartenance dans la boucle if

langage_programmation = ["python", "R", "SQL", "PHP"]

if "HTML" in langage_programmation:
    print("HTML est présent")
else:
    print("HTML n'est pas présent dans la liste")
    
## 3. La boucle while

x = 0
while x < 5:
    print(x)
    x+=1
    
## 4. La boucle for

langage_programmation = ["python", "R", "SQL", "PHP"]
for i in langage_programmation:
    print(i)


############################### L'ECRITURE DE FONCTIONS ###############################

## 1. Créons une fonction somme avec 2 arguments

def somme(x,y):
    print(x+y)

somme(1,2)

## 2. Créons une fonction somme utilisant un nombre 
## arbitraire d'argument et utilisant un tuple

def somme(*args):
    s = 0
    for n in args:
        s += n
        print("La somme vaut : ", s)

somme(15, 19, 145, 1, 42)

## 3. Créons une fonction somme utilisant un nombre 
## arbitraire d'argument et utilisant un dictionnaire

def presentation(**kwargs):
    for i, j in kwargs.items():
        print(i,j)
        
presentation(Prénom='Loïc', age=29, ville='La Louvière')

## 4. Utilisons la méthode *args sur une fonction ayant un nombre défini d'arguments

def somme(x,y):
    print(x+y)

s=[1,2]
somme(*s)

############################### LA PROGRAMMATION ORIENTE OBJET###############################


## 1. Créons une classe utilisateur prennant comme argument prénom et âge.
## Le prénom doit être visible via une méthode getter
class Utilisateur:
    def __init__(self, prenom, age):
        self.prenom = prenom
        self.age = age
    
    def getName(self):
        print("Salut, je suis", self.prenom)
    
moi = Utilisateur('Loïc', 29)
moi.getName()

## 2. Créons une classe utilisateur prennant comme argument prénom et âge.
## Le prénom et l'âge doit être visible via une méthode getter

class Utilisateur:
    def __init__(self, prenom, age):
        self.prenom = prenom
        self.age = age
    
    def getName(self):
        print("Salut, je suis", self.prenom)
        
class Presentation(Utilisateur):
    def getPresentation(self):
        print("Salut, je suis", self.prenom, "et j'ai", self.age)

moi = Presentation('Loïc', 29)
moi.getPresentation()

############################### L'IMPORT DE MODULES ###############################

import matplotlib.pyplot as plt
x = [1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5]
plt.hist(x, range = (0, 5), bins = 5, color = 'red', edgecolor='white')
plt.xlabel('valeurs')
plt.ylabel('nombres')
plt.title('Exemple d\' histogramme simple')
