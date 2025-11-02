happy_bday_lyrics = [
    "Happy birthday to you",
    "Happy birthday to you",
    "Happy birthday dear friend",
    "Happy birthday to you"
]

class Songs:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

song = Songs(happy_bday_lyrics)
song.sing_me_a_song()