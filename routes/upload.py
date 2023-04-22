import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import openpyxl

def Upload():
  uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
  if uploaded_file is not None:
      st.text(uploaded_file.name)
      df1 = pd.read_csv('https://docs.google.com/spreadsheets/d/1Y7dVjKqs-3G1xYvAntZJ2kcJuKd59HDctJvcFq6FsS0/export?format=csv&gid=2187210');
      # df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
      AgGrid(df1)
