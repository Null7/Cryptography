import base64

from Crypto.Cipher import XOR


def encrypt(key, plaintext):
    ''' encrypts the plaintext (utf-8) with a key
    based on the xor cipher algorithm
    and return the ciphertext (base64 encoded)
    (string, string) -> string
    '''
    key = bytes(key, 'utf-8')
    plaintext = bytes(plaintext, 'utf-8')
    xor = XOR.new(key)
    return base64.b64encode(xor.encrypt(plaintext)).decode('UTF-8')


def decrypt(key, ciphertext):
    ''' decrypts the ciphertext (base64 encoded) with a key
    based on the xor cipher algorithm
    and returns the plaintext (utf-8)
    (string, string) -> string
    '''    
    key = bytes(key, 'utf-8')
    ciphertext = base64.b64decode(ciphertext)
    xor = XOR.new(key)
    return xor.decrypt(ciphertext).decode('UTF-8')
