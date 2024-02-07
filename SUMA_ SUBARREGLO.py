"""Escribir una función recursiva que devuelva la suma de un subarreglo de N enteros,
límitado por indices (i,j)  en una lista de enteros L"""

def número_Elementos():
    n=-1

    while n <= 0:
        n=int(input("Cantidad de números: "))

    return n

def carga_numeros(n):
    lista = []

    for i in range (n):
        numero = int(input("Número entero: "))

        lista.append(numero)

    return lista

def sumaElementos(lista, i, j):
    if i > j:
        return 0
    else:
        return lista[i] + sumaElementos(lista, i+1, j)

def main():
    n = número_Elementos()
    lista = carga_numeros(n)
    i = int(input("Índice inicial: "))
    j = int(input("Índice final: "))
    suma = sumaElementos(lista, i, j)
    print("La suma de los elementos entre los índices", i, "y", j, "es:", suma)

main()
