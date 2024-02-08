import hashlib
import os

def create_test_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def calculate_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def compare_hashes(hash1, hash2):
    return hash1 == hash2

# Example usage
if __name__ == "__main__":
    # Create test files
    create_test_file('test_file1.txt', 'Hello, this is test file 1 content.')
    create_test_file('test_file2.txt', 'Different content for test file 2.')

    # Calculate hashes
    hash1 = calculate_file_hash('test_file1.txt')
    hash2 = calculate_file_hash('test_file2.txt')

    # Compare hashes
    if compare_hashes(hash1, hash2):
        print("File hashes match.")
    else:
        print("File hashes do not match.")
