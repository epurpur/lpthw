class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def print_song_lyrics(self):
        for line in self.lyrics:
            print (line)

cream = Song(["Cash rules everything around me C.R.E.A.M.",
                "Get the money, dolla dolla bills y'all."])

all_i_need = Song(["You're all that I need I'll be there for you.",
                    "You keep it real with me I'll keep it real with you."])

cream.print_song_lyrics()

all_i_need.print_song_lyrics()
