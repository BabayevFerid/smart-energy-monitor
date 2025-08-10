import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker='broker.emqx.io', port=1883):
        self.client = mqtt.Client()
        self.broker = broker
        self.port = port
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def connect(self):
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()
        self.client.subscribe("energy/consumption")

    def publish(self, topic, payload):
        self.client.publish(topic, payload)

    def on_connect(self, client, userdata, flags, rc):
        print(f"MQTT connected with code {rc}")

    def on_message(self, client, userdata, msg):
        print(f"Message received: {msg.topic} {msg.payload.decode()}")
        # Burada sensorlardan gələn real məlumatları işləyə bilərsən
