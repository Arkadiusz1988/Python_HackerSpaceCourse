import geopy.distance
import re

fileHandle = open('Zamu9HSa.txt', "r")
lineStr = fileHandle.read()
fileHandle.close()
numberOfPlace = lineStr.count("latitude")
print("„Witaj użytkowniku! Z okolicy znajduje się "+str(numberOfPlace)+ " miejsc, które warto odwiedzić”\n")
liczba=0
while liczba != 1:
    print("\nUzytkowniku, podaj swoja dlugosc geograficzna w formacie 54.366667")
    latitude = input()
    print("Uzytkowniku, podaj swoja szerokosc geograficzna w formacie 17.016667")
    longitude = input()

    coords_1 = (latitude, longitude)
    fileHandle1 = open('Zamu9HSa.txt', "r")
    lineList = fileHandle1.readlines()
    fileHandle1.close()
    a = 1
    print("Lista obiektow w promeniu 1 km od wspolrzednych ktore podales: \n")
    for n in range(len(lineList)):
        tmp=lineList[n].__contains__("latitude")
        if tmp:
            tmp1=re.findall('[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', lineList[n])
            tmp2=re.findall('[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', lineList[n+1])
            tmp3 = str(tmp1).replace("['", "").replace("']", "")
            tmp4 = str(tmp2).replace("['", "").replace("']", "")
            coords_2 = (tmp3, tmp4)
            try:
                distCalc=geopy.distance.vincenty(coords_1, coords_2).km
            except ValueError:
                print("To nie jest poprawna liczba w formacie xx.yyyy")
                liczba=2
                break
            if distCalc < 1:
                print("numer",a,lineList[n-10])
                a=a+1
                liczba=1
            else:
                print("Liczba obiektow to Zero dla podanych wspolrzednych")
                liczba=1
                break


