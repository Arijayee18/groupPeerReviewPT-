# Junee Omana
# CSCI128 - Section J
# Assessment 9
# References: no one
# Time: 2 hours

import string

def encrypt(message, shift):
    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    char_list = []
    shift = shift % 26
    if shift < 0:
        shift += 26
    for char in message:
        if char in uppercase:
            shifted = uppercase.index(char) + shift
            if shifted > 25:
                shifted = shifted - 26
            if shifted < 0:
                shifted = shifted + 26
            char_list.append(uppercase[shifted])
        elif char in lowercase:
            shifted = lowercase.index(char) + shift
            if shifted > 25:
                shifted = shifted - 26
            if shifted < 0:
                shifted = shifted + 26
            char_list.append(lowercase[shifted])
        else:
            char_list.append(char)
    char_list = ''.join(char_list)
    return char_list

def decrypt(message, keyword):
    for i in range(0, 26):
        char_list = encrypt(message, -i)
        if keyword in char_list:
            return [char_list, i]
        if i == 25:
            return "ERROR"
        
def test_encrypt(word, shift, expected):
    assert encrypt(word, shift) == expected

def test_decrypt(word, keyword, expected_word, expected_shift):
    assert decrypt(word, keyword) == [expected_word, expected_shift]


if __name__ == "__main__":
    choice = input("OPTION>")
    if choice == "1":
        x = input("MESSAGE>")
        y = int(input("SHIFT>"))
        result = encrypt(x, y)
        print(f'OUTPUT {result}')
    if choice == "2":
        x = input("MESSAGE>")
        y = input("KEY>")
        message_shift = decrypt(x, y)
        if message_shift == "ERROR":
            print("OUTPUT ERROR")
        else:
            print(f'OUTPUT {message_shift[0]}')
            print(f'OUTPUT {message_shift[1]}')
    if choice == "3":
        test_encrypt("mmmm raising canes", 13, "zzzz envfvat pnarf")
        test_encrypt("&%*#%$", 25, "&%*#%$")
        test_encrypt("love shrek***", 17, "cfmv jyivb***")
        test_decrypt("Qefveq 4iziv!", "Mabram", "Mabram 4ever!", 4)
        test_decrypt("ahrl fvby aptl...", "time", "take your time...", 7)
        test_decrypt("Nvfivfyt nodifn", "stinks", "Saknakdy stinks", 21)