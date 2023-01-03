import RPi.GPIO as GPIO
import config

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    if(GPIO.input(10) == GPIO.HIGH):
        print(config.exit_loop)
        config.exit_loop = False
        print(config.exit_loop)
        break
    
print("closing")
