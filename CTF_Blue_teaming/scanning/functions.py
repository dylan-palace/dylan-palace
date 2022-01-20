from subprocess import call
import os, json
import socket
import ipaddress
import string, random
import xml.etree.ElementTree as ET

#clears terminal
def clear():
    _ = call("clear" if os.name == "posix" else "cls")

#returns local ip
def get_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

#returns a dictionary of open services running on the machine
def xml_parser(xml):
    tree = ET.parse(xml)
    root = tree.getroot()
    for address in root.iter('address'):
        hosts = { 'ip': address.attrib['addr']}
    for hostname in root.iter('hostname'):
        hosts['hostname'] = hostname.attrib['name']
    for host in root.iter('host'):
        for port in host.iter('port'):
            local_state, local_name = "null", "null"
            for state in port.iter('state'):
                local_state = state.attrib["state"]
            for service in port.iter('service'):
                local_name = service.attrib["name"]
            hosts[port.attrib["portid"]] = [local_state, local_name]
    return hosts

#checks is an internal IP
def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address).is_private
        return address
    except ValueError:
        print(f"IP address {address} is not a valid internal address")

#random number string
def random_string(char_num):
    try:
        ran_string = "".join(
            random.choice(string.ascii_letters) for x in range(int(char_num))
        )
        return ran_string
    except:
        print("Invalid number specified")

#filenaming safe IP range
def idx(ip):
    return ip.replace(".", "-").replace("/", "-")

def write_json(content, fname):
    #try:
    with open(fname, 'w') as outfile:
        json.dump(content, outfile, indent=4, sort_keys=True)
    print(f"{fname} successsfuly written")
    #except:
        #print(f"Something went wrong writing {fname}")



if __name__ == "__main__":
    clear()
    print("RUNNING DEBUGGER TESTS")
    print(f"If the screen cleared, clear is working. os name is {os.name}")
    print(f"IP Address is: {get_ip()}")
    validate_ip_address(get_ip())
    print(f"here is a random string: {random_string(6)}")
    __parsed_xml = xml_parser('scans/Test_0/port-192-168-1-1.xml')
    print(f"validating xml from test file: {__parsed_xml}")
