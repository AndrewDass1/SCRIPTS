import glob
import random
import os

list_of_music_in_directory = glob.glob("*.mp3")
number_of_music_tracks = len(list_of_music_in_directory)

class Find_Music:

    def function():
        list_of_music_in_directory = glob.glob("*.mp3")
        number_of_music_tracks = len(list_of_music_in_directory)

        random_selector = random.randint(0, number_of_music_tracks-1)

        play_music_track = list_of_music_in_directory[random_selector]
        os.startfile(play_music_track)

        del list_of_music_in_directory[random_selector]
        number_of_music_tracks = len(list_of_music_in_directory)

while number_of_music_tracks > 0:
    try:
        print(Find_Music.function())
        
        number_of_music_tracks -= 1
