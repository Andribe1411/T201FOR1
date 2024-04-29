# Author: <Andri Benedikt>
# Date: <19.04.24>
# Project: <Lokapróf D4>


class Song:
    def __init__(self,title,artist,length) -> None:
        self.tile = title
        self.artist = artist
        self.length = length
    
    def get_artist(self):
        return self.artist


    def __str__(self) -> str:
        mins = self.length // 60
        secs = self.length % 60
        if secs < 10:
            secs = "0"+str(secs)
        if mins < 10:
            mins = "0"+str(mins)
        return f"{self.artist} - {self.tile} ({mins}:{secs})"
    
    def __gt__(self,other):
        return self.length>other.length
    def __lt__(self,other):
        return self.length<other.length
    def __ge__(self,other):
        return self.length>=other.length
    def __le__(self,other):
        return self.length<=other.length

        

class PlayList(Song):
    def __init__(self,playlist_name ) -> None:
        self.list_of_songs = []
        self.artist = self.get_artist()
        self.playlist_name = playlist_name


    def add(self,playlist_song):
        self.list_of_songs.append(playlist_song)

    def get_artist(self):
        artist = ""
        for loc,songs in enumerate(self.list_of_songs):
            if loc == 0:
                artist = songs.get_artist()
            if songs.get_artist() != artist:
                return "Various artists"
        return artist

    def longest_song(self):
        longest = self.list_of_songs[0]
        for songs in self.list_of_songs:
            if songs > longest:
                longest = songs
        return longest
    
    def name(self):
        return self.playlist_name
    
    def __add__(self,other):
        for x in other.list_of_songs:
            self.list_of_songs.append(x)
        self.playlist_name = "ADD"
        self.artist = self.get_artist()
        return self
    
    def __str__(self):
        song_list = ""
        print("Playlist:",self.playlist_name)
        print("Artist:",self.get_artist())
        print("Songs:")
        for songs in self.list_of_songs:
            if songs != self.list_of_songs[-1]:
                song_list += str(songs) + "\n"
            else:
                song_list += str(songs) + "\n"
        return song_list


