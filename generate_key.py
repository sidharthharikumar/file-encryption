from Crypto.Cipher import AES

key=b"Thesecretkey"
nonce=b"Thesecretkey"
cipher= AES.new(key, AES.MODE_EAX, nonce)
ciphertext=cipher.encrypt(b"helloworld")
print(ciphertext)