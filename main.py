import json
import os
from hash_utils import calculate_file_hash, get_all_files

HASH_RECORD_FILE = 'hash_records.json'
TARGET_DIRECTORY = 'files_to_monitor'  # <-- Create this folder too

def load_hash_records():
    if os.path.exists(HASH_RECORD_FILE):
        with open(HASH_RECORD_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_hash_records(records):
    with open(HASH_RECORD_FILE, 'w') as f:
        json.dump(records, f, indent=4)

def create_baseline(directory):
    print("[*] Creating baseline...")
    files = get_all_files(directory)
    records = {}
    for file in files:
        hash_value = calculate_file_hash(file)
        records[file] = hash_value
    save_hash_records(records)
    print("[+] Baseline saved.")

def check_integrity(directory):
    print("[*] Checking file integrity...")
    old_records = load_hash_records()
    current_files = get_all_files(directory)
    current_hashes = {file: calculate_file_hash(file) for file in current_files}

    for file, current_hash in current_hashes.items():
        old_hash = old_records.get(file)
        if not old_hash:
            print(f"[NEW FILE] {file}")
        elif old_hash != current_hash:
            print(f"[MODIFIED] {file}")
    
    for file in old_records:
        if file not in current_hashes:
            print(f"[DELETED] {file}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: python main.py [baseline|check]")
        exit(1)

    command = sys.argv[1].lower()
    os.makedirs(TARGET_DIRECTORY, exist_ok=True)

    if command == 'baseline':
        create_baseline(TARGET_DIRECTORY)
    elif command == 'check':
        check_integrity(TARGET_DIRECTORY)
    else:
        print("Unknown command. Use 'baseline' or 'check'.")