from engine import encrypt, decrypt

key = {
    "shift": 5,
    "block_size": 4,
    "password": "CIPHER",
    "noise_interval": 3,
    "noise_char": "~",
}

message = "The eagle lands at midnight"
print(f"Original:  {message}")

encrypted = encrypt(message, key)
print(f"Encrypted: {encrypted}")

decrypted = decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")

print(f"\nMatch: {message == decrypted}")
