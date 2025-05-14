import hashlib
import os
import json

# File to store the hash values
HASH_DB = "file_hashes.json"

def calculate_hash(filepath, algorithm='sha256'):
    """Calculate the hash of a file."""
    hash_func = hashlib.new(algorithm)
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        return None

def load_hashes():
    """Load existing hashes from JSON."""
    if not os.path.exists(HASH_DB):
        return {}
    with open(HASH_DB, 'r') as f:
        return json.load(f)

def save_hashes(hashes):
    """Save hash dictionary to file."""
    with open(HASH_DB, 'w') as f:
        json.dump(hashes, f, indent=4)

def scan_files(file_paths):
    """Scan files and compare hashes."""
    old_hashes = load_hashes()
    new_hashes = {}
    changes = []

    for path in file_paths:
        hash_val = calculate_hash(path)
        if hash_val is None:
            print(f"[ERROR] File not found: {path}")
            continue

        new_hashes[path] = hash_val

        if path not in old_hashes:
            changes.append((path, "NEW"))
        elif old_hashes[path] != hash_val:
            changes.append((path, "MODIFIED"))

    # Check for deleted files
    for path in old_hashes:
        if path not in new_hashes:
            changes.append((path, "DELETED"))

    save_hashes(new_hashes)

    return changes

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Monitor changes in files using hash comparison.")
    parser.add_argument("files", nargs="+", help="Paths to the files to monitor")

    args = parser.parse_args()
    changes_detected = scan_files(args.files)

    if not changes_detected:
        print("✅ No changes detected.")
    else:
        print("⚠️ Changes detected:")
        for path, status in changes_detected:
            print(f"  [{status}] {path}")
