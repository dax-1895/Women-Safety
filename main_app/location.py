import geocoder
g = geocoder.ip('me')
location=g.latlng
lat = str(location[0])
log = str(location[1])




