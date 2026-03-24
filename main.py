import turtle
import time
from turtle import Screen
from pista import Pista
from jogador import Jogador
from carro import CarroConfig
from pontuacao import Pontuacao

# --- CONFIGURAÇÃO DO AMBIENTE PADRÃO---
tela = Screen()
nome = tela.textinput("Tartaruga Esperta", "Digite seu nome:") # Prompt para o nome do jogador
tela.setup(600, 600)  # Define a resolução da janela
tela.bgcolor ('beige') # Cor de fundo para melhor contraste visual
tela.tracer(0)        # Desliga a animação automática para controle manual de frames (performance)
tela.title("Tartaruga esperta")
tela.listen()         # Habilita a escuta de eventos do teclado

# --- INSTANCIAÇÃO DOS OBJETOS ---
pista = Pista()             # Renderiza o cenário estático
jogador = Jogador()         # Inicializa o avatar do player
carro_config = CarroConfig() # Inicializa o gerenciador de obstáculos
pontuacao = Pontuacao()     # Inicializa a interface de score

# Turtle para mensagem de fim de jogo (não sobreposta)
mensagem_fim = turtle.Turtle()
mensagem_fim.hideturtle()
mensagem_fim.penup()

# --- MAPEAMENTO DE INPUTS ---
tela.onkey(jogador.mover_direita, 'Right') # Bind da tecla Direita
tela.onkey(jogador.mover_esquerda, 'Left') # Bind da tecla Esquerda

def game_over():
    mensagem_fim.clear()
    mensagem_fim.goto(0, 0)
    mensagem_fim.write('Fim de jogo', align='center', font=('Arial', 50, 'normal'))
    mensagem_fim.goto(0, -40)
    mensagem_fim.write(f'Pontuação final: {pontuacao.pontuacao}', align='center', font=('Arial', 30, 'normal'))
    for carrinho in carro_config.carros:
        carrinho.hideturtle()
    carro_config.carros.clear()



def iniciar_jogo():
    jogo_on = True
    while jogo_on:
        time.sleep(0.1)
        carro_config.aparecer_carro()
        carro_config.mover_carro()

        if jogador.xcor() > 120 or jogador.xcor() < -120:
            game_over()
            jogo_on = False

        for carrinho in carro_config.carros:
            if abs(jogador.xcor() - carrinho.xcor()) < 1 and jogador.distance(carrinho) < 65:
                game_over()
                jogo_on = False
                break

            if carrinho.ycor() < -230:
                pontuacao.aumentar_pontuacao()
                carrinho.hideturtle()
                carro_config.carros.remove(carrinho)

        tela.update()


iniciar_jogo()

# Mantém a janela aberta após o Game Over
tela.mainloop()