from gateway.gateway import PythonGateway
from handlers.temperature_handler import TemperatureHandler
from handlers.pump_handler import PumpHandler
from mqtt.topics import Topics
from services.automation_service import TemperatureAutomationService

def main():
    pygateway = PythonGateway()
    automation_service = TemperatureAutomationService(mqtt_client=pygateway.mqtt_ins)

    # Register handlers
    pygateway.register_handler(Topics.TEMPERATURE, TemperatureHandler(automation_service))
    pygateway.register_handler(Topics.PUMP, PumpHandler())

    # Subscribe the feeds
    pygateway.subscribe(Topics.TEMPERATURE)
    pygateway.subscribe(Topics.PUMP)

    # Start the MQTT client hehe
    pygateway.start_client()

if __name__ == "__main__":
    main()
