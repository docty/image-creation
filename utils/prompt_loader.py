import json

def load_prompts(filepath='utils/prompt_options.json'):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading prompts: {e}")
        return {}

