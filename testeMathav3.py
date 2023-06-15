'''PRECISO COLOCAR ALGO QUE PARE O PROGRAMA ASSIM QUE ELE NÃO FOR FÓRMULA BEM FORMULADA
TO DO:
1- COLOCAR CASO A SENTENÇA TENHA UMA NEGAÇÃO ~ 
2- COLOCAR CASO A SENTENÇA TENHA UM PARENTESES ABERTO E NÃO FECHADO
3- '''
import pandas as pd
#entrada das sentenças
quantidadeSentencas = int(input("quantas sentenças você quer adicionar?"))
sentencaCompleta=[]
ListaLetrasAlfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n', 'o','p','q','r','s','t','u','w','x','y','z']
listaOperadoesLogicos = ['^','v','~','>','-']
for i in range(quantidadeSentencas):
    print('não utilize a letra V para representar uma sentença')
    sentenca = input(f'escreva a sentença {i+1}: ')
    sentenca.lower()
    sentencaCompleta.append(sentenca)
    if ' ' in sentencaCompleta:
        sentencaCompleta = sentencaCompleta.remove(' ')

print(sentencaCompleta)


'''ETAPA 2'''
#etapa 2: análise sintática
#se a proxima letra é também uma letra, se for, não é uma fórmula bem formada
#se nao tiver operadores lógicos entre as letras não é uma fórmula bem formada
for i in range(len(sentencaCompleta)):
    sentenca = sentencaCompleta[i]
    list(sentenca) #transforma a sentença em uma lista de caracteres
    for j in range(len(sentenca)-1): #checagem de letras ao lado de letras
        if sentenca[j] in ListaLetrasAlfabeto and sentenca[j+1] in ListaLetrasAlfabeto:
            print('não é uma fórmula bem formada, faltou um operador lógico')
            break
        #se não faltou um operador lógico ele entra aqui
        else:
            continue
            #inicio da checagem de operador lógicos lado a lado
            #problema: so checa se forem operadores lógicos iguais!!!
            #se tiver >1 v
            if sentenca[j] in listaOperadoesLogicos and sentenca[j+1] == listaOperadoesLogicos:
                print('não é uma fórmula bem formada! oi')
                break
            else:
                print('é uma fórmula bem formada')
                
                '''continue
                #se tiver >1 ^
                if sentenca[j] == '^' and sentenca[j+1] == '^':
                    print('não é uma fórmula bem formada')
                    break
                else:
                    continue
                    #se tiver >1 >
                    if sentenca[j] == '>' and sentenca[j+1] == '>':
                        print('não é uma fórmula bem formada')
                        break
                    else:
                        continue
                        #se tiver >1 -
                        if sentenca[j] == '-' and sentenca[j+1] == '-':
                            print('não é uma fórmula bem formada')
                            break
                        else:
                            continue'''
print('etapa 2.1 ok')


'''se tiver parenteses abertos e não fechados, não é uma fórmula bem formulada
#como eu poderia fazer isso?
# aqui é apenas para a primeira parte, ANTES DO |-
# o que vem depois eu poderia salvar como um split sep e adicionar um separador e atribuir um separador tipo @'''

#TESTE COM O TEOREMA DE Tableaux
#no teorema a sentença so será tautologia se as duas letras assumirem valores T E V, no caso elas entram nas respectivas listas
listaLetrasFalsas = []
listaLetrasVerdadeiras = []
#etapa 3: análise teorema
for i in range(len(sentencaCompleta)):
    sentenca = sentencaCompleta[i] #acessei a sentença
    list(sentenca) #separei a sentença
    #caso ela comece com ~
    if sentenca[0] == '~':
        operadorLogico = sentenca[2]
    #caso não comece com ~
    #aplicar o teorema/assumindo que a sentença não termine não comece com ~	
    if len(sentenca)>1:
        operadorLogico = sentenca[1]
        if operadorLogico == 'v':
            #como estamos falando do lado esquerdo da sentença, vamos assumir para eles valores de f
            listaLetrasFalsas.append(sentenca[0])
            listaLetrasFalsas.append(sentenca[2])
        if operadorLogico == '>':
            listaLetrasVerdadeiras.append(sentenca[0])
            listaLetrasFalsas.append(sentenca[2])
        if operadorLogico == '^':
            listaLetrasFalsas.append(sentenca[0])
            listaLetrasFalsas.append(sentenca[2])
        if operadorLogico == '-':
            #como estamos falando do lado esquerdo da sentença, vamos assumir para eles valores de f
            listaLetrasVerdadeiras.append(sentenca[0])
            listaLetrasFalsas.append(sentenca[2])
    else: #caso seja apenas uma letra
        operadorLogico = sentenca[0]
        listaLetrasVerdadeiras.append(sentenca[0])

'''if operadorLogico == '-': ... COMPLETAR'''

set(listaLetrasFalsas) #remover as duplicatas
set(listaLetrasVerdadeiras)
list(listaLetrasFalsas) #trasnformar em lista novamente
list(listaLetrasVerdadeiras)
listaLetrasFalsas.sort() #organizar por ordem alfabetica
listaLetrasVerdadeiras.sort()
print(listaLetrasFalsas)#mostrar as listas
print(listaLetrasVerdadeiras)
#checar se é uma tautologia
somador=0
if len(listaLetrasFalsas) == len(listaLetrasVerdadeiras): #porque elas só podem ser iguais se tiverem o mesmo tamanho
    for j in range(len(listaLetrasFalsas)):
        if listaLetrasFalsas[j] in listaLetrasVerdadeiras:
            somador=somador+1
    if somador == len(listaLetrasFalsas):
        print('é uma tautologia')

else:
    print('não é uma tautologia')



        


    
