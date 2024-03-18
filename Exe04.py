# Crie uma interface chamada "Veículo " com métodos " acelerar " e "frear." Em seguida, crie classes 
# concretas como "Carro " e "Bicicleta " que implementem a interface "Veículo " e forneçam suas próprias 
# implementações dos métodos " acelerar " e "frear." Demonstre como o polimorfismo pode ser usado para 
# tratar diferentes tipos de veículos de maneira uniforme, chamando os métodos da interface.

class Veiculo:
    def __init__(self):
        pass

    def acelerar(self):
        pass

    def frear(self):
        pass

class Carro(Veiculo):
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self):
        if self.velocidade_atual < self.velocidade_maxima:
            self.velocidade_atual += 10
            return self.velocidade_atual
        else:
            print('Velocidade máxima atingida!')

    def frear(self):
        if self.velocidade_atual > 0:
            self.velocidade_atual -= 10
            return self.velocidade_atual
        else:
            print('Carro parado!')

class Bicicleta(Veiculo):
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self):
        if self.velocidade_atual < self.velocidade_maxima:
            self.velocidade_atual += 5
            return self.velocidade_atual
        else:
            print('Velocidade máxima atingida!')

    def frear(self):
        if self.velocidade_atual > 0:
            self.velocidade_atual -= 5
        else:
            print('Bicicleta parada!')

# Polimorfismo
def usar_veiculo(veiculo):
    veiculo.acelerar()
    veiculo.frear()

carro = Carro(180)
bicicleta = Bicicleta(30)

usar_veiculo(carro)
usar_veiculo(bicicleta)

