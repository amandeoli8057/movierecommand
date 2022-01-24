import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies =[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies



movies_dictionary = pickle.load(open('movierecdict.pkl','rb'))
movies=pd.DataFrame(movies_dictionary)
similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie recommendation system')

selected_movie_name = st.selectbox(
'Welcome to my project: AMANDEOLI',
movies['title'].values)

if st.button('Recommend more :)'):
    recommendations= recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)









