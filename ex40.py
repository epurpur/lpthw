class Song(object):
    def __init__(me, lyrics):
        me.lyrics = lyrics

    def sing_me_a_song(me):
        for line in me.lyrics:
            print (line)

#defines happy_bday as Song, with argument (lyrics of song)
happy_bday = Song(["Happy Birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there."])

#defines bulls_on_parade as Song, with argument (lyrics of song)
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells."])

#calls happy_bday with function sing_me_a_song as argument
happy_bday.sing_me_a_song()
#calls bulls_on_parade with function sing_me_a_song as argument
bulls_on_parade.sing_me_a_song()