# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 06:25:31 2021

@author: Θόδωρος
"""

## version 1.2


def googleMapsDirections(origin='', destination='', travelmode=''):
    #made by Οικονομίδης Θεόδωρος
    ## Options
        ## origin       : from
        ## destination  : to
        ## travelmode   :
            ## driving
            ## walking
            ## bicycling    NOTE : there are some areas in which bicycling is not supported by google maps.
            ## transit
            ## '' (none) 
    
    ## If called with origin specified as '', it completes <origin> with the user's location
    ## If called with any other parameter specified as '', the respective element will remain empty
    ## If called with no parameters, Opens empty google maps directions page
    ## If called with one (1) parameter, this parameter will be <origin>, and it Opens google maps directions page with <origin> filled
    ## If called with two (2) parameters, these will be <origin> and <destination>, and it Opens google maps directions page with <origin> and <destination> filled
    ## If called with three (3) parameters, these will be <origin>, <destination> and <travelmode>, and it Opens google maps directions page with <origin>, <destination> and <travelmode> filled
    
    try:
        
        # imports 
        
        from SMITY.urlHandling.openUrls import openUrl
        
        from urllib.parse import urlencode, quote_plus              # import the parts of the urllib.parse that are needed 
        
        # functionality
        
        returnCode = 0                                              # 0 : No Errors        
        
        url_base = 'https://www.google.com/maps/dir/?api=1'         # this is the url that leads to google maps directions
        
        payload = {'origin' : origin, 
                   'destination' : destination, 
                   'travelmode' : travelmode
                   }                                                # before it gets transformed into a url form, the payload must first be written as a dictionary. (The payload contains the search parameters)
        
        url_form_payload = urlencode(payload, quote_via=quote_plus) # convert the dictionary into url-compatible form
    
        final = url_base + '&' + url_form_payload                   # concatenate the url_base with the, url-compatible, payload (a '&' is needed in between)
        
        returnCode = openUrl(final)                                 # opens the final url in a Web Browser and passes the returned value in <returnCode>
        
        return returnCode
    
    except Exception: 
        
        return 1                                                    # 1 : Undefined Error


#end of googleMapsDirections