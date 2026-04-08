import numpy as np
import pygame
import time
from sheet_music import NOTES, BEAT_DURATION

GAP_FACTOR = 0.85 

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

def generate_sound(frequency, duration):
    if frequency == 0: return None
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Harmonic additive synthesis
    wave = 0.6 * np.sin(2 * np.pi * frequency * t)
    wave += 0.3 * np.sin(2 * np.pi * (frequency * 2) * t)
    wave += 0.1 * np.sin(2 * np.pi * (frequency * 3) * t)

    # Pluck Envelope
    envelope = np.exp(-3.0 * t / duration) 
    wave *= envelope

    audio = np.int16(wave * 32767)
    stereo_audio = np.column_stack((audio, audio))
    return pygame.sndarray.make_sound(stereo_audio)

def play_note(note_name, beats):
    total_duration = beats * BEAT_DURATION
        
    if note_name == 'R':
        time.sleep(total_duration)
    else:
        sound_duration = total_duration * GAP_FACTOR
        pause_duration = total_duration * (1 - GAP_FACTOR)

        sound = generate_sound(NOTES.get(note_name, 0), sound_duration)
        if sound:
            sound.play()
            time.sleep(sound_duration)
            time.sleep(pause_duration)

def play_melody(melody_data):
    for note_name, beats in melody_data:
        play_note(note_name, beats)
        

def play_melody_scrambeled(melody_data, scramble):
    for idx in scramble:
        note_name, beats = melody_data[idx]
        play_note(note_name, beats)
