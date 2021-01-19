def quicksort(vetor, dim):     # Algoritmo Quicksort com Pivô no início da lista #
    if dim == 1:
        return
    if dim == 2:
        if vetor[0] > vetor[1]:
            vetor[0], vetor[1] = vetor[1], vetor[0]
    else:
        pilha = []
        pilha.append(0)
        tamanho = int(len(vetor))
        pilha.append(tamanho)
        while pilha:
            lim_dir = pilha.pop()
            lim_esq = pilha.pop()
            if (lim_dir - lim_esq >= 2):
                pivo = auxiliar_quick_1(vetor, lim_esq, lim_dir)
                pilha.append(pivo + 1)
                pilha.append(lim_dir)
                pilha.append(lim_esq)
                pilha.append(pivo)

def auxiliar_quick_1(vetor, inicio, fim):
    pivo = vetor[inicio]
    i = fim
    j = fim - 1
    while j > inicio:
        if vetor[j] > pivo:
            i -= 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
        j -= 1
    while j != (i - 1):
        vetor[j] = vetor[j + 1]
        j += 1
    vetor[i - 1] = pivo
    return (i - 1)


def quicksort2(vetor, dim):     # Algoritmo Quicksort com Pivô no centro da lista #
    if dim == 1:
        return
    if dim == 2:
        if vetor[0] > vetor[1]:
            vetor[0], vetor[1] = vetor[1], vetor[0]
    else:
        pilha = []
        pilha.append(0)
        tamanho = int(len(vetor))
        pilha.append(tamanho - 1)
        while pilha:
            lim_dir = pilha.pop()
            lim_esq = pilha.pop()
            if (lim_esq < lim_dir):
                esquerda, direita = auxiliar_quick_2(vetor, lim_esq, lim_dir)
                pilha.append(esquerda)
                pilha.append(lim_dir)
                pilha.append(lim_esq)
                pilha.append(direita)

def auxiliar_quick_2(vetor, inicio, fim):
    pivo = vetor[int((inicio + fim) / 2)]
    esquerda = inicio
    direita = fim
    while esquerda <= direita:
        while vetor[esquerda] < pivo:
            esquerda += 1
        while vetor[direita] > pivo:
            direita -= 1
        if esquerda <= direita:
            vetor[esquerda], vetor[direita] = vetor[direita], vetor[esquerda]
            esquerda += 1
            direita -= 1
    return esquerda, direita