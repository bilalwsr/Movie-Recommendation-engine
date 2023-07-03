import streamlit as st
import pandas as pd 
import base64
import pickle
import requests
def fetch_poster(movieid):
    requests.get('')



def similar(movie):
    index = movieso[movieso['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(movieso.iloc[i[0]].title)
        return recommended_movies

st.markdown("<h1 style='text-align: center; font-family: Impact; -webkit-text-stroke: 1px black;'>Similar Movies Search</h1>", unsafe_allow_html=True)

        
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('img.jpg')





movies  = pickle.load(open('movie_list.pkl', 'rb'))
movieso = pd.DataFrame(movies)


similarity = pickle.load(open('similarity.pkl', 'rb'))


user_input_for_movies = st.selectbox('Enter Your Movie Name Here',
                                    movieso['title'].values)
if st.button('Search'):
    recommendations = similar(user_input_for_movies)
    st.write(user_input_for_movies)
    for i in recommendations:
        st.write(i)


# Remove the Streamlit footer
# Hide the "Made with Streamlit" footer
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


