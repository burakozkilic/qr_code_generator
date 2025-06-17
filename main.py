import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("420x600")
app.title("QR Kod Oluşturucu v1.0")

qr_image = None

def generate_qr():
    global qr_image
    data = entry.get()
    if not data:
        status_label.configure(text="⚠️ Lütfen bir metin girin.", text_color="red")
        return

    qr_img = qrcode.make(data)
    qr_img.save("qr_result.png")
    
    img = Image.open("qr_result.png").resize((200, 200))
    qr_image = ImageTk.PhotoImage(img)
    qr_label.configure(image=qr_image, text="")
    status_label.configure(text="✅ QR kod oluşturuldu. Şimdi indirebilirsiniz.", text_color="green")

def get_unique_filename(base_name="indirilen_qr", ext=".png"):
    index = 1
    while True:
        filename = f"{base_name}_{index}{ext}"
        if not os.path.exists(filename):
            return filename
        index += 1

def save_qr():
    if not os.path.exists("qr_result.png"):
        status_label.configure(text="⚠️ Önce QR kod oluşturmalısınız.", text_color="red")
        return

    save_path = get_unique_filename()
    Image.open("qr_result.png").save(save_path)
    status_label.configure(text=f"✅ QR kod '{save_path}' olarak indirildi.", text_color="lightgreen")

content_frame = ctk.CTkFrame(app)
content_frame.pack(fill="both", expand=True, padx=20, pady=20)

title_label = ctk.CTkLabel(content_frame, text="Metin veya URL girin:", font=ctk.CTkFont(size=16))
title_label.pack(pady=10)

entry = ctk.CTkEntry(content_frame, width=300)
entry.pack(pady=10)

generate_btn = ctk.CTkButton(content_frame, text="QR Kod Oluştur", command=generate_qr)
generate_btn.pack(pady=15)

download_btn = ctk.CTkButton(content_frame, text="QR Kod İndir", command=save_qr)
download_btn.pack(pady=5)

qr_label = ctk.CTkLabel(content_frame, text="")
qr_label.pack(pady=15)

status_label = ctk.CTkLabel(content_frame, text="", font=ctk.CTkFont(size=13))
status_label.pack(pady=5)

footer_frame = ctk.CTkFrame(app, fg_color="transparent")
footer_frame.pack(side="bottom", fill="x", pady=10)

github_label = ctk.CTkLabel(footer_frame, text="github.com/burakozkilic", text_color="gray", cursor="hand2", font=ctk.CTkFont(size=15))
github_label.pack()
github_label.bind("<Button-1>", lambda e: os.system("start https://github.com/burakozkilic"))

app.mainloop()
