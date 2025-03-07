print("----------------------------")
print("buscar un numero en conjunto")
print("----------------------------")

# definicionde la funcion

def buscardatosenlista(datosAbuscar, lista):
    r = False
    for i in lista:
        if i == datosAbuscar:
            r = True
    return r

# entrada

datos = int(input("numero a buscar: "))

# prosesamiento

lista = [1,2,3,4,5]
if buscardatosenlista(datos, lista):
    print("lo encontre")
else:
    print("no lo encontre")


# salida
print("\nEso era ...")