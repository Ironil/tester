# -*- coding: utf-8 -*-

"""
Created on Sun Jan 26 2014

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
        #Recorre les respostes entrades, i crea dinàmicament tants
        #atributs de la classe com preguntes. Seran foo.a, foo.b...
        for i,resposta in enumerate(llista[1:nopcions]):
            setattr(self,self.opcions[i],resposta)
            self.cadena = self.cadena+"\n"+resposta
            
        self.opciocorrecta = dictlletres[llista[-1]]

dictlletres = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
dictnum = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4:'e', 5:'f'}

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
			#En cas que arribem a la resposta, s'afegeix a la llista, i es crea
			#l'objecte corresponent, que es posa a la llista test
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
    elif dictlletres[entrada] == test[npreg].opciocorrecta:
            print("Bravo!\n")
            encerts = encerts+1
    else:
        print("MOOOC... La opció correcta és la: ", dictnum[test[npreg].opciocorrecta],"\n")
