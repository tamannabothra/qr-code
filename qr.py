import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import qrcode
from pyzbar.pyzbar import decode

def generate_qr_code():
    data = entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save("qrcode.png")
    
    # Open the generated QR code image
    qr_image = Image.open("qrcode.png")
    qr_image = ImageTk.PhotoImage(qr_image)
    
    # Display the QR code in the GUI
    qr_label.config(image=qr_image)
    qr_label.image = qr_image

    result.set("Generated QR code for:\n" + data)

def scan_qr_code():
    file_path = filedialog.askopenfilename()
    if file_path:
        scanned_data = scan_qr_code_image(file_path)
        if scanned_data:
            result.set("Scanned QR code data:\n" + scanned_data)
        else:
            result.set("No QR code found or couldn't be decoded.")

def scan_qr_code_image(image_path):
    image = Image.open(image_path)
    decoded_objects = decode(image)
    scanned_data = ""
    for obj in decoded_objects:
        scanned_data += obj.data.decode('utf-8') + "\n"
    return scanned_data

# Create the main window
window = tk.Tk()
window.title("QR Code Generator and Scanner")

# Customize the background color
style = ttk.Style()
style.configure('TButton', background='#3498db', font=('Roboto', 14), foreground='black')

# Create input field and buttons
frame = ttk.Frame(window)
frame.pack(padx=20, pady=20)
label = ttk.Label(frame, text="Enter data for QR code:")
entry = ttk.Entry(frame, font=('Roboto', 14))
generate_button = ttk.Button(frame, text="Generate QR Code", command=generate_qr_code)
scan_button = ttk.Button(frame, text="Scan QR Code", command=scan_qr_code)
result = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result, font=('Roboto', 12))

label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry.grid(row=0, column=1, padx=5, pady=5)
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky="ew")
scan_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky="ew")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

# QR code display label
qr_label = ttk.Label(window)
qr_label.pack(padx=20, pady=10)

# Customize the background color of the window
window.configure(background='black')

# Start the Tkinter main loop
window.mainloop()
