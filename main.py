import tkinter as tk
import threading
import random
from sorter import tomas_sorter_function
from engine import play_melody, play_melody_scrambeled
from sheet_music import MELODY

class MusicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sheet Music Player")
        self.root.geometry("350x200")
        self.root.configure(padx=20, pady=20)
        
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="♪ Melody Player ♪", font=("Helvetica", 16, "bold")).pack(pady=(0, 5))
        tk.Label(self.root, text="Tempo: 120 BPM | Signature: 3/4", font=("Helvetica", 10)).pack(pady=(0, 15))

        self.play_btn = tk.Button(
            self.root, 
            text="▶ Play Sheet Music", 
            command=self.start_playback,
            font=("Helvetica", 12), 
            bg="#2B422C", 
            fg="white", 
            width=20
        )
        self.play_btn.pack(pady=10)

    def start_playback(self):
        # We use a thread so the UI stays responsive while music plays
        # thread = threading.Thread(target=play_melody, args=(MELODY,), daemon=True)
        thread = threading.Thread(target=play_melody_scrambeled, args=(MELODY, tomas_sorter_function(self.melody_scramble()), ), daemon=True)
        thread.start()

    def melody_scramble(self):
        indices = list(range(len(MELODY)))
        random.shuffle(indices)
        return indices

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicApp(root)
    root.mainloop()