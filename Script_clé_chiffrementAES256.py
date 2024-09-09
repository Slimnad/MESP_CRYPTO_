import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import secrets

# Chiffrer une chaîne de caractères
def chiffre_message(cle, iv, message):
    padder = padding.PKCS7(128).padder()
    message = message.encode()
    message = padder.update(message) + padder.finalize()
    cipher = Cipher(algorithms.AES(cle), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(message) + encryptor.finalize()
    return ct

# Déchiffrer un message
def dechiffre_message(cle, iv, ct):
    cipher = Cipher(algorithms.AES(cle), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    message = decryptor.update(ct) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    message = unpadder.update(message) + unpadder.finalize()
    return message.decode()

k = secrets.token_bytes(32) # generation d'une cle AES
i = secrets.token_bytes(16) # generation d'IVs
c = chiffre_message(k,i,'test')
dechiffre_message(k,i,c)

clé = k
iv = i

print(clé)
print(iv)
print(chiffre_message(clé,iv,'salut'))


cclé = b'\xe1gp\x98U\x08\xcc0R\xf3Q\x9f\xac\x8d\xdfs|\xf0(\xa2\xf4\xa7Q\xb5\xcc\xfe\xb8f\xf4}\x9f\x81'
iiv = b'\x00\xa3I\n\x97\xd4].(\x9c2K\xb2\xccb\x08'
mess = b'\xf6\x84\x0f\xb5\x0cZ\xbf^\x07\xf7\x1d\x18\xbf\xda\xe0\xb5'

print(dechiffre_message(cclé,iiv,mess))

