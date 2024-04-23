# mensaje = "Hola Mundo"

# ACTIVIDAD 1
# print(mensaje)
# print("BIENVENIDO AL MUNDO DE LA PROGRAMACION") 
# nombre = input("Ingresa tu nombre\n")
# print(f"Bienvenido",nombre)

# ACTIVIDAD 2
# x = int(input("Dame un numero"))
# formula = (x**2+3*x+1)/4
# print(f"El resultado de la ecuacion es {formula} ")

# ACTIVIDAD 3
# nombre = input("Ingresa tu nombre\n")
# RUT = input("Ingresa tu rut\n")
# correo = input("Ingresa tu  correo\n")
# telefono = input("Ingresa tu telefono\n")
# print(F"NOMBRE:               {nombre}")
# print(f"RUT:                  {RUT}")
# print(f"CORREO:               {correo}")
# print(f"TELEFONO:             {telefono}")


# for i in range(5):
#     i = i + 2
#     print(i)
# print ("Programa que calcula el factorial")
# numero = int(input("Introduzca el número: "))

# factorial = 1

# i = 1
# while (i <= numero):
#     factorial = factorial * i
#     i = i + 1

# print ("El factorial de " + str(numero) + " es " + str(factorial))

# numero = int(input("Dame un numeron\n"))
# numero = numero%2
# if numero > 0 :
#     print("Numero impar")
# else:
#     print("Numero par")

# bandera = True

# while bandera:
#     numero = int(input("Ingrese numero impar"))
#     if numero%2==1 :
#         print(f"{numero} es impar, Multiplicado por 4 = {numero*4}")
#         bandera = False
        
#     else:
#         print("Error ingrsa un numero impar")
#         bandera = True
        
contadorproductos = 0
acomuladorproductos = 0
opcion = int(input("Desea llevar agua por 600?     1.-Si    2.-No"))
if opcion == 1:
    contadorproductos += 1
    acomuladorproductos += 600
opcion =int(input("Desea llevar azucar por 1200?      1.-Si   2.-No"))
if opcion ==1:
    contadorproductos += 1
    acomuladorproductos += 1200
opcion =int(input("Desea llevar aceite x 1500?         1.-Si      2.-No"))
if opcion ==1:
    contadorproductos += 1
    acomuladorproductos += 1500
opcion =int(input("desea agregar arroz x 1250      1.- Si    2.-No"))
if opcion ==1:
    contadorproductos +=1
    acomuladorproductos += 1250
opcion= int(input("Desea agregar fideos por 790?        1.-Si      2.-No"))
if opcion ==1:
    contadorproductos+=1
    acomuladorproductos += 790
opcion = int(input("desea agregar bebida por 1780?     1.-Si     2.-No"))
if opcion==1:
    contadorproductos+=1
    acomuladorproductos += 1780
opcion =int(input("Desea agregar chocolate por 2500?      1.Si     2.-No"))
if opcion ==1:
    contadorproductos +=1
    acomuladorproductos += 2500
opcion =int(input("desea agregar pan de molde por 1340?        1.-Si         2.-No"))
if opcion ==1:
    contadorproductos +=1
    acomuladorproductos += 1340
print(f"Llevas {contadorproductos} productos")
print(f"Llevas en total un saldo de {acomuladorproductos} pesos")
clientepreferencial = int(input("Es usted un cliente preferencial?  1.-si          2.-no"))
if clientepreferencial ==1:
    total = acomuladorproductos * 0.75
    descuento = acomuladorproductos * 0.25
else:
    total = acomuladorproductos
    descuento = 0
    
pago =int(input("con que pags?   1.-Efectivo     2.-Debito"))
if pago ==1:
    efectivo = int(input("Ingrese saldo en efectivo"))
    
vuelto = efectivo - total

print(f"Tu vuelto es {vuelto}")
            