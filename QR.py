import tkinter as tk
from tkinter import filedialog, messagebox
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
    return img

def save_image(img):
    # Open file dialog to save the image
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", '*.png'), ("All files", '*.*')])
    if file_path:
        img.save(file_path)
        messagebox.showinfo("Success", "QR Code saved successfully!")

def generate_button_click():
    url = url_entry.get()
    if url:
        try:
            img = create_qr_code(url)
            photo = ImageTk.PhotoImage(image=img)
            image_label.config(image=photo)
            image_label.image = photo  # keep a reference!
            image_label.pack(padx=10, pady=10)
            save_image(img)
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

# Create a button to generate and save QR code
generate_button = tk.Button(root, text="Generate and Save QR Code", command=generate_button_click, font=('Arial', 14))
generate_button.pack(padx=10, pady=10)

# Label to display the QR code image
image_label = tk.Label(root)
image_label.pack(padx=10, pady=10)

root.mainloop()
