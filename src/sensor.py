import json
from random import uniform

from config.mqtt_config import TOPIC_FORMAT


class Sensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id

    def generate_temperature(self):
        """Generate a random temperature value between 15.0 and 30.0 degrees Celsius"""
        return round(uniform(15.0, 30.0), 2)

    def send_data(self, mqtt_client):
        """Send temperature data via MQTT client"""
        temperature = self.generate_temperature()
        topic = TOPIC_FORMAT.format(id=self.sensor_id)
        payload = json.dumps({"temperature": temperature})
        
        mqtt_client.publish(topic, payload)
        print(f"Sensor {self.sensor_id}: Published {payload} to {topic}")