import turtle
import time
from turtle import Screen
from pista import Pista
from jogador import Jogador
from carro import CarroConfig
from pontuacao import Pontuacao

# --- CONFIGURAÇÃO DO AMBIENTE PADRÃO---
tela = Screen()
tela.setup(600, 600)  # Define a resolução da janela
tela.tracer(0)        # Desliga a animação automática para controle manual de frames (performance)
tela.title("Tartaruga esperta")
tela.listen()         # Habilita a escuta de eventos do teclado

# --- INSTANCIAÇÃO DOS OBJETOS ---
pista = Pista()             # Renderiza o cenário estático
jogador = Jogador()         # Inicializa o avatar do player
carro_config = CarroConfig() # Inicializa o gerenciador de obstáculos
pontuacao = Pontuacao()     # Inicializa a interface de score

# --- MAPEAMENTO DE INPUTS ---
tela.onkey(jogador.mover_direita, 'Right') # Bind da tecla Direita
tela.onkey(jogador.mover_esquerda, 'Left') # Bind da tecla Esquerda

# --- LOOP PRINCIPAL DO JOGO (GAME LOOP) ---
jogo_on = True
while jogo_on == True:
    time.sleep(0.1)             # Controla o "Frame Rate" (velocidade do loop)
    carro_config.aparecer_carro() # Verifica se precisa gerar novos carros no topo
    carro_config.mover_carro()    # Atualiza a posição Y de todos os carros ativos

    # CHECK 1: Verificação de Limites da Pista (Out of Bounds)
    if jogador.xcor() > 120 or jogador.xcor() < -120:
        turtle.write("Fim de jogo", align='center', font=('Arial', 50, 'normal'))
        jogo_on = False # Quebra o loop principal

    # LOOP DE PROCESSAMENTO DE OBSTÁCULOS
    for carrinho in carro_config.carros:
        # CHECK 2: Detecção de Colisão (Lógica de proximidade Euclidiana)
        # Verifica se estão na mesma faixa (x) e se a distância física é menor que 65px
        if abs(jogador.xcor() - carrinho.xcor()) < 1 and jogador.distance(carrinho) < 65:
            turtle.write("Fim de jogo", align='center', font=('Arial', 50, 'normal'))
            jogo_on = False

        # CHECK 3: Garbage Collection & Pontuação
        # Se o carro ultrapassar o limite inferior da tela (-230)
        if carrinho.ycor() < -230:
            pontuacao.aumentar_pontuacao()      # Incrementa o score
            carrinho.hideturtle()              # Remove o objeto visualmente
            carro_config.carros.remove(carrinho) # Remove o objeto da memória (lista)

    # RENDERIZAÇÃO: Atualiza todos os desenhos de uma vez (evita flickering)
    tela.update()

# Mantém a janela aberta após o Game Over até um clique manual
tela.exitonclick()