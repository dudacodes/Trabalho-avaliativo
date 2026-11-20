def validar_velocidade(velocidade):
    if velocidade <= 0 or velocidade > 80:
        raise ValueError("Velocidade inválida")
    return velocidade

def configurar_voo(velocidade):
    resultado = validar_velocidade(velocidade)
    return f"Velocidade configurada: {resultado} km/h"

def iniciar_missao(velocidade):
    try:
        return configurar_voo(velocidade)
    except ValueError as erro:
        return f"Missão cancelada: {erro}"

print(iniciar_missao(60))
print(iniciar_missao(100))
