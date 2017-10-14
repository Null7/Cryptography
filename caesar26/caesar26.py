
def encrypt(key, plaintext):
    ''' encrypts the plaintext with a key
    based on the caesar cipher algorithm
    and return the ciphertext
    (string, string) -> string
    REQ: key matches [0-9]*
    REQ: plaintext matches [a-z]*
    '''
    encrypted = ''
    for i in plaintext:
        encrypted +=  encrypt_help(key, i)
    return encrypted

def decrypt(key, ciphertext):
    decrypted = ''
    for i in ciphertext:
        decrypted +=  decrypt_help(key, i)
    return decrypted

def encrypt_help(key, plaintext):
    if(plaintext == ''):
        return ''
    if((ord(plaintext) - 96 + int(key)) % 26 == 0):
        return "z"
    ciphertext = chr((ord(plaintext) - 96 + int(key)) % 26 + 96)
    return ciphertext

 
def decrypt_help(key, ciphertext):
    ''' decrypts the ciphertext with a key
    based on the caesar cipher algorithm
    and returns the plaintext
    (string, string) -> string
    REQ: key matches [0-9]*
    REQ: ciphertext matches [a-z]*
    ''' 
    if(ciphertext == ''):
        return ''
    if((ord(ciphertext) - 96 - int(key)) % 26 == 0):
        return "z"
    plaintext = chr((ord(ciphertext) - 96 - int(key)) % 26 + 96)
    return plaintext
