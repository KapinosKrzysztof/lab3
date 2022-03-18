#zad 1
'''
a = [1-x for x in range(1,11)]
b = [4**i for i in range(1,8)]
c = [x for x in b if x % 2 == 0]

print(a)
print(b)
print(c)
'''

#zad 2
'''
from random import randint

lista = []

for i in range(0, 10):
    lista.append(randint(0, 100))
    lista = [i for i in lista if i % 2 == 0]
print(lista)
'''

#zad3


'''
slownik = {'chleb': 'szt', 'sok': 'litry','bółki': 'szt', 'jabłka': 'kilogramy', 'batony': 'szt'}
lista=slownik.items()
sztuki=[]
for i in lista:
  if "szt" in i:
   sztuki.append(i)
print(sztuki)
'''

#zad 4

'''
a = input("Podaj długość pierwszego boku")
b = input("Podaj długość drugiego boku")
c = input("Podaj długość trzeciego boku")

boki = [a, b, c]
boki.sort()
print(boki)

if (int(boki[0])**2)+(int(boki[1])**2)==(int(boki[2])**2):
    print("to jest trójkąt prostokątny")
else:
    print("to nie jest trójkąt prostokątny")
  '''


#zad5

'''
def trapez(a,b,h):
 print (((a+b)*h)/2)
 return a,b,h
print(trapez(1,2,3))
print(trapez(4,5,6))
print(trapez(7,8,9))

'''

#zad6

'''
def iloczyn(a,b,ile):
    while 0 < ile:
        ile -= 1
        print(a*b)
        a += 1
    return "koniec"
print(iloczyn(1,4,10))
'''

#zad7 nie zrobione
'''
def iloczyn(a,b,ile):
    while 0 < ile:
        ile -= 1
        print(a*b)
        a += 1
    return "koniec"
print(iloczyn(1,4,10))
'''
#zad 8
'''
def zakupy(** lista):
    suma = 0
    ilosc = 0
    for i in lista:
        suma += lista[i]
        ilosc += 1

    print("suma zakupów to",+ suma)
    print("ilość kupionych rzeczy to", + ilosc)
zakupy(a=1, b=1,c=1,d=1,e=1,f=1)
'''
#zad 10
'''
lista=[]
for i in range(101):
    if i % 4 == 0:
        lista.append(i)
print(lista)
plik = open("zad.txt","w")
if plik.writable():
    plik.write(str(lista))
plik.close()
'''
#zad11
'''
plik = open("zad.txt", "r")
if plik.readable():
    tekst = plik.read()
    print(tekst)
plik.close()
'''
