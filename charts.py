import pandas as pd
import geopy
from geopy.geocoders import Nominatim
import streamlit as st
import random


def Charts():
    st.title('Charts visualization')
    st.write(
        'Displays a bar chart of steorotype values for a list of legal judgments.')

    # create a list of court locations
    court_locations = [
        'Krajský soud v Brně',
        'Městský soud v Praze',
        'Krajský soud v Ostravě',
        'Krajský soud v Plzni',
        'Krajský soud v Ústí nad Labem',
        'Krajský soud v Hradci Králové',
        'Krajský soud v Olomouci',
        'Krajský soud v Českých Budějovicích',
        'Krajský soud v Liberci',
        'Krajský soud v Pardubicích'
    ]

    # create a list of stereotype values
    stereotype = ['yes', 'no']

    # create an empty dataframe with the desired columns
    df = pd.DataFrame(
        columns=[
            # 'Legal Judgment',
            'Court Location',
            'Stereotype'
        ]
    )

    # initialize the geocoding service
    geolocator = Nominatim(user_agent='my_app')

    # generate ten random rows and add them to the dataframe
    for i in range(10):
        # generate a random legal judgment name
        legal_judgment = f"{random.randint(1, 10)} T {random.randint(1, 100)}-{random.randint(2000, 2023)}  {random.choice(court_locations)}"
        # generate a random court location
        court_location = random.choice(court_locations)
        # generate a random stereotype value
        stereotype_value = random.choice(stereotype)
        # add the row to the dataframe
        df = df.append({
            # 'Legal Judgment': legal_judgment,
            'Court Location': court_location,
            'Stereotype': stereotype_value
        },
            ignore_index=True
        )

    # display the dataframe
    st.bar_chart(df)
