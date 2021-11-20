import streamlit as st
import requests
import datetime
import pandas as pd
import numpy as np

'''
# New York Taxi
'''
date_time = st.date_input("Date and time", datetime.date(2012, 10, 20))
pickup_lat = st.text_input('Pickup latitude', '40.7614327')
pickup_lon = st.text_input('Pickup longitute', '-73.9798156')
dropoff_lat = st.text_input('Dropoff latitude', '40.6513111')
dropoff_lon = st.text_input('Dropoff longitude', '-73.8803331')
passenger_count = st.text_input('Passenger count', '2')

#pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2

para = {
    'Date and time': date_time,
    'Pickup latitude': pickup_lat,
    'Pickup longitute': pickup_lon,
    'Dropoff latitude': dropoff_lat,
    'Dropoff longitude': dropoff_lon,
    'Passenger count': passenger_count
}

@st.cache
def get_map_data():

    return pd.DataFrame(
        np.array([(float(pickup_lat), float(pickup_lon)),(float(dropoff_lat),float(dropoff_lon))]),
        #np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

df = get_map_data()

st.map(df)

url = 'https://taxifare.lewagon.ai/predict'
url_para = f'{url}?pickup_datetime={date_time}%2012:10:20&pickup_longitude={pickup_lon}&pickup_latitude={pickup_lat}&dropoff_longitude={dropoff_lon}&dropoff_latitude={dropoff_lat}&passenger_count={passenger_count}'



if url == 'https://taxifare.lewagon.ai/predict':
    response = requests.get(url_para).json()

"""
# Yor fare price:
"""
st.markdown(round(response['prediction'],2))
