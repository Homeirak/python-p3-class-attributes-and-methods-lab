# song.py
class Song:

    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        self.add_to_genre_count(self.genre)
        self.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment
    
    @classmethod
    def add_to_genres(cls, new_genre):
        if new_genre not in cls.genres:
            cls.genres.append(new_genre)
    
    @classmethod
    def add_to_artists(cls, new_artist):
        if new_artist not in cls.artists:
            cls.artists.append(new_artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, new_artist):
        if new_artist in cls.artist_count:
            cls.artist_count[new_artist] += 1
        else:
            cls.artist_count[new_artist] = 1
