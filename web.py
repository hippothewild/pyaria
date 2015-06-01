from flask import Flask
from crossdomain import Crossdomain
import ARIA

app = Flask(__name__)

@app.route('/encrypt/<string:hex_plain>/<int:key>/<int:bits>/')
@Crossdomain(origin='*')
def encrypt(hex_plain, key, bits):
    if len(hex_plain) % 32: # hex_plain length is not divisible by 32
        hex_plain += '0' * (32 - len(hex_plain) % 32)
    result = str()
    for i in range( len(hex_plain)//32 ):
        encrypt = hex( ARIA.ARIA_encryption( int( hex_plain[i*32: (i+1)*32], 16 ), key, bits ) )[2:]
        encrypt = '0' * (32 - len(encrypt)) + encrypt
        result += encrypt
    return result

@app.route('/decrypt/<string:hex_cipher>/<int:key>/<int:bits>/')
@Crossdomain(origin='*')
def decrypt(hex_cipher, key, bits):
    if len(hex_cipher) % 32: # hex_cipher length is not divisible by 32
        hex_cipher += '0' * (32 - len(hex_cipher) % 32)
    result = str()
    for i in range( len(hex_cipher)//32 ):
        decrypt = hex( ARIA.ARIA_decryption( int( hex_cipher[i*32: (i+1)*32], 16 ), key, bits ) )[2:]
        decrypt = '0' * (32 - len(decrypt)) + decrypt
        result += decrypt
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
