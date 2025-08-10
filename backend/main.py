from flask import Flask, render_template, jsonify
from energy_sensor import get_current_consumption, get_consumption_history
from mqtt_client import MQTTClient

app = Flask(__name__, template_folder='../dashboard/templates', static_folder='../dashboard/static')

mqtt_client = MQTTClient()
mqtt_client.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/consumption/current')
def current_consumption():
    power = get_current_consumption()
    return jsonify({"power": power})

@app.route('/api/consumption/history')
def consumption_history():
    history = get_consumption_history()
    return jsonify(history)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
