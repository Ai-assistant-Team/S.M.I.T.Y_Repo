from win10toast import ToastNotifier # python -m pip install win10toast
#made by Γεωργία Βαλκάνη

try:
   toaster = ToastNotifier() # One-time initialization
   
   def checkNotif():
      toaster.show_toast(title='Notification!'title, content, threaded=True, # Show notification whenever needed
      icon_path=None, duration=180)  # 180seconds
      
   return 0
      
except:
   return 1
