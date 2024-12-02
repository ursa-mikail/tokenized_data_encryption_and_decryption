# Tokenized Data Encryption and Decryption Script

## Overview
Generates random hex data, encrypts it using AES-256-CBC encryption with a specified key and iterations, and saves the encrypted data into files. It supports multiple label formats for storing the encrypted data, including the `key=value` format. The script reads the files, extracts the encrypted tokens, decrypts them, and compares the decrypted data to ensure correctness.

## Functions
- **generate_random_hex()**: Generates random hexadecimal data of a specified length.
- **encrypt_data()**: Encrypts the given data using AES-256-CBC encryption and outputs the encrypted data.
- **decrypt_data()**: Decrypts the encrypted data using AES-256-CBC and checks if it matches the original data.
- **create_sample_files()**: Creates files containing encrypted data between labels.
- **process_and_compare_files()**: Extracts encrypted tokens from files, decrypts them, and compares them to original data.

## Labels Explained
The labels that enclose the encrypted tokens in the files can vary based on the format. Here's how different variations affect the extraction:

### 1. **With Square Brackets (`[]`)**: 
This is the default format used in this script. The labels are defined as:
- **Start label**: `[tag_x_start]`
- **End label**: `[tag_x_end]`

Using square brackets is common in many scenarios as they clearly mark the boundaries of tags in data. These brackets are part of the regular expression used to extract the encrypted tokens. When using this format, it is easy to clearly demarcate the start and end of the encrypted data, ensuring proper extraction and validation.

Example:
```plaintext
[tag_x_start] U2FsdGVkX1+hs1234... [tag_x_end]


2. With Angle Brackets (<>):
This variant uses angle brackets (<, >) instead of square brackets to enclose the tags. This format can still be handled by adjusting the regular expression pattern to account for the different delimiters.

Example:

plaintext

<tag_x_start> U2FsdGVkX1+hs1234... <tag_x_end>
3. Key-Value Format (key=value):
In this format, the encrypted data is stored as a key-value pair, where the key is a descriptor (e.g., ciphered) and the value is the encrypted token. This format is simpler and more human-readable, but requires a different method of extraction.

Example:

plaintext
Copy code
ciphered=U2FsdGVkX1+hs1234...
4. Canonized with Square Brackets ([]):
This format is the same as the first, where the encrypted data is consistently enclosed within square brackets. Canonized labels (standardized or fixed) ensure consistency across different files and implementations, reducing the risk of parsing errors.

Example:

plaintext

[tag_x_start] U2FsdGVkX1+hs1234... [tag_x_end]
Differences Between Formats
Parsing Differences: Square brackets are often the most common format used for data labeling. If using different delimiters (such as angle brackets or key-value pairs), the regular expression should be adjusted to match these new boundaries.
Key-Value Pairing: The key=value format is a simple and clean way to label the encrypted data, but parsing may require searching for the specific key (e.g., ciphered) rather than just using start and end labels.
Reliability: Canonized labels (i.e., consistently using the same tag format) help prevent errors that may arise from inconsistent tagging across files.
Regex Compatibility: If the format changes (e.g., from [] to <> or key=value), the extraction process needs to account for those changes in the regular expression. The script uses a customizable regex pattern that can handle different tag formats.

## 
# Data Encryption and Decryption Script

## Overview
This script generates random hex data, encrypts it using AES-256-CBC encryption with a specified key and iterations, and saves the encrypted data into files. It supports multiple label formats for storing the encrypted data, including the `key=value` format. The script reads the files, extracts the encrypted tokens, decrypts them, and compares the decrypted data to ensure correctness.

## Functions
- **generate_random_hex()**: Generates random hexadecimal data of a specified length.
- **encrypt_data()**: Encrypts the given data using AES-256-CBC encryption and outputs the encrypted data.
- **decrypt_data()**: Decrypts the encrypted data using AES-256-CBC and checks if it matches the original data.
- **create_sample_files()**: Creates files containing encrypted data between labels.
- **process_and_compare_files()**: Extracts encrypted tokens from files, decrypts them, and compares them to original data.

## Labels Explained
The labels that enclose the encrypted tokens in the files can vary based on the format. Here's how different variations affect the extraction:

### 1. **With Square Brackets (`[]`)**: 
This is the default format used in this script. The labels are defined as:
- **Start label**: `[tag_x_start]`
- **End label**: `[tag_x_end]`

Using square brackets is common in many scenarios as they clearly mark the boundaries of tags in data. These brackets are part of the regular expression used to extract the encrypted tokens. When using this format, it is easy to clearly demarcate the start and end of the encrypted data, ensuring proper extraction and validation.

Example:
```plaintext
[tag_x_start] U2FsdGVkX1+hs1234... [tag_x_end]

### 2. With Angle Brackets (<>):
This variant uses angle brackets (<, >) instead of square brackets to enclose the tags. This format can still be handled by adjusting the regular expression pattern to account for the different delimiters.

Example:

```plaintext

<tag_x_start> U2FsdGVkX1+hs1234... <tag_x_end>

### 3. Key-Value Format (key=value):
In this format, the encrypted data is stored as a key-value pair, where the key is a descriptor (e.g., ciphered) and the value is the encrypted token. This format is simpler and more human-readable, but requires a different method of extraction.

Example:

```plaintext

ciphered=U2FsdGVkX1+hs1234...

### 4. Canonized with Square Brackets ([]):
This format is the same as the first, where the encrypted data is consistently enclosed within square brackets. Canonized labels (standardized or fixed) ensure consistency across different files and implementations, reducing the risk of parsing errors.

Example:

```plaintext

[tag_x_start] U2FsdGVkX1+hs1234... [tag_x_end]

## Differences Between Formats
Parsing Differences: Square brackets are often the most common format used for data labeling. If using different delimiters (such as angle brackets or key-value pairs), the regular expression should be adjusted to match these new boundaries.
Key-Value Pairing: The key=value format is a simple and clean way to label the encrypted data, but parsing may require searching for the specific key (e.g., ciphered) rather than just using start and end labels.
Reliability: Canonized labels (i.e., consistently using the same tag format) help prevent errors that may arise from inconsistent tagging across files.
Regex Compatibility: If the format changes (e.g., from [] to <> or key=value), the extraction process needs to account for those changes in the regular expression. The script uses a customizable regex pattern that can handle different tag formats.

Output:
Files are created in the ./sample_data/ directory.

Encrypted tokens are saved between the start and end labels or as key-value pairs.
Each file is processed to ensure the data is decrypted correctly.

## Notes
The script assumes that the encrypted data is properly formatted between the start and end labels or as key-value pairs. Ensure that the labels are consistently used in the files to avoid errors during parsing.

### Summary of Differences:
- **With `[]`**: Square brackets are used for clear, standardized labeling, ensuring reliable extraction and consistency across the files.
- **With `<>`**: Angle brackets are used as delimiters instead of square brackets. To handle this, the regular expression needs to be modified accordingly.
- **With `key=value`**: This format uses a key-value pair (e.g., `ciphered=...`) to store the encrypted data. This is simpler and more readable but requires different handling during extraction.
- **Canonized Labels (`[]`)**: Using consistent labels throughout your files helps ensure that data extraction and decryption are performed smoothly without errors.

This README explains how the script works with different label formats, including `key=value`, and guides users on using the script effectively while considering the differences in label formats.
