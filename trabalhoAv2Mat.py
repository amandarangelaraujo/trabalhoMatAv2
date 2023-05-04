#fazer o baralho

from itertools import combinations

def gerar_baralho():
    naipes = ['copas', 'ouros', 'espadas', 'paus']
    valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    baralho = []
    for naipe in naipes:
        for valor in valores:
            baralho.append((naipe, valor))
    return baralho

#distribuir as cartas, recebendo o return da função gerar_baralho
def distribuir_cartas(baralho):
    import random
    #mistura aleatoriamente as cartas
    random.shuffle(baralho)
    mao_jogadores = []
    #vai distribuir 4 vezes, já que são quatro jogadores, 3 cartas

    for i in range (4):
        mao=[] #a vez de que receber
        for j in range(3): #a distribuição de cartas em si
            mao.append(baralho.pop(0)) #remove a carta da primeira posição e salva ela na lista mão
        mao_jogadores.append(mao) 
      
    mesa = []
    #distribuir as cartas da mesa
    for i in range(2):
        mesa.append(baralho.pop(0)) #tira de baralho as cartas e salva na variavel mesa

    #a função retorna a variável mao, que tem as cartas dos jogadores e mesa, que tem as cartas que estão na mesa
    return mao_jogadores, mesa

#atribuindo a variáveis fora das funções o seu retorno

baralho = gerar_baralho()
mao_jogadores,mesa = distribuir_cartas(baralho)

#definindo as cartas dos jogadores
jogadorNumero1=mao_jogadores[0]
jogadorNumero2=mao_jogadores[1]
jogadorNumero3=mao_jogadores[2]
jogadorNumero4=mao_jogadores[3]
print(f"{jogadorNumero1} \n {jogadorNumero2} \n {jogadorNumero3} \n {jogadorNumero4}" )


#combinar as cartas da mesa com as cartas da mão, depois fazer uma combinação dessas 
# cartas para poder formar um trio.
#LIMPAR ESSE CÓDIGO!!!
print('##########')
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


print(f'possibilidades para o jogador 1: {list(trioJogador1)}')
print(f'possibilidades para o jogador 2: {list(trioJogador2)}')
print(f'possibilidades para o jogador 3: {list(trioJogador3)}')
print(f'possibilidades para o jogador 4: {list(trioJogador4)}')

pontosJogador1=[]
pontosJogador2=[]
pontosJogador3=[]
pontosJogador4=[]

##CHECAR SE DO MESMO NAIPE, SOMAR UM PONTO.
def checarNaipeCopas():
    print("oioioi")

def checarNaipeEspadas():
    print("oioioi")

def checarNaipeOuros():
    print("oioioi")

def checarNaipePaus():
    print("oioioi")


def chegarSequência():
    print("oioioi")
    #poderia fazer uma função para cada naipe que rodasse a lista e chegasse se tem uma string que armazenada esse dado
    #la em cima chamaria a função para cada jogador
    #seriam 4 funções.
    ##CHEGAR SE SEQUÊNCIA USANDO O I I-1 PARA VER SE É UMA SEQUÊNCIA
    for i in range(60): ##ta falando que não tem len nessa type.
    #quantidade de combinaçoes possiveis==60
        if trioJogador1[i+1]-trioJogador1[i]==1:  ##TypeError: 'itertools.combinations' object is not subscriptable
            pontosJogador1=pontosJogador1+1
        else:
            continue
print(f'o jogador numero 1 recebeu {pontosJogador1}')

#função sort = sorted(trioJogador1)
# if (trioJogador[0] + 1 == trioJogador[1] and triojogador[1] + 1 == triojogador[2])
#mas esse abrange todas as cartas?

#teria que trocar os vetores pelos dicionários.
#pecorrer os dicinários>>>>pegaria direito.
