import os
import sys
import time

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.mqtt_client import MQTTClient
from src.sensor import Sensor


def main():
    """Main function to simulate multiple temperature sensors"""
    print("Starting MQTT Sensor Simulator...")
    print("Simulating 3 sensors sending data every 20 seconds")
    print("Press Ctrl+C to stop\n")
    
    # Create MQTT client and connect
    mqtt_client = MQTTClient()
    mqtt_client.connect()

    # Create 3 sensors with IDs 1, 2, and 3
    sensors = [Sensor(sensor_id) for sensor_id in range(1, 4)]

    try:
        while True:
            # Each sensor sends data
            for sensor in sensors:
                sensor.send_data(mqtt_client)
            
            # Wait 20 seconds before next round
            print(f"\nWaiting 20 seconds...\n")
            time.sleep(20)
    except KeyboardInterrupt:
        print("\n\nStopping sensor simulator...")
    finally:
        mqtt_client.disconnect()
        print("Sensor simulator stopped.")


if __name__ == "__main__":
    main()