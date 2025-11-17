# MQTT Sensor Simulator

This project simulates multiple temperature sensors that publish random temperature data to a local Mosquitto MQTT broker. The sensors send data at regular intervals, allowing for real-time monitoring of temperature readings.

## Project Structure

```
mqtt-sensor-simulator
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── mqtt_client.py
│   └── sensor.py
├── config
│   └── mqtt_config.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mqtt-sensor-simulator
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Before running the project, configure the MQTT settings in `config/mqtt_config.py`. You can specify the broker address, port, and topic format.

## Usage

To start the sensor simulation, run the following command:
```
python src/main.py
```

This will initialize the MQTT client and start emulating three sensors that publish temperature data every 20 seconds.

## Dependencies

This project requires the following Python package:
- `paho-mqtt`: For MQTT communication.

You can install it using pip as mentioned in the installation section.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.