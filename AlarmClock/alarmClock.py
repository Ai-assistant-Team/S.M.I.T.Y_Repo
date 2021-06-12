import datetime # imports the needed library
import time # imports the needed library
import winsound

def check_alarm_input(alarm_time):
	# made by Γεωργία Βαλκάνη

	#Checks to see if the user has entered in a valid alarm time
	if len(alarm_time) == 1:
		if alarm_time[0] < 24 and alarm_time[0] >= 0:
			return True
	if len(alarm_time) == 2: # (Hour:Min) Format
		if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
		   alarm_time[1] < 60 and alarm_time[1] >= 0:
			return True
	elif len(alarm_time) == 3: # (Hour:Min:Sec) Format
		if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
		   alarm_time[1] < 60 and alarm_time[1] >= 0 and \
		   alarm_time[2] < 60 and alarm_time[2] >= 0:
			return True
	return False

print('Set a time for the alarm (Ex. 06:30 or 18:30:00)')
while True:
	alarm_input = input('Time to wake up: ') # Get user input for the alarm time
	try:
		alarm_time = [int(n) for n in alarm_input.split(":")]
		if check_alarm_input(alarm_time):
			break
		else:
			raise ValueError
	except ValueError: # the answer is not valid
		print('ERROR: Enter time in HH:MM or HH:MM:SS format') # prints to try again

# Convert the alarm time from [H:M] or [H:M:S] to seconds
seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and Second
alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

now = datetime.datetime.now() # Get the current time of day in seconds
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])


time_diff_seconds = alarm_seconds - current_time_seconds # Calculate the number of seconds until alarm goes off

# If time difference is negative, set alarm for next day
if time_diff_seconds < 0:
	time_diff_seconds += 86400 # number of seconds in a day

# Display the amount of time until the alarm goes off
print('Alarm set to go off in %s' % datetime.timedelta(seconds=time_diff_seconds))

time.sleep(time_diff_seconds)# Sleep until the alarm goes off

print('Wake Up!') # Time for the alarm to go off

