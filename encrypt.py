def decrypt(sender_public_key, receiver_public_key, message):
    # Mappings
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphaToNum = {i:ord(i)-65 for i in alpha}
    # Variables
    p, q = 23, 17
    priv_lo, priv_hi = 5, 30
    # Possible private keys
    sender_private_keys = []
    receiver_private_keys = []
    # Brute force every private key - small interval makes it possible
    for i in range(priv_lo, priv_hi+1):
        if q**i % p == sender_public_key:
            sender_private_keys.append(i)
        if q**i % p == receiver_public_key:
            receiver_private_keys.append(i)
    # Decrypt message
    shared_key = sender_public_key**receiver_private_keys[0] % p
    decrypted = "".join([alpha[(alphaToNum[char]-shared_key)%26] for char in message])
    # Print info
    print("Sender private key(s):", *sender_private_keys)
    print("Receiver private key(s):", *receiver_private_keys)
    print("Encrypted message:", message)
    print("Decrypted message:", decrypted)

# Some test cases
decrypt(19, 21, "FYOTCPNEPO")
decrypt(19, 21, "XLES")