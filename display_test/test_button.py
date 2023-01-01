import RPi.GPIO as GPIO
import config

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    if(GPIO.input(10) == GPIO.HIGH):
        config.exit_loop = True
        break
    
print("closing")
GPIO.cleanup()