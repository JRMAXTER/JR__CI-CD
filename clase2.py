n_1 = 5
n_2 = 12

print(n_1+n_2)
print(n_1-n_2)
print(n_1*n_2)
print(n_1/n_2)
print(n_1%n_2)

print(n_1>n_2)
print(n_1<n_2)
print(n_1>=n_2)
print(n_1<=n_2)
print(n_1==n_2)
print(n_1!=n_2)
#condiciones
print( n_1>2 and n_2<15)
print( n_1>2 or n_2<15)
#print( n_2<2 not n_1>15)


numero = 15
if(numero > 0):
    print("el numero es mayor a cero")
elif( numero < 0):
    print("el numero es negativo")    
else:
    print("el numero es cero")

#imput
#nombre = input("ingresa tu nobre")
#23print("hola"+ nombre)

numero = int(input( "ingrese su numero"))
print("El numero es:"+ str(numero))

if (numero<18):
    print("menor de edad")
elif (numero>18 and numero<25):
    print("adulto joven") 
else:
    print("adulto mayor")       