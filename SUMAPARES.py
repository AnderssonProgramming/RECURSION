"""Escribir una función y un programa que encuentre la suma de los enteros positivos pares desde N hasta 2."""

def número_Elementos():
    n=-1

    while n <= 0:
        n=int(input("Número entero: "))

    return n

def sumaPares(n):
    if n < 2:
        return 0
    elif n % 2 != 0:
        return sumaPares(n-1)
    else:
        return n + sumaPares(n-2)

def main():
    n = número_Elementos()
    sumaParesF = sumaPares(n)

    print(sumaParesF)

main()
