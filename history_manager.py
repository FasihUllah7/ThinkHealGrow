import json
from datetime import datetime
import os

def save_history(history, filename="chat_history.json"):
    timestamp = datetime.now().isoformat()
    chat_record = {"timestamp": timestamp, "history": history}

    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(chat_record)

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def load_history(filename="chat_history.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []
