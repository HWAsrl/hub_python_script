import paho.mqtt.client as mqtt

from config.mqtt_config import BROKER, PORT


class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client()
        self.broker_address = BROKER
        self.broker_port = PORT

    def connect(self):
        self.client.connect(self.broker_address, self.broker_port)
        self.client.loop_start()
        print(f"Connected to MQTT broker at {self.broker_address}:{self.broker_port}")

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        print("Disconnected from MQTT broker")

    def publish(self, topic, payload):
        result = self.client.publish(topic, payload)
        return result