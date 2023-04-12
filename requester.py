# File requester
# Author: Heikki Jarvinen
# Description: class used to request data from movie database

# pip install requests
import requests
import video


class Requester():
    def __init__(self):
        self.api_key = open('api_key.txt', 'r').read()
        self.media_type = "all"
        self.time_window = "week"
        self.response = f"https://api.themoviedb.org/3/trending/{self.media_type}/{self.time_window}?api_key={self.api_key}"


    def get_trending(self, media_type, time_window):
        self.media_type = media_type
        self.time_window = time_window
        self.response = f"https://api.themoviedb.org/3/trending/{self.media_type}/{self.time_window}?api_key={self.api_key}"

        trending = requests.get(self.response).json()
        print(trending)

        if self.media_type == "tv":
            trending_shows = dict()
            shows = trending['results']
            for show in shows:
                id = show['id']
                release_date = show['first_air_date']
                name = show['name']
                tv_show = video.Tv_show(id, release_date, name)
                trending_shows[name] = tv_show
            return trending_shows

        elif self.media_type == "movie":
            trending_movies = dict()
            movies = trending['results']
            for movie in movies:
                id = movie['id']
                release_date = movie['release_date']
                name = movie['title']
                movie_o = video.Movie(id, release_date, name)
                trending_movies[name] = movie_o
            return trending_movies
    
    
