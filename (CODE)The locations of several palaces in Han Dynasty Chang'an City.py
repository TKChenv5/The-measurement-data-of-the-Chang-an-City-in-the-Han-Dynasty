# Install folium if not already installed
! pip install folium

import folium

# Create a map centered on the approximate location of Han Chang'an in modern Xi'an
m = folium.Map(location=[34.3225, 108.879], zoom_start=13, tiles='OpenStreetMap')

# Define the approximate polygon coordinates for Han Chang'an city walls, extended to include Jianzhang Palace
polygon_coords = [
    [34.354, 108.83],  # Northwest corner
    [34.354, 108.914],  # Northeast corner
    [34.291, 108.914],  # Southeast corner
    [34.291, 108.83],  # Southwest corner
    [34.354, 108.83]   # Close the polygon
]

# Add the polygon overlay for the city walls outline
folium.Polygon(
    locations=polygon_coords,
    color='brown',  # Color of the outline
    weight=5,       # Thickness of the line
    fill=True,
    fill_color='yellow',
    fill_opacity=0.3  # Semi-transparent fill
).add_to(m)

# Optimized markers for major historical palaces with revised approximate coordinates based on the provided map
# Using Font Awesome icons for better visual representation (e.g., 'university' for palace-like structures)
# First, add Font Awesome support by adding the script to the map header
m.get_root().html.add_child(folium.Element("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
"""))

# Weiyang Palace (未央宫) - Confirmed correct
folium.Marker(
    location=[34.3044, 108.8572],
    popup='未央宫 (Weiyang Palace)',
    icon=folium.Icon(color='red', prefix='fa', icon='crown')
).add_to(m)

# Changle Palace (长乐宫) - Adjusted to match relative position east of Weiyang
folium.Marker(
    location=[34.3044, 108.8975],  # Aligned latitude with Weiyang for better relative match
    popup='长乐宫 (Changle Palace)',
    icon=folium.Icon(color='blue', prefix='fa', icon='star')
).add_to(m)

# Jianzhang Palace (建章宫) - West, outside main wall
folium.Marker(
    location=[34.3086, 108.8333],
    popup='建章宫 (Jianzhang Palace)',
    icon=folium.Icon(color='green', prefix='fa', icon='building')
).add_to(m)

# Mingguang Palace (明光宫) - North of Changle
folium.Marker(
    location=[34.325, 108.8975],
    popup='明光宫 (Mingguang Palace)',
    icon=folium.Icon(color='purple', prefix='fa', icon='sun')
).add_to(m)

# Gui Palace (桂宫) - Adjusted position based on feedback
folium.Marker(
    location=[34.325, 108.8572],
    popup='桂宫 (Gui Palace)',
    icon=folium.Icon(color='orange', prefix='fa', icon='tree')
).add_to(m)

# North Palace (北宫) - Adjusted position based on feedback
folium.Marker(
    location=[34.325, 108.87],
    popup='北宫 (North Palace)',
    icon=folium.Icon(color='black', prefix='fa', icon='arrow-up')
).add_to(m)

# Save the map as HTML
m.save('xi_an_with_han_changan_outline_and_optimized_palaces.html')

# Display the map in Colab (optional)
m