import matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
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

    for i, row in enumerate(mx):
        if sum(row) == 2:
            for j, col in enumerate(row):
                if col == 1:
                    for k in range(j + 1, len(row)):
                        if row[k] == 1:
                            edges.append((j + 1, k + 1))
                if col == 2:
                    edges.append((j + 1, j + 1))
        graph.add_node(i + 1)

    graph.add_edges_from(edges)
    return graph


with open('issue-1/matrix.csv', 'r') as f:
    reader = csv.reader(f)
    matrix = []
    for row in list(reader):
        line = []
        for col in row:
            line.append(int(col))
        matrix.append(line)
    matrix = np.transpose(matrix)

g = matrix_to_graph(matrix)

# Выводит изоморфные графы
nx.draw_random(g, with_labels=True)
plt.show()
