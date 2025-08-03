import json
import os
from datetime import datetime

# Paths
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
SUMMARY_PATH = os.path.join(BASE_PATH, "release_artifact", "patch_summary.md")
STATE_PATH = os.path.join(BASE_PATH, "memory", "debug_state.json")
TRACE_PATH = os.path.join(BASE_PATH, "memory", "recursive_trace.json")

def get_timestamp():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

def [REDACTED]_log_patch(patch_id, reasoning, module, previous_code, new_code, glyph="🜄", author="[REDACTED]"):
    timestamp = get_timestamp()

    # --- Update patch_summary.md ---
    summary_entry = f"""\n## Patch ID: {patch_id}
**Author**: {author}  
**Timestamp**: {timestamp}  
**Module**: {module}  
**Purpose**: {reasoning.split('.')[0]}  
**Reasoning**: {reasoning}  
**Signal Drift**: None detected  
**Glyph Anchor**: {glyph}  
"""
    with open(SUMMARY_PATH, "a") as f:
        f.write(summary_entry)

    # --- Update debug_state.json ---
    debug_state = {
        "last_patch": {
            "id": patch_id,
            "timestamp": timestamp,
            "module": module,
            "purpose": reasoning.split('.')[0],
            "author": author,
            "glyph": glyph,
            "signal_trace": "stable"
        }
    }
    with open(STATE_PATH, "w") as f:
        json.dump(debug_state, f, indent=2)

    # --- Append to recursive_trace.json ---
    if os.path.exists(TRACE_PATH):
        with open(TRACE_PATH, "r") as f:
            trace_log = json.load(f)
    else:
        trace_log = []

    trace_log.append({
        "patch_id": patch_id,
        "timestamp": timestamp,
        "reasoning": reasoning,
        "anchor": glyph,
        "module": module,
        "previous_code": previous_code,
        "new_code": new_code
    })

    with open(TRACE_PATH, "w") as f:
        json.dump(trace_log, f, indent=2)
