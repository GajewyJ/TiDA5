from math import sqrt


def wypelnij_tablice(A):
    for i in range(0, 100):
        A.append(True)

def sito_erastotenesa(A, n):
    i = 2
    while i <= sqrt(n):
        if A[i] == True:
            x = 2
            j = x * i
            while j < n:
                A[j] = False
                x += 1
                j = x * i
        i += 1

n = 100
A = []
wypelnij_tablice(A)
sito_erastotenesa(A, n)

print("Liczby pierwsze: ")
for i in range(2, n):
    if A[i] == True:
        print(i,end=", ")