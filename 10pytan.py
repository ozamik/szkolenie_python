"""
Programik - test z pierwszych zajęć z Pythona.
10 pytań.
Za prawidłową odpowiedź gracz dostaje punkt.
Brak odpowiedzi lub zła odpowiedź - zero punktów.
Podsumowanie:
- ilość pytań,
- ilość udzielonych odpowiedzi,
- ilość odpowiedzi prawidłowych,
- procent prawidłowych odpowiedzi względem zadanych pytań.
Autor: Róża Spiliszewska
Data: 16.08 2018
"""

name=input('Jak masz na imię? ')
print ()
print('Hej', name+ ', zapraszam do gry z podstaw Pythona!')
print('Zabawa zawiera 10 pytań podstawowych z Pythona z pierwszej lekcji.')
print('Za każdą dobrą odpowiedź gracz dostaje 1 punkt.')
print('Za brak odpowiedzi i za złą odpowiedź gracz dostaje 0 punktów.')
print('Na końcu program zlicza udzielone odpowiedzi, odpowiedzi prawidłowe i procent odpowiedzi prawidłowych względem zadanych pytań.')
print ()
print ('Udanej zabawy!')
print ()

# zmienne:
nr = 1 # numer pytania
punkty = 0 # ilość punktów łącznie = liczba prawidłowych odpowiedzi
iloscOdpowiedzi = 0 # ilość udzielonych odpowiedzi

#Pytanie nr 1 - o język programowania
print("Pytanie nr ", (nr),":")
odpowiedz=input("Jak nazywa się język programowania, którego dotyczy ta gra? ")
odpowiedz=odpowiedz.lower()
if odpowiedz == 'python' or odpowiedz =='pyton' or odpowiedz =='pajton':
    print("Brawo - otrzymujesz 1 punkt.")
    punkty = punkty+1 #suma punktów za odpowiedzi zliczana po każdej odpowiedzi
    iloscOdpowiedzi += 1 #suma udzielonych odpowiedzi
    print("Zdobyłeś punktów:", (punkty))
elif odpowiedz == (""):
    print ("Nie udzielono odpowiedzi. Zadam Ci kolejne pytanie.")
else:
    print ("Zła odpowiedź, otrzymujesz 0 punktów. Zadam Ci kolejne pytanie.")
    iloscOdpowiedzi += 1 #suma udzielonych odpowiedzi
print ()

#Pytanie nr 2 - o firmę, w której pracujesz
nr+=1
print("Pytanie nr ", (nr),":")
odpowiedz=input("Jak nazywa się firma, w której pracujesz? Podaj jednowyrazową nazwę. ")
odpowiedz=odpowiedz.lower()
if odpowiedz == 'nokia':
    print("Brawo - otrzymujesz 1 punkt.")
    punkty = punkty+1 
    iloscOdpowiedzi +=1
    print("Zdobyłeś punktów:", (punkty))
elif odpowiedz == (""):
    print ("Nie udzielono odpowiedzi. Zadam Ci kolejne pytanie.")
else:
    print ("Zła odpowiedź, otrzymujesz 0 punktów. Zadam Ci kolejne pytanie.")
    iloscOdpowiedzi+=1
print ()

#Pytanie nr 3 - o imię prowadzącego
nr+=1
print("Pytanie nr ", (nr),":")
odpowiedz=input("Jak ma na imię prowadząca szkolenie? ")
odpowiedz=odpowiedz.lower()
if odpowiedz == "Tatsiana" or odpowiedz == "tatsiana":
    print("Brawo - otrzymujesz 1 punkt.")
    punkty = punkty+1 
    iloscOdpowiedzi = iloscOdpowiedzi+1
    print("Zdobyłeś punktów:", (punkty))
elif odpowiedz == (""):
    print ("Nie udzielono odpowiedzi. Zadam Ci kolejne pytanie.")
elif odpowiedz == ("tatiana") or odpowiedz == ("tatjana"):
    print ("Zła odpowiedź. Lepiej sprawdź prawidłową pisownię imienia.")
    iloscOdpowiedzi+=1
else:
    print ("Zła odpowiedź, otrzymujesz 0 punktów. Zadam Ci kolejne pytanie.")
    iloscOdpowiedzi+=1
print ()

#Pytanie nr 4 - o uzgodnioną wersję języka
nr+=1
print("Pytanie nr ", (nr),":")
odpowiedz=input("Na pierwszych zajęciach uzgodniliśmy, że będziemy używać jednej wersji Pythona. Jakiej? Wybierz 2 lub 3: ")
if odpowiedz == "3" :
    print("Brawo - otrzymujesz 1 punkt.")
    punkty = punkty+1
    iloscOdpowiedzi = iloscOdpowiedzi+1
    print("Zdobyłeś punktów:", (punkty))
elif odpowiedz == (""):
    print ("Nie udzielono odpowiedzi. Zadam Ci kolejne pytanie.")
else:
    print ("Zła odpowiedź, otrzymujesz 0 punktów. Zadam Ci kolejne pytanie.")
    iloscOdpowiedzi+=1
print ()

#Pytanie nr 5 - o pierwsze zdanie w Pythonie
nr+=1
print("Pytanie nr ", (nr),":")
odpowiedz=input("Jak brzmiało pierwsze zdanie napisane przez nas w Pythonie? Podpowiedź: po angielsku znaczy tyle co >>Witaj świecie<< ")
odpowiedz=odpowiedz.lower()
if odpowiedz == "hello world" or odpowiedz == "hello world!" or odpowiedz == "Hello word" or odpowiedz == "Hello word!":
    print("Brawo - otrzymujesz 1 punkt.")
    punkty = punkty+1
    iloscOdpowiedzi = iloscOdpowiedzi+1
    print("Zdobyłeś punktów:", (punkty))
elif odpowiedz == (""):
    print ("Nie udzielono odpowiedzi. Zadam Ci kolejne pytanie.")
else:
    print ("Zła odpowiedź, otrzymujesz 0 punktów. Zadam Ci kolejne pytanie.")
    iloscOdpowiedzi+=1
print ()

#Pytanie nr 6 - o cudzysłów
nr+=1
print("Pytanie nr ", (nr),":")
odpowiedz=input('Czy trzeba używać jednakowych znaków cudzysłowia w jednym ciągu np. (" ") lub (\' \') ? ')
odpowiedz=odpowiedz.lower()
if odpowiedz == "Tak" :
    print("Brawo - otrzymujesz 1 punkt.")
    punkty = punkty+1
    iloscOdpowiedzi = iloscOdpowiedzi+1
    print("Zdobyłeś punktów:", (punkty))
elif odpowiedz == (""):
    print ("Nie udzielono odpowiedzi. Zadam Ci kolejne pytanie.")
else:
    print ("Zła odpowiedź, otrzymujesz 0 punktów. Zadam Ci kolejne pytanie.")
    iloscOdpowiedzi+=1
print ()

#Pytanie nr 7 - o znaki matematyczne
nr+=1
print("Pytanie nr ", (nr),":")
odpowiedz=input("Czy w Pythonie znaki: + ; - ; * ; / to zwykłe matematyczne działania (dodawanie, odejmowanie, mnożenie, dzielenie? ")
odpowiedz=odpowiedz.lower()
if odpowiedz == "tak" :
    print("Brawo - otrzymujesz 1 punkt.")
    punkty = punkty+1
    iloscOdpowiedzi = iloscOdpowiedzi+1
    print("Zdobyłeś punktów:", (punkty))
elif odpowiedz == (""):
    print ("Nie udzielono odpowiedzi. Zadam Ci kolejne pytanie.")
else:
    print ("Zła odpowiedź, otrzymujesz 0 punktów. Zadam Ci kolejne pytanie.")
    iloscOdpowiedzi+=1
print ()


#Pytanie nr 8 - o potęgę
nr+=1
print("Pytanie nr ", (nr),":")
odpowiedz=input("Ile wynosi 2**3? ")
odpowiedz=odpowiedz.lower()
if odpowiedz == "8" :
    print("Brawo - otrzymujesz 1 punkt.")
    punkty = punkty+1
    iloscOdpowiedzi = iloscOdpowiedzi+1
    print("Zdobyłeś punktów:", (punkty))
elif odpowiedz == (""):
    print ("Nie udzielono odpowiedzi. Zadam Ci kolejne pytanie.")
else:
    print ("Zła odpowiedź, otrzymujesz 0 punktów. Zadam Ci kolejne pytanie.")
    iloscOdpowiedzi+=1
print ()


#Pytanie nr 9 - o porównanie
nr+=1
print("Pytanie nr ", (nr),":")
odpowiedz=input("Czy za pomocą znaku == można dokonać porównania wielkości? ")
odpowiedz=odpowiedz.lower()
if odpowiedz == "tak" :
    print("Brawo - otrzymujesz 1 punkt.")
    punkty = punkty+1
    iloscOdpowiedzi = iloscOdpowiedzi+1
    print("Zdobyłeś punktów:", (punkty))
elif odpowiedz == (""):
    print ("Nie udzielono odpowiedzi. Zadam Ci kolejne pytanie.")
else:
    print ("Zła odpowiedź, otrzymujesz 0 punktów. Zadam Ci kolejne pytanie.")
    iloscOdpowiedzi+=1
print ()


#Pytanie nr 10 - o znak nierówności 
nr+=1
print("Pytanie nr ", (nr),":")
odpowiedz=input("Czy znak != oznacza nierówność? ")
odpowiedz=odpowiedz.lower()
if odpowiedz == "tak" :
    print("Brawo - otrzymujesz 1 punkt.")
    punkty = punkty+1
    iloscOdpowiedzi = iloscOdpowiedzi+1
    print("Zdobyłeś punktów:", (punkty))
elif odpowiedz == (""):
    print ("Nie udzielono odpowiedzi. Zadam Ci kolejne pytanie.")
else:
    print ("Zła odpowiedź, otrzymujesz 0 punktów. Zadam Ci kolejne pytanie.")
    iloscOdpowiedzi+=1
print ()

print ()
print ("To było ostatnie pytanie. Poniżej podsumowanie zabawy:")
print (" - ilość zadnych pytań wynosi", (nr))
print (" - ilość udzielonych odpowiedzi wynosi", (iloscOdpowiedzi))
print (" - ilość prawidłowych odpowiedzi wynosi", (punkty))
procent = 100*punkty//nr
print (" - procent prawidłowych odpowiedzi wynosi", (procent),"%" )
if procent >=60:
    print ("Gratulacje,", (name),"! Jesteś naprawdę dobrym graczem :-)")
elif procent>=40 and procent <60:
    print ((name),", jest dobrze, może być jeszcze lepiej!")
else:
    print ((name),", chyba nie byłeś na pierwszych zajęciach.")
print ("Dziękuję za wspólną zabawę :-)")
input()
