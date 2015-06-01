import ARIA

__all__ = ['ARIA_encryption', 'ARIA_decryption']

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

def ARIA_encryption(plain, key, bits):
    if bits not in [128, 192, 256]:
        print("Key length must be 128/192/256bits!")
        return
    if len(hex(plain)[2:-1]) > 32:
        print("Plain text should be 128bits!")
        return
    if len(hex(key)[2:-1]) > bits//4:
        print("Key should be {0:}bits!".format(bits))
        return
    byte_plain = int_to_byte(plain, 16)
    byte_key = int_to_byte(key, bits//8)
    byte_roundkeys = ARIA.KeyExpansion(byte_key)
    byte_cipher = ARIA.cipher(byte_plain, byte_roundkeys)
    return byte_to_int(byte_cipher)

def ARIA_decryption(cipher, key, bits):
    if bits not in [128, 192, 256]:
        print("Key length must be 128/192/256bits!")
        return
    if len(hex(cipher)[2:-1]) > 32:
        print("Cipher text should be 128bits!")
        return
    if len(hex(key)[2:-1]) > bits//4:
        print("Key should be {0:}bits!".format(bits))
        return
    byte_cipher = int_to_byte(cipher, 16)
    byte_key = int_to_byte(key, bits//8)
    byte_roundkeys = ARIA.DecKeyExpansion(byte_key)
    byte_plain = ARIA.cipher(byte_cipher, byte_roundkeys)
    return byte_to_int(byte_plain)
