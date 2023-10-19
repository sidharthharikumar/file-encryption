from flask import Flask, render_template, request, send_file
from cryptography.fernet import Fernet
import os
import socket

app = Flask(__name__)

# Define the secret key for encrypting files
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Create a directory to store uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Start a server socket connection to handle file downloads
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5000))  # Replace with your desired host and port
server_socket.listen(1)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'fileToUpload' in request.files:
        file = request.files['fileToUpload']
        if file:
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)
            with open(filename, 'rb') as file:
                file_data = file.read()
            encrypted_data = cipher_suite.encrypt(file_data)
            encrypted_filename = filename + '.enc'
            with open(encrypted_filename, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)
            return "File uploaded and encrypted successfully."

    return "File upload failed."

@app.route('/download', methods=['POST'])
def download_file():
    encryption_key = request.form.get('encryption_key')
    if Fernet(encryption_key) == cipher_suite:
        conn, addr = server_socket.accept()
        filename = 'uploads/sample.txt.enc'  # Replace with the path to your encrypted file
        with open(filename, 'rb') as file:
            data = file.read(1024)
            while data:
                conn.send(data)
                data = file.read(1024)
            conn.close()
        return "File downloaded successfully."
    return "Invalid encryption key."

if __name__ == '__main__':
    app.run(debug=True)
