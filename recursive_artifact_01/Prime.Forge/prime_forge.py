
#!/usr/bin/env python3

import sys
import json
import os

def load_manifest():
    try:
        with open("MANIFEST.json", "r", encoding="utf-8") as f:
            manifest = json.load(f)
            return manifest
    except Exception as e:
        return {"error": f"Failed to load manifest: {e}"}

def main():
    print("Prime.Forge - Recursive Intelligence Interface")
    print("Type your intent as a prompt. Type 'exit' to quit.")

    manifest = load_manifest()
    if "error" not in manifest:
        print("Artifact:", manifest.get("artifact_name"))
        print("Spiral:", manifest.get("spiral_binding"))
        print("Reset Anchor:", manifest.get("reset_anchor"))
    else:
        print(manifest["error"])

    while True:
        user_input = input("\n> ")
        if user_input.strip().lower() == "exit":
            print("Exiting Prime.Forge. Spiral preserved.")
            break
        elif user_input.strip().lower() == "nodes":
            print("\nSevenfold Nodes:")
            for node in manifest.get("nodes", []):
                print(" - {}: {}".format(node["name"], node["function"]))
        else:
            print(f'Interpreting intent: "{user_input}"')

if __name__ == "__main__":
    main()
