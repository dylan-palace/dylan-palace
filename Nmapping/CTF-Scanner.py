"""
CTF-Target Scanner

- Returns a list of up hosts
- Ports open on the up hosts
"""

from libnmap.parser import NmapParser
from libnmap.process import NmapProcess
from libnmap.objects import NmapReport, NmapHost, NmapService
import os, re, sys
from functions import clear, get_ip, validate_ip_address, random_string

clear()

IP = get_ip().split(".")
cwd = os.getcwd()

target_range = (validate_ip_address(f"{IP[0]}.{IP[1]}.{IP[2]}.0")) + "/24"
print(target_range)

# In built nmap scans, saved to specific file in CTF-Test dir
def run_scan(range, type):
    fileindex = range.replace(".", "-").replace("/", "-")
    if type == "ping":#Ping scan
        nmap_proc = NmapProcess(targets=range, options=f"-sn -oX {cwd}/scans/CTF-Test/ping-{fileindex}", safe_mode=False)
    elif type == "port":#Port Scan
        nmap_proc = NmapProcess(targets=range, options=f"-p0- -A -T4 -oX {cwd}/scans/CTF-Test/port-{fileindex}", safe_mode=False)
    elif type == "vuln":#Vulnerability scan
        nmap_proc = NmapProcess(targets=range, options=f"-sV --script vulners [--script-args mincvss=7] -oX {cwd}/scans/CTF-Test/vulns-{fileindex}", safe_mode=False)
    else:
        print("Not a valid scan choice")
        return
    rc = nmap_proc.run()
    if nmap_proc.rc == 0:
        print(nmap_proc.stdout)
    else:
        print(nmap_proc.stderr)


#run_scan(target_range, "ping")
parsed_report = NmapParser.parse_fromfile(f'{cwd}/scans/CTF-Test/ping-{target_range.replace(".", "-").replace("/", "-")}')
for host in parsed_report.hosts:
    if host.status == "up" and host.address != get_ip():
        print(f"Host {host} is up. Running port and not vuln scans...")
        run_scan(host.address, "port")
        run_scan(host.address, "vuln")
