import os
import subprocess
import random
import string
import re

label_tag_start = '[tag_x_start]'
label_tag_end = '[tag_x_end]'

label_tag_start = '<tag_x_start>'
label_tag_end = '<tag_x_end>'


def generate_random_hex(length=32):
    return ''.join(random.choices(string.hexdigits.lower(), k=length))

def encrypt_data(hex_data, key, iterations):
    command = f'echo "{hex_data}" | openssl enc -aes-256-cbc -pbkdf2 -iter {iterations} -a -k "{key}" | tr -d "\n"'
    print(f"Encrypting data: {hex_data}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Encryption failed: {result.stderr}")
    encrypted_data = result.stdout.strip()
    print(f"Encrypted data: {encrypted_data}")
    return encrypted_data

def decrypt_data(encrypted_data, key, iterations):
    # Clean the encrypted data to avoid leading/trailing spaces/newlines
    encrypted_data = encrypted_data.strip()
    
    # Ensure that data is correctly quoted for passing into subprocess
    command = f'echo "{encrypted_data}" | openssl enc -aes-256-cbc -pbkdf2 -iter {iterations} -d -a -k "{key}"'
    print(f"Decrypting data: {encrypted_data}")
    
    # Run the decryption command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise Exception(f"Decryption failed: {result.stderr}")
    
    decrypted_data = result.stdout.strip()
    print(f"Decrypted data: {decrypted_data}")
    return decrypted_data


def create_sample_files(directory, num_files, key, iterations):
    os.makedirs(directory, exist_ok=True)
    file_names_and_plaintext_hex = []

    for i in range(num_files):
        file_name = f"file_{i:02}.txt"
        file_path = os.path.join(directory, file_name)
        original_hex = generate_random_hex()
        encrypted_data = encrypt_data(original_hex, key, iterations)
        with open(file_path, "w") as file:
            file.write(f"{label_tag_start} {encrypted_data} {label_tag_end}")
        file_names_and_plaintext_hex.append((file_path, original_hex))
        print(f"Created file: {file_path} with original hex: {original_hex}")
    
    return file_names_and_plaintext_hex

def process_and_compare_files(file_names_and_plaintext_hex, key, iterations):
    pattern = re.compile(rf'{re.escape(label_tag_start)}\s*(.*?)\s*{re.escape(label_tag_end)}', re.DOTALL)
    for file_path, original_hex in file_names_and_plaintext_hex:
        with open(file_path, "r") as file:
            content = file.read()
        
        print(f"File content:\n{content}")  # Debug: print the whole content to see what's inside
        
        match = pattern.search(content)
        if match:
            encrypted_token = match.group(1).strip()  # strip any leading/trailing spaces
            print(f"Extracted encrypted token: {encrypted_token}")
            decrypted_token = decrypt_data(encrypted_token, key, iterations)
            if decrypted_token == original_hex:
                print(f"{file_path}: Decryption successful and matches original data.")
            else:
                print(f"{file_path}: Decryption does not match original data. Expected: {original_hex}, Got: {decrypted_token}")
        else:
            print(f"{file_path}: Encrypted token not found.")


if __name__ == "__main__":
    directory = "./sample_data"
    num_files = 11
    key = "your_decryption_key"  # Replace with your actual decryption key
    iterations = 10000  # Replace with the actual number of rounds

    # Create sample files
    file_paths = create_sample_files(directory, num_files, key, iterations)

    # Process and compare files
    process_and_compare_files(file_paths, key, iterations)

"""
Encrypting data: ae9cb6deedaa6979947addbcb1ff9198
Encrypted data: U2FsdGVkX1/E6fGKekdc93B64rfN0oWz+Qb6MmUIz97rKdPb2seLItVOPp5ic6zOghvnOOrbwoXV+lZGYSV8YA==
Created file: ./sample_data/file_00.txt with original hex: ae9cb6deedaa6979947addbcb1ff9198
:
File content:
<tag_x_start> U2FsdGVkX1/E6fGKekdc93B64rfN0oWz+Qb6MmUIz97rKdPb2seLItVOPp5ic6zOghvnOOrbwoXV+lZGYSV8YA== <tag_x_end>
Extracted encrypted token: U2FsdGVkX1/E6fGKekdc93B64rfN0oWz+Qb6MmUIz97rKdPb2seLItVOPp5ic6zOghvnOOrbwoXV+lZGYSV8YA==
Decrypting data: U2FsdGVkX1/E6fGKekdc93B64rfN0oWz+Qb6MmUIz97rKdPb2seLItVOPp5ic6zOghvnOOrbwoXV+lZGYSV8YA==
Decrypted data: ae9cb6deedaa6979947addbcb1ff9198
./sample_data/file_00.txt: Decryption successful and matches original data.
:

"""