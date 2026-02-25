from handlers.base_handler import BaseHandler
from services.farm_service import FarmService

class PumpHandler(BaseHandler):
    def update(self, topic: str, payload: str):
        if payload == "ON":
            FarmService.turn_on_pump()
        elif payload == "OFF":
            FarmService.turn_off_pump()