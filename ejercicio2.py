print("---------------------------------")
print("mostar cadena N veses en pantalla")
print("---------------------------------")

cadena = input("digite la cadena: ")
n = int(input("digite el numero de veses que quiere mostrar la cadena: "))

def mostrarnombre(cadena, n):
    for i in range(1,n+1):
        print(f"{i} . {cadena}")

mostrarnombre(cadena, n)

print("\neso era ...")