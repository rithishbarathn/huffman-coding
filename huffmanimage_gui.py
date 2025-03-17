import heapq
from collections import defaultdict, Counter
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2

class HuffmanNode:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    frequency = Counter(data)
    heap = [HuffmanNode(value, freq) for value, freq in frequency.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0] if heap else None

def generate_huffman_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.value is not None:
            codebook[node.value] = prefix
        generate_huffman_codes(node.left, prefix + "0", codebook)
        generate_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

def compress_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    flat_image = image.flatten()
    
    root = build_huffman_tree(flat_image)
    huffman_codes = generate_huffman_codes(root)
    compressed_data = "".join(huffman_codes[pixel] for pixel in flat_image)
    
    return compressed_data, huffman_codes, root, image.shape

def decompress_image(compressed_data, root, shape):
    decoded_pixels = []
    node = root
    
    for bit in compressed_data:
        node = node.left if bit == "0" else node.right
        if node.value is not None:
            decoded_pixels.append(node.value)
            node = root
    
    decompressed_image = np.array(decoded_pixels, dtype=np.uint8).reshape(shape)
    return decompressed_image

def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if not file_path:
        return
    global compressed_data, stored_root, image_shape
    compressed_data, huffman_codes, stored_root, image_shape = compress_image(file_path)
    messagebox.showinfo("Success", "Image compressed successfully!")

def save_decompressed_image():
    decompressed_img = decompress_image(compressed_data, stored_root, image_shape)
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG file", "*.png")])
    if save_path:
        cv2.imwrite(save_path, decompressed_img)
        messagebox.showinfo("Success", "Image saved successfully!")

# GUI Setup
root = tk.Tk()
root.title("Huffman Image Compression")
root.geometry("400x300")
root.configure(bg="#D3D3D3")

tk.Label(root, text="Huffman Image Compression", font=("Arial", 14, "bold"), bg="#D3D3D3", fg="#333").pack(pady=10)

tk.Button(root, text="Load Image", command=load_image, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=5)

tk.Button(root, text="Save Decompressed Image", command=save_decompressed_image, bg="#FF5733", fg="white", font=("Arial", 12)).pack(pady=5)

root.mainloop()
