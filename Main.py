import cv2
import pytesseract
from PIL import Image
import os

# If on Windows, set the path to Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\yassi\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    text = pytesseract.image_to_string(gray)
    return text

# Folder containing screenshots
folder_path = "screenshots"
output_file = "extracted_text.txt"

# Process all images in the folder
with open(output_file, "w", encoding="utf-8") as f:
    for filename in os.listdir(folder_path):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(folder_path, filename)
            text = extract_text_from_image(image_path)
            f.write(f"--- {filename} ---\n{text}\n\n")

print(f"Text extracted and saved to {output_file}")
