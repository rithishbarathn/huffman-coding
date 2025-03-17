import heapq
from collections import defaultdict
import tkinter as tk
from tkinter import scrolledtext

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0] if heap else None

def generate_huffman_codes(root, prefix="", codebook={}):
    if root is not None:
        if root.char is not None:
            codebook[root.char] = prefix
        generate_huffman_codes(root.left, prefix + "0", codebook)
        generate_huffman_codes(root.right, prefix + "1", codebook)
    return codebook

def huffman_compress(text):
    root = build_huffman_tree(text)
    huffman_codes = generate_huffman_codes(root)
    compressed_text = "".join(huffman_codes[char] for char in text)
    return compressed_text, huffman_codes, root

def huffman_decompress(compressed_text, root):
    decoded_text = ""
    node = root
    for bit in compressed_text:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            decoded_text += node.char
            node = root
    return decoded_text

def compress_text():
    text = input_text.get("1.0", tk.END).strip()
    compressed_text, huffman_codes, root = huffman_compress(text)
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Compressed Text:\n{compressed_text}\n\nHuffman Codes:\n{huffman_codes}")
    decompress_button.config(state=tk.NORMAL)
    global stored_root
    stored_root = root

def decompress_text():
    compressed_text = output_text.get("1.0", tk.END).strip().split("\n")[1]
    decompressed_text = huffman_decompress(compressed_text, stored_root)
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Decompressed Text:\n{decompressed_text}")

# GUI Setup
root = tk.Tk()
root.title("Huffman Compression")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Enter Text:", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="blue").pack()
input_text = scrolledtext.ScrolledText(root, height=5, font=("Arial", 10))
input_text.pack()

tk.Button(root, text="Compress", command=compress_text, font=("Arial", 12, "bold"), bg="green", fg="white").pack()

tk.Label(root, text="Output:", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="red").pack()
output_text = scrolledtext.ScrolledText(root, height=10, font=("Arial", 10))
output_text.pack()

decompress_button = tk.Button(root, text="Decompress", command=decompress_text, state=tk.DISABLED, font=("Arial", 12, "bold"), bg="orange", fg="white")
decompress_button.pack()

root.mainloop()