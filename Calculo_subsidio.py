def subsidio(quintil, estado_laboral, edad):

    if quintil in [1, 2] and estado_laboral == "desempleado":
        subsidio = 10000
    elif quintil in [1, 2] and estado_laboral == "empleado":
        subsidio = 8000
    elif quintil == 3 and estado_laboral == " desempleado":
        subsidio = 6000
    elif quintil == 3 and estado_laboral == "empleado":
        subsidio = 4000
    elif quintil in [4, 5]:
        subsidio = 1500

    else:
        return "datos invalidos"
    if quintil in [1,2]:
        subsidio += 2000
    if edad > 65:
        subsidio += 3000
    
    return subsidio

quintil = int(input("¿Cual es su quintil? (1, 5): "))
estado_laboral = input("¿Cual es su estado laboral? (empleado/desempleado): ")
edad= int(input("¿Cual es su edad?: "))

monto_total = subsidio(quintil, estado_laboral, edad)
print("El subsidio total del gas es: ", monto_total)