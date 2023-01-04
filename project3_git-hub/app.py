import pandas
import pickle
import streamlit as st

with open('movi.pkl', 'rb') as mv:
    movies = pickle.load(mv)
with open('sim.pkl', 'rb') as s:
    cosine_sim = pickle.load(s)

def get_recommendations(title):
    # 영화 제목을 통해 전체 데이터 기준 그 영화의 index 얻기
    idx = movies[movies['title'] == title].index[0]
    # 코사인 유사도 매트릭스에서 위 인덱스 기준의 데이터 찾기
    sim_scores = list(enumerate(cosine_sim[idx]))
    # 유사도 내림차순
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # 자신을 제외한 상위 유사도 4개 슬라이싱
    sim_scores = sim_scores[1:5]
    # 슬라이싱한 4개 유사도의 인덱스 추출
    movie_indices = [i[0] for i in sim_scores]
    # 인덱스 정보로 영화정보 추출
    titles = []
    stars = []
    directors = []
    main_actors = []
    genres = []
    writers = []
    like_ages = []

    for i in movie_indices:
        titles.append(movies['title'].iloc[i])
        stars.append(movies['stars'].iloc[i])
        genres.append(movies['genre'].iloc[i])
        directors.append(movies['director'].iloc[i])
        main_actors.append(movies['actor'].iloc[i])
        writers.append(movies['writer'].iloc[i])
        like_ages.append(movies['highest_age'].iloc[i])
    return titles, stars, genres, directors, main_actors, writers, like_ages


st.set_page_config(layout='wide')
st.header('좋아하는 영화에 기반한 영화 추천 드립니다')

movie_list = movies['title'].values
title = st.selectbox('좋아하는 영화를 선택하고 추천을 누르세요', movie_list)

if st.button('추천'):
    titles, stars, genres, directors, main_actors, writers, like_ages = get_recommendations(title)

    idx = 0
    # range 가로줄, columns 세로줄
    for i in range(0, 1):
        cols = st.columns(4)
        for col in cols:
            col.write(titles[idx])
            col.write(stars[idx])
            col.write(genres[idx])
            col.write(directors[idx])
            col.write(main_actors[idx])
            col.write(writers[idx])
            col.write(like_ages[idx])
            idx += 1
