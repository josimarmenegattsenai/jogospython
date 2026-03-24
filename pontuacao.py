from turtle import Turtle

class Pontuacao(Turtle):
    def __init__(self):
        super().__init__()
        self.pontuacao = 0
        self.penup()
        self.goto(-220,150)
        self.pontuacao_config()
    def pontuacao_config(self):
        self.write(f'Pontuação: \n {self.pontuacao}', align='left', font=('Arial', 12, 'normal'))

    def aumentar_pontuacao(self):
        self.pontuacao += 1
        self.clear()
        self.pontuacao_config()