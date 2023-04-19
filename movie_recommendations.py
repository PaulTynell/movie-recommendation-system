#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd

movies = pd.read_csv("movies.csv")


# In[38]:


movies


# In[39]:


import re

def clean_title(title):
    return re.sub("[^a-zA-Z0-9 ]", "", title)


# In[40]:


movies["clean_title"] = movies["title"].apply(clean_title)


# In[41]:


movies


# In[42]:


from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(ngram_range=(1,2))

tfidf = vectorizer.fit_transform(movies["clean_title"])


# In[43]:


from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def search(title):
    title = clean_title(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = movies.iloc[indices][::-1]
    return results


# In[32]:


import ipywidgets as widgets
from IPython.display import display

movie_input = widgets.Text(
    value="Toy Story",
    description="Movie Title:",
    disabled=False
)
movie_list = widgets.Output()

def on_type(data):
    with movie_list:
        movie_list.clear_output()
        title = data["new"]
        if len(title) > 5:
            display(search(title))
            
movie_input.observe(on_type, names='value')



# In[44]:


ratings = pd.read_csv("ratings.csv")


# In[45]:


ratings


# In[46]:


ratings.dtypes


# In[47]:


movie_id = 1


# In[50]:


similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] > 4)]["userId"].unique()


# In[51]:


similar_users


# In[55]:


similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)]["movieId"]


# In[56]:


similar_user_recs


# In[58]:


similar_user_recs = similar_user_recs.value_counts() / len(similar_users)

similar_user_recs = similar_user_recs[similar_user_recs > .1]


# In[59]:


similar_user_recs


# In[60]:


all_users = ratings[(ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)]


# In[62]:


all_users_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())


# In[63]:


all_users_recs


# In[65]:


rec_percentages = pd.concat([similar_user_recs, all_users_recs], axis=1)
rec_percentages.columns = ["similar", "all"]


# In[66]:


rec_percentages


# In[67]:


rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]


# In[68]:


rec_percentages = rec_percentages.sort_values("score", ascending=False)


# In[69]:


rec_percentages


# In[70]:


rec_percentages.head(10).merge(movies, left_index=True, right_on="movieId")


# In[71]:


def find_similar_moviesadadadad(movie_id):
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
    
    return rec_percentages.head(10).merge(movies, left_index=True, right_on="movieId")[["title", "genres"]].to_string(index=False)


def find_similar_moviesplace(movie_id):
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
    
    # Left-justify the title and genres strings with a width of 50 characters
    formatted_output = rec_percentages.head(10).merge(movies, left_index=True, right_on="movieId")[["title", "genres"]].applymap(lambda x: x.ljust(50))
    
    return formatted_output.to_string(index=False, header=False)

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



