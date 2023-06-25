import subprocess
import random
import time

def generate_random_message():
    with open('http3_tests.txt', 'r') as file:
        phrases = file.readlines()
    return random.choice(phrases).strip()

# Number of terminals to open
num_terminals = 1

# Command to be executed in each terminal
command = "python3 ../http3_client.py --print-response --ca-certs ../certificates/pycacert.pem wss://localhost:4433/ws"

# Set the shell to zsh
shell = "/bin/zsh"

# Loop to open the terminals and send random messages
for _ in range(num_terminals):
    terminal = subprocess.Popen([shell, "-c", command], stdin=subprocess.PIPE)
    while True:
        message = generate_random_message()
        terminal.stdin.write(f"{message}\n".encode())  # Send the message to the terminal
        terminal.stdin.flush()
        time.sleep(0.001)
