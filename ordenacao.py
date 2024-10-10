import time
import random


def bubble_sort(lista):
    tam = len(lista)
    while tam > 1:
        for j in range(tam - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        tam -= 1


def insertion_sort(lista):
    for i in range(1, len(lista)): #assume que o primeiro elemento já esta ordenado, então começa do 1
        ordem = lista[i] #guarda o elemento que sera inserido
        j = i-1 
        while j>=0 and lista[j] > ordem:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = ordem

       
def selection_sort(lista):
    for i in range(len(lista)): 
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]           


def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda =  lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        e = d = l = 0

        while e < len(esquerda) and d < len(direita):
            if esquerda[e] < direita[d]:
                lista [l] = esquerda[e]

                e += 1
            else:
                lista [l] = direita[d]

                d += 1
            l += 1

        while e < len(esquerda):
            lista[l] = esquerda[e]
            e += 1
            l += 1

        while d < len(direita):
            lista[l] = direita[d]
            d += 1
            l += 1
            


def ordenar(lista, algoritmo):
    inicio = time.time()
    if algoritmo == 1:
       bubble_sort(lista) 
    elif algoritmo == 2:
        selection_sort(lista)
    elif algoritmo == 3:
        insertion_sort(lista)
    elif algoritmo == 4:
        merge_sort(lista)
    else:
        print("Algoritmo inválido. Escolha um número entre 1 e 4.")
    
    fim = time.time()
    return fim - inicio


def main():
    lista = []

    i = 0
    while (i  < 5000):
        lista.append(random.randint(0, 5000))
        i += 1


    algoritmo = int(input("1. Bubble Sort\n2. Selection Sort\n3. Insertion Sort\n4. Merge Sort\n"))
    ordenar(lista, algoritmo)

    tempos = []
    for _ in range(3):
        execucao_total = ordenar(lista[:], algoritmo)
        tempos.append(execucao_total)

    soma = 0
    for i in tempos:
        soma += i

    media = soma / len(tempos)

    print(f"Algoritmo: {algoritmo}\nTempo de execução: {execucao_total:.3f} segundos\nMédia dos tempos: {media:.3f}")


def arquivo_seq():
    with open("cp/sequencia.txt", "w") as arquivo:
        seq = []
        i = 0
        while (i  < 50):
            seq.append(random.randint(0, 50))
            i += 1
        
        arquivo.write(str(seq))
    arquivo.close()


def seq_ordenada():
    with open("cp/seq-ordenada.txt", "w") as arquivo:
        seq = []
        i = 0
        while (i  < 50):
            seq.append(random.randint(0, 50))
            i += 1
        
        bubble_sort(seq)
        arquivo.write(str(seq))
    arquivo.close


main()
arquivo_seq()
seq_ordenada()
