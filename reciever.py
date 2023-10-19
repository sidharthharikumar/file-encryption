import tqdm
import socket
from Crypto.Cipher import AES

key = b"TheNeuralNineKey"
nonce = b"The NeuralNineNce"
cipher = AES.new(key, AES.MODE_EAX, nonce)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

client, addr = server.accept()

file_name = client.recv(1024).decode()
print("Receiving file:", file_name)

file_size = int.from_bytes(client.recv(8), byteorder='big')
print("File size:", file_size)

file = open("decrypted_" + file_name, "wb")

file_bytes = b""
end_marker = b"<END>"

progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))

while True:
    data = client.recv(1024)
    if data[-len(end_marker):] == end_marker:
        file.write(cipher.decrypt(data[:-len(end_marker)]))
        break
    file.write(cipher.decrypt(data))
    progress.update(len(data))

file.close()
client.close()
server.close()
