import streamlit as st
import requests
from streamlit_lottie import st_lottie
def app():
    import pickle
    import pandas as pd
    import numpy as np 

    def lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation = lottie_url('https://lottie.host/38efa188-7a40-4b7d-9310-c78cbe40aa80/h9beQGtPKw.json')
    with st.sidebar:    
        st_lottie(lottie_animation , height= 290 , width=200 , speed=1)

    
                   

    with open('data.pkl','rb') as file:
        df = pickle.load(file)

    


    with open('pipeline.pkl','rb') as file:
        pipeline = pickle.load(file)

    st.header('Enter your demand')
    #['society', 'bedRoom', 'bathroom', 'balcony', 'floorNum',
        #'agePossession', 'built_up_area', 'study room', 'pooja room',
        #'store room', 'others', 'servant room', 'furnished_type', 'sector']

    #society

    society = st.selectbox('society',df['society'].unique().tolist())
    #bedroom

    bedRoom = int(st.selectbox('bedRoom',sorted(df['bedRoom'].unique().tolist())))
    #batroom
    bathroom = int(st.selectbox('bathroom',sorted(df['bathroom'].unique().tolist())))
    #balcony
    balcony = int(st.selectbox('balcony',sorted(df['balcony'].unique().tolist())))
    #floorNum

    floorNum = float(st.selectbox('floorNum',sorted(df['floorNum'].unique().tolist())))
    #agePossession
    agePossession = st.selectbox('agePossession',sorted(df['agePossession'].unique().tolist()))

    built_up_area = float(st.selectbox('built_up_area',sorted(df['built_up_area'].unique().tolist())))


    study_room = int(st.selectbox('study_room',sorted(df['study room'].unique().tolist())))


    pooja_room = int(st.selectbox('pooja_room',sorted(df['pooja room'].unique().tolist())))


    store_room = int(st.selectbox('store_room',sorted(df['store room'].unique().tolist())))

    others = int(st.selectbox('others',sorted(df['others'].unique().tolist())))

    servant_room = int(st.selectbox('servant_room',sorted(df['servant room'].unique().tolist())))

    furnished_type = st.selectbox('furnished_type',sorted(df['furnished_type'].unique().tolist()))


    sector = st.selectbox('sector',sorted(df['sector'].unique().tolist()))

    # prediction button
    if st.button('check price'):
        data = [[society, bedRoom, bathroom, balcony, floorNum, agePossession, built_up_area, study_room, pooja_room, store_room, others, servant_room, furnished_type, sector ]]
        columns = ['society', 'bedRoom', 'bathroom', 'balcony', 'floorNum',
        'agePossession', 'built_up_area', 'study room', 'pooja room',
        'store room', 'others', 'servant room', 'furnished_type', 'sector']
        data_frame = pd.DataFrame(data, columns = columns)

        st.dataframe(data_frame)

        txt  = np.expm1(pipeline.predict(data_frame))
        st.text(f'price {txt -0.1} - {txt +0.1} cr')

