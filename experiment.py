import os
from engine import (
    encrypt,
    decrypt,
    phase1_encrypt,
    phase2_encrypt,
    phase3_encrypt,
    phase4_encrypt,
    phase5_encrypt,
)

key = {
    "shift": 5,
    "block_size": 4,
    "password": "CIPHER",
    "noise_interval": 3,
    "noise_char": "~",
}

message = "www"

# SELF-EXPERIMENTATION
phase1_encrypted = phase1_encrypt(message, key)
print(f"Phase 1 Encrypt: {phase1_encrypted}")

phase2_encrypted = phase2_encrypt(phase1_encrypted, key)
print(f"Phase 2 Encrypt: {phase2_encrypted}")

phase3_encrypted = phase3_encrypt(phase2_encrypted, key)
print(f"Phase 3 Encrypt: {phase3_encrypted}")

phase4_encrypted = phase4_encrypt(phase3_encrypted, key)
print(f"Phase 4 Encrypt: {phase4_encrypted}")

phase5_encrypted = phase5_encrypt(phase4_encrypted, key)
print(f"Phase 5 Encrypt: {repr(phase5_encrypted)}")

decrypted = decrypt(phase5_encrypted, key)
print(f"Decryption: {decrypted}")

if decrypted == message:
    print("PASSED DECRYPTION")
else:
    print("FAIL TO DECRYPT")
