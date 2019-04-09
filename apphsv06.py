# AppHS
# Aplikacja prowadzi rejestr członków stowarzyszenia Hackerspace


# ******** FUNKCJE ********
# Funkcja sprawdzająca poprawność wprowadzonego tekstu i zwracająca poprawny tekst
# import sqlite3
# import sqlite3
#
# import MySQLdb as mysql1
import linecache

from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)


def SprawdzenieTekstu(typ, tekst_zachety, komunikat_bledu):
    tekst_do_sprawdzenia = ''
    while not tekst_do_sprawdzenia.isalpha():
        tekst = input(tekst_zachety)
        if typ == 'proste':
            tekst_do_sprawdzenia = tekst
        elif typ == 'złożone':
            tekst_do_sprawdzenia = tekst.replace(' ', '')
            tekst_do_sprawdzenia = tekst_do_sprawdzenia.replace('-', '')
        if not tekst_do_sprawdzenia.isalpha():
            print(komunikat_bledu)
    return tekst



# Funkcja sprawdzająca poprawność wprowadzonej liczby i zwracająca poprawnę liczbę
def SprawdzenieLiczby(tekst_zachety, komunikat_bledu, dolna_granica, gorna_granica):
    liczba = ''
    while not liczba.isdigit():
        liczba = input(tekst_zachety)
        if not liczba.isdigit():
            print(komunikat_bledu)
            liczba = ''
        elif not int(liczba) in range(dolna_granica, gorna_granica + 1):
            print(komunikat_bledu)
            liczba = ''
    return int(liczba)



# ******** PROCEDURY ********
# Procedura wyświetlająca listę członków stowarzyszenia
def ListaCzlonkow():
    # lista_czlonkow = open('lista_czlonkow.txt').read()
    print('Lista członków stowarzyszenia: ')
    print(open('lista_czlonkow.txt').read())

# Procedura dodająca członków stowarzyszenia do pliku lista_czlonków.txt i wyświetlająca dane każdego dodanego członka
def DodawanieCzlonkow():
    ilosc_dodawanych_czlonkow = SprawdzenieLiczby('Podaj ilu członków dodajesz do listy: ',

                                                'To nie jest poprawna liczba członków.\nWprowadź liczbę od 1 do 10.', 1, 10)

    for n in range(ilosc_dodawanych_czlonkow):
        imie_czlonka = SprawdzenieTekstu('proste', 'Podaj imię: ', \

                                        'To nie jest poprawne imię!\nPoprawne imię składa się wyłącznie z liter.')

        nazwisko_czlonka = SprawdzenieTekstu('złożone', 'Podaj nazwisko: ', \

                                            'To nie jest poprawne nazwisko!\nPoprawne nazwisko składa sie wyłącznie z liter spacji i myślników.')

        rok_urodzenia = SprawdzenieLiczby('Podaj rok urodzenia: ', \

                                        'Musisz podać rok pomiędzy 1880 a obecnym.', 1880, teraz.year)

        wiek = teraz.year - rok_urodzenia
        lista_czlonkow = open('lista_czlonkow.txt', 'a')
        if linecache.getline('lista_czlonkow.txt', 1) == '':
            nowy = [n + 1, imie_czlonka, nazwisko_czlonka, rok_urodzenia]
            lista_czlonkow.write(str(nowy) + '\n')
            lista_czlonkow.close()
            print('Dodano:\n' + imie_czlonka, nazwisko_czlonka + '\nRok urodzenia:', rok_urodzenia, 'Wiek:', wiek)
        else:
            fileHandle = open('lista_czlonkow.txt', "r")
            lineList = fileHandle.readlines()
            fileHandle.close()
            nowy = [len(lineList)+1, imie_czlonka, nazwisko_czlonka, rok_urodzenia]
            lista_czlonkow.write(str(nowy) + '\n')
            lista_czlonkow.close()
            print('Dodano:\n' + imie_czlonka, nazwisko_czlonka + '\nRok urodzenia:', rok_urodzenia, 'Wiek:', wiek)

# Procedura dodająca członków stowarzyszenia do pliku lista_czlonków.txt i wyświetlająca dane każdego dodanego członka
def EdycjaCzlonkow():
    print('Lista członków stowarzyszenia: ')
    print(open('lista_czlonkow.txt').read())
    nr_wiesza_do_edycji = SprawdzenieLiczby('\nPodaj nr wiersza do edycji: ',

                                                'To nie jest poprawny nr wiersza.\nWprowadź liczbę od 1 do 10.', 1, 10)


    imie_czlonka = SprawdzenieTekstu('proste', 'Podaj imię: ', \

                                        'To nie jest poprawne imię!\nPoprawne imię składa się wyłącznie z liter.')

    nazwisko_czlonka = SprawdzenieTekstu('złożone', 'Podaj nazwisko: ', \

                                            'To nie jest poprawne nazwisko!\nPoprawne nazwisko składa sie wyłącznie z liter spacji i myślników.')

    rok_urodzenia = SprawdzenieLiczby('Podaj rok urodzenia: ', \

                                        'Musisz podać rok pomiędzy 1880 a obecnym.', 1880, teraz.year)

    edytowany = [nr_wiesza_do_edycji, imie_czlonka, nazwisko_czlonka, rok_urodzenia]
    edytowanyStr = str(edytowany)+'\n'
    tmp = linecache.getline('lista_czlonkow.txt', nr_wiesza_do_edycji)
    replace('lista_czlonkow.txt', tmp, edytowanyStr)
    print('Lista członków stowarzyszenia: ')
    print(open('lista_czlonkow.txt').read())

# ******** GŁÓWNY PROGRAM ********
# Pobranie aktualnej daty i czasu

import datetime
teraz = datetime.datetime.now()

# Menu główne
pozycja_menu = 0
while pozycja_menu != 4:
    pozycja_menu = SprawdzenieLiczby('''1 - Lista członków stowarzyszenia
2 - Dodanie nowych danych
3 - Edycja listy czlonkow
4 - Koniec programu
Wybierz polecenie: ''', \
'To nie jest poprawne polecenie.\nWybierz jedną z dostępnych opcji 1 do 4', 1, 4)
    if pozycja_menu == 1:
        ListaCzlonkow()
    elif pozycja_menu == 2:
        DodawanieCzlonkow()
    elif pozycja_menu == 3:
        EdycjaCzlonkow()

# Koniec
input('Aby zakończyć naciśnij klawisz ENTER.')


# modul standardowy pythona potrzebny do wykonania zadania, dodac zeby
# indeks bazy danych przy dodawaniu recordu poprawnie ikrementowal licznik
# czyli import linecache, pobranie danego wiersza