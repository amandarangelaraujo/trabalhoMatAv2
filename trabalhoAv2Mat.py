#fazer o baralho
def gerar_baralho():
    naipes = ['copas', 'ouros', 'espadas', 'paus']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'valete', 'dama', 'rei', 'ás']
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