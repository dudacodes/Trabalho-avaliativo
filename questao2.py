def validar_altitude(altitude):
    if altitude < 10 or altitude > 120:
        raise ValueError("Altitude não permitida")
    return altitude


def solicitar_altitude(altitude):
    try:
        resultado = validar_altitude(altitude)
        return f"Altitude definida: {resultado} m"
    except ValueError as erro:
        return f"Falha: {erro}"

print(solicitar_altitude(50))
print(solicitar_altitude(150))