from flask import Flask, request, jsonify, send_file
import heapq
import os
import matplotlib.pyplot as plt
import networkx as nx

app = Flask(__name__)

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)

    return heap[0] if heap else None

def draw_huffman_tree(root, filename="huffman_tree.png"):
    G = nx.DiGraph()

    def add_edges(node, parent=None, label=""):
        if node:
            node_id = id(node)
            G.add_node(node_id, label=node.char if node.char else f"{node.freq}")
            if parent is not None:
                G.add_edge(parent, node_id, label=label)

            add_edges(node.left, node_id, "0")
            add_edges(node.right, node_id, "1")

    add_edges(root)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    labels = {node: G.nodes[node]["label"] for node in G.nodes}
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000, node_color="lightblue", font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d["label"] for u, v, d in G.edges(data=True)})
    plt.savefig(filename)
    plt.close()

@app.route('/generate_tree', methods=['POST'])
def generate_tree():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    tree = build_huffman_tree(text)
    if tree:
        draw_huffman_tree(tree)
        return send_file("huffman_tree.png", mimetype='image/png')
    else:
        return jsonify({"error": "Could not build Huffman Tree"}), 500

if __name__ == '__main__':
    app.run(debug=True)
