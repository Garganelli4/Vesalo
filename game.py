from words import word_list
import random


izabrana = random.choice(word_list)

lista_karaktera = []
lista_pogodaka = []
broj_karaktera = 0
broj_pokusaja = 6

for karakter in izabrana:
    if karakter == " ":
        lista_karaktera.append(" ")
        lista_pogodaka.append(" ")
    else:
        lista_karaktera.append(karakter)
        lista_pogodaka.append("_")
        broj_karaktera = broj_karaktera + 1


while broj_pokusaja > 0 and broj_karaktera > 0:
    for karakter in lista_pogodaka:
        print("{0} ".format(karakter),end=" ")
    print("")
    print("Broj pokušaja: {0}".format(broj_pokusaja))
    unos = input("Unesite slovo: ")
    i = 0
    n = len(lista_karaktera)
    pronadjen = False
    while i < n:
        if lista_karaktera[i] == unos.lower():
            lista_pogodaka[i] = lista_karaktera[i]
            broj_karaktera = broj_karaktera - 1
            pronadjen = True
        i = i + 1
    if pronadjen == False:
        broj_pokusaja = broj_pokusaja - 1

if broj_karaktera == 0:
    print("Čestitamo! Reč je bila {0}".format(izabrana))
else:
    print("Nažalost ste izgubili. Reč je bila {0}".format(izabrana))