class Graph:
    @staticmethod
    def build_graph(file_path):
        graph = {}

        with open(file_path, "r") as file: #leitura do arquivo
            for line in file:
                Graph.input_string(graph, line.strip())

        return graph

    @staticmethod
    def input_string(graph, string):
        list_str = string.split("->") #separa a string de entrada usando "->" como delimitador
        valores_origem = list_str[0].split(" ") #obtem os valores da origem da aresta

        if len(valores_origem) == 3: #verifica se a origem tem 3 valores (representando um único nó) e adiciona ao grafo
            Graph.add_element(graph, string)
        else:
            #caso tenha 3 valores, itera pares de valores e cria novas strings
            #com cada par e o destino, adicionando cada uma ao grafo
            for i in range(0, len(valores_origem) - 1, 2):
                nova_string = valores_origem[i] + " " + valores_origem[i + 1] + " ->" + list_str[1]
                Graph.add_element(graph, nova_string)

    @staticmethod
    def add_element(graph, string):
        values = string.split(" ") #reparte a string de entrada em valores usando espaços em branco como delimitador
        value_aresta, elem_origem, _, _, elem_destino = values #obtem os valores relevantes da string
        #garante que os elementos de origem e destino estejam presentes no grafo
        graph.setdefault(elem_origem, [])
        graph.setdefault(elem_destino, [])
        #adiciona a aresta ao grafo, representada como uma tupla
        graph[elem_origem].append((elem_destino, value_aresta))

    @staticmethod
    def calculate_sum(graph, node, current_product=1, visited=None):
        global visited_set #declaracao de uma variável global para armazenar os nodos visitados
    
        if visited is None:
            visited = visited_set
            visited.add(node)

        #caso o nodo não tiver vizinhos, retorna o produto acumulado até esse ponto
        if not graph[node]:
            return current_product

        #recursão usada para calcular a soma dos produtos ao longo dos vizinhos do nodo atual
        return sum(
        Graph.calculate_sum(graph, neighbor, current_product * int(value), visited)
        for neighbor, value in graph[node]
        if neighbor not in visited
    )

visited_set = set() #inicializa um conjunto vazio para buscar os nodos visitados

