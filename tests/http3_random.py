import subprocess
import random
import time
import argparse

# Function to generate a random message from file
def generate_random_message():
    with open('tests/random_messages.txt', 'r') as file:
        phrases = file.readlines()
    return random.choice(phrases).strip()

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--fast', required=False, help='Enable faster mode')
parser.add_argument('--term', required=False, help='Number of terminals to open')
args = parser.parse_args()

speed = 0.001 if args.fast else 0.5
num_terminals = int(args.term) if args.term else 1

# Open terminals and execute the command
terminals = []

for i in range(num_terminals):
    terminal = subprocess.Popen(
        [
            "/bin/zsh", 
            "-c", 
            "python3 ./src/quic/http3_client.py --print-response --ca-certs certificates/pycacert.pem --username term_{} wss://localhost:4433/ws".format(i + 1)
        ], 
        stdin=subprocess.PIPE)
    terminals.append(terminal)

# Send random messages to each terminal
while True:
    for terminal in terminals:
        message = generate_random_message()
        terminal.stdin.write(f"{message}\n".encode())
        terminal.stdin.flush()
    time.sleep(speed)
