import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Average Age, Height, and Weight of Players Over Time")
data = pd.read_csv("all_seasons.csv")

#st.write(data)
df_age = round(data.groupby(['season'], as_index = False)['age'].mean(),2)
# df_age["age"] = round(df_age["age"],2)
# st.write(df_age)
line = alt.Chart(df_age, title = "Average Player Age Over Time").mark_line().encode(
    x = 'season',
    y=alt.Y('age', scale=alt.Scale(domain=[25, 30]))
)
st.altair_chart(line, use_container_width=True)

data["player_height"] = data["player_height"]/2.54
df_mean_height = round(data.groupby(['season'], as_index = False)['player_height'].mean(),2)
line2 = alt.Chart(df_mean_height, title = "Average Player Height Over Time (in Inches)").mark_line().encode(
    x = 'season',
    y=alt.Y('player_height', scale=alt.Scale(domain=[76, 80]))
)
st.altair_chart(line2, use_container_width=True)

data["player_weight"] = data["player_weight"] * 2.2046
df_mean_weight = round(data.groupby(['season'], as_index = False)['player_weight'].mean(),2)
line3 = alt.Chart(df_mean_weight, title = "Average Player Weight Over Time (in Pounds)").mark_line().encode(
    x = 'season',
    y=alt.Y('player_weight', scale=alt.Scale(domain=[210, 230]))
)
st.altair_chart(line3, use_container_width=True)
