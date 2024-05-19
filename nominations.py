import requests

def gps_coordinate(city):
    url=f"https://nominatim.openstreetmap.org/search?q=Cairns&format=json"
    x=input("Enter the city name:")
    if x in url:
     print(url[x])
    response = requests.get(url)
    getcord = response.json()
    a=getcord[lat][long]
    return a

def gps(city):
    x=gps_coordinate(city)
    print(x)