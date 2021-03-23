# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 06:25:31 2021

@author: Θόδωρος
"""


def googleMapsDirections(origin="", destination="", travelmode=""): #waypoints=[] :: TO ADD
    ## Options
        ## origin       : from
        ## destination  : to
        ## travelmode   :
            ## driving
            ## walking
            ## bicycling
            ## transit
            ## "" (none) 
        ## waypoints        ---> TODO : Add Waypoints
    
    ## If called with origin specified as "", it completes <origin> with the user's location
    ## If called with any other parameter specified as "", the respective element will remain empty
    ## If called with no parameters, Opens empty google maps directions page
    ## If called with one (1) parameter, this parameter will be <origin>, and it Opens google maps directions page with <origin> filled
    ## If called with two (2) parameters, these will be <origin> and <destination>, and it Opens google maps directions page with <origin> and <destination> filled
    ## If called with three (3) parameters, these will be <origin>, <destination> and <travelmode>, and it Opens google maps directions page with <origin>, <destination> and <travelmode> filled
    
    from openUrls import openUrl
    
    from urllib.parse import urlencode, quote_plus              # import the parts of the urllib.parse that are needed 
    
    
    url_base = "https://www.google.com/maps/dir/?api=1"         # this is the url that leads to google maps directions
    
    payload = {"origin" : origin, 
               "destination" : destination, 
               "travelmode" : travelmode
               }                                 # before it gets transformed into a url form, the payload must first be written as a dictionary. (The payload contains the search parameters)
    
    url_form_payload = urlencode(payload, quote_via=quote_plus) # convert the dictionary into url-compatible form

    final = url_base + "&" + url_form_payload                   # concatenate the url_base with the, url-compatible, payload (a '&' is needed in between)
    
    openUrl(final)                                              # opens the final url in a Web Browser


  


def test():
    ## Used only for testing the code
    
    # googleMapsDirections()                                      # Opens empty google maps directions page
    # googleMapsDirections("New York")                            # Opens google maps directions page with <origin> filled
    # googleMapsDirections("New York", "Miami")                   # Opens google maps directions page with <origin> and <destination> filled
    # googleMapsDirections("New York", "Miami", "walking")        # Opens google maps directions page with <origin>, <destination> and <travelmode> filled
    
    googleMapsDirections("", "8ball club, Thessaloniki", "driving")
    
    
    
test()