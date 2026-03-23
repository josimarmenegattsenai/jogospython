from turtle import Turtle

class Jogador(Turtle):
    def __init__(self):
        super(Jogador, self).__init__()
        self.shape('turtle')
        self.shapesize(3,3)
        self.setheading(90)
        self.penup()
        self.goto(0,-220)

    def mover_direita(self):
        nova_pos = self.xcor()+60
        self.goto(nova_pos,self.ycor())
        print(nova_pos)

    
    def mover_esquerda(self):
        nova_pos = self.xcor()-60
        self.goto(nova_pos,self.ycor())
        print(nova_pos)
