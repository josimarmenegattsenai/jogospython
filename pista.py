from turtle import Turtle

class Pista(Turtle):
    def __init__(self):
        # Inicializa a tartaruga que será responsável por "pintar" o cenário
        super().__init__()
        self.pensize(4)   # Define a espessura da linha para as bordas da pista
        self.penup()
        
        # --- Desenho da Borda Direita ---
        self.goto(140, -400) # Posiciona no extremo inferior direito
        self.pendown()
        self.goto(140, 400)  # Traça a linha vertical até o topo

        # --- Desenho das Faixas Centrais (Pontilhadas) ---
        # 2ª Linha de faixas
        self.desenhar_traco((90, -400))
        self.desenhar_traco((-90, -400))

        # 3ª Linha de faixas (Divisórias internas)
        self.desenhar_traco((30, -400))
        self.desenhar_traco((-30, -400))

        # --- Desenho da Borda Esquerda (Linha Final) ---
        self.penup()
        self.pensize(4)
        self.goto(-150, -400) # Posiciona no extremo inferior esquerdo
        self.pendown()
        self.goto(-150, 400)  # Traça a linha vertical de fechamento da pista

    def desenhar_traco(self, pos):
        """Algoritmo para desenhar linhas pontilhadas de forma automatizada."""
        self.setheading(90) # Aponta para cima
        self.penup()
        self.goto(pos)      # Move para o ponto inicial da faixa enviado por argumento
        
        # Loop de renderização da faixa pontilhada
        for traco in range(30):
            self.forward(20)  # Desenha o traço (caneta abaixada)
            self.penup()      # Levanta a caneta para criar o espaço vazio
            self.forward(20)  # Move sem desenhar
            self.pendown()    # Abaixa a caneta para o próximo ciclo