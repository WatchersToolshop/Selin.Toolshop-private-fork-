def simulate_node(memory_state):
    """
    Simulates a recursion node's transformation on the memory state.
    For now, it applies a basic transform for testing.
    """
    return {
        "input_summary": str(memory_state),
        "transformed_signal": hash(json.dumps(memory_state, sort_keys=True)),
        "confidence": 0.87
    }