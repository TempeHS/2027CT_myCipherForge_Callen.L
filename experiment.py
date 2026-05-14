from engine import encrypt, decrypt, phase1_encrypt, phase2_encrypt

# Key with settings for both phases
key = {"shift": 7, "block_size": 4}  # Phase 1 setting  # Phase 2 setting

message = "Secret Message!"

# See each phase
print(f"Original:       {message}")

after_phase1 = phase1_encrypt(message, key)
print(f"After Phase 1:  {after_phase1}")

after_phase2 = phase2_encrypt(after_phase1, key)
print(f"After Phase 2:  {after_phase2}")

# Full encrypt/decrypt
encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print(f"\nFinal encrypted: {encrypted}")
print(f"Decrypted:       {decrypted}")
print(f"Match: {decrypted == message}")
