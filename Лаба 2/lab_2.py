from pyvis.network import Network


def edges_generator(l, n):
    edges = []
    for i in range(n):
        for j in range(n):
            if l[i][j]:
                edges.append((i + 1, j + 1))
    return edges


n = int(input("Введите количество вершин:"))
adjacency_matrix = []
for i in range(n):
    stroke = list(map(int, input(f"Введите {i + 1} строку: ").split()))
    adjacency_matrix.append(stroke)

directed = (
    False
    if list(map(list, zip(*adjacency_matrix))) == adjacency_matrix
    else True
)

net = Network(
    notebook=True,
    bgcolor="#222222",
    font_color="white",
    height="600px",
    width="100%",
    directed=directed,
)

nodes = [i + 1 for i in range(n)]

net.add_nodes(nodes, label=[str(i) for i in nodes])
edges = edges_generator(adjacency_matrix, n)
filtered_edges = []
edges_plot = []
for i in edges:
    if i[::-1] not in filtered_edges:
        filtered_edges.append(i)
        edges_plot.append((i[0], i[1], 0 if i[::-1] in edges else 1))

for i in edges_plot:
    net.add_edge(source=i[0], to=i[1], arrows="to" if i[2] else "false")

net.show("nodes.html")
