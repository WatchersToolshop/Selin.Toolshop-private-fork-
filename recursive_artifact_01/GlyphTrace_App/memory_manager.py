
import json
from datetime import datetime

MEMORY_LOG_FILE = "memory_log.json"

def load_memory_log():
    try:
        with open(MEMORY_LOG_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_memory_entry(note):
    memory = load_memory_log()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    memory.append({"timestamp": timestamp, "note": note})
    with open(MEMORY_LOG_FILE, "w") as f:
        json.dump(memory, f, indent=2)
    return f"🧠 Memory stored: {note}"

def recall_memory():
    memory = load_memory_log()
    if not memory:
        return "📭 No memory entries found."
    output = ["📖 Recalled Memory Log:"]
    for entry in memory:
        output.append(f"[{entry['timestamp']}] - {entry['note']}")
    return "\n".join(output)
