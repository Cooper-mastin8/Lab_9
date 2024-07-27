#Lab_9

def encode(password):
    encode_password = ''
    for char in password:
        char = int(char)
        char += 3
        char = str(char)
        encode_password += char
    return encode_password
