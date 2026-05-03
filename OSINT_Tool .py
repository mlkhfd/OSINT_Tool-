import tkinter as tk
import webbrowser
from tkinter import messagebox

def get_ip():
    ip = entry.get().strip()
    if not ip:
        messagebox.showwarning("Erreur", "Veuillez entrer une adresse IP")
        return None
    return ip

def open_shodan():
    ip = get_ip()
    if ip:
        webbrowser.open(f"https://www.shodan.io/host/{ip}")

def open_virustotal():
    ip = get_ip()
    if ip:
        webbrowser.open(f"https://www.virustotal.com/gui/ip-address/{ip}")

def open_maltego():
    webbrowser.open("https://www.maltego.com/")

root = tk.Tk()
root.title("OSINT Tool")
root.geometry("600x350")
root.config(bg="#e8f5e9")

title = tk.Label(root, text="OSINT Tool", font=("Arial", 18, "bold"),
                 bg="#e8f5e9", fg="#2e7d32")
title.pack(pady=10)

subtitle = tk.Label(root, text="IP Investigation Tool",
                    font=("Arial", 10), bg="#e8f5e9", fg="#388e3c")
subtitle.pack()

entry = tk.Entry(root, width=30, font=("Arial", 12),
                 bd=2, relief="groove", justify="center")
entry.pack(pady=15)
entry.insert(0, "151.101.1.69")

frame = tk.Frame(root, bg="#e8f5e9")
frame.pack(pady=10)

btn_style = {
    "font": ("Arial", 11, "bold"),
    "width": 14,
    "height": 2,
    "bd": 0,
    "cursor": "hand2"
}

btn1 = tk.Button(frame, text="Shodan", bg="#a5d6a7", fg="black",
                 activebackground="#81c784", command=open_shodan, **btn_style)
btn1.grid(row=0, column=0, padx=8, pady=10)

btn2 = tk.Button(frame, text="VirusTotal", bg="#c8e6c9", fg="black",
                 activebackground="#a5d6a7", command=open_virustotal, **btn_style)
btn2.grid(row=0, column=1, padx=8, pady=10)

btn3 = tk.Button(frame, text="Maltego", bg="#dcedc8", fg="black",
                 activebackground="#c5e1a5", command=open_maltego, **btn_style)
btn3.grid(row=0, column=2, padx=8, pady=10)

footer = tk.Label(root, text="Simple OSINT Interface",
                  font=("Arial", 8), bg="#e8f5e9", fg="#66bb6a")
footer.pack(side="bottom", pady=10)

root.mainloop()
