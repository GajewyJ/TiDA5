import random

#***********************************************************************************************************
#   nazwa:                  losowanie
#   opis:                   Losuje podaną ilość liczb z zakresu od 1 do 6 i zapisuje je do listy 'liczby'
#   parametry:              ilosc - liczba całkowita będąca ilością liczb, które funkcja ma wylosować
#   zwracany typ i opis:    list - lista wylosowanych liczb
#   autor:                  Jakub Gajewy 5D
#***********************************************************************************************************
def losowanie(ilosc):
    liczby = []
    kostka = 1

    for i in range(ilosc):
        liczba = random.randint(1, 6)
        liczby.append(liczba)
        komunikat = "Kostka " + str(kostka) + ": " + str(liczba)
        print(komunikat)
        kostka += 1

    return liczby

#***********************************************************************************************************
#   nazwa:                  liczPunkty
#   opis:                   Oblicza ilość punktów uzyskanych z wylosowanych liczb
#   parametry:              wylosowaneLiczby - lista losowych liczb z zakresu od 1 do 6
#   zwracany typ i opis:    int - Ilość punktów uzyskana przez gracza z losowania
#   autor:                  Jakub Gajewy 5D
#***********************************************************************************************************
def liczPunkty(wylosowaneLiczby):
    punkty = 0

    for i in range(1, 7):
        iloscWystapien = 0
        for j in range(len(wylosowaneLiczby)):
            if(wylosowaneLiczby[j] == i):
                iloscWystapien += 1
        if(iloscWystapien > 1):
            punkty += i * iloscWystapien

    return punkty

statusGry = "t"

while(statusGry == "t"):
    ilosc = 0
    while(ilosc < 3 or ilosc > 10):
        print("Ile kostek chcesz rzucić?(3-10)")
        ilosc = int(input())

    wylosowaneLiczby = losowanie(ilosc)

    print("Liczba uzyskanych punktów: " + str(liczPunkty(wylosowaneLiczby)))

    print("Jeszcze raz? (t/n)")
    statusGry = input()