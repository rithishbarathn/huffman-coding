function showSection(sectionId) {
    document.querySelectorAll('.content-section').forEach(section => {
        section.classList.add('hidden');
    });
    document.getElementById(sectionId).classList.remove('hidden');
}

// Huffman Node Class
class HuffmanNode {
    constructor(char, freq) {
        this.char = char;
        this.freq = freq;
        this.left = null;
        this.right = null;
    }
}

// Function to Build Huffman Tree
function buildHuffmanTree(freqMap) {
    let nodes = Object.entries(freqMap).map(([char, freq]) => new HuffmanNode(char, freq));

    while (nodes.length > 1) {
        nodes.sort((a, b) => a.freq - b.freq); // Sort nodes by frequency

        let left = nodes.shift();
        let right = nodes.shift();

        let newNode = new HuffmanNode(null, left.freq + right.freq);
        newNode.left = left;
        newNode.right = right;

        nodes.push(newNode);
    }

    return nodes[0];
}

// Function to Generate Huffman Codes
function generateHuffmanCodes(root, code = "", huffmanMap = {}) {
    if (root == null) return;

    if (root.char !== null) {
        huffmanMap[root.char] = code;
    }

    generateHuffmanCodes(root.left, code + "0", huffmanMap);
    generateHuffmanCodes(root.right, code + "1", huffmanMap);

    return huffmanMap;
}

// Function to Start the Game
function startHuffmanGame() {
    let inputText = document.getElementById("userInput").value;
    if (inputText.trim() === "") {
        alert("Please enter some text to generate Huffman codes!");
        return;
    }

    // Frequency Calculation
    let freqMap = {};
    for (let char of inputText) {
        freqMap[char] = (freqMap[char] || 0) + 1;
    }

    let root = buildHuffmanTree(freqMap);
    let huffmanCodes = generateHuffmanCodes(root);

    // Display Results
    let outputDiv = document.getElementById("huffmanOutput");
    outputDiv.innerHTML = "<h3>Huffman Codes:</h3><ul>";
    for (let [char, code] of Object.entries(huffmanCodes)) {
        outputDiv.innerHTML += `<li>${char}: ${code}</li>`;
    }
    outputDiv.innerHTML += "</ul>";
}
