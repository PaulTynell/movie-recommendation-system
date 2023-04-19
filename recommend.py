# File recommend.py
# Author: Heikki Jarvinen
# Description: search function for finding movies and recommendations

from movie_recommendations import search, find_similar_movies 

def get_recommendation(title):
    movies = search(title)
    movie_id = movies.iloc[0]["movieId"]
    return find_similar_movies(movie_id)
