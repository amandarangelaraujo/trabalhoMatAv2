
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


#fazer todas as combinações possíveis:

"""# cartas para poder formar um trio.
#LIMPAR ESSE CÓDIGO!!!
print('##########')
jogadorNumero1.sort()
print(jogadorNumero1)
cincoCartasJogador1=[]
for i in range(3):
    cincoCartasJogador1.append(jogadorNumero1[i])
for i in range(2):
    cincoCartasJogador1.append(mesa[i])

print('##########')
print(cincoCartasJogador1)

print('calcular as possibilidades de combinações entre essas cartas:')
trioJogador1=combinations(cincoCartasJogador1, 3)

print('##########')
print(jogadorNumero2)
cincoCartasJogador2=[]
for i in range(3):
    cincoCartasJogador2.append(jogadorNumero2[i])
for i in range(2):
    cincoCartasJogador2.append(mesa[i])

print('##########')
print(cincoCartasJogador2)

print('calcular as possibilidades de combinações entre essas cartas:')
trioJogador2=combinations(cincoCartasJogador2, 3)

print('##########')
print(jogadorNumero3)
cincoCartasJogador3=[]
for i in range(3):
    cincoCartasJogador3.append(jogadorNumero3[i])
for i in range(2):
    cincoCartasJogador3.append(mesa[i])

print('##########')
print(cincoCartasJogador3)

print('calcular as possibilidades de combinações entre essas cartas:')
trioJogador3=combinations(cincoCartasJogador3, 3)

print('##########')
print(jogadorNumero4)
cincoCartasJogador4=[]
for i in range(3):
    cincoCartasJogador4.append(jogadorNumero4[i])
for i in range(2):
    cincoCartasJogador4.append(mesa[i])

print('##########')
print(cincoCartasJogador4)

print('calcular as possibilidades de combinações entre essas cartas:')
trioJogador4=combinations(cincoCartasJogador4, 3)








#numpy.matrix.sort



#fatiamento de vetores:



##CHECAR SE DO MESMO NAIPE, SOMAR UM PONTO.
#def checarNaipe(maoJogador):
    ##lops para checar olhando a string, acessando o vetor de vetores
    ##vários if vetor na posição tal == 'copas'
    #   somador+1
    #todas as combinações possíveis?






##def checarSequência():
    ##print("oioioi")
    #poderia fazer uma função para cada naipe que rodasse a lista e chegasse se tem uma string que armazenada esse dado
    #la em cima chamaria a função para cada jogador
    #seriam 4 funções.
    ##CHEGAR SE SEQUÊNCIA USANDO O I I-1 PARA VER SE É UMA SEQUÊNCIA
    ##for i in range(60): ##ta falando que não tem len nessa type.
    #quantidade de combinaçoes possiveis==60
        #if trioJogador1[i+1]-trioJogador1[i]==1:  ##TypeError: 'itertools.combinations' object is not subscriptable
            #pontosJogador1=pontosJogador1+1
        #else:
            #continue
#print(f'o jogador numero 1 recebeu {pontosJogador1}')"""

#função sort = sorted(trioJogador1)
# if (trioJogador[0] + 1 == trioJogador[1] and triojogador[1] + 1 == triojogador[2])
#mas esse abrange todas as cartas?

#teria que trocar os vetores pelos dicionários.
#pecorrer os dicinários>>>>pegaria direito.
#a função gerarBaralho fica dentro do obj jogador, jogador chama a função!!!!!! POO
#a função recebe como parâmetro o próprio baralho.

#sort para por em sequência
#vetor de vetores, teria que acessar um elemento dentro dele e fazer o sort, como acessar esse elementos???
#numpy.matrix.sort