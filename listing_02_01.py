# Sprawdzenie typu danych i pętla

# Pobieranie imienia użytkownika do zmiennej imie
imie = input('Podaj swoje imię: ')

# Pobranie aktualnej daty i czasu
import datetime
teraz = datetime.datetime.now()


# Pobieranie roku urodzenia użytkownika do zmiennej rok oraz zdefiniowanie typu
sprawdzenie = ''
while sprawdzenie != 1:
    rok_urodzenia = input('Podaj swój rok urodzenia: ')
    try:
        rok_urodzenia = int(rok_urodzenia)
        if rok_urodzenia < teraz.year - 150:
            print('Naprawdę urodziłeś się ponad 150 lat temu?')
        elif rok_urodzenia > teraz.year:
            print('Jeszcze nie ma takiego roku!')
        elif rok_urodzenia == teraz.year:
            print('Naprawdę nie masz jeszcze roku?')
        else:
            sprawdzenie = 1
    except ValueError:
        tmp = float(rok_urodzenia)
        if rok_urodzenia == tmp:
            print('To jest ułamek a nie poprawny rok!')
        else:
            print('To nie jest liczba!')

wiek = teraz.year - rok_urodzenia

if wiek >= 10:
    ostatnia_cyfra = wiek % 10
else:
    ostatnia_cyfra = wiek

if wiek == 1:
    odmiana = 'rok'
elif ostatnia_cyfra == 2:
    odmiana = 'lata'
elif ostatnia_cyfra == 3:
    odmiana = 'lata'
elif ostatnia_cyfra == 4:
    odmiana = 'lata'
else:
    odmiana = 'lat'


# home work after lessons 2
if imie.endswith('a'):
    print('Mamy rok', str(teraz.year) + '.', 'Masz więc', wiek, odmiana+'.', imie[0:len(imie)-1]+imie[-1].replace('a', 'o')+'! jak na kobiete to calkiem niezle')
else:
    print('Mamy rok', str(teraz.year) + '.', 'Masz więc', wiek, odmiana+'.', imie+'! jak na faceta to calkiem niezle')


