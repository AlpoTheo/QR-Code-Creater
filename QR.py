import tkinter as tk
from tkinter import simpledialog, messagebox
import qrcode
from PIL import Image, ImageTk

def create_qr_code(url):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    
    # Convert QR code image to PhotoImage for Tkinter compatibility
    img = img.convert('RGB')
    photo = ImageTk.PhotoImage(image=img)
    return photo

def generate_button_click():
    url = url_entry.get()
    if url:
        try:
            photo = create_qr_code(url)
            image_label.config(image=photo)
            image_label.image = photo  # keep a reference!
            image_label.pack(padx=10, pady=10)
        except Exception as e:
            messagebox.showerror("Error", "Failed to generate QR Code: " + str(e))
    else:
        messagebox.showwarning("Warning", "Please enter a URL.")

# Setup the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create entry for URL input
url_entry = tk.Entry(root, font=('Arial', 14), width=50)
url_entry.pack(padx=10, pady=10)

# Create a button to generate QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_button_click, font=('Arial', 14))
generate_button.pack(padx=10, pady=10)

# Label to display the QR code image
image_label = tk.Label(root)
image_label.pack(padx=10, pady=10)

root.mainloop()
