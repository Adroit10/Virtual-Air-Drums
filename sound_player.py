import pygame
import os
import time

class SoundPlayer:
    def __init__(self,sound_folder="sounds"):
        pygame.mixer.init()
        self.sounds = {}

        sound_files = {
            "snare":"snare.wav",
            "kick":"kick.wav",
            "hihat":"hihat.wav"
        }

        for name,filename in sound_files.items():
            path = os.path.join(sound_folder,filename)
            if not os.path.exists(path):
                raise FileNotFoundError(f"Sound file not found: {path}")
            self.sounds[name] = pygame.mixer.Sound(path)

        print("Sound system initialized. Loaded sounds:", list(self.sounds.keys()))

    def play(self,drum_name,volume=1.0):
        if drum_name not in self.sounds:
            print(f"No sound mapped for drum: {drum_name}")
            return
        
        volume = max(0.0,min(volume,1.0))
        self.sounds[drum_name].set_volume(volume)
        time.sleep(0.4)
        self.sounds[drum_name].play()

    def stop_all(self):
        pygame.mixer.stop()
