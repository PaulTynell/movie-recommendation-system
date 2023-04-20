# File: movie_recommender
# Author: Heikki Jarvinen
# Description: modified version of the jupyter notebook file. Used to get movie recommendations

import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# reads the .csv files that contain the dataset
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# using regex to clean the title of unwanted characters
def clean_title(title):
    return re.sub("[^a-zA-Z0-9 ]", "", title)

movies["clean_title"] = movies["title"].apply(clean_title)

vectorizer = TfidfVectorizer(ngram_range=(1,2))

tfidf = vectorizer.fit_transform(movies["clean_title"])

# searches the most likely movie from dataset
def search(title):
    title = clean_title(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = movies.iloc[indices][::-1]
    return results

# function finds most similar movies to given movie
def find_similar_movies(movie_id):
    similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] > 4)]["userId"].unique()
    similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)]["movieId"]
    
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)
    similar_user_recs = similar_user_recs[similar_user_recs > .10]
    
    all_users = ratings[(ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)]
    all_users_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())
    
    rec_percentages = pd.concat([similar_user_recs, all_users_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]
    
    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    
    rec_percentages = rec_percentages.sort_values("score", ascending=False)
    
    # modify formatting of recommendation results
    rec_text = ""
    for title, genres, score in rec_percentages.head(10).merge(movies, left_index=True, right_on="movieId")[["title", "genres", "score"]].values:
        rec_text += f"{title.ljust(50)}{genres.rjust(50)}\n"
    
    return rec_text


# combines search and find_similar_movies into one function
def get_recommendation(title):
    movies = search(title)
    movie_id = movies.iloc[0]["movieId"]
    return find_similar_movies(movie_id)