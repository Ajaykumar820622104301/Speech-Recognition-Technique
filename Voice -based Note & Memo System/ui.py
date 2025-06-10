import tkinter as tk
from tkinter import messagebox
from voice_note import VoiceNoteSystem

class VoiceNoteApp:
    def __init__(self):
        self.note_system = VoiceNoteSystem()
        self.root = tk.Tk()
        self.root.title("Voice Note & Memo System")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text="Voice Memo System", font=("Arial", 18))
        self.label.pack(pady=20)

        self.record_button = tk.Button(self.root, text="🎤 Record Note", command=self.record_note, width=20, height=2)
        self.record_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Exit", command=self.root.quit, width=20)
        self.quit_button.pack(pady=10)

    def record_note(self):
        note = self.note_system.listen()
        if note:
            file = self.note_system.save_note(note)
            self.note_system.speak("Note saved successfully.")
            messagebox.showinfo("Note Saved", f"Note saved to {file}\n\nContent:\n{note}")
        else:
            messagebox.showwarning("Warning", "No note captured.")

    def run(self):
        self.root.mainloop()
