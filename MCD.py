"""Dada una función recursiva para MCD cómo

MCD = M si N =0
MCD = MCD (N, M mod N) si N <> 0

Escriba un programa que le permita al usuario ingresar los valores para M y N desde la consola.
Una función recursiva es entonces llamada para calcular el MCD. El programa entonces imprime el valor para el MCD."""

def mcd(M, N):
    if N == 0:
        return M
    else:
        return mcd(N, M % N)

M = int(input("Ingrese el valor para M: "))
N = int(input("Ingrese el valor para N: "))

result = mcd(M, N)

print("El Máximo Común Divisor (MCD) de", M, "y", N, "es", result)
