from Crypto.Cipher import ARC4
import wave

def encrypt(key_filename, input_filename, output_filename):
    ''' 
    Encrypts the wave input file (input_filename) with the key (key_filename) using the rc4 cipher (from pycrypto)
    and writes the wave output file (output_filename). 
    The wave output file must be a playable wave file.
    (string, string, string) -> None
    
    '''
    file = wave.open(input_filename, 'r')
    out = wave.open(output_filename, 'w')
    out.setparams(file.getparams())
    
    with open(key_filename, 'r') as myfile:
        key = myfile.read()
    cipher = ARC4.new(key)
    msg = cipher.encrypt(file.readframes(file.getnframes()))
    out.writeframes(msg)
    
    file.close()
    out.close()

def decrypt(key_filename, input_filename, output_filename):
    ''' 
    Decrypts the wave input file (input_filename) with the key (key_filename) using the rc4 cipher (from pycrypto)
    and writes the wave output file (output_filename). 
    The wave output file must be a playable wave file. 
    (string, string, string) -> None
    '''
    out = wave.open(input_filename, 'r')
    file = wave.open(output_filename, 'w')
    file.setparams(out.getparams())
    
    with open(key_filename, 'r') as myfile:
        key = myfile.read()
    cipher = ARC4.new(key)
    msg = cipher.decrypt(out.readframes(out.getnframes()))
    file.writeframes(msg)
    
    file.close()
    out.close()

 