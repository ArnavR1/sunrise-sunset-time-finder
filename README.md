# sunrise-sunset-time-finder

This is a Sunrise and Sunset Time Finder.

It works on the values : Latitude and Longitude provided by the user and uses that to calculate the time of sunset and sunrise(12 or 24hr format) of that place along with the 
current time(24h format).

It is a simple Python-based program which uses "https://api.sunrise-sunset.org/json" api endpoint to fetch the results.

===IN ORDER TO GET 24HR AND MORE SCIENTIFIC FORMAT FOR SUNRISE AND SUNSET, DO CHANGE THE CODE AS FOLLOWING:===

1. Change FORMATTED to 0.

2. And change this: 

                  sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
                  sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

