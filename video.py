# File: video.py
# Author: Heikki Jarvinen
# Description: class used to model movies and tv shows

class Video:
    def __init__(self, id, release_date, genre):
        self.id = id
        self.release_date = release_date
        self.genre = genre

    def set_id(self, id):
        self.id = id

    def set_release_date(self, release_date):
        self.release_date = release_date

    def set_genre(self, genre):
        self.genre = genre

    def get_id(self):
        return self.id
    
    def get_release_date(self):
        return self.release_date
    
    def get_genre(self):
        return self.genre
    
    def __str__(self):
        return f"ID: {self.id}, Release date: {self.release_date}, Genre: {self.genre}"

class Movie(Video):
    def __init__(self, id, release_date, genre, title):
        super().__init__(id, release_date, genre)
        self.title = title

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title
    
    def __str__(self):
        return f"Title: {self.title} ID: {self.id}, Release date: {self.release_date}, Genre: {self.genre}"
    
class Tv_show(Video):
    def __init__(self, id, release_date, genre, name):
        super().__init__(id, release_date, genre)
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def __str__(self):
        return f"Name: {self.name} ID: {self.id}, Release date: {self.release_date}, Genre: {self.genre}"
