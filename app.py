from flask import Flask
import watering  

app = Flask(__name__)
app.register_blueprint(watering.watering) 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
