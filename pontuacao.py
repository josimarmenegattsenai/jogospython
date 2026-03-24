from turtle import Turtle

# A classe Pontuacao gerencia o estado do placar e a renderização de texto na tela
class Pontuacao(Turtle):
    def __init__(self):
        # Inicializa a base da Turtle para usar métodos de escrita e posicionamento
        super().__init__()
        self.hideturtle()       # Oculta o ícone da tartaruga; queremos ver apenas o texto
        self.pontuacao = 0      # Atributo que armazena o valor numérico do score
        self.penup()            # Garante que a tartaruga não risque a tela ao se posicionar
        self.goto(-250, 130)    # Posiciona o placar no canto superior esquerdo (HUD)
        self.pontuacao_config() # Renderiza o texto inicial (0)

    def pontuacao_config(self):
        """Método de renderização: desenha o texto atualizado na interface."""
        # O f-string permite inserir a variável diretamente no texto
        # \n é usado para quebrar a linha, deixando o número abaixo da palavra
        self.write(f'Pontuação: \n {self.pontuacao}', align='left', font=('Arial', 12, 'normal'))

    def aumentar_pontuacao(self):
        """Lógica de atualização de estado e re-renderização."""
        self.pontuacao += 1     # Incrementa o valor lógico (back-end)
        self.clear()            # Limpa o desenho anterior da tela para evitar sobreposição de texto
        self.pontuacao_config() # Desenha o novo valor (front-end)