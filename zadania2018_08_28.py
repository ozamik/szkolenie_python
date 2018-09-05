"""
Autor: Róża Spiliszewska
Kurs 
1. Proszę wprowadzić liczbę (funkcja_input).
Jeżeli liczba jest parzysta - ValueError;
jeżeli liczba< 0 - TypeError;
jeżeli liczba> 10 - IndexError.
Proszę wychwycić wyjątek i powiedzieć użytkownikowi w czym jego problem.
"""

print("Zadanie 1. Proszę wprowadzić liczbę (funkcja_input).")
print("Jeżeli liczba jest parzysta - ValueError;")
print("jeżeli liczba< 0 - TypeError;")
print("jeżeli liczba> 10 - IndexError.")
print("Proszę wychwycić wyjątek i powiedzieć użytkownikowi w czym jego problem.")
print()

try:
    liczba=int(input("Podaj liczbę: "))
    if liczba < 0:
        raise TypeError ("liczba ujemna")
    if liczba > 10:
        raise IndexError ("liczba większa niż 10")
    if liczba%2 == 0:
        raise ValueError ("liczba parzysta")
except ValueError as v:
    print ("Exception: " ,v)
except TypeError as t:
    print ("Exception: " ,t)
except IndexError as i:
    print ("Exception: ", i)
else:
    print ("Nie znaleziono wyjątku. Twoja liczba jest prawidłowa.")


print()
print("Zapraszam do kolejnej gry.")
print()
print()

"""
2. Stworzyć listę.
Użytkownik może wprowadzić index listy, który chce zobaczyć.
Jeżeli taki index istnieje – proszę wyprowadzić jego do konsoli,
jeżeli nie – proszę zgłosić wyjątek z jego opisem.
"""


print("Zadanie 2. Stworzyć listę.")
print("Użytkownik może wprowadzić index listy, który chce zobaczyć.")
print("Jeżeli taki index istnieje – proszę wyprowadzić go do konsoli")
print("jeżeli nie – proszę zgłosić wyjątek z jego opisem.")
print()
print("Autor stworzył listę, o której nic nie wiesz.")
print("Podaj index i spóbuj zgadnąć index mniejszy niż gługość tej listy.")
lista = [11,"jabłko",15,"Adam",1,"drzewo",53,"raj","Ewa",62,74]
b = lista.index(74)
while True:
    a = int(input("Podaj liczbę: "))
    try:
        if b < a:
            raise ValueError ("za dużo")
    except ValueError as value:
        print ("Nie zgadłeś: ", value, "próbuj dalej")
    if b >= a:
        break
print("Brawo! Zgadłeś index w zakresie listy!")
print("Kryje się pod nim element:", lista[a],)

print()
print("Dziękuję za wspólną zabawę.")
print()
print()
