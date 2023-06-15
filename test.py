import requests
import structlog

logger = structlog.getLogger(__name__)

response = requests.get('https://example.com/')

logger.info('asdasd', status_code=response.status_code)
