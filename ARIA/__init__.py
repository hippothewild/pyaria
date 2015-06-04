from . import ARIA_Byte as ARIA

__version__ = "1.0.0"
__all__ = ['ARIA_encryption', 'ARIA_decryption', 'toggleprint']
printIntermediate = False

def int_to_byte(num, num_byte):
    b = list()
    for i in range(num_byte):
        b.append(num % 256)
        num //= 256
    b.reverse()
    return b

def byte_to_int(byte):
    n = 0
    for b in byte:
        n *= 256
        n += b
    return n

def toggleprint():
    """
    Function that toggles whether print each round's result or not
    """
    global printIntermediate
    printIntermediate = not printIntermediate
    if printIntermediate:
        print("Print each round's results")
    else:
        print("Do not print each round's results")

def ARIA_encryption(plain, key, bits):
    if bits not in [128, 192, 256]:
        print("Key length must be 128/192/256bits!")
        return
    plain_len = len(hex(plain)[2:])
    if  plain_len > 32:
        print("Plain text should be 128bits!")
        return
    key_len = len(hex(key)[2:])
    if key_len > bits//4:
        print("Key should be {0:}bits!".format(bits))
        return
    # Change integer to byte array
    byte_plain = int_to_byte(plain, 16)
    byte_key = int_to_byte(key, bits//8)
    byte_roundkeys = ARIA.KeyExpansion(byte_key)  # Round key generation
    byte_cipher = ARIA.cipher(byte_plain, byte_roundkeys, printIntermediate)  # Encryption
    return byte_to_int(byte_cipher)

def ARIA_decryption(cipher, key, bits):
    if bits not in [128, 192, 256]:
        print("Key length must be 128/192/256bits!")
        return
    cipher_len = len(hex(cipher)[2:])
    if  cipher_len > 32:
        print("Cipher text should be 128bits!")
        return
    key_len = len(hex(key)[2:])
    if key_len > bits//4:
        print("Key should be {0:}bits!".format(bits))
        return
    # Change integer to byte array
    byte_cipher = int_to_byte(c, 16)
    byte_key = int_to_byte(key, bits//8)
    byte_roundkeys = ARIA.DecKeyExpansion(byte_key)  # Round key generation
    byte_plain = ARIA.cipher(byte_cipher, byte_roundkeys, printIntermediate)  # Decryption
    return byte_to_int(byte_plain)
