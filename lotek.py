from collections import Counter
import random
lista=[]
licz=3
for losowania in range(licz):
    los=random.sample(range(1,49),6)
    #los
    if los not in lista:
        lista.append(los)
for counter, value in enumerate(lista,1):           #wypisanie ponumerowanej zawartosci listy
    print(counter, value)
#c= dict(Counter(lista))
#print (c)




