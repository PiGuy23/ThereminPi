from time import sleep
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Set pin 21 to be an input pin and set initial value to be pulled low (off)
print("setup done")
while True: # Run forever
    if GPIO.input(40) == GPIO.HIGH:
        print("Yes")
        
    else :
        print("No")
        
    sleep(1)