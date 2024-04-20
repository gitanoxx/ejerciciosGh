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

bandera = True

while bandera:
    numero = int(input("Ingrese numero impar"))
    if numero%2==1 :
        print(f"{numero} es impar, Multiplicado por 4 = {numero*4}")
        bandera = False
        
    else:
        print("Error ingrsa un numero impar")
        bandera = True
        
        