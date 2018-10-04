"""
Python 3.6.
Autor: Róża Spiliszewska
03.10.2018
"""
"""
Zad. 1: Gra 'zgadnij liczbę'.
"""
print("Zad.1 Gra zgadnij liczbę.")
print("Zasady gry:")
print("Podam ci przedział, w jakim znajduje się zgadywana liczba.")
print("Jest to liczba całkowita, wybrana losowo przez komputer z podanego przedziału.")
print("Poproszę Cię o podanie ile prób chcesz podjąć.")

from random import randint
liczba = randint(1,21)

print("Komputer wylosował liczbę całkowitą z przedziału 1-20.")
n = int(input("Ile chcesz podjąć prób: "))

print("No to zaczynamy!")

for j in range(n):
    odp = int(input("Zgadnij jaka to liczba: "))
    if odp > 20:
       print("Podałeś liczbę spoza przedziału (1-20). Straciłeś jedną próbę.")
    elif liczba < odp:
       print("Za dużo...")
    elif liczba > odp:
       print("Za mało...")
    else:
       print("Gratuluję! Zgadłeś! Znasz logikę random w Pythonie!")
       break

print("Wyczerpałeś ilość prób.")
print("Wylosowana liczba to: ", liczba)
print()
print()
print("---------------")



"""
Zad. 2: Gra 'kółko i krzyżyk'.
"""

from random import randint #import liczb z random

#dane
X = 'X'#gracz
O = 'O'#komputer
EMPTY = ' '#puste pole na tablicy
CONT = 9#ilość pól tablicy
board = []#pusta tablica

print('Zadanie nr 2. Zabawa w kółko i krzyżyk z komputerem.')
print("Zasady: gracz gra 'X', komputer gra 'O'. Gracz może wybrać czy chce rozpocząć grę.")
print("Komputer losowo zajmuje pole wypełniając je kółkiem.")
print("Komputer nie jest inteligentny - wybiera pola losowo!")
print("Wygrywa ten, kto uzyska swoje znaki w trzech polach znajdujących się w jednej linii(poziomej, pionowej, przekątnej.")

#definicje
def addboard():#dodawanie do tablicy w zakresie CONT
    for i in range(CONT):
        board.append(i)
    return board

board = addboard()#zmiana w tablicy - teraz będzie dodawac

def clearboard():#pusta tablica bez ponumerowanych pól
    for i in range(CONT):
       board[i] = EMPTY

def white_board(board):#tablica z ponumerowanymi polami
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "_________")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "_________")
    print("\n\t", board[6], "|", board[7], "|", board[8], "\n")
    
def check_number(number):#sprawdzenie numeru pola
    while number not in range(0,9):#sprawdzanie czy podane pole jest na tablicy
        number = int(input('Pole poza zakresem! Wybierz pole między 0 a 8: '))
    while board[number] != ' ':#sprawdzenie czy pole jest zajęte
        number = int(input('Pole zajęte! Wybierz inne wolne pole: '))
    return number

def computer_move(board):#komputer losowo zajmuje puste pole
    while True:
        move = randint(0,8)
        if board[move] == EMPTY:
            return move

def winner(board):#definicja zwycięstwa
    a = ((0,1,2), (3,4,5), (6,7,8),#linie poziome
         (0,3,6), (1,4,7), (2,5,8),#linie pionowe
         (0,4,8), (2,4,6)) #linie ukośne
    for i in a:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            if board[i[0]] == O:
                return 0
            elif board[i[0]] == X:
                return 1
    return None#jak nikt nie wygrywa

#Zaczynamy grę
white_board(board)#wywołanie tablicy z numerowanymi polami

# wybór gracza zaczynającego
if 't' == input('Chcesz grać jako pierwszy (t/n)? '):
    clearboard()#czysta tablica
    box = int(input('Wybierz pole: '))
    board[check_number(box)] = X
    white_board(board)#wywołanie tablicy z wyborem gracza
    print('Ruch komputera:')
    board[computer_move(board)] = O
    white_board(board)#wywołanie tablicy z wyborem gracza i komputera
    #dalsza gra w pętli aż do zwycięstwa sprawdzanego po każdym ruchu   
    for movie in range (2,6):
        box = int(input('Wybierz pole: '))
        board[check_number(box)] = X
        white_board(board)
        win = winner(board)#sprawdzanie zwycięzcy po każdym ruchu gracza 
        if win == 0:
            print("Gra skończona, wygrał komputer.")
            break
        elif win == 1:
            print("Brawo! Wygrałeś!")
            break
        print('Ruch komputera:')
        board[computer_move(board)] = O
        white_board(board)
        win = winner(board)#sprawdzanie zwycięzcy po każdym ruchu komputera
        if win == 0:
            print("Gra skończona, wygrał komputer.")
            break
        elif win == 1:
            print("Brawo! Wygrałeś!")
            break

else:#odwrotnie niż powyżej zaczyna grę komputer
    clearboard()
    print('Ruch komputera:')
    board[computer_move(board)] = O
    white_board(board)
    box = int(input('Wybierz pole: '))
    board[check_number(box)] = X
    white_board(board)
    #dalsza gra w pętli aż do zwycięstwa sprawdzanego po każdym ruchu    
    for movie in range (2,6):
        print('Ruch komputera:')
        board[computer_move(board)] = O
        white_board(board)
        win = winner(board)
        if win == 0:
            print("Gra skończona, wygrał komputer.")
            break
        elif win == 1:
            print("Brawo! Wygrałeś!")
            break
        box = int(input('Wybierz pole: '))
        board[check_number(box)] = X
        white_board(board)
        win = winner(board)
        if win == 0:
            print("Gra skończona, wygrał komputer.")
            break
        elif win == 1:
            print("Brawo! Wygrałeś!")
            break
       
print()
print()
print("---------------")       
print("Koniec gry. Kliknij dowolny klawisz, żeby zamknąć okno.")
input()
    
