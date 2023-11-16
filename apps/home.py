import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Project Canopy 🌲")

    st.markdown(
        """
    Project Canopy allows you to select any area of your choice and produces a comprehensive deforestation report on it.
    Check out https://www.projectcanopy.org/ for more details. 

    """
    )

    # m = leafmap.Map(locate_control=True)
    # m.add_basemap("ROADMAP")
    # m.to_streamlit(height=700)
