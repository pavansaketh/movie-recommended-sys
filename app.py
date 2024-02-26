import streamlit as st
import pickle
import pandas as pd

def recomended(movies):
    movie_index = movie[movie['title'] == movies].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recomended_list = []
    for i in movies_list:
       ### movie_id = movie.iloc[i[0]].movie_id
        recomended_list.append(movie.iloc[i[0]].title)

    return recomended_list

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movie = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("MOVIE RECOMENDER SYSTEM")

box = st.selectbox('select your movie',movie['title'].values)

if st.button('Recomend'):
    recomendations = recomended(box)
    for i in recomendations:
        st.write(i)