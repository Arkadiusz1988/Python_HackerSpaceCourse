# Aplikacja prowadzi rejestr członków stowarzyszenia Hackerspace


# ******** FUNKCJE ********
# Funkcja sprawdzająca poprawność wprowadzonego tekstu i zwracająca poprawny tekst
# import sqlite3
# import sqlite3
#
import linecache
import MySQLdb as mysql

try:
    moja_baza = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = "coderslab",
        database ="pytNowa"
    )
    wskaznik = moja_baza.cursor()
except (mysql.Error, mysql.Warning) as e:
    print(e)
# wskaznik.execute("CREATE TABLE lista_czlonkow (id INT AUTO_INCREMENT PRIMARY KEY, imie VARCHAR(255), nazwisko VARCHAR(255), wiek int )")


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

def kasowanie():
    print("podaj id wiersza do usuniecia?")
    usunWiersz=input()
    # moja_baza.cursor().execute("DELETE FROM `pytNowa`.`lista_czlonkow` WHERE `id` = ",usunWiersz)
    try:
        query = "DELETE FROM `pytNowa`.`lista_czlonkow` WHERE id = %s"
        moja_baza.cursor().execute(query, usunWiersz)
        moja_baza.commit()
        print("delete successfull")
    except (mysql.Error, mysql.Warning) as e:
        print(e)

# ******** PROCEDURY ********
# Procedura wyświetlająca listę członków stowarzyszenia
def ListaCzlonkow():
    try:
        print('Lista członków stowarzyszenia: ')
        print(open('lista_czlonkow.txt').read())
    except FileNotFoundError:
        print('taki plik nie istnieje badz niepoprawna sciezka')


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

        wiek1 = teraz.year - rok_urodzenia
        try:
            moja_baza.cursor().execute("INSERT INTO `pytNowa`.`lista_czlonkow` VALUES (%s,%s,%s,%s)", (0,imie_czlonka, nazwisko_czlonka,wiek1))
            moja_baza.commit()
            print("add successfull")
        except (mysql.Error, mysql.Warning) as e:
            print(e)

def EdycjaCzlonkow():
    ListaCzlonkow()
    nr_wiesza_do_edycji = SprawdzenieLiczby('\nPodaj nr wiersza do edycji: ',

                                                'To nie jest poprawny nr wiersza.\nWprowadź liczbę od 1 do 10.', 1, 10)


    imie_czlonka = SprawdzenieTekstu('proste', 'Podaj imię: ', \

                                        'To nie jest poprawne imię!\nPoprawne imię składa się wyłącznie z liter.')

    nazwisko_czlonka = SprawdzenieTekstu('złożone', 'Podaj nazwisko: ', \

                                            'To nie jest poprawne nazwisko!\nPoprawne nazwisko składa sie wyłącznie z liter spacji i myślników.')

    rok_urodzenia = SprawdzenieLiczby('Podaj rok urodzenia: ', \

                                        'Musisz podać rok pomiędzy 1880 a obecnym.', 1880, teraz.year)
    try:
        moja_baza.cursor().execute("update lista_czlonkow set imie=%s, nazwisko=%s, wiek=%s where id=%s", (imie_czlonka, nazwisko_czlonka, rok_urodzenia, nr_wiesza_do_edycji))
        moja_baza.commit()
        print("udpate successfull")
    except (mysql.Error, mysql.Warning) as e:
        print(e)

# ******** GŁÓWNY PROGRAM ********
# Pobranie aktualnej daty i czasu

import datetime
teraz = datetime.datetime.now()

# Menu główne
pozycja_menu = 0
while pozycja_menu != 5:
    pozycja_menu = SprawdzenieLiczby('''1 - Lista członków stowarzyszenia
2 - Dodanie nowych danych
3 - Edycja listy czlonkow
4 - Kasowanie Członkow
5 - Koniec programu
Wybierz polecenie: ''', \
'To nie jest poprawne polecenie.\nWybierz jedną z dostępnych opcji 1 do 5', 1, 5)
    if pozycja_menu == 1:
        ListaCzlonkow()
    elif pozycja_menu == 2:
        DodawanieCzlonkow()
    elif pozycja_menu == 3:
        EdycjaCzlonkow()
    elif pozycja_menu == 4:
        kasowanie()

# Koniec
input('Aby zakończyć naciśnij klawisz ENTER.')
