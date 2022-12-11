import streamlit as st
import pandas as pd
import numpy as np

st.title("Colleges and Countries that produce the most NBA players")

data = pd.read_csv("all_seasons.csv")
colleges = data[['player_name','college']].drop_duplicates()
countries = data[['player_name','country']].drop_duplicates()

df_college = (colleges.groupby('college').size().rename('count').reset_index().sort_values(by='count', ascending=False))
df_country = (countries.groupby('country').size().rename('count').reset_index().sort_values(by='count', ascending=False))

col1, col2 = st.columns(2)

with col1:
    st.markdown("Top 10 Colleges")
    st.write(df_college.head(10).reset_index())
    st.markdown("None refers to players who are international, were drafted straight from high school, or Americans who played overseas for a year before joining the NBA")

with col2:
    st.markdown("Top 10 countries")
    st.write(df_country.head(10).reset_index())