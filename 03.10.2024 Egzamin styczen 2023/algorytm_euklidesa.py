#******************************************************************************************************************
#   nazwa funkcji:          NWD
#   opis funkcji:           Oblicza i zwraca największy wspólny dzielnik dwóch podanych jako parametry liczb
#   parametry:              a - liczba pierwsza
#                           b - liczba druga
#   zwracany typ i opis:    int - największy wspólny dzielnik liczb podanych jako parametry
#   autor:                  Jakub Gajewy
#******************************************************************************************************************
def NWD(a, b):
    while a!= b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

a = 0
b = 0
while a <= 0 or b <= 0:
    print("Podaj a: ", end="")
    a = int(input())
    print("Podaj b: ", end="")
    b = int(input())
    if a <= 0 or b <= 0:
        print("Liczby muszą być większe od zera!")

wynik = NWD(a, b)
print("NWD = " + str(wynik))