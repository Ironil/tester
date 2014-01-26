# -*- coding: utf-8 -*-


"""
Created on Sun Jan 26 17:03:48 2014

@author: Ironil
"""

from random import randint

# Crear la classe pregunta
class Pregunta:
    """
    llista conté l'enunciat, les opcions, i la resposta
    nopcions és el nombre d'opcions que té la pregunta
    La funció genera un atribut per cada resposta
    """
    numpreguntes = 0
    opcions=["a","b","c","d","e","f"]
    
    def __init__(self, llista, nopcions):
        self.enunciat = llista[0]
        self.nopcions = nopcions
        self.cadena = ""
        for i,resposta in enumerate(llista[1:nopcions]):
            setattr(self,self.opcions[i],resposta)
            self.cadena = self.cadena+"\n"+resposta
            
        self.opciocorrecta = tradueix(llista[-1])

def tradueix(lletra):
    """
    Mira si se li ha entrat una lletra o un numero. Si és una
    lletra, la passa a numero de 0 a el que sigui
    """
    try:
        if lletra.isdigit():
            return lletra
        elif lletra == "a":
            return 0
        elif lletra == "b":
            return 1
        elif lletra == "c":
            return 2
        elif lletra == "d":
            return 3
        elif lletra == "e":
            return 4
        elif lletra == "f":
            return 5
    except:
        if lletra == 0:
            return "a"
        if lletra == 1:
            return "b"
        if lletra == 2:
            return "c"
        if lletra == 3:
            return "d"
        if lletra == 4:
            return "e"
        if lletra == 5:
            return "f"

linia = ""
test = []
nl = 0
llistapregunta = []

with open("preguntes.dat", mode="r", encoding='utf-8') as f:
   for linia in f:
        if linia[0] != "#":
            #Llistapregunta conté pregunta, després les opcions
            llistapregunta.append(linia)
        else:
            llistapregunta.append(linia[1])
            test.append(Pregunta(llistapregunta,len(llistapregunta)-2))
            nl = nl+1
            #I ara reinicialitzar les variables per preparar per la segÜent pregunta
            llistapregunta = []

entrada = ""
opcions=["a","b","c","d","e","f"]
preguntesfetes = 0
encerts = 0
while entrada != "quit":
    preguntesfetes = preguntesfetes+1
    npreg = randint(0,len(test)-1)
    
    print(test[npreg].enunciat + "\n" + test[npreg].cadena)
    entrada = input("Resposta: ")
    if entrada == "quit":
        print("La teva puntuació és: ",encerts,"de",preguntesfetes-1)
    elif entrada not in opcions:
        print("Hey, no has respost el que toca!")
    elif tradueix(entrada) == test[npreg].opciocorrecta:
            print("Bravo!\n")
            encerts = encerts+1
    else:
        print("MOOOC... La opció correcta és la: ", tradueix(test[npreg].opciocorrecta),"\n")
        
