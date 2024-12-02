import subprocess
import re
import requests

# Define the URL and the regular expression to extract the encrypted token
url = "https://raw.githubusercontent.com/ursa-mikail/toolings/refs/heads/main/python/git/git_frequency_monitoring.ipynb"
pattern = re.compile(r'ciphered: ([A-Za-z0-9+/=]+)')

""" # if the pattern is between tags: [tag_x_start] and [tag_x_end]. Note the labels are within `[]`
label_tag_start = 'tag_x_start'
label_tag_end = 'tag_x_end'

pattern = re.compile(rf'\[{label_tag_start}\](.+?)\[{label_tag_end}\]')
"""
# Read the content from the URL
response = requests.get(url)
content = response.text

# Extract the encrypted token
match = pattern.search(content)
if match:
    encrypted_token = match.group(1)  # .strip()
    print("Encrypted Token:", encrypted_token)
else:
    print("Encrypted token not found in the file.")
    exit(1)

# Define the number of cipher nonce rounds and the decryption key
number_of_cipher_nonce_rounds = 100  # Replace with the actual number of rounds
decryption_key = "<key>"  # Replace with actual decryption key

# Decrypt the token using OpenSSL
try:
    # Create the shell command. Note: the cipher used may differ. 
    command = f'echo "{encrypted_token}" | openssl enc -aes-256-cbc -pbkdf2 -iter {number_of_cipher_nonce_rounds} -d -a -k "{decryption_key}"'
    
    # Run the command using subprocess
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("Error during decryption:", result.stderr)
    else:
        print("Decrypted Token:", result.stdout.strip())
except Exception as e:
    print("Exception during decryption:", str(e))


"""
Encrypted Token: U2FsdGVkX1+7TtLL8EZXcO+sDvRQ830mnmRH+1bPozCC3DDFIc4hyk/kAlvk6OBrlMhC6s/DVrAJypjnA/6zdQ==
Decrypted Token: <decrypted>
"""