import random
def sumar_pares_lista(lista):
    suma = 0
    num = 0
    num = num + 1
    for i in lista:
        if i % 2 == 0:
            suma = suma + i
            num = num + 1
    parametro = suma / num
    return parametro

lista = []
n = int(input("digite el tamaño de la lista: "))
for i in range(n):
    num = random.randint(1,n)
    lista.append(num)


print("lista ", lista)
print("el promedio es: ", sumar_pares_lista(lista))
print("\neso era ...")