from win10toast import ToastNotifier # python -m pip install win10toast
#made by Γεωργία Βαλκάνη

toaster = ToastNotifier() # One-time initialization
def checkNotif():
# Show notification whenever needed
   toaster.show_toast("Notification!", "Alert!", threaded=True,
                   icon_path=None, duration=180)  # 180seconds

   import time

   while toaster.notification_active(): # To check if any notifications are active,
# use `toaster.notification_active()`
       time.sleep(0.1)
checkNotif()
# end of <checkNotif>