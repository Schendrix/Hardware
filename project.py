def caesar_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def encrypt_file(input_file, key_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    with open(key_file, 'r') as key_file:
        key = int(key_file.read())

    encrypted_text = caesar_cipher(text, key)

    with open(output_file, 'w') as file:
        file.write(encrypted_text)

encrypt_file('input.txt', 'key.txt', 'output.txt')