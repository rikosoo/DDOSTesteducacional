# 🛡️ ICMP Flood - Teste de Carga em Rede

Este projeto é um **simulador de ICMP Flood** para **testes de carga e segurança** em redes locais.  
Ele permite avaliar o impacto de pacotes ICMP em um **ambiente controlado**, ajudando a entender como esses ataques funcionam e como mitigá-los.

⚠ **Aviso Importante**  
Este projeto **deve ser usado apenas em sua própria máquina virtual ou ambiente de testes**.  
Não utilize este código para fins maliciosos, pois ataques DDoS são **ilegais** em redes públicas.

---

## 🚀 Como funciona?
1. O script envia pacotes ICMP (`ping`) em alta frequência para um **IP de destino**.
2. O número de pacotes enviados e o **tempo de duração** do teste podem ser configurados.
3. O objetivo é analisar a resposta do sistema-alvo e **avaliar a capacidade da rede** em lidar com esse tipo de carga.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **Módulo `os`** para executar comandos no terminal
- **Módulo `time`** para controle de tempo
- **Módulo `threading`** para execução assíncrona do ataque

---

## 📜 Como rodar o script?

### **1️⃣ Clonar o repositório**
```bash
git clone https://github.com/rikosoo/icmp-flood-test.git
cd icmp-flood-test
