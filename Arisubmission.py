'''
Ari'Jaye Derritt
Section J
References: TA xander, Casa Tutors 
Time: 4 hours 
'''

def encrypt(message, shift):
    new_message = ""
    
    for letter in message:
        if letter.isalpha():
            shiftNum = shift % 26
            if letter.islower():
                new_letter = chr(((ord(letter)-ord('a') + shiftNum) % 26) + ord('a'))
            else:
                new_letter = chr(((ord(letter)-ord('A') + shiftNum) % 26) + ord('A'))
            new_message += new_letter
        else:
            new_message += letter
    return new_message

def decrypt(text, keyword):
    shift = 0
    textlst = []
    for i in range(26):
        shift = shift + 1 
        newText = encrypt(text ,i)
        if keyword in newText:
            textlst = [newText, (26-i) % 26]
            return textlst
    if keyword not in newText:
        return "ERROR"
        

def test_encrypt(word, shift , expected):
    test = encrypt(word, shift)
    assert expected == test 


def test_decrypt(word, keyword, expected_word, expected_shift):
    test = decrypt(word, keyword)
    if test != "ERROR":
        assert test[0] == (expected_word)
        assert test[1] == expected_shift
    else:
        assert test == "ERROR"
if __name__ == '__main__':
   

    option = int(input("OPTION> "))
    print(encrypt("My secret message", 10))
    if option == 1:
        message = input("MESSAGE> ")
        shift = int(input("SHIFT> "))
        print('OUTPUT',encrypt(message,shift))
    elif option == 2:
        message = input("MESSAGE> ")
        key = input("key> ")
        decrypt1 = decrypt(message,key)
        if decrypt1 != "ERROR":
            print('OUTPUT', decrypt1[0])
            print('OUTPUT', decrypt1[1])
        else:
            print('OUTPUT', decrypt1)
    elif option == 3:
        print(test_encrypt('quizzes', 1 , 'rvjaaft'))
        print(test_decrypt("Ujqhlgyjshzq ak fwsl!", "is",'Cryptography is neat!', 18))
        print(test_decrypt("Ujqhlgyjshzq ak fwsl!", "is",'Cryptography is neat!', 18))
        print(test_decrypt("Ujqhlgyjshzq ak fwsl!", "is",'Cryptography is neat!', 18))
