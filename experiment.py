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
    "block_size": 2,
    "password": "cheap",
    "noise_interval": 5,
    "noise_char": "~",
}

message = "type wghatejhgfdfguiuyfdxfghjuiuygfdfghjuhgfdxcfghjkiugfcvhsver"

# SELF-EXPERIMENTATION
print("=" * 60)
print("EXPERIMENTING ENCRYPTION")
print("=" * 60)
phase1_encrypted = phase1_encrypt(message, key)
print(f"✅ Completed Phase 1 Encrypt: {phase1_encrypted}")

phase2_encrypted = phase2_encrypt(phase1_encrypted, key)
print(f"✅ Completed Phase 2 Encrypt: {phase2_encrypted}")

phase3_encrypted = phase3_encrypt(phase2_encrypted, key)
print(f"✅ Completed Phase 3 Encrypt: {phase3_encrypted}")

phase4_encrypted = phase4_encrypt(phase3_encrypted, key)
print(f"✅ Completed Phase 4 Encrypt: {phase4_encrypted}")

phase5_encrypted = phase5_encrypt(phase4_encrypted, key)
print(f"✅ Completed Phase 5 Encrypt: {repr(phase5_encrypted)}")
print("=" * 60)
decrypted = decrypt(phase5_encrypted, key)
print(f"Decryption: {decrypted}")
print("=" * 60)
if decrypted == message:
    print("🎉 ALL TESTS PASSED! The 5-phase algorthm is completed!")
else:
    print("❌ Failed Decryption Test, Please verify the code! ")
