from turtle import Turtle
import random
class CarroConfig: 
    def __init__(self):
        self.carros = []
        self.local = [(0,100), (60,100), (120,100), (-60,100), (-120,100)]
        self.criar_carro()
    
    def criar_carro(self):
        novo_carro = Turtle()
        cores = ['brown', 'white', 'black', 'cyan', 'grey', 'green', 'yellow', 'purple']
        novo_carro.shape('square')
        novo_carro.shapesize(2.5, 3.2)
        novo_carro.color(random.choice(cores))
        novo_carro.goto(random.choice(self.local))