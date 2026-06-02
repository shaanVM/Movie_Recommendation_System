import streamlit as st
import pickle

import requests

API_KEY = "42ab5bf1da5f9f5c211d4054dfad7d03"

def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    data = requests.get(url).json()

    poster_path = data['poster_path']

    full_path = "https://image.tmdb.org/t/p/w500" + poster_path

    return full_path


def recommend_movie(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    recommended_movies = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    movie_names = []
    movie_posters = []

    for i in recommended_movies:

        movie_id = movies.iloc[i[0]].movie_id

        movie_names.append(
            movies.iloc[i[0]].title
        )

        movie_posters.append(
            fetch_poster(movie_id)
        )

    return movie_names, movie_posters


movies=pickle.load(open('artifacts\movies.pkl','rb'))
similarity=pickle.load(open('artifacts\similarity.pkl','rb'))
movies_list=movies['title'].values

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a Movie",
    (movies_list),
)
st.write("You selected:", selected_movie_name)

if st.button("Recommend"):
    st.balloons()

    movie_names, movie_posters = recommend_movie(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(movie_posters[0])
        st.caption(movie_names[0])

    with col2:
        st.image(movie_posters[1])
        st.caption(movie_names[1])

    with col3:
        st.image(movie_posters[2])
        st.caption(movie_names[2])

    with col4:
        st.image(movie_posters[3])
        st.caption(movie_names[3])

    with col5:
        st.image(movie_posters[4])
        st.caption(movie_names[4])




