def executar_verificacao(duracao):
    historico = []

    try:
        if duracao < 1 or duracao > 60:
            raise ValueError("Duração inválida")

    except ValueError as erro:
        historico.append(f"ERRO: {erro}")

    else:
        historico.append("Missão liberada")

    finally:
        historico.append("Verificação encerrada")

    return historico

print(executar_verificacao(30))
print(executar_verificacao(70))
