import os
import socket
from Crypto.Cipher import AES


key = b"TheNeuralNineKey"
nonce = b"The NeuralNineNce"

cipher = AES.new(key, AES.MODE_EAX, nonce)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

file_name = "hh.mp4"
file_size = os.path.getsize(file_name)

# Send the file name
client.send(file_name.encode())

# Send the file size
client.send(int(file_size).to_bytes(8, byteorder='big'))

# Send the encrypted data
with open(file_name, "rb") as f:
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        encrypted_chunk = cipher.encrypt(chunk)
        client.send(encrypted_chunk)

# Send an end marker
client.send(b"<END>")

client.close()
