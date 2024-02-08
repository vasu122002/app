import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import seaborn as sns
import plotly.express as px

def app():

    data = pd.read_csv('main_latlong_file')
    fig = px.scatter_mapbox(data[['Sector','latitude','longitude','price']], lat="latitude", lon="longitude", color="price",
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",text=data['Sector'])
    st.plotly_chart(fig,use_container_width=True)

    st.write('Check expensive sectors')
    value = int(st.selectbox('select value' , [5 ,10,15]))
    fig1 =  px.bar(data.sort_values(by = 'price' , ascending= False).head(value) , x  = 'Sector' , y = 'price' , color = 'Sector')
    st.plotly_chart(fig1 , use_container_width= True)