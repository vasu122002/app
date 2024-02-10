import streamlit as st
import requests

from streamlit_lottie import st_lottie

import json


def app():
    def lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation = lottie_url('https://lottie.host/44a79658-438b-4643-a6a6-aced9302e247/OydNXgCBQr.json')
    st_lottie(lottie_animation , height= 250 , width=-1500 , speed=2)
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Welcome to AI based Real e-state web APP </p>', unsafe_allow_html=True)
    
    st.write('Step into the future of real estate with AI, an innovative AI-based web application designed to redefine the way you experience property transactions. Our cutting-edge technology seamlessly combines artificial intelligence with real estate expertise, creating a user-friendly platform that simplifies the entire property journey.')
    st.write('Key Features:')
    st.write('Intelligent Pricing: Say goodbye to uncertainty. Our AI-powered pricing tool analyzes market trends, property features, and other relevant data to provide accurate and fair property valuations.')
    st.write('Predictive Analytics: Stay ahead of the curve with our predictive analytics. Anticipate market trends, investment opportunities, and potential property value fluctuations, empowering you to make informed decisions.')
    with st.sidebar:
        st.write('project developed by Tushar Sharma & Vasu Kumar Rana')
        
        st.write('Special Thanks:')
        st.write('A heartfelt thank you to our esteemed teacher, Dr. Shashi, whose guidance and mentorship have lead us to create this project')
    def lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    


    #society
