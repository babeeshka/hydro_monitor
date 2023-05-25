import RPi.GPIO as GPIO
import datetime
import time
import logging

GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme

def fetch_last_watered_time():
    # Read the last watered timestamp from the file
    try:
        with open("last_watered.txt", "r") as f:
            return f.readline()
    except FileNotFoundError:
        logging.error("Could not find 'last_watered.txt'.")
        return "Never watered!"
    except Exception as e:
        logging.error(f"Unexpected error occurred when trying to read 'last_watered.txt': {e}")
        return "Unexpected error occurred."

def check_soil_moisture(pin = 8):
    GPIO.setup(pin, GPIO.IN) 
    return GPIO.input(pin)

def initialize_gpio_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)

def enable_auto_watering(delay = 5, pump_pin = 7, water_sensor_pin = 8):
    consecutive_water_count = 0
    initialize_gpio_output(pump_pin)
    logging.info("Starting auto watering. Press CTRL+C to exit")
    try:
        while 1 and consecutive_water_count < 10:
            time.sleep(delay)
            is_dry = check_soil_moisture(pin = water_sensor_pin) == 0
            if not is_dry:
                if consecutive_water_count < 5:
                    activate_pump(pump_pin, 1)
                consecutive_water_count += 1
            else:
                consecutive_water_count = 0
    except KeyboardInterrupt:
        GPIO.cleanup()

def activate_pump(pump_pin = 7, delay = 1):
    initialize_gpio_output(pump_pin)
    try:
        with open("last_watered.txt", "w") as f:
            f.write(f"Last watered at {datetime.datetime.now()}")
    except Exception as e:
        logging.error(f"Unexpected error occurred when trying to write 'last_watered.txt': {e}")
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pump_pin, GPIO.HIGH)
