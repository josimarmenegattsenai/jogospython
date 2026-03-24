from turtle import Turtle
import random

class CarroConfig: 
    def __init__(self):
        # Armazena as instâncias de Turtle criadas para manipulação em lote
        self.carros = []
        
        # Definição dos spawn points (eixos X e Y) para as faixas da pista
        self.local = [(0,100), (60,100), (120,100), (-60,100), (-120,100)]
        
        # Gera o primeiro carro assim que a classe é instanciada
        self.criar_carro()
    
    def criar_carro(self):
        """Instancia um novo objeto Turtle com propriedades de obstáculo."""
        novo_carro = Turtle()
        cores = ['brown', 'black', 'white', 'cyan', 'grey', 'green', 'yellow', 'purple']
        
        novo_carro.shape('square')      # Define o corpo do carro como um quadrado
        novo_carro.shapesize(3, 3.2)    # Estica o quadrado para parecer um retângulo/carro
        novo_carro.setheading(270)      # Aponta para baixo (Sul) na tela
        novo_carro.color(random.choice(cores)) # Atribui uma cor aleatória do pool
        novo_carro.penup()              # Evita que o carro 'desenhe' uma linha ao se mover
        
        # Posiciona o carro em uma das faixas definidas aleatoriamente
        novo_carro.goto(random.choice(self.local))
        
        # Registra o novo objeto na lista de controle
        self.carros.append(novo_carro)

    def aparecer_carro(self):
        """Controla o fluxo de entrada de novos carros (Spawn Rate)."""
        # Se o último carro criado descer abaixo da coordenada Y 20, cria um novo
        # Isso garante um espaçamento consistente entre os obstáculos
        if self.carros[-1].ycor() <= 20:
            self.criar_carro()

    def mover_carro(self):
        """Aplica o deslocamento físico em todos os objetos ativos na lista."""
        for carro in self.carros:
            # Como o heading é 270, forward(20) move o carro para baixo
            carro.forward(20)