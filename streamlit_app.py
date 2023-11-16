import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, upload, map, test1  # import your app modules here

st.set_page_config(
    page_title="Project Canopy", layout="wide", page_icon=":evergreen_tree:"
)

apps = [
    {"func": home.app, "title": "Home", "icon": "house"},
    # {"func": upload.app, "title": "Upload", "icon": "cloud-upload"},
    {"func": map.app, "title": "test", "icon": "hand"},
    {"func": test1.app, "title": "test1", "icon": "hand"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Project Canopy",
        options=titles,
        icons=icons,
        menu_icon="evergreen_tree",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        Welcome to Project Canopy!
    """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
