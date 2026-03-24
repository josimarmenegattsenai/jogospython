from turtle import Turtle

# A classe Jogador herda todas as funcionalidades da classe Turtle
class Jogador(Turtle):
    def __init__(self):
        # Inicializa a classe pai (Turtle) para que este objeto tenha todas as suas propriedades
        super(Jogador, self).__init__()
        
        self.shape('turtle')    # Define o avatar visual do jogador
        self.shapesize(3, 3)    # Aumenta o tamanho da tartaruga para facilitar a visualização
        self.setheading(90)     # Aponta a tartaruga para o Norte (topo da tela)
        self.penup()            # Desativa o desenho de linhas; o jogador apenas se desloca
        self.goto(0, -220)      # Define o ponto de spawn inicial (centro inferior)

    def mover_direita(self):
        """Calcula e executa o deslocamento lateral para a direita."""
        # Obtém a coordenada X atual e soma 60 unidades (largura de uma faixa)
        nova_pos = self.xcor() + 60 
        self.goto(nova_pos, self.ycor()) # Move para a nova posição mantendo a mesma altura Y
        print(nova_pos) # Log de depuração para monitorar a posição no console

    def mover_esquerda(self):
        """Calcula e executa o deslocamento lateral para a esquerda."""
        # Obtém a coordenada X atual e subtrai 60 unidades
        nova_pos = self.xcor() - 60 
        self.goto(nova_pos, self.ycor()) # Move para a nova posição
        print(nova_pos) # Log de depuração