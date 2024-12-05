import requests
import os
from dotenv import load_dotenv
from peerbots_types import PeerbotsMessage

load_dotenv()


url = "https://api.peerbots.org/v1"
api_key = os.getenv("PEERBOTS_API_KEY")

headers = {"Accept": "application/json", "X-API-KEY": api_key}


def send_message(username: str, message: PeerbotsMessage):
    """Send a message to a username

    Args:
        username (str): _description_
        message (PeerbotsMessage): _description_
    """
    req = requests.post(f"{url}/send-message/{username}", headers=headers, json=message)
    print(req.json())


if __name__ == "__main__":
    main_message: PeerbotsMessage = {
        "title": "Hello",
        "speech": "Hello through the API!",
        "color": "Light Blue",
        "emotion": "Happy",
    }
    send_message("GuestUsername", main_message)
