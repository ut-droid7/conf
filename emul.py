import os
import socket
import configparser

def cli():
    username = os.getlogin()
    hostname = socket.gethostname()

    while True:
        prompt = username + "@" + hostname + ":~$ "
        user_input = input(prompt).strip()

        if not user_input:
            continue

        parts = user_input.split()
        command = parts[0]
        args = parts[1:]

        if command == "exit":
            break

        elif command == "ls":
            print(f"ls: arguments: {args}")

        elif command == "cd":
            if len(args) > 1:
                print(f"cd: too many arguments")
            else:
                print(f"cd: arguments: {args}")

        else:
            print(command + ": command not found")


#cli()

config = configparser.ConfigParser()
config.read("config.ini")
print(config["DEFAULT"]["vfs"])