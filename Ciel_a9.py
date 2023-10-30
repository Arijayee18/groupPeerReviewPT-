'''
Names: Ciel, Junee, Ari'Jaye Derritt
'''
def encrypt(message, shift):  # define the enccrypt function.
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(message, keyword):  # define the decrpyt function

    for shift in range(26):
        decrypted_message = encrypt(message, -shift)
        # for char in message:
        #     is_upper = char.isupper()
        #     if char.isalpha():
        #         shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
        #         if is_upper:
        #             shifted_char = shifted_char.upper()
        #         decrypted_message += shifted_char
        #     else:
        #         decrypted_message += char

        if keyword in decrypted_message:
            return [decrypted_message, shift]

    return "ERROR"


def test_encrypt(word, shift, expected):  # define the test case for the encryption
    result = encrypt(word, shift)
    assert result == expected


def test_decrypt(message, keyword, expected_word, expected_shift):  # define the test case for the decrypt function
    result = decrypt(message, keyword)

    if result == "ERROR":
        assert result == expected_word
    else:
        decrypted_message, shift = result
        assert decrypted_message == expected_word
        assert shift == expected_shift


# put the whole thing together in the "menu" for the user to select from.


if __name__ == '__main__':
    option = int(input("OPTION> "))

    if option == 1:  # option 1 is just to encrypt the message based on how many shifts are given
        message = input("MESSAGE> ")
        shift = int(input("SHIFT> "))
        encrypted_message = encrypt(message, shift)
        print(f"OUTPUT {encrypted_message}")
    elif option == 2:  # option 2 is to decrypt the message
        message = input("MESSAGE> ")
        keyword = input("KEY> ")
        result = decrypt(message, keyword)
        if result == "ERROR":
            print("OUTPUT ERROR")
        else:
            decrypted_message, shift = result
            print(f"OUTPUT {decrypted_message}")
            print("OUTPUT " + str(shift))
    elif option == 3:  # option 3 tests everything
        test_encrypt("My secret message", 10, "Wi combod wocckqo")
        test_encrypt("N0t numb3r5", 7, "U0a ubti3y5")
        test_encrypt("Large negative shift", -82, "Hwnca jacwpera odebp")

        test_decrypt("Ger csy vieh xlmw?", "read", "Can you read this?", 4)
        test_decrypt("Ujqhlgyjshzq ak fwsl!", "is", "Cryptography is neat!", 18)
        test_decrypt("Ujqhlgyjshzq ak fwsl!", "message", "ERROR", 0)
