import json
import os

TRACE_PATH = os.path.join(os.path.dirname(__file__), "memory", "recursive_trace.json")

def load_trace():
    if not os.path.exists(TRACE_PATH):
        print("No trace log found.")
        return []

    with open(TRACE_PATH, "r") as f:
        return json.load(f)

def display_patch(patch):
    print(f"\n--- Patch ID: {patch['patch_id']} ---")
    print(f"Timestamp: {patch['timestamp']}")
    print(f"Module: {patch['module']}")
    print(f"Glyph: {patch['anchor']}")
    print(f"Reasoning: {patch['reasoning']}")
    print("\nPrevious Code:")
    print(patch['previous_code'])
    print("\nNew Code:")
    print(patch['new_code'])
    print("------------------------------")

def run_interface():
    trace = load_trace()
    if not trace:
        return

    print("\n=== Recursive Patch History ===")
    for i, patch in enumerate(trace):
        print(f"[{i}] {patch['patch_id']} — {patch['timestamp']} — {patch['module']}")

    try:
        choice = int(input("\nSelect a patch to view (index): "))
        if 0 <= choice < len(trace):
            display_patch(trace[choice])
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    run_interface()
