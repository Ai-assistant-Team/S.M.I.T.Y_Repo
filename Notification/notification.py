"""
Created on We Jun 16 20:16:19 2021
@author: manolispolymeneris
"""

from win10toast import ToastNotifier # python -m pip install win10toast

try:
   toaster = ToastNotifier() # One-time initialization
   
   def Notify(content, title='Notification!'):
      toaster.show_toast(title, content, threaded=True, # Show notification whenever needed
      icon_path=None, duration=180)  # 180 seconds
      
   return 0
      
except:
   return 1
