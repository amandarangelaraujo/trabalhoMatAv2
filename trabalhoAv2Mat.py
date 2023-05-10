import random
from collections import Counter
from itertools import combinations
#fazer o baralho
def gerar_baralho():
    naipes = ['copas', 'ouros', 'espadas', 'paus']
    valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    baralho = []
    for valor in valores:
        for naipe in naipes:
            baralho.append((valor, naipe))
    return baralho

#distribuir as cartas, recebendo o return da função gerar_baralho
def distribuir_cartas(baralho):
    random.shuffle(baralho)
    mao_jogadores = []
    for i in range (4):
        mao=[]
        for j in range(3):
            mao.append(baralho.pop(0))
        mao_jogadores.append(mao)
    #distribuir as cartas da mesa
    mesa = []
    for i in range(2):
        mesa.append(baralho.pop(0))
    return mao_jogadores, mesa
    
#atribuindo o resultado à variáveis fora das funções.
baralho=gerar_baralho()
mao_jogadores,mesa = distribuir_cartas(baralho)

#definindo as cartas dos jogadores
jogadorNumero1=mao_jogadores[0]
jogadorNumero2=mao_jogadores[1]
jogadorNumero3=mao_jogadores[2]
jogadorNumero4=mao_jogadores[3]
print(f"O primeiro jogador recebeu as cartas: {jogadorNumero1}\nO segundo jogador recebeu: {jogadorNumero2}\nO terceiro Jogador recebeu: {jogadorNumero3}\nO quarto jogador recebeu: {jogadorNumero4}" )


#juntar as cartas da mão de cada jogador com as cartas da mesa:
jogadorNumero1.extend(mesa)
jogadorNumero2.extend(mesa)
jogadorNumero3.extend(mesa)
jogadorNumero4.extend(mesa)
print(f"juntando com as cartas da mesa o primeiro jogador tem: {jogadorNumero1}")
print(f"juntando com as cartas da mesa o segundo jogador tem: {jogadorNumero2}")
print(f"juntando com as cartas da mesa o terceiro jogador tem: {jogadorNumero3}")
print(f"juntando com as cartas da mesa o quarto jogador tem: {jogadorNumero4}")

def pontuacao(_mao):
    naipes = {}
    valores = {}
    for carta in _mao:
        naipe, valor = carta
        if naipe not in naipes:
            naipes[naipe] = 1
        else:
            naipes[naipe] += 1
        if valor not in valores:
            valores[valor] = 1
        else:
            valores[valor] += 1
    # Fazer soma de pontos por quantidade de cartas do mesmo naipe
    pontos = sum([1 for naipe in naipes if naipes[naipe] >= 3])

    # Fazer a soma de pontos por sequencia de cartas
    quantia_valores = Counter(valores)
    _valores = list(valores)
    for valor in quantia_valores:
        if _valores.index(valor) <= 10:
            contador_sequencia = 0
            for i in range(_valores.index(valor), _valores.index(valor) + 3):
                # Checando se o valor está dentro do range para nao receber IndexError
                if i <= len(_valores) - 1:
                    if _valores[i] in quantia_valores:
                        contador_sequencia += 1
            if contador_sequencia == 3:
                pontos += 2
    return pontos

print("Jogador 1:",pontuacao(jogadorNumero1))
print("Jogador 2:",pontuacao(jogadorNumero2))
print("Jogador 3:",pontuacao(jogadorNumero3))
print("Jogador 4:",pontuacao(jogadorNumero4))
