import socket, time

# Dichiara ip+porta
ip_server = ""
port_server = 44445

# Crea Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Binda su ip+port
s.bind((ip_server, port_server))
print(f"-UDP bind su porta: {port_server}")

# Variabile per ricezione
data = s.recv(1024).decode("utf-8")
# Inizio Ciclo
while True:
    # Variabile per ricezione
    data = s.recv(1024).decode("utf-8")
    # Se non arriva nulla, fai un print
    if not data:
        print(f"Nessun dato ricevuto...\n-UDP bind su porta: {port_server}")
    # Altrimenti stampa la lunghezza dei pacchetti che arrivano
    else:
        print(f"[+]{len(data)}bytes")


        
