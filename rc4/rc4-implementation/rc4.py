def ksa(key):
    S = []
    for i in range(0, 256):
        S.append(i)
    j = 0
    for i in range(0, 256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    return S


def prga(S):
    i = 0; j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K


def rc4(key, inputStream):
    ''' returns the RC4 encoding of inputStream based on the key
    (bytes, bytes) -> bytes
    '''
    S = ksa(key)
    K = prga(S)
    r = b''
    for i in inputStream:
        r += bytes(chr(i ^ next(K)), 'UTF-8')
    return r