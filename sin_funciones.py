print("----------------------------")
print("buscar un numero en conjunto")
print("----------------------------")

# entrada
b = int(input("numero a buscar: "))

# prosesamiento
a = [1,2,3,4,5]
r = False

for i in a:
    if i == b:
        print("lo encontre")
        r = True
if r == True:
    print("no lo encontre")

# salida

print("\nEso era...")