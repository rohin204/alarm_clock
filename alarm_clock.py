from playsound import playsound
import time 

CLEAR = "\033[2J" # clear the terminal
CLEAR_AND_RETURN = "\033[H" # returns the cursor the home position , if we print it prints over existing one

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        # total seconds left to reach given 'seconds'
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 # 125s // 60 = 2 , gives int division
        seconds_left = time_left % 60 # 125 % 60 gives 5 remainder , which is seconds

        print(f"{CLEAR_AND_RETURN}Alarm will ring in: {minutes_left:02d}:{seconds_left:02d}") # :02d makes it two digits , 00:00 format 
        

    playsound("alarm-clock-short-6402.mp3")

#minutes = int(input("How many minutes: ") ) # with 'int()' specified it will read values as 'str'
#seconds = int(input("How many seconds: "))

#map() takes two args it takes a list and iterates through each item with the specified function , map(do this, given list)
minutes, seconds = map(int, input("Enter time in minutes seconds seperated by ':' ").split(":"))
total_sec = minutes*60 + seconds


alarm(total_sec)