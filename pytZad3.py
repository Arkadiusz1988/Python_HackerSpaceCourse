
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

pozycja_menu = 0
while pozycja_menu != 5:
    pozycja_menu = SprawdzenieLiczby('''Użytkowniku! pole jakiej figury chcesz policzyć? (trójkąt -1, trapez - 2, prostokąt - 3, kwadrat - 4, Koniec - 5)''', \
'To nie jest poprawne polecenie.\nWybierz jedną z dostępnych opcji 1 do 5', 1, 5)
    if pozycja_menu == 1:
        a=input("podaj dlugosc boku trojkata 'a'")
        h=input("podaj wysokosc trojkata 'h'")
        pole=(int(a)*int(h))/2
        print("pole trojkata wynosi: ",pole)
    elif pozycja_menu == 2:
        a=input("podaj dlugosc gornej podstawy trapezu 'a'")
        b=input("podaj dlugosc dolnej podstawy trapezu 'b'")
        h=input("podaj wysokosc trapezu 'h'")
        pole=((int(a)+int(b))*int(h))/2
        print("pole trapezu wynosi: ",pole)
    elif pozycja_menu == 3:
        a = input("podaj dlugosc boku prostokata 'a'")
        b = input("podaj dlugosc drugiego boku prostokata 'b'")
        pole = int(a)*int(b)
        print("pole prostokata wynosi: ", pole)
    elif pozycja_menu == 4:
        a = input("podaj dlugosc boku kwadratu 'a'")
        pole=int(a)*int(a)
        print("pole kwadratu wynosi: ", pole)

# Koniec
input('Aby zakończyć naciśnij klawisz ENTER.')