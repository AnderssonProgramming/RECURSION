"Programe un método recursivo que transforme un número entero positivo a notación binaria."

def a_binario(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return a_binario(n // 2) + str(n % 2)

n = int(input("Ingrese un número entero positivo: "))

resultado = a_binario(n)

print("La representación binaria de", n, "es", resultado)
