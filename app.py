import streamlit as st
import pickle
import pandas as pd

movies = pd.read_csv('movies.csv')
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),key=lambda x:x[1], reverse=True)[1:6]
    return [(movies.iloc[i[0]].movie_id,movies.iloc[i[0]].title) for i in movies_list]

st.title('Movie Recommeder System')

selected_movie = st.selectbox(
    'Search the movies.',
    movies['title']
)

if st.button('Recommend'):
    for i in recommend(selected_movie):
        st.write(i[0], i[1])

