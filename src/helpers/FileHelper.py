__package__ = "helpers"

import jsonpickle
import random
import string

def check_file(file_path: str, code: str) -> bool:
    full_path = file_path + code + ".json"
    try:
        with open(full_path, 'r') as file:
            return True
    except FileNotFoundError:
        return False
    
def get_file(file_path: str, code: str) -> dict:
    full_path = file_path + code + ".json"
    try:
        with open(full_path, 'r') as file:
            return jsonpickle.decode(file.read())
    except FileNotFoundError:
        return None
    
def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))