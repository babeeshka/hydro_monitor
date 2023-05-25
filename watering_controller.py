from flask import Blueprint, render_template, g
import datetime
import os
import logging

import water

# Create a blueprint
watering_blueprint = Blueprint('watering', __name__)

@watering_blueprint.route("/last_watered")
def get_last_watered_time():
    # Fetch the timestamp of the last watering operation
    g.last_watered = water.fetch_last_watered_time()
    return render_template('main.html')

@watering_blueprint.route("/sensor")
def get_soil_status():
    # Check the status of the soil
    soil_status = water.check_soil_moisture()
    g.soil_status_msg = "Water me please!" if soil_status == 1 else "I'm a happy plant"
    return render_template('main.html')

@watering_blueprint.route("/water")
def trigger_watering():
    # Execute a single watering operation
    water.activate_pump()
    g.watering_msg = "Watered Once"
    return render_template('main.html')

@watering_blueprint.route("/auto/water/<toggle>")
def toggle_auto_watering(toggle):
    lock_file = "/tmp/auto_water.lock"
    if toggle == "ON":
        if os.path.exists(lock_file):
            g.auto_watering_msg = "Auto watering is already running"
            logging.info("Attempted to start auto watering, but it is already running.")
        else:
            os.system("touch {}".format(lock_file))
            os.system("python3 auto_water.py&")
            g.auto_watering_msg = "Auto watering turned ON"
            logging.info("Auto watering turned ON.")
    else:
        if os.path.exists(lock_file):
            os.system("rm {}".format(lock_file))
        os.system("pkill -f auto_water.py")
        g.auto_watering_msg = "Auto watering turned OFF"
        logging.info("Auto watering turned OFF.")
    return render_template('main.html')

@watering_blueprint.context_processor
def provide_template_variables():
    return dict(
        title="hydro_monitor",
        time=datetime.datetime.now(),
        text=g.text
    )
