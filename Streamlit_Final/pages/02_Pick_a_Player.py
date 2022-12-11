import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

data = pd.read_csv("all_seasons.csv")
data["pts"] = round(data["pts"],2)
data["reb"] = round(data["reb"],2)
data["ast"] = round(data["ast"],2)
#st.write(data.head())

player_info = data[["player_name","team_abbreviation","college","country","draft_year","draft_round","gp","pts","reb","ast",
                    "net_rating","usg_pct","ts_pct","season"]]

players = data["player_name"].unique()
player = st.selectbox('Pick a Player',sorted(players))
df2 = player_info.loc[player_info.player_name == player]

st.write(df2)

teams = data["team_abbreviation"].unique()
team = st.selectbox('Pick a Team', sorted(teams))
df3 = player_info.loc[player_info.team_abbreviation == team]

st.write(df3)



