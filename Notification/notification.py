from win10toast import ToastNotifier # python -m pip install win10toast
#made by Γεωργία Βαλκάνη

try:
   toaster = ToastNotifier() # One-time initialization
   def checkNotif():
   # Show notification whenever needed
      toaster.show_toast("Notification!", "Alert!", threaded=True,
         icon_path=None, duration=180)  # 180seconds

   checkNotif()
   # end of <checkNotif>
