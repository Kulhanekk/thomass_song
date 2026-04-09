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
    
    # 1. Odd Harmonic Additive Synthesis
    # Clarinet spectra are dominated by odd harmonics (1, 3, 5)
    wave = 0.7 * np.sin(2 * np.pi * frequency * t)         # Fundamental
    wave += 0.25 * np.sin(2 * np.pi * (frequency * 3) * t)  # 3rd Harmonic
    wave += 0.1 * np.sin(2 * np.pi * (frequency * 5) * t)   # 5th Harmonic
    
    # 2. Add subtle breathiness (Noise)
    # This simulates the sound of air passing through the instrument
    noise = (np.random.random(len(t)) - 0.5) * 0.02
    wave += noise

    # 3. ADSR Envelope (Attack, Decay, Sustain, Release)
    # Instead of a pluck (exponential decay), we use a wind envelope
    total_samples = len(t)
    attack_samples = int(sample_rate * 0.04) # 40ms attack
    release_samples = int(sample_rate * 0.05) # 50ms release
    
    envelope = np.ones(total_samples)
    
    # Attack: Fade in
    if attack_samples < total_samples:
        envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
    
    # Release: Fade out
    if release_samples < total_samples:
        envelope[-release_samples:] = np.linspace(1, 0, release_samples)
    
    wave *= envelope

    # 4. Final Processing
    # Normalize and convert to 16-bit PCM
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
