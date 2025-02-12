# 🖼️ Image Text Extractor
Extract text from images using Python + Tesseract OCR

## 🚀 Features
- Supports **JPG, PNG, JPEG** images
- Converts images to text using **Tesseract OCR**
- Processes all images inside the `screenshots/` folder
- Saves extracted text to `extracted_text.txt`

## 🛠️ Setup
### 1️⃣ Install Dependencies
```sh
pip install pytesseract pillow opencv-python
```

### 2️⃣ Install Tesseract OCR
- **Windows:** [Download & Install](https://github.com/UB-Mannheim/tesseract/wiki)
- **Linux/macOS:** Install via package manager:
  ```sh
  sudo apt install tesseract-ocr  # Ubuntu/Debian
  brew install tesseract          # macOS
  ```

### 3️⃣ Set Tesseract Path (Windows Only)
If Tesseract is not in your system `PATH`, add this to `main.py`:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Path\To\Tesseract-OCR\tesseract.exe'
```
_Default path: `C:\Program Files\Tesseract-OCR\tesseract.exe`_

## 📂 Usage
1. Place your images inside the `screenshots/` folder
2. Run the script:
   ```sh
   python main.py
   ```
3. Extracted text will be saved in `extracted_text.txt`

## ❓ Issues
If you face errors, check:
- **Tesseract is installed & working** (`tesseract --version` in CMD)
- **Correct Tesseract path** in `main.py`
- **Images exist** inside `screenshots/` folder

🔥 Happy Coding! 🔥

