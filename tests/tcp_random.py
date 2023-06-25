import subprocess
import random
import time

def generate_random_message():
    with open('tests/random_messages.txt', 'r') as file:
        phrases = file.readlines()
    return random.choice(phrases).strip()

# Número de terminais
num_terminals = 1

# Comando a ser executado
command = "python3 ./src/tcp/tcp_client.py"

# O `shell` do sistema
shell = "/bin/zsh"

# Loop para o terminal e enviar as mensagens
for _ in range(num_terminals):
    terminal = subprocess.Popen([shell, "-c", command], stdin=subprocess.PIPE)
    while True:
        message = generate_random_message()
        terminal.stdin.write(f"{message}\n".encode()) 
        terminal.stdin.flush()
        time.sleep(0.5)
