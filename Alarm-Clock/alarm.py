#  imports
from datetime import datetime
from playsound import playsound

time = input("Enter the time of alarm to be set:HH:MM:SS ")
hour = time[0:2]
minute = time[3:5]
seconds = time[6:8]
period = time[9:11].upper()

# setting up alarm
while(1):
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(period == current_period) and (hour == current_hour) and (minute == current_minute) and (seconds == current_seconds):
        print("Wake Up!")
        playsound('audio.mp3')
        break
