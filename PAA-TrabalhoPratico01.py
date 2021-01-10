
# ====================================================================================================================  #

#  TRABALHO PRÁTICO DA DISCIPLINA DE PROJETO E ANÁLISE DE ALGORÍTIMOS - 2020/2021 - CÓDIGO FONTE                        #
#  Bacharelado em Ciência da Computação, Faculdade de Ciências e Tecnologia - UNESP. Campus de Presidente Prudente, SP  #
#  Alunos:                                                                                                              #
#  Pedro Henrique Zago Costa - R.A.: 181257084 - e-mail institucional: pedro.zago@unesp.br                              #
#  David Jr. Rodrigues - R.A.: 181257629 - e-mail institucional: david.junior@unesp.br                                  #                                                            #
#  Gabriel Cecon Carlsen - R.A.: 181250969 - e-mail institucional: cecon.carlsen@unesp.br                               #
#  Professor: Danilo Medeiros Eler                                                                                      #
#  Linguagem Escolhida: Python 3                                                                                        #

# ====================================================================================================================  #


# ====================================================================================================================  #
#  -> FUNCIONAMENTO <-                                                                                                  #
#  O Terminal fará três perguntas bem simples:                                                                          #
#  I. Algoritmo: Aqui é inserido qual algoritmo de ordenação se deseja usar. As opções são (insira o número):           #
#    1- Bubblesort                                                                                                      #
#    2- Bubblesort com Melhorias                                                                                        #
#    3- Quicksort com o Pivô no início da lista                                                                         #
#    4- Quicksort com o Pivô no centro da lista                                                                         #
#    5- Insertionsort                                                                                                   #
#    6- Shellsort                                                                                                       #
#    7- Selectionsort                                                                                                   #
#    8- Heapsort                                                                                                        #
#    9- Mergesort                                                                                                       #
#  II. Entradas: Aqui é inserido quantas entradas (números a serem ordenados) teremos.                                  # 
#    - Testamos com os valores 1.000, 5.000, 10.000, 15.000, 20.000 e 25.000; mas qualquer entrada é válida             # 
#  III. Modo: Aqui é inserido de que modo os valores serão inseridos nos algoritmos de ordenação. Podem ser:            #
#    1- Normal (padrão, aleatório, caso médio)                                                                          #
#    2- Ordenado (melhor caso, ideal)                                                                                   #
#    3- Ordenado Inversamente (pior caso)                                                                               #
# ====================================================================================================================  #


import random
import time


def modo(vetor, dim, opcao):     # Ordena os dados em modo crescente ou decrescente para testar o melhor ou pior caso #
    if opcao == 1:
        print(" Caso Médio -", end = '')
    elif opcao == 2:
        selectionsort(vetor, dim)
        print(" Melhor Caso -", end = '')
    else:
        i = 0
        while i < (dim - 1):
            maior = i
            j = (i + 1)
            while j < dim:
                if vetor[j] > vetor[maior]:
                    maior = j
                j += 1
            if vetor[i] != vetor[maior]:
                vetor[i], vetor[maior] = vetor[maior], vetor[i]
            i += 1
        print(" Pior Caso -", end = '')


def bubblesort(vetor, dim):     # Algoritmo Bubblesort #
    i = 1 
    j = 0
    while i < dim:
        while j < (dim - i):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
            j += 1
        j = 0
        i += 1


def bubblesort2(vetor, dim):     # Algoritmo Bubblesort Melhorado #   
    troca = True
    i = 0
    j = 0
    while i < (dim - 1) and troca == True:
        troca = False
        while j < (dim - i - 1):
            if vetor[j] > vetor[j + 1]:
                troca = True
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
            j += 1
        j = 0
        i += 1     


def quicksort(vetor):     # Algoritmo Quicksort com Pivô no início da lista #
    auxiliar_quick_1(vetor, 0, len(vetor) -1)

def auxiliar_quick_1(vetor, inicio, fim):
    if inicio < fim:
        div = auxiliar_quick_2(vetor, inicio, fim)
        auxiliar_quick_1(vetor, inicio, div - 1)
        auxiliar_quick_1(vetor, div + 1, fim)

def auxiliar_quick_2(vetor, inicio, fim):
    pivo = vetor[inicio]
    esquerda = inicio + 1
    direita = fim
    ok = False
    while ok != True:
        while esquerda <= direita and vetor[esquerda] <= pivo:
            esquerda += 1
        while direita >= esquerda and vetor[direita] >= pivo:
            direita -= 1
        if direita < esquerda:
            ok = True
        else:
            vetor[esquerda], vetor[direita] = vetor[direita], vetor[esquerda]
    vetor[inicio], vetor[direita] = vetor[direita], vetor[inicio]
    return direita


def quicksort2(vetor, inicio, fim):     # Algoritmo Quicksort com Pivô no centro da lista #
    if inicio < fim:
        pivo = auxiliar_quick_3(vetor, inicio, fim)
        quicksort2(vetor, inicio, pivo - 1)
        quicksort2(vetor, pivo + 1, fim)

def auxiliar_quick_3(vetor, inicio, fim):
    pivo = vetor[inicio]
    esquerda = inicio + 1
    direita = fim
    ok = False
    while ok != True:
        while esquerda <= direita and vetor[esquerda] <= pivo:
            esquerda += 1
        while direita >= esquerda and vetor[direita] >= pivo:
            direita -= 1
        if direita < esquerda:
            ok = True
        else:
            vetor[esquerda], vetor[direita] = vetor[direita], vetor[esquerda]
    vetor[inicio], vetor[direita] = vetor[direita], vetor[inicio]
    return direita


def insertionsort(vetor, dim):     # Algoritmo Insertionsort #
    i = 1
    while i < dim:
        x = vetor[i]
        j = (i - 1)
        while j >= 0 and vetor[j] > x:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = x
        i += 1


def shellsort(vetor, dim):     # Algoritmo Shellsort #
    h = 1
    while h < dim:
        h = 3 * h + 1
    while h > 1:
        h = int(h / 3)
        i = h
        while i < dim:
            aux = vetor[i]
            j = i - h
            while j >= 0 and aux < vetor[j]:
                vetor[j + h] = vetor[j]
                j -= h
            vetor[j + h] = aux
            i += 1


def selectionsort(vetor, dim):     # Algoritmo Selectionsort #
    i = 0
    while i < (dim - 1):
        menor = i
        j = (i + 1)
        while j < dim:
            if vetor[j] < vetor[menor]:
                menor = j
            j += 1
        if vetor[i] != vetor[menor]:
            vetor[i], vetor[menor] = vetor[menor], vetor[i]
        i += 1


def heapsort(vetor, dim):     # Algoritmo Heapsort #
    i = int(dim / 2)
    while i >= 0:
        auxiliar_heap(vetor, i, dim - 1)
        i -= 1
    i = dim - 1
    while i >= 1:
        vetor[0], vetor[i] = vetor[i], vetor[0]
        auxiliar_heap(vetor, 0, i - 1)
        i -= 1

def auxiliar_heap(vetor, raiz, fundo):
    ok = False
    while (raiz * 2) <= fundo and ok != True:
        if (raiz * 2) == fundo:
            maximo = raiz * 2
        elif vetor[(raiz * 2)] > vetor[(raiz * 2) + 1]:
            maximo = raiz * 2
        else:
            maximo = (raiz * 2) + 1
        
        if vetor[raiz] < vetor[maximo]:
            vetor[raiz], vetor[maximo] = vetor[maximo], vetor[raiz]
            raiz = maximo
        else:
            ok = True


def mergesort(vetor):     # Algoritmo Mergesort #
    if len(vetor) > 1:
        mid = int(len(vetor) / 2)
        esquerda = vetor[:mid]
        direita = vetor[mid:]
        mergesort(esquerda)
        mergesort(direita)
        i = 0
        j = 0
        k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1
        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1


valido = 0
while valido == 0:
    print("")
    print(" Algoritmo: ", end = '')     # Escolhendo o algoritmo desejado #
    alg = int(input())
    if alg >= 1 and alg <= 9:
        valido = 1
    else:
        print(" Por favor, insira um valor válido (entre 1 e 9). ")
        print("")
valido = 0
while valido == 0:        
    print(" Entradas: ", end = '')     # Escolhendo o número de entradas desejado #
    ent = int(input())
    if ent > 0:
        valido = 1
    else:
        print(" Por favor, insira um valor válido (maior que zero). ")
        print("")
valido = 0
while valido == 0:
    print(" Modo: ", end = '')     # Escolhendo o modo desejado (normal, melhor ou pior caso)#
    mod = int(input())
    if mod >= 1 and mod <= 3:
        valido = 1
    else:
        print(" Por favor, insira um valor válido (entre 1 e 3). ")
        print("")


elementos = []
for j in range(0, ent):
    i = random.randint(0, 25000)
    elementos.append(i)


Dim = len(elementos)
modo(elementos, Dim, mod)


clock_start = time.time()
if alg == 1:
    print(" Bubblesort ")
    print("")
    if Dim <= 20:
        print(" pré-ordenação: ", elementos)
    bubblesort(elementos, Dim)
elif alg == 2:
    print(" Bubblesort Melhorado ")
    print("")
    if Dim <= 20:
        print(" pré-ordenação: ", elementos)
    bubblesort2(elementos, Dim)
elif alg == 3:
    print(" Quicksort com Pivô no início da lista ")
    print("")
    if Dim <= 20:
        print(" pré-ordenação: ", elementos)
    quicksort(elementos)
elif alg == 4:
    print(" Quicksort com Pivô no centro da lista ")
    print("")
    if Dim <= 20:
        print(" pré-ordenação: ", elementos)
    quicksort2(elementos, 0, Dim - 1)
elif alg == 5:
    print(" Insertionsort ")
    print("")
    if Dim <= 20:
        print(" pré-ordenação: ", elementos)
    insertionsort(elementos, Dim)
elif alg == 6:
    print(" Shellsort ")
    print("")
    if Dim <= 20:
        print(" pré-ordenação: ", elementos)
    shellsort(elementos, Dim)
elif alg == 7:
    print(" Selectionsort ")
    print("")
    if Dim <= 20:
        print(" pré-ordenação: ", elementos)
    selectionsort(elementos, Dim)
elif alg == 8:
    print(" Heapsort ")
    print("")
    if Dim <= 20:
        print(" pré-ordenação: ", elementos)
    heapsort(elementos, Dim)
else:
    print(" Mergesort ")
    print("")
    if Dim <= 20:
        print(" pré-ordenação: ", elementos)
    mergesort(elementos)

clock_end = time.time()
if Dim <= 20:
    print(" pós-ordenação: ", elementos)
print(" tempo de execução: ",(clock_end - clock_start), " segundos.")
print("")
print(" Pedro Henrique Zago Costa, David Jr. Rodrigues e Gabriel Cecon Carlsen. ")
print("")


# ========================================================================= #
#  Pedro Henrique Zago Costa - David Jr. Rodrigues - Gabriel Cecon Carlsen  #
# ========================================================================= #