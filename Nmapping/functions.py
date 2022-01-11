from subprocess import call
import os
import socket
import ipaddress
import string, random

def clear():
    _ = call('clear' if os.name =='posix' else 'cls')

def get_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address).is_private
        print(f"Internal IP address {address} is valid.")
        return address
    except ValueError:
        print(f"IP address {address} is not a valid internal address")

def random_string(char_num):
    try:
        ran_string = ''.join(random.choice(string.ascii_letters) for x in range(int(char_num)))
        return ran_string
    except:
        print("Invalid number specified")

if __name__ == "__main__":
    clear()
    print("RUNNING DEBUGGER TESTS")
    print(f"If the screen cleared, clear is working. os name is {os.name}")
    print(f"IP Address is: {get_ip()}")
    validate_ip_address(get_ip())
    print(f"here is a random string: {random_string(6)}")
