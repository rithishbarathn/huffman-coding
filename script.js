function showPage(pageId) {
    let pages = document.querySelectorAll('.page');
    pages.forEach(page => page.style.display = 'none');
    document.getElementById(pageId).style.display = 'block';
}

function showSubPage(subPageId) {
    document.getElementById('textCompression').style.display = 'none';
    document.getElementById('imageCompression').style.display = 'none';
    document.getElementById(subPageId).style.display = 'block';
}

// Huffman Tree Visualization
function buildHuffmanTree(input) {
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

    return nodes[0];
}

function generateExplanation(tree) {
    return "<p>Huffman tree generated. Each leaf represents a character.</p>";
}

function drawHuffmanTree(tree) {
    let canvas = document.getElementById('huffmanTreeCanvas');
    let ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    function drawNode(node, x, y, level) {
        if (!node) return;

        ctx.fillStyle = "black";
        ctx.beginPath();
        ctx.arc(x, y, 20, 0, 2 * Math.PI);
        ctx.fill();
        ctx.fillStyle = "white";
        ctx.textAlign = "center";
        ctx.fillText(node.char || "*", x, y + 5);

        if (node.left) {
            ctx.beginPath();
            ctx.moveTo(x, y);
            ctx.lineTo(x - 50 / level, y + 50);
            ctx.stroke();
            drawNode(node.left, x - 50 / level, y + 50, level + 1);
        }

        if (node.right) {
            ctx.beginPath();
            ctx.moveTo(x, y);
            ctx.lineTo(x + 50 / level, y + 50);
            ctx.stroke();
            drawNode(node.right, x + 50 / level, y + 50, level + 1);
        }
    }

    drawNode(tree, canvas.width / 2, 50, 1);
}
