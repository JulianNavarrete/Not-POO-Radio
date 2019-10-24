import time
import vlc

#libvlc_audio_set_volume(vlc, 50)
#video_get_title_description(self)
#get_media()

class Asd:

    def __init__(self):
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new('http://stream.simulatorradio.com:8002/stream.mp3')
        Media.get_mrl()
        player.set_media(Media)
        player.play()
        player.audio_set_volume(50)
        #print(player.libvlc_audio_get_track_description())
        #player.libvlc_audio_get_track()
        time.sleep(999999)

Asd()



'''
def audio_get_track_description(self):
    """Get the description of available audio tracks."""
    return track_description_list(libvlc_audio_get_track_description(self))
'''

