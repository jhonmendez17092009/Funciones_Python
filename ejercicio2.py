print("---------------------------------")
print("mostar cadena N veses en pantalla")
print("---------------------------------")

cadena = input("digite la cadena: ")

def mostrarnombre(cadena):
    for i in range(1,19):
        print(f"{i} . {cadena}")

mostrarnombre(cadena)

print("\neso era ...")