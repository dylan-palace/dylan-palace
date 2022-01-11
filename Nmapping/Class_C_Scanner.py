"""
Class C IP Scanner

- Returns a list of up hosts
- Ports open on the up hosts

"""

from libnmap.parser import NmapParser
from libnmap.process import NmapProcess
from libnmap.objects import NmapReport, NmapHost, NmapService
import os
from functions import clear
import re

clear()


IP = "192.168.1.0"
Subnet = "/24"

target_range = IP + Subnet
for fourth_byte in range(0, 256):
    IP = "192.168." + str(fourth_byte) + ".0"
    run_scan(range=IP, type="ping")
    ports_of_interest("scan.xml")
    print(hosts)


nmap_proc = NmapProcess(targets=target_range, options="-sP -oX /scans/Class-C/{}".format(target_range[8:]))


print("NMAP SESSION...")
parsed_report = NmapParser.parse_fromfile('/scans/test.txt')
for host in parsed_report.hosts:
    if host.status == "up":
        for port in host.get_open_ports():
            if port[1] == 'tcp' and port[0] == 443:
                print("host {}:".format(host.address), host.get_open_ports())
                print(type(host.get_open_ports()))
