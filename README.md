Huffman Image Compression GUI
This project implements Huffman Image Compression using Python and Tkinter. The application allows users to select an image, compress it using Huffman encoding, and then decompress it back to its original form.

Features
Load an image from your system
Apply Huffman compression to reduce image size
Decompress and view the original image
Simple GUI using Tkinter
Supports grayscale image compression
Requirements
Ensure you have the following dependencies installed:

Step 1
Copy
Edit
pip install opencv-python numpy pillow
Installation
Clone the repository (or download the source files):

Step 2
Copy
Edit
git clone https://github.com/your-repo/huffman-image-compression.git
cd huffman-image-compression
Install required dependencies:

Step 3
Copy
Edit
pip install -r requirements.txt
Run the application:

Step 4
Copy
Edit
python huffmanimage_gui.py
Usage
Open the application and click "Load Image".
The image will be displayed in the GUI.
Click "Compress" to apply Huffman compression.
Click "Decompress" to restore the original image.
You can save the compressed image if needed.
Troubleshooting
If you get an error "No module named 'cv2'", install OpenCV:

Step 5
Copy
Edit
pip install opencv-python
If you get an error "No module named 'PIL'", install Pillow:
sh
Copy
Edit

Step 6
pip install pillow
