from typing import Optional

from handlers.base_handler import BaseHandler
from services.automation_service import TemperatureAutomationService
from utils.logger import get_logger

logger = get_logger(__name__)

class TemperatureHandler(BaseHandler):
    def __init__(self, automation_service: Optional[TemperatureAutomationService] = None):
        self.automation_service = automation_service or TemperatureAutomationService()

    def update(self, topic: str, payload: str):
        try:
            temp = float(payload)
        except (TypeError, ValueError):
            logger.warning(f"[TEMPERATURE] Invalid payload: {payload}")
            return

        logger.info(f"[TEMPERATURE] Current temperature: {temp}°C")
        self.automation_service.process_temperature(temp)