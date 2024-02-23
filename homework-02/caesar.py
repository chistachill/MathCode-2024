import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for l in plaintext:
        if l.isupper():
            l_code = ord(l)
            l_index = ord(l) - ord("A")
            new_index = (l_index + shift) % 26
            new_letter = chr(new_index + ord("A"))
            ciphertext += new_letter
        elif l.islower():
            l_index = ord(l) - ord('a')
            ciphertext += chr((l_index + shift) % 26 + ord('a'))
        else:
            ciphertext += l
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for l in ciphertext:
        if l.isupper():
            l_code = ord(l)
            l_index = ord(l) - ord("A")
            new_index = (l_index - shift) % 26
            new_code = new_index + ord("A")
            new_letter = chr(new_code)
            plaintext += new_letter
        elif l.islower():
            l_index = ord(l) - ord('a')
            l_index = (l_index - shift) % 26 + ord('a')
            l_code = chr(l_index)
            plaintext += l_code
        else:
            plaintext += l
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift