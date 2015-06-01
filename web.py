from flask import Flask
import ARIA

app = Flask(__name__)



@app.route('/encrypt/<int:plain>/<int:key>/<int:bits>/')
def encrypt(plain,key,bits):
    return str(ARIA.ARIA_encryption(plain,key,bits))

@app.route('/decrypt/<int:cipher>/<int:key>/<int:bits>/')
def decrypt(cipher,key,bits):
    return str(ARIA.ARIA_decryption(cipher,key,bits))

if __name__ == '__main__':
    app.run()
