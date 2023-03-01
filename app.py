import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import geopandas
from countryinfo import CountryInfo
import folium
import streamlit as st
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

st.sidebar.image('https://cdn.pixabay.com/photo/2017/02/01/10/00/cartography-2029310__340.png')
df = pd.read_csv("countries_continents_codes_flags_url.csv")
df = df.replace('https://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Afghanistan.svg',
                'https://upload.wikimedia.org/wikipedia/commons/c/cd/Flag_of_Afghanistan_%282013%E2%80%932021%29.svg')
st.sidebar.title("Country  Analysis")
country = df['country'].dropna().unique().tolist()
coutry = country.insert(0,'Click Here!')
selected_country = st.sidebar.selectbox('Select a Country',country)

if selected_country=='Click Here!':
    st.subheader('Instructions:')
    st.caption("Press on 'Click Here!'")
    st.caption("Select a country")
    st.caption('Now, you can see the info of selected country')
    # st.image("https://cdn.pixabay.com/photo/2014/03/25/15/18/globe-296471__340.png")
else:
    col1, col2, col3, col4, col5= st.columns(5)
    # with col1:
    #     st.title('')
    #     st.title("Analysis of")
    #     st.title(selected_country)
    with col2:
        try:
            st.image(df[df['country'] == selected_country].values[0][2], width=400)
        except:
            pass

    try:
        country = CountryInfo(selected_country)
        info = country.info()
        region = info.get('region')
        capital = info.get('capital')
        curr = info.get('currencies')[0]
        wiki = info.get('wiki')

        st.title("Info about "+selected_country)
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header('Region')
            st.title(region)
        with col2:
            st.header('Capital')
            st.title(capital)
        with col3:
            st.header('Currency')
            st.title(curr)
    except:
        pass

    try:
        area = str(info.get('area'))
        pop = str(info.get('population'))
        dail_cod = str(info.get('callingCodes')[0])
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header('Area')
            st.title(area+' Km2')
        with col2:
            st.header('Population')
            st.title(pop+' million')
        with col3:
            st.header('Call Code')
            st.title('+'+dail_cod)
    except:
        pass


    st.title('')

    try:
        st.header('Map of '+selected_country)
        loc = Nominatim(user_agent="GetLoc")
        getLoc = loc.geocode(selected_country)
        lat=getLoc.latitude
        long=getLoc.longitude

        map=folium.Map(location=[lat,long],zoom_start=6)
        folium.Marker(
            [lat,long], popup=wiki, tooltip=selected_country
        ).add_to(map)
        st_data = st_folium(map,height=500,width=800)
    except:
        pass

