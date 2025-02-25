import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import cv2
import pytesseract
import os

# Set tesseract path (adjust if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\yassi\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return "Error reading image."
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

# Global variables to store user's selection
selected_folder = ""
selected_files = []
mode = None  # Either "folder" or "files"

def select_folder():
    global selected_folder, mode
    folder = filedialog.askdirectory(title="Select Folder Containing Images")
    if folder:
        selected_folder = folder
        mode = "folder"
        lbl_selected.config(text=f"Folder selected:\n{selected_folder}")
    else:
        messagebox.showwarning("Warning", "No folder selected.")

def select_files():
    global selected_files, mode
    files = filedialog.askopenfilenames(
        title="Select Image Files", 
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
    )
    if files:
        selected_files = files
        mode = "files"
        filenames = [os.path.basename(f) for f in selected_files]
        lbl_selected.config(text=f"Files selected:\n{', '.join(filenames)}")
    else:
        messagebox.showwarning("Warning", "No files selected.")

def process_images():
    images = []
    if mode == "folder":
        if not os.path.isdir(selected_folder):
            messagebox.showerror("Error", "Invalid folder selected!")
            return
        images = [os.path.join(selected_folder, f) for f in os.listdir(selected_folder)
                  if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    elif mode == "files":
        images = list(selected_files)
    else:
        messagebox.showerror("Error", "No images selected!")
        return

    if not images:
        messagebox.showerror("Error", "No valid image files found!")
        return

    output_file = "extracted_text.txt"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for img_path in images:
                text = extract_text_from_image(img_path)
                filename = os.path.basename(img_path)
                f.write(f"--- {filename} ---\n{text}\n\n")
        messagebox.showinfo("Success", f"Text extracted and saved to:\n{output_file}")
        root.destroy()  # Close the application after user clicks OK
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# Set up the tkinter window with a modern style
root = tk.Tk()
root.title("Image to Text Extractor")
root.geometry("800x600")  # Bigger window for a spacious design

# Define colors
primary_color = "#2C3E50"
secondary_color = "#ECF0F1"
accent_color = "#1ABC9C"

# Apply styles
style = ttk.Style(root)
style.theme_use("clam")  # Modern, clean theme

# Configure styles
style.configure("TFrame", background=primary_color)
style.configure("TLabel", background=primary_color, foreground=secondary_color, font=("Helvetica", 14))
style.configure("TButton", background=accent_color, foreground=secondary_color, font=("Helvetica", 14, "bold"), borderwidth=0, padding=10)
style.map("TButton", background=[("active", "#16A085")])  # Darker teal when button is pressed

# Create and pack the main frame
frame = ttk.Frame(root, padding=50)
frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

# Buttons
btn_folder = ttk.Button(frame, text="📁 Select Folder", command=select_folder)
btn_folder.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

btn_files = ttk.Button(frame, text="🖼️ Select Files", command=select_files)
btn_files.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

# Label to show selected folder/files
lbl_selected = ttk.Label(frame, text="No folder or files selected", wraplength=600, justify="center")
lbl_selected.grid(row=2, column=0, pady=30)

# Process button
btn_process = ttk.Button(frame, text="🚀 Process Images", command=process_images)
btn_process.grid(row=3, column=0, pady=20, sticky="ew")

# Run the application
root.mainloop()