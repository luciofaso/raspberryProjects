# Hello World + button + turn on lead when pushed

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

print("system has started...")


def button_callback(channel):
    print("Button was pushed! Led blinking")
    GPIO.output(8, GPIO.HIGH)  # Turn on
    sleep(1)  # Sleep for 1 second
    GPIO.output(8, GPIO.LOW)

GPIO.add_event_detect(7,GPIO.RISING,callback=button_callback)

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up

# non event-based
# while True: # Run forever
#    if GPIO.input(10) == GPIO.HIGH:
#        print("Button was pushed!")


