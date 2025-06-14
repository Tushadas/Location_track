import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

key = "16a80d8687ee4c61be0530b9de62c6a9"  # Geocoder API Key
number = input("Please give your number: ")
new_number = phonenumbers.parse(number)
location = geocoder.description_for_number(new_number, "IN")
print("Location:", location)

service_name = carrier.name_for_number(new_number, "IN")
print("Service Name:", service_name)

geocoder = OpenCageGeocode(key)
query = str(location)

# Test with a known location
query = "West Bengal, India"  # Uncomment this line to test with a known location

result = geocoder.geocode(query)
print("Geocode Result:", result)

if result and len(result) > 0 and 'geometry' in result[0]:
    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']

    print("Latitude:", lat)
    print("Longitude:", lng)

    my_map = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(my_map)

    my_map.save("location.html")
    print("Location tracking completed")
else:
    print("No valid geocode results found.")

print("Thank you")
