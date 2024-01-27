import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')


df = pd.read_csv("india.csv")

state_list = list(df['State'].unique())
state_list.insert(0,'Overall India')

st.sidebar.title("India Cencus Data Visulization")




selected_state = st.sidebar.selectbox("Select the State : ",state_list)
primary = st.sidebar.selectbox("Select Primary Parameter : ",sorted(df.columns[4:]))
secondary = st.sidebar.selectbox("Select Secondary Parameter : ",sorted(df.columns[4:]))


btn = st.sidebar.button("Plot Graph")

# ['State', 'District', 'Latitude', 'Longitude', 'Population',
if btn:
    st.write("Size represent the Primary Parameter")
    st.write("Color represent the Secondary Parameter")
    if selected_state =='Overall India':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color=secondary, size=primary,
                                size_max=15, zoom=3.5,mapbox_style="carto-positron",
                                width=1200,height=800,hover_name='District',
                                color_continuous_scale=px.colors.cyclical.IceFire)
        st.plotly_chart(fig,use_container_width=True)

    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", color=secondary, size=primary,
                                size_max=15, zoom=6, mapbox_style="carto-positron",
                                width=1200, height=800, hover_name='District',
                                color_continuous_scale=px.colors.sequential.Viridis)
        st.plotly_chart(fig, use_container_width=True)

