import tkinter as tk
import threading
import numpy as np
import pygame
import time

# 1. Initialize Pygame Mixer for Audio Generation
# We use stereo (channels=2) to avoid common array dimension errors
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

def generate_sound(frequency, duration):
    if frequency == 0: return None
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Layer 1: Fundamental frequency
    wave = 0.6 * np.sin(2 * np.pi * frequency * t)
    # Layer 2: First Harmonic (adds richness)
    wave += 0.3 * np.sin(2 * np.pi * (frequency * 2) * t)
    # Layer 3: Second Harmonic (adds brightness)
    wave += 0.1 * np.sin(2 * np.pi * (frequency * 3) * t)

    # PLUCK ENVELOPE: Starts loud, decays immediately
    # This mimics the physics of a string being hit
    envelope = np.exp(-3.0 * t / duration) 
    wave *= envelope

    audio = np.int16(wave * 32767)
    stereo_audio = np.column_stack((audio, audio))
    return pygame.sndarray.make_sound(stereo_audio)

def play_music():
    """Loops through the MELODY and adds a small gap between notes."""
    # GAP_FACTOR of 0.9 means the note plays for 90% of its duration, 
    # and 10% is a silent pause.
    GAP_FACTOR = 0.85 

    for note_name, beats in MELODY:
        total_duration = beats * BEAT_DURATION
        
        if note_name == 'R':
            time.sleep(total_duration)
        else:
            # Calculate sounding time vs silent time
            sound_duration = total_duration * GAP_FACTOR
            pause_duration = total_duration * (1 - GAP_FACTOR)
            
            sound = generate_sound(NOTES[note_name], sound_duration)
            if sound:
                sound.play()
                # Wait for the sound to finish
                time.sleep(sound_duration)
                # Mini pause before the next note
                time.sleep(pause_duration)

def start_playback():
    """Starts playback in a separate thread so the GUI doesn't freeze."""
    threading.Thread(target=play_music, daemon=True).start()

# --- GUI Setup ---
root = tk.Tk()
root.title("Sheet Music Player")
root.geometry("350x200")
root.configure(padx=20, pady=20)

title_label = tk.Label(root, text="♪ Melody Player ♪", font=("Helvetica", 16, "bold"))
title_label.pack(pady=(0, 5))

info_label = tk.Label(root, text="Tempo: 160 BPM  |  Time Signature: 3/4", font=("Helvetica", 10))
info_label.pack(pady=(0, 15))

play_btn = tk.Button(
    root, 
    text="▶ Play Sheet Music", 
    command=start_playback, 
    font=("Helvetica", 12), 
    bg="#2B422C", 
    fg="white", 
    width=20
)
play_btn.pack(pady=10)

root.mainloop()