import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # Inisialisasi variabel
    dist = {node: float('inf') for node in graph.nodes()}
    dist[start] = 0
    visited = set()

    while len(visited) != len(graph.nodes()):
        # Pilih node dengan jarak terpendek yang belum dikunjungi
        min_dist = float('inf')
        min_node = None
        for node in graph.nodes():
            if node not in visited and dist[node] < min_dist:
                min_dist = dist[node]
                min_node = node

        # Perbarui jarak ke node tetangga
        for neighbor in graph.neighbors(min_node):
            edge_weight = graph[min_node][neighbor]['weight']
            dist[neighbor] = min(dist[neighbor], dist[min_node] + edge_weight)

        visited.add(min_node)

    return dist

def calculate_shortest_path():
    start_node = start_entry.get()
    end_node = end_entry.get()

    if start_node not in graph.nodes() or end_node not in graph.nodes():
        messagebox.showerror('Error', 'Node tidak valid.')
        return

    shortest_dist = dijkstra(graph, start_node)
    shortest_path = nx.shortest_path(graph, start_node, end_node)

    shortest_dist_str = ', '.join(f'{node}: {dist}' for node, dist in shortest_dist.items())
    shortest_path_str = ' -> '.join(shortest_path)

    messagebox.showinfo('Hasil', f'Jarak terpendek:\n{shortest_dist_str}\n\nJalur terpendek:\n{shortest_path_str}')

def draw_graph():
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos, with_labels=True, node_size=500, node_color='lightblue')
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title('Grafik')
    plt.axis('off')
    plt.show()

# Membangun GUI
window = tk.Tk()
window.title('Algoritma Dijkstra')
window.geometry('400x200')

start_label = tk.Label(window, text='Node Awal:')
start_label.pack()

start_entry = tk.Entry(window)
start_entry.pack()

end_label = tk.Label(window, text='Node Akhir:')
end_label.pack()

end_entry = tk.Entry(window)
end_entry.pack()

calculate_button = tk.Button(window, text='Hitung', command=calculate_shortest_path)
calculate_button.pack()

draw_button = tk.Button(window, text='Gambar Grafik', command=draw_graph)
draw_button.pack()

# Membaca grafik dari file
graph = nx.Graph()
graph.add_edge('A', 'B', weight=3)
graph.add_edge('A', 'C', weight=4)
graph.add_edge('B', 'C', weight=2)
graph.add_edge('B', 'D', weight=1)
graph.add_edge('C', 'D', weight=5)
graph.add_edge('C', 'E', weight=3)
graph.add_edge('D', 'E', weight=2)

window.mainloop()
