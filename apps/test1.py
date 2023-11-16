import folium
import webbrowser


class Map:
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start

    def showMap(self):
        # Create the map
        my_map = folium.Map(location=self.center, zoom_start=self.zoom_start)

        # Display the map
        my_map.save("footprint.html")
        webbrowser.open("footprint.html")


def app():
    # Define coordinates of where we want to center our map
    coords = [22, 1]
    map = Map(center=coords, zoom_start=5)
    map.showMap()
