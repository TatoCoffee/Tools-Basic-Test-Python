import socket
import hashlib

def get_hostname():
    return socket.gethostname()

def get_ip_address():
    return socket.gethostbyname(get_hostname())

def scan_port(ip):
    objetivo = socket.gethostbyname(ip)
    resultado_scan = ""
    try:
        for port in range(1, 150):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            resultado = s.connect_ex((objetivo, port))
            if resultado == 0:
                resultado_scan += f"The port {port} is open\n"
            s.close()
    except:
        resultado_scan = "\n Exiting..."
    return resultado_scan

def find_password_in_dict(input_hash, pass_doc):
    encontrada = 0
    try:
        pass_file = open(pass_doc, 'r')
    except:
        return f"Error: {pass_doc} not found"
    for palabra in pass_file:
        palabra_cifrada = palabra.encode('utf-8')
        palabra_hasheada = hashlib.md5(palabra_cifrada.strip())
        digest = palabra_hasheada.hexdigest()

        if digest == input_hash:
            encontrada = 1
            return f"Password found\nPassword: {palabra}"
    if not encontrada:
        return f"Not Found: {pass_doc}"

def decimal_to_binary(decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2 
    return str(decimal) + binario
