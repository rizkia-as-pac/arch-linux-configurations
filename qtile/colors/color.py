import re
import json

def extract_color_codes(file_path):
    with open(file_path, "r") as file:
        sequence = file.read()

    # Use regex to directly extract color codes with "#"
    color_matches = re.findall(r'#(\w{6})', sequence)

    # Prepend "#" to each color code in the same list comprehension
    result = {f"c_{i}": f"#{color}" for i, color in enumerate(color_matches)}
    
    return result

def cs_from_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data