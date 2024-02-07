"""Escriba una función recursiva que ordene de menor a mayor una lista de enteros
basándose en la siguiente idea: coloque el elemento más pequeño en la primera
ubicación, y luego ordene el resto del arreglo con una llamada recursiva. """

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

def menor_mayor(lista):
    
    if len(lista) <= 1:
        return lista
    else:
        menorNumero = min(lista)

        lista.remove(menorNumero)

    return [menorNumero] + menor_mayor(lista)

def imprimirLista(listaAscendente):
    for elem in listaAscendente:
        print(elem)

def main():
    n= número_Elementos()
    lista = carga_numeros(n)
    listaAscendente = menor_mayor(lista)
    imprimirLista(listaAscendente)
main()
