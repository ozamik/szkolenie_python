"""
Napisane w Python 3.7.
Autor: Róża Spiliszewska
Kurs: Python podstawy
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Zadanie 1. Proszę o napisanie funkcji, która otrzymuje jakąkolwiek ilość agrumentów,znajduje max i min i wyprowadza do konsoli.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

print ("Zadanie 1. Kalkulatorek wyszukujący wartość max i min z podanych przez gracza liczb.")

print("Podaj liczby całkowite. Liczby mogą być dodatnie i ujemne.")

lista = [] #pusta lista, do której wpiszą się liczby podane przez gracza
i = int(input("Podaj liczbę "))
lista.append(i) #dodaje podawane liczby do listy

while True: #pętla dodawania kolejnych liczb do listy
    i = int(input ("Podaj kolejną liczbę: "))
    lista.append(i)
    j = input ("Czy to ostatnia liczba (t/n): ")
    if j == "t":
        break

def liczba_max(input_i): #definicja liczby maksymalnej z podanych przez gracza
    return max(lista)
maksymalna = liczba_max(lista)

def liczba_min(input_i): #definicja liczby minimalnej z podanych przez gracza
    return min(lista)
minimalna = liczba_min(lista)

print("Lista wprowadzonych liczb:")
print(lista)
print("Liczba maksymalna:", maksymalna)
print("Liczba minimalna:", minimalna)

print()
print()

"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Zadanie 2. Proszę o napisanie funkcji, która ma 2 argumenty: str i flagę (jako typ bool), która domyślnie jest ustawiona na True.
Jeżeli flaga jest prawdziwa - to proszę wyprowadzić string do konsoli duzymi literami, jak nie - małymi.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

print ("Zadanie 2. String i flaga. Jeśli zgadłeś, to wypiszę stringa dużymi literami.")
print ("Zadanie dotyczyć będzie miast Polski (według GUS na dzień 31.12.2017 r.)")
print()
i = input ("Jakie jest największe miasto w Polsce? ")
lista1 = ["Warszawa", "warszawa"]

def miasto_max(flaga = True, name="warszawa"): #definicja największego miasta
    if flaga:
        print("Zgadłeś, to jest", i.upper())

if i in lista1:
    najwieksze = miasto_max(i)
else:
        print("Niestety to nie jest", i.lower())

print()
print("Teraz trudniejsze pytanie.")
print()
j = input ("Które miasto ma więcej mieszkańców: Kraków czy Wrocław? ")
lista2 = ["Kraków", "kraków", "krakow"]

def miasto_drugie(flaga = True, name="kraków"): #definicja drugiego miasta
    if flaga:
        print("Zgadłeś, to jest", j.upper(),"- na koniec 2017 r. miał prawie 770 tys. mieszkańców.")

if j in lista2:
    drugie = miasto_drugie(j)
else:
    print("Niestety to nie jest", j.lower(), "- na koniec 2017 r. miał ponad 100 tys. mieszkańców mniej niż Kraków.")
print()
print()
print()

"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
3. Proszę o napisanie funkcji, która przyjmuje nieokreśloną ilość argumentów typu string i jeden argument glue=':'.
Połączyć wszystkie słowa większe niż 3 litery za pomocą argumentu glue.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

print ("Zadanie 3. String i glue. Podasz mi słowa a ja skleję te, które mają więcej niż 3 litery.")
print ("Spróbuj wynik wymówić na głos ;-)")
print()

#dane
lista3 = [] #lista wszystkich podanych słów
lista4 = [] #lista słów > 3 liter

slowo = input("Podaj słowo: ")
print("Długość słowa:", len(slowo))#kontrolne wyświetlenie długości

#definicje

def slowo_3(slowo): #definicja słowa>3 liter dodaje do lista4
    if len(slowo) > 3:
        lista4.append(slowo)
    return lista4

def klej(lista4, glue=":"): #definicja sklejanie słów glutem z lista4
    s = glue.join(lista4)
    return s

#zaczynamy
lista3.append(slowo) #dodaje do listy wszystkich słów
dlugie = slowo_3(slowo)#wywołanie funkcji wyszukiwania słów>3

while True: #pętla dodawania słów do obu list
    slowo = input ("Podaj kolejne słowo: ")
    print("Długość słowa:", len(slowo))#kontrolne wyświetlenie długości
    lista3.append(slowo)
    koniec = input ("Czy to ostatnie słowo (t/n): ")
    dlugie = slowo_3(slowo)#wyszukuje słowa>3 liter
    if koniec == "t":
        break
s = klej(lista4) #sklejenie słów>3 liter

print("Lista podanych słów:", lista3)        
print("Lista słów dłuższych niż 3-literowe:", lista4)
print("Lista sklejonych za pomocą ':' słów dłuższych niż 3-literowe:")
print(s)
print()


input()
