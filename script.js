function generateHuffmanTree() {
    let input = document.getElementById('inputString').value;
    if (input.trim() === '') {
        alert("Please enter a string.");
        return;
    }

    fetch("http://127.0.0.1:5000/generate_tree", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: input })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Error generating Huffman tree");
        }
        return response.blob();
    })
    .then(blob => {
        let imgURL = URL.createObjectURL(blob);
        document.getElementById("treeExplanation").innerHTML = `<img src="${imgURL}" alt="Huffman Tree" />`;
    })
    .catch(error => console.error("Error:", error));
}
