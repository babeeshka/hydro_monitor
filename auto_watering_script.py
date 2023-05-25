import watering_operations

# This script is intended to be run as a standalone process.
# It invokes the automatic watering function from the `watering_operations` module,
# which controls the watering process based on the moisture sensor's reading.

if __name__ == "__main__":
    # The `auto_water` function is set with the default parameters:
    # delay = 5 minutes, pump_pin = 7, water_sensor_pin = 8.
    # This means that the script checks the soil status every 5 minutes,
    # and if the soil is dry, it activates the water pump (connected to pin 7)
    # and checks the status again after the specified delay.
    # If the soil remains dry for more than 5 consecutive checks,
    # the script stops the watering process to prevent overwatering.
    watering_operations.auto_water()


# an example cron entry might look like this to run the script every 20 minutes:
# */20 * * * * /usr/bin/python3 /path/to/auto_watering_script.py
