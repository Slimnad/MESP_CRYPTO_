from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import itertools
import string

def des_encrypt(key, plaintext):
    cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(64).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    ct = encryptor.update(padded_data) + encryptor.finalize()
    return ct

def des_decrypt(key, ciphertext):
    cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    pt = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(64).unpadder()
    unpadded_data = unpadder.update(pt) + unpadder.finalize()
    return unpadded_data


# Clé partielle fournie et complétée avec les 4 octets manquants
partial_key = b'12345678bien'


# Message chiffré intercepté
ciphertext = b'\xd72U\xc03.\xda\x99Q\xb5\x020\xc4\xb8\x16\xc6\xfa-\xb9U+\xda\\\x126L\xf3~\xbd8\x12q\x02?\x80\xeaVI\xa9\xe1'

# Liste des caractères à essayer (ici on utilise des caractères alphanumériques)
characters = string.ascii_lowercase

# Boucle sur toutes les combinaisons possibles des 4 caractères
for combo in itertools.product(characters, repeat=4):
    # Construire la clé complète
    full_key = partial_key + ''.join(combo).encode()
    key = full_key
    # Déchiffrement
    try: 
        print(key)
        decrypted_message = des_decrypt(key, ciphertext)
        print(decrypted_message.decode('utf-8'))
        break
    except:
        continue
        if (decrypted_message) == True :
            break

print(key)

