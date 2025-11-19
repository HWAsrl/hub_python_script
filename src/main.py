import os
import sys
import time
import uuid

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

    #TODO Modify to use UUIDs from db 
    sensor_ids = [
        "550e8400-e29b-41d4-a716-446655440000",
        "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
        "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    ]
    sensors = [Sensor(sensor_id) for sensor_id in sensor_ids]


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