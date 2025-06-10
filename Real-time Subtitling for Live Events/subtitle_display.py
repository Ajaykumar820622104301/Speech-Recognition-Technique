import tkinter as tk
import threading

class SubtitleDisplay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Live Subtitles")
        self.root.geometry("800x200")
        self.root.configure(bg='black')

        self.label = tk.Label(self.root, text="", font=("Arial", 24),
                              fg="white", bg="black", wraplength=750, justify="center")
        self.label.pack(expand=True)

        threading.Thread(target=self.root.mainloop, daemon=True).start()

    def update_subtitle(self, text):
        self.label.config(text=text)
