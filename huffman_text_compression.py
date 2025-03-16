#!/usr/bin/python3

import cgi
import sys

def huffman_encoding(text):
    from collections import Counter
    import heapq
    
    class Node:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

    def build_tree(frequencies):
        heap = [Node(char, freq) for char, freq in frequencies.items()]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = Node(None, left.freq + right.freq)
            merged.left, merged.right = left, right
            heapq.heappush(heap, merged)
        
        return heap[0]

    def generate_codes(node, code=""):
        if node is None:
            return {}
        if node.char is not None:
            return {node.char: code}
        
        codes = {}
        codes.update(generate_codes(node.left, code + "0"))
        codes.update(generate_codes(node.right, code + "1"))
        return codes

    frequencies = Counter(text)
    tree = build_tree(frequencies)
    huffman_codes = generate_codes(tree)

    encoded_text = ''.join(huffman_codes[char] for char in text)
    
    return encoded_text, huffman_codes

print("Content-type: text/html\n")
form = cgi.FieldStorage()
user_input = form.getvalue("text", "")

if user_input:
    encoded_text, codes = huffman_encoding(user_input)
    
    print("<html><body>")
    print("<h2>Huffman Encoding Result</h2>")
    print("<p><b>Original Text:</b> {}</p>".format(user_input))
    print("<p><b>Encoded Binary:</b> {}</p>".format(encoded_text))
    print("<h3>Huffman Codes:</h3>")
    print("<ul>")
    for char, code in codes.items():
        print("<li>{}: {}</li>".format(char, code))
    print("</ul>")
    print("</body></html>")
else:
    print("<html><body>")
    print("<h2>Huffman Encoding</h2>")
    print("<form method='get'>")
    print("Enter text: <input type='text' name='text'>")
    print("<input type='submit' value='Compress'>")
    print("</form>")
    print("</body></html>")
