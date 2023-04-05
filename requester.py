# File requester
# Author: Heikki Jarvinen
# Description: class used to request data from movie database

# pip install requests
import requests


class Requester():
    def __init__(self):
        self.api_key = open('api_key.txt', 'r').read()
        self.media_type = "all"
        self.time_window = "week"
        self.response = f"https://api.themoviedb.org/3/trending/{self.media_type}/{self.time_window}?api_key={self.api_key}"


    def get_trending(self,media_type, time_window):
        self.media_type = media_type
        self.time_window = time_window
        self.response = f"https://api.themoviedb.org/3/trending/{self.media_type}/{self.time_window}?api_key={self.api_key}"

        trending = requests.get(self.response).json()

        if self.media_type == "tv":
            shows = trending['results']
            for show in shows:
                print(show['name'])

        elif self.media_type == "movie":
            movies = trending['results']
            for movie in movies:
                print(movie['title'])

    
