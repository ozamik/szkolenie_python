"""
1. Napisać program, który oblicza pole prostokąta. Jeżeli to jest kwadrat, to udostępnia daną informację.
"""

print ("Zad. 1. Kalkulatorek obliczający pole prostokąta na podstawie wzoru P=a*b")

print("Jeśli chcesz podać ułamek, użyj kropki zamiast przecinka. Liczby muszą być dodatnie.")
a = input ("Podaj w cm długość jednego boku: a = ")
b = input ("Podaj w cm długość drugiego boku: b = ")
if a == b:
    print ("To jest kwadrat, którego pole wynosi", float (a)*float(a), "cm^2")
else:
    print ("Pole prostokąta wynosi", float (a) * float (a), "cm^2")
print()
print()


"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++
2. Napisać program, który wyprowadza wszystkie liczby pierwsze od 0 do zadanej przez użytkownika liczby
"""

print ("Zad. 2. Wyprowadzenie liczb pierwszych w zakresie zadanym przez użytkownika.")

from random import randint

n = int(input("Do jakiej liczby szukać liczb pierwszych? Podaj górną granicę: "))
lista = []  # pusta lista

def pierwsza(i): #definicja liczby pierwszej - jeśli się nie dzieli na przez inne liczby niż 1 i sama 
    for j in range (2, i):
        if i%j == 0: #nie jest pierwsza
            return False
    return True

for i in range(2, n+1): #n+1, bo chcę, by n też był brany pod uwagę
    if pierwsza(i):
        lista.append(i) #dodaj do listy

print (lista)
print()
print()


"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++
3. Napisać prosty kalkulator
"""

print ("Zad. 3. Prosty kalkulatorek: dodaje, odejmuje, mnoży i dzieli dwie liczby.")
print ("Jeśli chcesz podać ułamek, zamiast przecinka użyj kropki!")

x = float((input ("Podaj pierwszą liczbę: x= ")))
y = float((input ("Podaj drugą liczbę: y= ")))

if y == "0":
    print ("Dzielnik nie może być zerem!")
    y = float((input ("Podaj ponownie drugą liczbę: y= ")))
else:
    print(" x + y = " + str(x + y))
    print(" x - y = " + str(x - y))
    print(" x * y = " + str(x * y))
    print(" x / y = " + str(x / y))

print()
print()


"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++
4. Napisz program, który wyprowadza wszystkie liczby % na 5 bez reszty w zadanym przez użytkownika przedziale
"""

print ("Zad. 4. Wyprowadzenie liczb podzielnych przez 5 bez reszty w zakresie zadanym przez użytkownika.")

from random import randint
a = int(input("Podaj dolną granicę przedziału: "))
b = int(input("Podaj górną granicę przedziału: "))
lista1 = []  # pusta lista

def podzielnaPrzez5(i): #definicja podzielnej przez 5 bez reszty 
    if i%5 == 0:
        return True
    else:
        return False
    
for i in range(a, b+1): #n+1, bo chcę, by n też był brany pod uwagę
    if podzielnaPrzez5(i):
        lista1.append(i) #dodaj do listy

print (lista1)

print()
print()


"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++
5. Stworzyć listę z 6 randomowych liczb i odsortować.
"""

print("Zad. 5. Tu sworzysz listę 6 dowolnych liczb, a ja je posortuję od najmniejszej do największej.")

print("Jeśli chcesz podać ułamek, użyj kropki zamiast przecinka")

print("Podaj kolejno 6 dowolnych liczb:")
a = float(input ("pierwsza liczba = "))
b = float(input ("druga liczba = "))
c = float(input ("trzecia liczba = "))
d = float(input ("czwarta liczba = "))
e = float(input ("piąta liczba = "))
f = float(input ("szósta liczba = "))

tablica = [a, b, c, d, e, f]

print("Tak wygląda ciąg podanych przez ciebie liczb:")
print(tablica)

tablica.sort()
print("Tak wygląda posortowana tablica z podanymi przez ciebie liczbami:")
print(tablica)

print()
print()


"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++
6. Stworzyć słownik z 5-ciu part int -> str, np {6: '6'}, i wyprowadzić każde znaczenie do konsoli osobno
"""

print("Zad. 6. Stworzyć słownik z 5-ciu part int -> str, np {6: '6'}, i wyprowadzić każde znaczenie do konsoli osobno. ")

slownik = {1 : "jeden", 2 : "dwa", 3 : "trzy", 4 : "cztery", 5 : "pięć"} 
print("Słownik z danymi:")
print(slownik)
print()

print("Dane ze słownika pogrupowane parami:")
for i in slownik: 
    print(i," - ", slownik[i]) 

print()
print()


"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++
7. Stworzyć tuple z 10 liczb i znaleźć min/max
"""

print("Zad. 7. Stworzyć listę z tuple z 10 liczb i znaleźć min/max. ")

lista7 = (1,12,5,8,0,26,126,2,1,-45)  # lista 10 liczb
print(lista7, "- lista danych")

print(min(lista7), " - minimum z listy")
print(max(lista7), " - maksimum z listy")

print()
print()


"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++
8. Stworzyć listę z 3 słów : ['Earth', 'Poland', 'Wroclaw'], i pojednać wszystko w jednym stringu:
'Earth -> Poland -> Wroclaw'
"""

print("Zad. 8. Stworzyć listę z 3 słów i połączyć je słowa w jeden ciąg: 'Earth -> Poland -> Wroclaw' ")

lista8 = ["Earth","Poland","Wroclaw"]
print(lista8)

p = lista8[0]
q = lista8[1]
r = lista8 [2]
print (p, "->", q,"->", r)

print()
print()


"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++
9. Rozbić string  '/bin:/usr/bin:/usr/local/bin' do osobnej listy po  ':'
"""

print("Zad. 9. Rozbić string  '/bin:/usr/bin:/usr/local/bin' do osobnej listy po  ':' ")

lista9 = ['/bin:/usr/bin:/usr/local/bin']
print(lista9)

s=":".join(lista9) #separator ":" w liście9
print(s)
print(s.split(":")) #wyświetl podzieloną listę

print()
print()


"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++
10. W przedziale [1,100] znaleźć wszystkie liczby, które dzielą się na 7 bez reszty.
"""

print ("Zad. 10. Wyprowadzenie liczb podzielnych przez 7 bez reszty w przedziale [1,100].")

lista10 = []  # pusta lista

def podzielnaPrzez7(i): #definicja podzielnej przez 7 bez reszty 
    if i%7 == 0:
        return True
    else:
        return False
    
for i in range(1, 101): #101, bo chcę, by 100 też był brany pod uwagę
    if podzielnaPrzez7(i):
        lista10.append(i) #dodaj do listy

print (lista10)

print()
print()


"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++
11. Stworzyć listę jakichkolwiek liczb 3x4, najpierw wyprowadzić wierszy, zatem kolumny.
"""

print("Zad. 11. Stworzyć listę jakichkolwiek liczb 3x4, najpierw wyprowadzić wiersze, potem kolumny.")

n = 3 #ilość wierszy
m = 4 #ilość kolumn
"""
generator macierzy dla n wierszy i m kolumn.
piersza część to wzór jak ma wypełnić kolumny (j przed 'for', czyli po kolei je numeruje)
druga część to wzór dla wierszy (nie ma nic przed 'for' więc nic nie robi z kolumnami).
"""
d = [[j for j in range(m)] for i in range(n)]
for row in d:
    print(' '.join([str(elem) for elem in row])) #wyświetla całą macierz
print()

print(d[0], "- pierwszy wiersz macierzy")
print(d[1], "- drugi wiersz macierzy")
print(d[2], "- trzeci wiersz macierzy")
print()

print("Poszczególne kolumny macierzy:") #wyświetla kolumny inaczej niż wiersze, bo Python czyta wierszami
for i in range(4):
    print("Kolumna {}".format(i))
    for row in d:
        print(row[i])
 
print()
print()

      
"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++
12. Stworzyć listę i wyprowadzić listę i index
"""

print ("Zad. 12. Stworzyć listę i wyprowadzić listę i index.")

lista12 = [11,15,123,23,53,1,"Anna",62,74]
print(lista12, "- moja lista")
a = lista12.index(53)
print(a, "- to index liczby 53 na liście")
b = lista12.index("Anna")
print(b, "- to index słowa 'Anna' na liście")
print()
print()


"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++
13.Stworzyć listę z 3 znaczeniami 'to-delete' i kilku innymi i zabrać wszystkie łancuchy 'to-delete'
"""

print("Zad. 13. Stworzyć listę z 3 znaczeniami 'to-delete' i kilku innymi i zabrać wszystkie łancuchy 'to-delete'.")
lista13 = ['to-delete', 'dont', 'not-to-do', 'to-delete', 'to-delete', 'anna', 3]
print("Lista oryginalna:")
print(lista13)
print("Lista bez usuniętych elementów:")
lista14 = [element for element in lista13 if element != 'to-delete']
print(lista14)
print()
print()


"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++
14. Sortowanie odwrotne: z listy od 1 do 10 wyprowadzić do konsoli w odwrotnym znaczeniu. 
"""
print()
print ("Zad. 14. Sortowanie odwrotne listy 1 do 10")
x = 10
tab = [x for x in range (1,11)]
print ("Tak wygląda oryginalna tablica:")
print (tab)
print ("Tak wygląda tablica wyświetlona od końca:")
print (tab[::-1])
print()
print ("Koniec zadań z pierwszej serii.")
input()
