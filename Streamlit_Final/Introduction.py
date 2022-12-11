import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    #st.image("NBA_Logo.png")

with col3:
    st.write(' ')

st.markdown("The NBA was founded in 1946 in New York City. The league consists of 30 teams split evenly between the eastern and western conferences.")
st.markdown("The dataset I used was from Kaggle. It contains 12,306 rows and 22 columns of data. Data goes from the 1996/1997 season to the 2021/2022 season.")
