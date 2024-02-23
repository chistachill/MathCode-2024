def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isupper():
            b = i % (len(keyword))
            l_index = ord(plaintext[i]) - ord("A")
            new_index = (l_index + (ord(keyword[b]) - ord("A"))) % 26
            new_code = new_index + ord("A")
            new_letter = chr(new_code)
            ciphertext += new_letter
        elif plaintext[i].islower():
            b = i % (len(keyword))
            l_index = ord(plaintext[i]) - ord("a")
            new_index = (l_index + (ord(keyword[b])) - ord("a")) % 26
            new_code = new_index + ord("a")
            new_letter = chr(new_code)
            ciphertext += new_letter
        elif plaintext[i].isdigit():
            l_code = (int(l) + (ord(keyword[b]) - ord("a"))) % 10
            cithertext += str(l_code)
        else: ciphertext = ciphertext + plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isupper():
            b = i % (len(keyword))
            l_index = ord(ciphertext[i]) - ord("A")
            new_index = (l_index - (ord(keyword[b]) - ord("A"))) % 26
            new_code = new_index + ord("A")
            new_letter = chr(new_code)
            plaintext += new_letter
        elif ciphertext[i].islower():
            b = i % (len(keyword))
            l_index = ord(ciphertext[i]) - ord("a")
            new_index = (l_index - (ord(keyword[b]) - ord("a"))) % 26
            new_code = new_index + ord("a")
            new_letter = chr(new_code)
            plaintext += new_letter
        elif ciphertext[i].isdigit():
            l_code = (int(l) - (ord(keyword[b]) - ord("a"))) % 10
            plaintext += str(l_code)
        else: plaintext = plaintext + ciphertext[i]
    return plaintext