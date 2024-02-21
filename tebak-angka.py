import tkinter as tk
from tkinter import messagebox
import random

class TebakAngkaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Tebak Angka")
        
        self.angka_rahasia = random.randint(1, 100)
        self.jumlah_tebakan = 0

        self.label_instruksi = tk.Label(root, text="Saya akan memilih sebuah angka antara 1 dan 100, coba tebak!")
        self.label_instruksi.pack()

        self.entry_tebakan = tk.Entry(root)
        self.entry_tebakan.pack()

        self.button_tebak = tk.Button(root, text="Tebak", command=self.tebak)
        self.button_tebak.pack()

    def tebak(self):
        tebakan = self.entry_tebakan.get()
        try:
            tebakan = int(tebakan)
            self.jumlah_tebakan += 1

            if tebakan < self.angka_rahasia:
                messagebox.showinfo("Info", "Tebakan Anda terlalu rendah, coba lagi.")
            elif tebakan > self.angka_rahasia:
                messagebox.showinfo("Info", "Tebakan Anda terlalu tinggi, coba lagi.")
            else:
                messagebox.showinfo("Info", f"Selamat! Anda berhasil menebak angka {self.angka_rahasia} dalam {self.jumlah_tebakan} tebakan.")
                self.root.destroy()
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid.")

def main():
    root = tk.Tk()
    app = TebakAngkaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()