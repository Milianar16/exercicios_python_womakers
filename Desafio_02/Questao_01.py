#crie uma classe que modele o objeto "carro"
#Um carro tem os seguintes atributos : ligado, cor,modelo,velocidade
#Um carro tem os seguintes comportamentos: liga,desliga,acelera,desacelera



class Carro:
    def __init__(self, cor,modelo):
        self.cor = cor
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0.0
        self.limite_velocidade = 180.0

    def liga(self):
        self.ligado = True

    def desliga(self):
        self.ligado = False
        self.velocidade = 0.0

    def acelera(self):
        if self.ligado == False:
            return
        if self.velocidade < self.limite_velocidade:
            self.velocidade += 5

    def desacelera(self):
        if self.ligado == False:
            return
        if self.velocidade > 0:
            self.velocidade -= 5

    def __str__(self):
        ligado_str = "ligado" if self.ligado == True else " desligado"
        return f"Carro {self.modelo} da cor { self.cor} está {ligado_str}, à velocidade de  { self.velocidade}km/h."


#Crie uma instância da classe carro
carro = Carro("cinza", "Honda Civic")
print(carro)

#Faça o carro "andar" utilizando os métodos das classe
carro.liga()
print(carro)

for i in range(5):
    carro.acelera()

print(carro)

#Faça o carro "Parar" utilizando os métodos da sua classe

carro.desliga()
print(carro)
