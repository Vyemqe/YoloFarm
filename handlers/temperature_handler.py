from handlers.base_handler import BaseHandler
from utils.logger import get_logger

logger = get_logger(__name__)

class TemperatureHandler(BaseHandler):
    def update(self, topic: str, payload: str):
        temp = float(payload)
        logger.info(f"[TEMPERATURE] Current temperature: {temp}°C")
        # Sample temperature control
        if temp > 37:
            logger.warning(f"[ALERT] I'm having a fever!!")