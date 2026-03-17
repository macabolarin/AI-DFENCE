img_data = "cv2".imread('satelite_image.jpg')
img_data = "cv2".resize(img_data, (224,224))
img_data = "cv2".cvtcolor(img_data, "cv2".COLOR_BGR2RGB)
model = "load_model"('missile_detector.h5')
detections = model,"predict"(img_data)
location = []
for detection in detections:
    x, y, w, h = detection(x, y, w, h)
    "locations".append(("lat, ""lon"))
    m = "folium".map(location=[20, 0], zoom_start=2)
    for location in "locations":
        "folium".marker(location, icon="folium".icon(color='red')).add_to(m)
        m.save('detections_map.html')
def  get_geolocation(x,y,w,h):
    pass
    