from gateway.gateway import PythonGateway
from handlers.temperature_handler import TemperatureHandler
from handlers.pump_handler import PumpHandler
from mqtt.topics import Topics

def main():
    pygateway = PythonGateway()

    # Register handlers
    pygateway.register_handler(Topics.TEMPERATURE, TemperatureHandler())
    pygateway.register_handler(Topics.PUMP, PumpHandler())

    # Subscribe the feeds
    pygateway.subscribe(Topics.TEMPERATURE)
    pygateway.subscribe(Topics.PUMP)

    # Start the MQTT client hehe
    pygateway.start_client()

if __name__ == "__main__":
    main()