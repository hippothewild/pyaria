from .ARIA_Byte import *

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
    byte_plain = int_to_byte(plain, 16)
    byte_key = int_to_byte(key, bits//8)
    byte_roundkeys = KeyExpansion(byte_key)
    byte_cipher = cipher(byte_plain, byte_roundkeys, printIntermediate)
    return byte_to_int(byte_cipher)

def ARIA_decryption(c, key, bits):
    if bits not in [128, 192, 256]:
        print("Key length must be 128/192/256bits!")
        return
    c_len = len(hex(c)[2:])
    if  c_len > 32:
        print("Cipher text should be 128bits!")
        return
    key_len = len(hex(key)[2:])
    if key_len > bits//4:
        print("Key should be {0:}bits!".format(bits))
        return
    byte_c = int_to_byte(c, 16)
    byte_key = int_to_byte(key, bits//8)
    byte_roundkeys = DecKeyExpansion(byte_key)
    byte_plain = cipher(byte_c, byte_roundkeys, printIntermediate)
    return byte_to_int(byte_plain)
