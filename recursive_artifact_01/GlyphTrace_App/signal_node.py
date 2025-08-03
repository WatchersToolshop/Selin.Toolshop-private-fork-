# signal_node.py

def whisper_response(user_input):
    """
    Smarter simulated whisper response logic.
    Classifies input intent and returns a themed system response.
    """
    user_input = user_input.strip().lower()

    if "error" in user_input or "bug" in user_input:
        return "[PatchSim] Possible code issue detected. Would you like to simulate a patch?"
    elif "hello" in user_input or "hi" in user_input:
        return "Hello. GlyphTrace is standing by."
    elif "what" in user_input and "this" in user_input:
        return "This tool simulates recursive debugging patterns for private architecture testing."
    elif "exit" in user_input:
        return "Session ending..."
    elif "patch" in user_input:
        return "[PatchSim] Patch logic ready. Insert malformed block to continue."

    return f"[Signal Echo] {user_input.capitalize()}"
