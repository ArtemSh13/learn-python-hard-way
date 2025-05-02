class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

song1 = ["Happy birthday to you!",
                   "Happy birthday to you!",
                   "Happy birthday, dear Python,",
                   "Happy birthday to you!"]
song2 = ["Далеко-далеко на лугу пасётся коооооо...",
                        "ПРАВИЛЬНО, КОРОВИНА (нативная интеграция колбасы \"Коровина\")"]

happy_bday = Song(song1)

bulls_on_parade = Song(song2)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()