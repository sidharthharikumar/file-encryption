import socket
def find_available_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port

port = find_available_port()
server_socket.bind(('', port))
