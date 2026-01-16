from sound_player import SoundPlayer
import time

player = SoundPlayer()

print("Playing snare...")
player.play("snare",0.7)
time.sleep(2)

print("PLaying Kick...")
player.play("kick",0.6)
time.sleep(2)

print("Playing hihat...")
player.play("hihat",1.0)
time.sleep(1)

print("Test complete")