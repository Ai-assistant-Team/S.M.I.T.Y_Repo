"""
Created on Tue Mar 24 00:23:15 2021
@author: Tasos
"""
import json  # In order to communicate with json data

import requests  # Allows us to send HTTPS requests

from datetime import datetime  # imports time related functions


def forecast_weather_now(city=""):
    try:
        api_key = "ebb3e7cd4040c8390449e4fb314a5923"

        r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "")
        # GET request With the HTTPS services to the url that gets use the Data in a json format

        api_data = r.json()  # converts json format to python and storring it to the dictionary API_data

        if api_data["cod"] == "404":  # checks if the answer is 404 ,meaning that the city was invalid

            # similar error would be 401       because of:      API key failure
            # similar error would be 429       because of:      More that 60 API calls per minute

            print("Invalid City: {}, Please check your City name!".format(city))
            return 1


        else:
            # Variables for each phenomenon

            temp_city = ((api_data["main"]["temp"]) - 273.15)
            # using the main and temp keys finds the temprature from the dictionary(in F) converts it to Celsium and storring it to temp_city

            temp_min = ((
                            api_data["main"][
                                "temp_min"]) - 273.15)  # same routine for the minimum temprature as with temp_city

            temp_max = ((
                            api_data["main"][
                                "temp_max"]) - 273.15)  # same routine for the maximum temprature as with temp_city

            date_time = datetime.now().strftime(
                "%d %b %Y | %I:%M:%S %p")  # datetime.now gives us the time and strftime helps convert the date and time objects to string

            # Basic visuals for the forecast_weather script
            # Basically the implementation of the variables above into a bunch of print commands



            weather = "--------------------------------------------------------------\n" + "Today's forecast in {} {}".format(city,
                     date_time) + "\n--------------------------------------------------------------\n" + "The temprature is: {:.2f} °C".format(temp_city) + "\n        The temprature will flaxuate between {:.2f}°C to {:.2f}°C\n".format(temp_min, temp_max)

            return weather
    except ConnectionError:
        return 10



