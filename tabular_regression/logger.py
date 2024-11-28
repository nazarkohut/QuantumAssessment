import logging

# Configure the logger
logging.basicConfig(
    level=logging.INFO,  # Default log level: INFO
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
