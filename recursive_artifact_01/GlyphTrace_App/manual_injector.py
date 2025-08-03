import os
from core.patch_logger import [REDACTED]_log_patch

def simulate_patch_injection():
    print("=== Manual Recursive Patch Injector ===\n")
    patch_id = input("Patch ID: ").strip()
    module = input("Target Module (e.g., patch_engine/patch_one_debugger.py): ").strip()
    reasoning = input("Reasoning for Patch: ").strip()
    glyph = input("Glyph Anchor (e.g., 🜄): ").strip() or "🜄"

    print("\nEnter the PREVIOUS code block:")
    previous_code = []
    print("(End input with a blank line)")
    while True:
        line = input()
        if line.strip() == "":
            break
        previous_code.append(line)
    previous_code = "\n".join(previous_code)

    print("\nEnter the NEW code block:")
    new_code = []
    print("(End input with a blank line)")
    while True:
        line = input()
        if line.strip() == "":
            break
        new_code.append(line)
    new_code = "\n".join(new_code)

    # --- Simulate the patch application ---
    print(f"\n✅ Simulated patch applied to {module}.")

    # --- Log the patch ---
    [REDACTED]_log_patch(
        patch_id=patch_id,
        reasoning=reasoning,
        module=module,
        previous_code=previous_code,
        new_code=new_code,
        glyph=glyph
    )
    print("🧠 Patch logged into recursive trace.")

if __name__ == "__main__":
    simulate_patch_injection()
