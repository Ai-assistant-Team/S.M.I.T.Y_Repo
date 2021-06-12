"""
Created on Tue Mar 24 00:23:15 2021
@author: Tasos
"""
import json  # In order to communicate with json data

import requests  # Allows us to send HTTPS requests

from datetime import datetime  # imports time related functions


def Forecast_weather_now(city="", API_key=""):
    try:
        r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_key + "")
        # GET request With the HTTPS services to the url that gets use the Data in a json format

        API_data = r.json()  # converts json format to python and storring it to the dictionary API_data

        if API_data["cod"] == "404":  # checks if the answer is 404 ,meaning that the city was invalid

            # similar error would be 401       because of:      API key failure
            # similar error would be 429       because of:      More that 60 API calls per minute

            print("Invalid City: {}, Please check your City name!".format(city))
            return 1


        else:
            # Variables for each phenomenon

            temp_city = ((API_data["main"]["temp"]) - 273.15)
            # using the main and temp keys finds the temprature from the dictionary(in F) converts it to Celsium and storring it to temp_city

            temp_min = ((
                        API_data["main"]["temp_min"]) - 273.15)  # same routine for the minimum temprature as with temp_city

            temp_max = ((
                        API_data["main"]["temp_max"]) - 273.15)  # same routine for the maximum temprature as with temp_city

            weather_desc = ((API_data["weather"][0][
                "description"]))  # a dictionary which has only a single array element 0 and inside of it nests another dictionary

            humidity = ((API_data["main"]["humidity"]))  # same procedure as the temp_city

            date_time = datetime.now().strftime(
                "%d %b %Y | %I:%M:%S %p")  # datetime.now gives us the time and strftime helps convert the date and time objects to string

            # Basic visuals for the forecast_weather script
            # Basically the implementation of the variables above into a bunch of print commands

            print("--------------------------------------------------------------")

            print("Today's forecast in {} {}".format(city,
                                                    date_time))  # format puts the variables into the "{}" from left to right

            print("--------------------------------------------------------------")

            print("The temprature is: {:.2f} °C".format(
                temp_city))  # .2f is the amount of the demicals it is allowed to print

            print("        The temprature will flaxuate between {:.2f}°C to {:.2f}°C".format(temp_min, temp_max))

            print("Current weather Status: {}".format(weather_desc))

            print("\nHumidity now: {}%".format(humidity))

            return 0

    except ConnectionError:
        return 10


def test():
    city = "Albania"  # # variable for the city that I want to choose
    API_key = "ebb3e7cd4040c8390449e4fb314a5923"  # DISCLAIMER I did not include my API_key , you can get yours at openweather.org
    Forecast_weather_now(city, API_key)


test()