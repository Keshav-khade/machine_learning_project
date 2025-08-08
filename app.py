import os
import gdown
import pickle
import pandas as pd
import requests
import streamlit as st

# fetch api key from render's environmental variable
API_KEY = os.environ.get("API_KEY")


# Download similarity.pkl from Google Drive if not present
if not os.path.exists("similarity.pkl"):
    file_id = "1SnFrHlMl3Rc1cl7PB_3ejpZtUS7k7_8P"
    url ="https://drive.google.com/uc?id=1SnFrHlMl3Rc1cl7PB_3ejpZtUS7k7_8P"
    gdown.download(url, "similarity.pkl", quiet=False)

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to get movie poster using TMDb API
def fetch_poster(movie_title):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": API_KEY,
        "query": movie_title
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data["results"]:
        poster_path = data["results"][0].get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return "https://via.placeholder.com/500x750?text=No+Poster"

# Recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(title))

    return recommended_movies, recommended_posters

# Streamlit UI
st.title('🎬 Prime_Flix - Movie Recommender')

selected_movie_name = st.selectbox(
    "Hey! What are you waiting for? Start browsing movies!",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    # Show in a grid layout (5 columns per row)
    for i in range(0, len(names), 5):
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            if i + idx < len(names):
                with col:
                    st.image(posters[i + idx], use_container_width=True)
                    st.caption(names[i + idx])
