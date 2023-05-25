from flask import Flask
import watering_controller  

app = Flask(__name__)
app.register_blueprint(watering_controller.watering) 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
