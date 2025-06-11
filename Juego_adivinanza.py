import random

minimo = int(input("ingrese limite inferior: "))
maximo = int(input("ingrese limite superior: "))

while minimo >= maximo:
    print("el limite inferior debe ser menor que el superior")
    minimo = int(input("ingrese limite inferior: "))
    maximo = int(input("ingrese limite superior: "))

numero = random.randint(minimo, maximo)
numero = round(numero / 4) * 4

for intento in range (1, 4):
    adivina = int(input("intente adivinar: "))

    if adivina == numero:
        if intento == 1:
            print("felicitaciones, adivinaste en el primer intento")
        else:
            print("correcto")
        break
    else:
        if intento < 3:
            pista = "mayor" if adivina < numero else "menor"
            print("el numero es: ", pista)
        else:
            print("perdiste, el numero es: ", numero)