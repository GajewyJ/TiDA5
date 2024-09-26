# **********************************************************************************************************************
# nazwa funkcji:            sprawdz_plec
# opis funkcji:             Na podstawie podanego jako parametr numeru pesel sprawdza płeć posiadającej go osoby.
#                           Zwraca 'M' jeśli jest to mężczyzna lub 'K' jeśli jest to kobieta
# parametry:                numer_pesel - numer pesel do sprawdzenia płci. Może być typu tekstowego lub jako tablica
#                           znaków
# zwracany typ i opis:      str - 'M' jeśli PESEL należy do mężczyzny lub 'K' jeśli należy do kobiety
# autor:                    Jakub Gajewy 5D
# **********************************************************************************************************************
def sprawdz_plec(numer_pesel):
    if int(numer_pesel[9]) % 2 == 0:
        return 'K'
    else:
        return 'M'


def suma_kontrolna(numer_pesel):
    wagi_cyfr = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    s = 0
    for i in range(len(wagi_cyfr)):
        s += (int(numer_pesel[i]) * wagi_cyfr[i])

    m = s % 10
    if m == 0:
        r = 0
    else:
        r = 10 - m

    if r == int(numer_pesel[10]):
        return True
    else:
        return False


pesel = '55030101193'

print("Podaj numer PESEL: ")
podany_pesel = input()

if sprawdz_plec(podany_pesel) == 'M':
    print("Mężczyzna")
else:
    print("Kobieta")

if suma_kontrolna(podany_pesel):
    print("Suma kontrolna numeru PESEL jest zgodna")
else:
    print("Suma kontrolna numeru PESEL nie jest zgodna")
