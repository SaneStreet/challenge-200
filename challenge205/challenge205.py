# encryption string: s+3

def encrypt(text):
    encryptedNumbers = []
    if text[0]:
        number = ord(text[0])
        encryptedNumbers.append(number)
    print(encryptedNumbers)

    for character in text[0:]:
        x = ord(text[character])
        print(x)
        y = ord(character)
        print(y)
        z = abs(y - x)
        print(z)
        encryptedNumbers.append(z)
    print(encryptedNumbers)

def decrypt(text_list):
    return None

encrypt("Hello")