import time
from graph import Graph

def main():
    inicio = time.time() #marca o tempo de início da execução
    grafo = Graph.build_graph("casoteste.txt") #inserir nome do arquivo
    total_sum = Graph.calculate_sum(grafo, list(grafo.keys())[0]) #calcula a soma total dos produtos a partir de um nodo inicial no grafo
    fim = time.time() #marca o tempo de início da execução

    #resultado
    print("Hidrogênios: " + str(total_sum))
    #calcula tempo de execucao
    print("Tempo de Execução: {:.2f} segundos".format(fim - inicio))

if __name__ == "__main__":
    main()
