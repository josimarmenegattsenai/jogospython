import turtle
import time
from turtle import Screen
from pista import Pista
from jogador import Jogador
from carro import CarroConfig
from pontuacao import Pontuacao

tela = Screen()
tela.setup(600,600)
tela.tracer(0)
tela.title("Tartaruga esperta")
tela.listen()
pista = Pista()
jogador = Jogador()
carro_config = CarroConfig()
pontuacao = Pontuacao()
tela.onkey(jogador.mover_direita, 'Right')
tela.onkey(jogador.mover_esquerda, 'Left')
jogo_on =  True
while jogo_on == True:
    time.sleep(0.1)
    carro_config.aparecer_carro()
    carro_config.mover_carro()
    if jogador.xcor() > 120 or jogador.xcor() < -120:
        turtle.write("Fim de jogo", align='center', font=('Arial', 50, 'normal'))
        jogo_on = False
    for carrinho in carro_config.carros:
        if abs(jogador.xcor() - carrinho.xcor()) < 1 and jogador.distance(carrinho) < 65:
            turtle.write("Fim de jogo", align='center', font=('Arial', 50, 'normal'))
            jogo_on = False
        if carrinho.ycor() < -230:
            pontuacao.aumentar_pontuacao()
            carrinho.hideturtle()
            carro_config.carros.remove(carrinho)
    tela.update()
    
tela.exitonclick()
