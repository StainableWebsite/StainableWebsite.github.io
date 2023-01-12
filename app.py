from flask import Flask, render_template, url_for, request
import folium
import pandas as pd

app=Flask(__name__)

# download all pictures
darkblue_ic = "static/img/darkblue_icon.png"
green_ic = "static/img/green_icon.png"
grey_ic = "static/img/grey_icon.png"
lightblue_ic = "static/img/lightblue_icon.png"
orange_ic = "static/img/orange_icon.png"
pink_ic = "static/img/pink_icon.png"
purple_ic = "static/img/purple_icon.png"
yellow_ic = "static/img/yellow_icon.png"

h = 30
w = 40

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/map")
def map():
    start_coords = (39.937282,116.403187)
    map = folium.Map(
    location=[0,0],
    tiles='Stamen Toner',
    zoom_start=2.4,
    max_bounds=True
    )

    # custom markers
    darkblue_icon = folium.features.CustomIcon(darkblue_ic,icon_size=(h,w))
    green_icon = folium.features.CustomIcon(green_ic,icon_size=(h,w))
    lightblue_icon = folium.features.CustomIcon(lightblue_ic,icon_size=(h,w))
    orange_icon = folium.features.CustomIcon(orange_ic,icon_size=(h,w))
    pink_icon = folium.features.CustomIcon(pink_ic,icon_size=(h,w))
    purple_icon = folium.features.CustomIcon(purple_ic,icon_size=(h,w))
    yellow_icon = folium.features.CustomIcon(yellow_ic,icon_size=(h,w))

    data = pd.DataFrame({
        'lon':[36,54,40,-5,-24,-27,60], #up and down
        'lat':[100,10,-113,-45,120,23,80], # right and left
        'name':['China','Germany', 'US','Brazil', 'Australia', 'South Africa', 'Russia'],
        'ref_link':['about_china','about_germany','about_us','about_brazil','about_australia','about_southafrica','about_russia'],
        'icon':[darkblue_icon, green_icon, lightblue_icon, orange_icon, pink_icon, purple_icon, yellow_icon]
    })

    for i in range(0, len(data)):
        folium.Marker(
            location=[data.iloc[i]['lon'], data.iloc[i]['lat']], 
            popup=data.iloc[i]['name']+"\n<a href=/"+data.iloc[i]['ref_link']+" target='_top'>"+data.iloc[i]['ref_link']+"</a>",
            tooltip='Click here to see Popup', 
            color='#FFFF00', 
            icon=data.iloc[i]['icon']
        ).add_to(map)
    
    return render_template('map.html', map=map._repr_html_())


@app.route("/about_china")
def about_china():
    return render_template('china.html')

@app.route("/about_germany")
def about_germany():
    return render_template('germany.html')

@app.route("/about_us")
def about_us():
    return render_template('us.html')

@app.route("/about_brazil")
def about_brazil():
    return render_template('brazil.html')

@app.route("/about_australia")
def about_australia():
    return render_template('australia.html')

@app.route("/about_southafrica")
def about_southafrica():
    return render_template('southafrica.html')

@app.route("/about_russia")
def about_russia():
    return render_template('russia.html')

@app.route("/make_a_difference")
def make_a_difference():
    return render_template('make_a_difference.html')

@app.route("/learn_more")
def learn_more():
    return render_template('learn_more.html')


if __name__ == "__main__":
    app.run(debug=True)


    