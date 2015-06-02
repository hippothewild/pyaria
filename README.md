# PyARIA
## Caution! This package is NOT compatible with Python 2.x
ARIA implementation with Python

**APIs**

 - ARIA_encryption(plain, key, bits)
   - Input
     1. plain: Plaintext. Nonnegative integer at most 128bits.
     2. key: Key value. Nonnegative integer at most *bits*bits.
     3. bits: Number of bits of key. One of 128/192/256.
    - Output
     - Ciphertext. Nonnegative integer at most 128bits.
 - ARIA_decryption(cipher, key, bits)
   - Input
     1. cipher: Ciphertext. Nonnegative integer at most 128bits.
     2. key: Key value. Nonnegative integer at most *bits*bits.
     3. bits: Number of bits of key. One of 128/192/256.
   - Output
     - Plaintext. Nonnegative integer at most 128bits.
