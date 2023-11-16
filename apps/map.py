import folium
import streamlit as st

from streamlit_folium import st_folium
import os


def app():
    # center on Liberty Bell, add marker
    m = folium.Map(location=[22, 1], zoom_start=5)
    # folium.Marker(
    #     [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
    # ).add_to(m)
    input_mask_folder = "output"
    dir_values = os.listdir(input_mask_folder)
    for i in range(len(dir_values)):
        if dir_values[i].endswith(".geojson"):
            test = "output/" + dir_values[i]
            folium.GeoJson(test).add_to(m)

    folium.LayerControl().add_to(m)
    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=725)
