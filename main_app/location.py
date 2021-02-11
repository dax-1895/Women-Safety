

# city = data['city']
# state = data['region']
# location = data['loc'].split(',')
# lat = location[0]
# log = location[1]
import geocoder
g = geocoder.ip('me')
location=g.latlng
lat = str(location[0])
log = str(location[1])




