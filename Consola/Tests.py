import vlc
import time
import os
import sys

'''
sound_file = vlc.MediaPlayer (r'D:\\Escritorio\\Reptile.mp3')
sound_file.play()
time.sleep(10)

for line in file:
    print(line.strip("\n"))'''

'''
lines = file.read()         # read the entire file into a string
print(lines)                # print contents
'''
'''
lines = []                                      # Declare an empty list named mylines.
with open('links.txt', 'rt') as file:           # Open lorem.txt for reading text data.
    for line in file:                           # For each line, stored as myline,
        lines.append(line.strip("\n"))          # add its contents to mylines.
print(lines)                                    # Print the list.
'''
'''
if a != int(a):
    print("Error")
else:
    print("Funciona")
'''
'''
try:
    a = int(input("Ingresá algo: "))
    print("Opción existente")
except:
    print("Opción no existente")
'''

file = open("prueba.txt", "r")

a = 0

#while a == 0:
Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new('http://stream.simulatorradio.com:8002/stream.mp3')
print("\nReproduciendo Simulator Radio")
# print(lines[index])
Media.get_mrl()
player.set_media(Media)
player.play()
player.audio_set_volume(20)
time.sleep(5)


file.close()


'''
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new('http://stream.simulatorradio.com:8002/stream.mp3')
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    player.audio_set_volume(50)
    # print(player.libvlc_audio_get_track_description())
    # player.libvlc_audio_get_track()
'''
