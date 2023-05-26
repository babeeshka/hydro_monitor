# Raspberry Pi Water Pump Monitor and Controller (hydro_monitor)
This project involves creating a Flask web application to monitor and control a water pump connected to a Raspberry Pi. The application provides a web interface where the user can check the pump's status, manually control the pump, and schedule automatic watering.

## Prerequisites
- Raspberry Pi (tested with 3B model)
- Python 3.7 or above
- Flask
- RPi.GPIO Python library
- 4 channel relay
- 5V water pump

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/<your-repo-name>.git
    ```
2. Navigate into the project directory:
    ```bash
    cd <your-repo-name>
    ```
3. Install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask server:
    ```bash
    python3 app.py
    ```
5. To start the auto watering script, run the following command:
    ```bash
    python3 auto_watering_script.py
    ```

## Usage
Navigate to the IP address of your Raspberry Pi in a web browser. From there, you can:

- Check the last time the plant was watered
- Check the status of the soil
- Manually water the plant
- Enable or disable automatic watering

The application also serves an API with the following endpoints:

- `/last_watered`: Returns the last time the plant was watered
- `/sensor`: Returns the status of the soil
- `/water`: Waters the plant once
- `/auto/water/<toggle>`: Enables or disables automatic watering

## Auto Watering Script
To have the system automatically water the plant, set up a cron job to execute the auto_watering_script.py script periodically. Here's an example of a cron job that runs the script every 20 minutes:

```bash
*/20 * * * * /usr/bin/python3 /home/pi/<your-repo-name>/auto_watering_script.py >> /home/pi/<your-repo-name>/cronjob.log 2>&1
```

## Caution
Please ensure that all wiring connections are solid and correct. Miswiring can cause damage to the Raspberry Pi or other components. Be very careful when dealing with water around electronics. Always double-check your setup and proceed with caution.
