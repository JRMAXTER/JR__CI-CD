# probando ando 

palabra = input("ingrese una palabra").lower()
contador = 0
for letra in palabra:
    if letra in vocales:
        contador += 1

print(f"La palabra {palabra} tiene {contador} vocal(es).")
