#Lab_9
from ppp_decode import decode
def encode(password):
    encode_password = ''
    for char in password:
        char = int(char)
        char += 3
        char = str(char)
        encode_password += char
    return encode_password

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
    print()


if __name__ == '__main__':
    while True:
        menu()

        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)

            print("Your password has been encoded and stored!")
            print()

        if option == 2:
            print(
                f'The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.')
            print()

        if option == 3:
            exit()