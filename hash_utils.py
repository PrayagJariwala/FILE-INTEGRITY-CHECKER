import hashlib
import os

def calculate_file_hash(filepath, algo='sha256'):
    hash_func = hashlib.new(algo)
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def get_all_files(directory):
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_list.append(filepath)
    return file_list