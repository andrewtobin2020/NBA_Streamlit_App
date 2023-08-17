import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Stats include points, rebounds, assists, and True Shooting percentage (overall measure of a player's shooting ability). Games played is also included")
data = pd.read_csv("all_seasons.csv")
 
df_pts = round(data.groupby('player_name').agg(
            Pts=('pts', np.mean),
            GP=('gp', np.sum)),2)

df_reb = round(data.groupby('player_name').agg(
            Reb=('reb', np.mean),
            GP=('gp', np.sum)),2)

df_ast = round(data.groupby('player_name').agg(
            Ast=('ast', np.mean),
            GP=('gp', np.sum)),2)


df_pts = df_pts.sort_values(by='Pts', ascending = False)
df_reb = df_reb.sort_values(by='Reb', ascending = False)
df_ast = df_ast.sort_values(by='Ast', ascending = False)

col1, col2 = st.columns(2)

with col1:
    st.markdown("Points Per Game Leaders")
    st.write(df_pts.head(10))
    st.markdown("Rebounds Per Game Leaders")
    st.write(df_reb.head(10))

with col2:
    st.markdown("Assists Per Game Leaders")
    st.write(df_ast.head(10))

    df_ts = round(data.groupby('player_name').agg(
            Ts_pct=('ts_pct', np.mean),
            GP=('gp', np.sum)),2)
    df_ts = df_ts.sort_values(by='Ts_pct', ascending = False)
    st.markdown("True Shooting leaders")
    st.write(df_ts.head(10))
