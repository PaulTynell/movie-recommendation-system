# File requester.py
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
        self.movie_genres = self.get_movie_genres()
        self.tv_genres = self.get_tv_genres()


    # Returns a dictionary of trending tv shows or movies
    def get_trending(self, media_type, time_window):
        self.media_type = media_type
        self.time_window = time_window
        self.response = f"https://api.themoviedb.org/3/trending/{self.media_type}/{self.time_window}?api_key={self.api_key}"

        trending = requests.get(self.response).json()

        if self.media_type == "tv":
            trending_shows = dict()
            shows = trending['results']
            for show in shows:
                id = show['id']
                release_date = show['first_air_date']
                genre = show['genre_ids']
                name = show['name']
                tv_show = video.Tv_show(id, release_date, self.assign_genres_tv(genre), name)
                trending_shows[name] = tv_show
            return trending_shows

        elif self.media_type == "movie":
            trending_movies = dict()
            movies = trending['results']
            for movie in movies:
                id = movie['id']
                release_date = movie['release_date']
                genre = movie['genre_ids']
                name = movie['title']
                movie_o = video.Movie(id, release_date, self.assign_genres_movie(genre), name)
                trending_movies[name] = movie_o
            return trending_movies
    
    # Get movie genres from api
    def get_movie_genres(self):
        self.response = f"https://api.themoviedb.org/3/genre/movie/list?api_key={self.api_key}&language=en-US"
        
        response = requests.get(self.response).json()
        genres = dict()
        genres_response = response['genres']
        for genre in genres_response:
            id = genre['id']
            name = genre['name']
            genres[id] = name
        return genres

    # Get tv show genres from api
    def get_tv_genres(self):
        self.response = f"https://api.themoviedb.org/3/genre/tv/list?api_key={self.api_key}&language=en-US"
    
        response = requests.get(self.response).json()
        genres = dict()
        genres_response = response['genres']
        for genre in genres_response:
            id = genre['id']
            name = genre['name']
            genres[id] = name
        return genres

    # Assigns genres to genre ids for movies
    def assign_genres_movie(self, ids: list):
        genres = []
        for id in ids:
            for x, y in self.movie_genres.items():
                if id == x:
                    genres.append(y)
        return genres
    
    # Assigns genres to genre ids for tv shows
    def assign_genres_tv(self, ids: list):
        genres = []
        for id in ids:
            for x, y in self.tv_genres.items():
                if id == x:
                    genres.append(y)
        return genres
