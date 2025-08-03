def extract_glyph(node_response):
    """
    Extracts a glyph from the node response.
    This is symbolic for the signal transformation logic.
    """
    glyph = f"glyph::{abs(node_response['transformed_signal']) % 100000}"
    return glyph
