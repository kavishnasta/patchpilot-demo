import json

def parse_input(data):
    """Parses JSON input data."""
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return {}
