import time
import random

_current_power = 350.0
_history = []

def get_current_consumption():
    global _current_power, _history
    # Power dəyərini simulyasiya edirik
    _current_power += random.uniform(-10, 10)
    if _current_power < 0:
        _current_power = 0

    timestamp = time.time()
    _history.append({"timestamp": timestamp, "power": round(_current_power, 2)})

    # Yalnız son 24 saatlıq məlumatı saxlayırıq
    cutoff = timestamp - 86400
    _history = [entry for entry in _history if entry["timestamp"] >= cutoff]

    return round(_current_power, 2)

def get_consumption_history():
    return _history
