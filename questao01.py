class Drone:
    def __init__(self, codigo, bateria):
        self.codigo = codigo
        self.bateria = bateria

    def voar(self, minutos):
        if minutos <= 0:
            raise ValueError("Tempo de voo inválido")

        consumo = minutos * 4

        if self.bateria < consumo:
            raise ValueError("Bateria insuficiente")

        self.bateria -= consumo

        return self.bateria

drone = Drone("D01", 80)
print(drone.voar(5))
