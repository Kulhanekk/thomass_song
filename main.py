import tkinter as tk
import threading
import random
from sorter import tomas_sorter_function
from engine import play_melody, play_melody_scrambeled
from sheet_music import MELODY

class MusicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("tomasovo potkani s jindrou v hospode")
        self.root.geometry("1280x720")
        self.root.configure(padx=20, pady=20)
        self.root.state('zoomed')

        self.setup_ui()

    def setup_ui(self):
        self.bg = tk.PhotoImage(file="./images/regular.png")
        label1 = tk.Label(self.root, image=self.bg)

        label1.place(x = 0, y = 0)

        self.play_btn = tk.Button(
            self.root, 
            text="▶ Play Music", 
            command=self.start_playback,
            font=("Helvetica", 35), 
            bg="#2B422C", 
            fg="white", 
            width=20
        )
        self.play_btn.pack(pady=150)

    def start_playback(self):
        try:
            input_arr = tomas_sorter_function(self.melody_scramble())
            if input_arr == sorted(input_arr):
                self.bg = tk.PhotoImage(file="./images/playing_happy.png")
            else:
                self.bg = tk.PhotoImage(file="./images/playing_angry.png")
            label1 = tk.Label(self.root, image=self.bg)
            label1.place(x = 0, y = 0)
        except:
            label1 = tk.Label(self.root, image=self.bg)
            label1.place(x = 0, y = 0)
            self.bg = tk.PhotoImage(file="./images/playing_angry.png")
            error_msg = tk.Label(self.root, text="Žádné fancy funkce, tak rychle z toho nevyvázneš", 
                                 font=("Helvetica", 10)) # Added bg for visibility
            error_msg.pack(pady=(20, 0))
        
        # We use a thread so the UI stays responsive while music plays
        # thread = threading.Thread(target=play_melody, args=(MELODY,), daemon=True)
        thread = threading.Thread(target=play_melody_scrambeled, args=(MELODY, input_arr, ), daemon=True)
        thread.start()

    def melody_scramble(self):
        indices = list(range(len(MELODY)))
        random.shuffle(indices)
        return indices

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicApp(root)
    root.mainloop()