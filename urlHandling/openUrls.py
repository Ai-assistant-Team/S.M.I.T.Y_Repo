# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 08:45:24 2021

@author: Θόδωρος
"""

import webbrowser                                           # imports the needed library

def openUrl(url=''):
    #made by Οικονομίδης Θεόδωρος
        
    try:
        
        webbrowser.open_new(url)                            # opens the given url, using a webbrowser

        return 0
    
    except:
        
        return 14                                           # 14 : Problem occured while opening url.
        
    
#end of openUrl