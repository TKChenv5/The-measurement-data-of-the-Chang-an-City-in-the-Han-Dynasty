! pip install folium branca jinja2


import folium

# Approximate center of Han Chang'an City for map focus
center_lat = 34.322
center_lon = 108.8835

# Create the map with modern tiles
m = folium.Map(location=[center_lat, center_lon], zoom_start=13, tiles='OpenStreetMap')

# Approximate polygon coordinates for Han Chang'an City walls (based on historical ranges)
han_walls = [
    [34.2913, 108.849],  # Southwest corner
    [34.2913, 108.918],  # Southeast corner
    [34.353, 108.918],   # Northeast corner
    [34.353, 108.849]    # Northwest corner
]

# Add the polygon overlay for city walls
folium.Polygon(
    locations=han_walls,
    color="red",
    weight=3,
    fill=True,
    fill_color="red",
    fill_opacity=0.2,
    popup="Approximate boundaries of Han Chang'an City Walls (Western Han Dynasty, ~202 BC - AD 9). Historical dimensions: North wall ~5950m, South ~6250m, East ~5940m, West ~4550m."
).add_to(m)

# Marker for Weiyang Palace with enhanced remarks on roles
folium.Marker(
    [34.30444, 108.85722],
    popup="Weiyang Palace: Largest palace complex in history (~4.8 km²), built ~198 BC. Served as the primary administrative center for imperial conferences, royal residence for emperors, political decision-making hub, and command center for the Silk Road initiatives.",
    tooltip="Weiyang Palace"
).add_to(m)

# Marker for Changle Palace with enhanced remarks on roles
folium.Marker(
    [34.31111, 108.8975],
    popup="Changle Palace: Built ~200 BC over Qin ruins (~6 km²). Initially functioned as the imperial court and political center for receiving officials; later repurposed as residence for empress dowagers, empresses, and concubines, including halls like Changxin, Changqiu, Yongshou, and Yongning.",
    tooltip="Changle Palace"
).add_to(m)

# Marker for Jianzhang Palace with enhanced remarks on roles
folium.Marker(
    [34.30863, 108.83348],
    popup="Jianzhang Palace: Built 104 BC in Shanglin Park (~20×30 li). Acted as a ceremonial and leisure palace for imperial hunts, displays of wealth, and mythological recreations (e.g., artificial islands); featured over 1,000 gates and 10,000 rooms, connected to Weiyang Palace.",
    tooltip="Jianzhang Palace"
).add_to(m)

# Marker for Gui Palace with enhanced remarks on roles
folium.Marker(
    [34.3226, 108.8538],
    popup="Gui Palace: Built 101 BC as harem extension north of Weiyang, rectangular (~880m E-W, 1800m N-S). Primarily served as residential quarters for concubines and imperial consorts, supporting the emperor's personal and family life.",
    tooltip="Gui Palace (Approximate)"
).add_to(m)

# Marker for North Palace (Bei Gong) with enhanced remarks on roles
folium.Marker(
    [34.3226, 108.862],
    popup="North Palace (Bei Gong): Built ~200 BC, expanded under Emperor Wu (~620m E-W, 1710m N-S). Functioned as a residential palace for the imperial family, including consorts and relatives, located adjacent to Gui Palace in the northern sector.",
    tooltip="North Palace (Approximate)"
).add_to(m)

# Marker for Mingguang Palace with enhanced remarks on roles
folium.Marker(
    [34.33, 108.8975],
    popup="Mingguang Palace: Built 101 BC north of Changle. Served as a guesthouse for visitors and additional residential space, interconnected with Changle and Weiyang Palaces via flying corridors for secure imperial movement.",
    tooltip="Mingguang Palace (Approximate)"
).add_to(m)

# Save the map as HTML
m.save("han_changan_modern_map_enhanced.html")
print("Map saved to han_changan_modern_map_enhanced.html. Download and open in a browser to view interactively.")