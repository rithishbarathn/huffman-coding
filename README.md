This project implements Huffman Compression for both text and images using Python and Tkinter. The application provides a user-friendly GUI to compress and decompress text as well as grayscale images.

Features
🔹 Huffman Text Compression:
Enter text input in the GUI.
Apply Huffman encoding to compress the text.
Decompress and restore the original text.
Displays Huffman codes used for encoding.

🔹 Huffman Image Compression:
Load an image from your system.
Apply Huffman compression to reduce image size.
Decompress and restore the original image.
Supports grayscale image compression.
Requirements
Ensure you have Python and the required dependencies installed:

Step 1
Copy
Edit
pip install opencv-python numpy pillow
Installation
Clone the repository (or download the source files):

Step 2
Copy
Edit
git clone https://github.com/your-repo/huffman-compression.git
cd huffman-compression
Install required dependencies:

Step 3
Copy
Edit
pip install -r requirements.txt
Run the Text Compression GUI:

Step 4
Copy
Edit
python huffmantext_gui.py
Run the Image Compression GUI:

Step 5
Copy
Edit
python huffmanimage_gui.py
Usage

📜 Text Compression:
Open the Huffman Text Compression GUI.
Enter the text in the input box.
Click "Compress" to apply Huffman encoding.
Click "Decompress" to restore the original text.
View Huffman codes used for encoding.

🖼 Image Compression:
Open the Huffman Image Compression GUI.
Click "Load Image" to select an image.
Click "Compress" to apply Huffman encoding.
Click "Decompress" to restore the original image.
Optionally, save the compressed image.
Troubleshooting
"No module named 'cv2'" → Install OpenCV:

Step 6
Copy
Edit
pip install opencv-python
"No module named 'PIL'" → Install Pillow:

Step 7
Copy
Edit
pip install pillow
GUI not opening? Ensure you are running Python 3.7+.

License
This project is open-source and available under the MIT License.
