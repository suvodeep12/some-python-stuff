import json
import urllib.parse
import urllib.request

address = input("Enter location: ")
service_url = "http://py4e-data.dr-chuck.net/geojson?"

full_address = service_url + urllib.parse.urlencode({'address': address})
print('Retrieving', full_address)

uh = urllib.request.urlopen(full_address)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

print(json.dumps(js, indent=4))
place_id = js["results"][0]["place_id"]
print("Place", place_id)
