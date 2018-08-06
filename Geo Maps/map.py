import folium
import pandas

map = folium.Map()
df=pandas.read_csv("Volcanoes_USA.txt")
lat=list(df["LAT"])
lon=list(df["LON"])
elev=list(df["ELEV"])
### liso=[str(lat[i]) + ',' + str(lon[i]) for i in range(len(lat))]
##for item in liso:
###    fg.add_child(folium.Marker(location=[float(item[0]),float(item[1])], popup="Hi! I am a marker", icon=folium.Icon(color='green')))
def clor(Elevation):
    if Elevation<=1000:
        return 'green'
    elif 1000>Elevation<=2000:
        return 'blue'
    elif 2000>Elevation<=3000:
        return 'orange'
    else: return 'red'

fg=folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6,
    popup=folium.Popup("Elevation "+str(el)+" m", parse_html=True),
    fill=True, fill_color = clor(el), color='grey', fill_opacity=1.0))

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data = open('world.json','r',encoding='utf-8-sig').read() ,
style_function=lambda x: { 'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000<= x['properties']['POP2005']<20000000 else 'red' } ))

map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("map.html")
