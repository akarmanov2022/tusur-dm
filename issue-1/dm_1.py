import matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import csv

matplotlib.use('TkAgg')


def matrix_to_graph(mx: list) -> nx.Graph():
    """
    Генерирует граф по матрице инцидентности.
    :param mx: Матрица инцидентности.
    :return: Сгенерированный граф по матрице инцидентности.
    """
    graph = nx.Graph()
    edges = []
    for i, line in enumerate(mx, start=1):
        for j, number in enumerate(line, start=1):
            i_number = int(number)
            if i_number == 1:
                edges.append((i, j))
        i_line = map(int, line)
        if sum(i_line) == 0:
            graph.add_node(i)
    graph.add_edges_from(edges)
    return graph


with open('issue-1/matrix.csv', 'r') as f:
    reader = csv.reader(f)
    matrix = list(reader)

g = matrix_to_graph(matrix)

# Выводит изоморфные графы
nx.draw_random(g, with_labels=True)
plt.show()
