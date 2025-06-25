import json 
import os
import string
import random

DATA_FILE = 'data.json'

#Load existing mappings 
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    
    return {}

# Save mappings
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Generate random short code
def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Shorten a URL
def shorten(url, data):
    for code, original in data.items():
        if original == url:
            return code
    code = generate_code()
    while code in data:
        code = generate_code()
    data[code] = url
    save_data(data)
    return code

# Expand a short code
def expand(code, data):
    return data.get(code, None)