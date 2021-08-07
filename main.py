import requests
import datetime as dt

MY_LAT = float(input("Enter the latitude: "))
MY_LONG = float(input("Enter the longitude: "))
FORMATTED = 1  # 0 for 24hr format(more scientific one) & 1 for 12hr format

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": FORMATTED
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()  # Exception for any error
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print("Sunrise: ", sunrise)
print("Sunset: ", sunset)
print("Present time: ", dt.datetime.now().hour, "hrs")
