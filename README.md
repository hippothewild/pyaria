# PyARIA
## Caution! This package is NOT compatible with Python 2.x
ARIA implementation with Python

**How to Install**
 1. Download *setup.py* and *ARIA* folder.
 2. Open a terminal, move to the directory that files are downloaded and run
```
$ python setup.py install
```
 - Shortcut version for Windows Users
  1. Download a *PyARIA-1.0.0.win32.exe*.
  2. Run the *PyARIA-1.0.0.win32.exe*.

**How to Use**
```Python
import ARIA
```
or
```Python
from ARIA import *
```

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
