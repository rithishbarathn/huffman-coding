// Function to switch between pages
function showPage(pageId) {
    let pages = document.querySelectorAll('.page');
    pages.forEach(page => page.style.display = 'none');
    document.getElementById(pageId).style.display = 'block';
}

// Function to display sub-pages under Real-Time Applications
function showSubPage(subPageId) {
    document.getElementById('textCompression').style.display = 'none';
    document.getElementById('imageCompression').style.display = 'none';
    document.getElementById(subPageId).style.display = 'block';
}

// Function to generate Huffman Code
function generateHuffmanCode() {
    let input = document.getElementById('inputString').value;
    if (input.length === 0) {
        alert('Please enter a string.');
        return;
    }
    
    let freqMap = {};
    for (let char of input) {
        freqMap[char] = (freqMap[char] || 0) + 1;
    }

    let nodes = Object.keys(freqMap).map(char => ({ char, freq: freqMap[char], left: null, right: null }));

    while (nodes.length > 1) {
        nodes.sort((a, b) => a.freq - b.freq);
        let left = nodes.shift();
        let right = nodes.shift();
        let newNode = { char: null, freq: left.freq + right.freq, left, right };
        nodes.push(newNode);
    }

    let huffmanCodes = {};
    function generateCodes(node, code = "") {
        if (!node) return;
        if (node.char) huffmanCodes[node.char] = code;
        generateCodes(node.left, code + "0");
        generateCodes(node.right, code + "1");
    }
    
    generateCodes(nodes[0]);

    let encodedString = input.split("").map(char => huffmanCodes[char]).join("");
    let outputDiv = document.getElementById("output");
    outputDiv.innerHTML = `<p>Encoded String: <strong>${encodedString}</strong></p><p>Huffman Codes: ${JSON.stringify(huffmanCodes)}</p>`;
}
