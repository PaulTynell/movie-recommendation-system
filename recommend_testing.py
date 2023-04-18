from movie_recommendations import search, find_similar_movies 


def get_recommendation(title):
    movies = search(title)
    movie_id = movies.iloc[0]["movieId"]
    return find_similar_movies(movie_id)

print(get_recommendation("Harry Potter"))
