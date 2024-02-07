"Programe un método recursivo que invierta los números de un arreglo de enteros"

def lista():
    lista = []
    n = int(input("Cantidad de nùmeros: "))

    for i in range (n):
        numero = int(input("Nùmero: "))
        lista.append(numero)

    return lista
def reverse_Array(list):

    if len(list) == 0:
        return []
    else:
        return [list[-1]] + reverse_Array(list[:-1])

def main():
    listA = lista()
    ArregloInvertido = reverse_Array(listA)

    print("Arreglo invertido: ",ArregloInvertido)
main()

