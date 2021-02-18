import logging

import requests

logger = logging.getLogger(__name__)


def get_random_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        response.raise_for_status()
        data = response.json()
        return f"{data['setup']} {data['punchline']}"
    except Exception as e:
        logger.exception("Something wrong.", exc_info=e)
        return "Unavailable at moment."
