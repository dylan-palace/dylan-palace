"""
CTF-Target Scanner
- Returns a list of up hosts
- Ports open on the up hosts
"""

from libnmap.parser import NmapParser
from libnmap.process import NmapProcess
from libnmap.objects import NmapReport, NmapHost, NmapService
import os, re, sys
from functions import *
#Get target range
clear()
IP = get_ip().split(".")
target_range = (validate_ip_address(f"{IP[0]}.{IP[1]}.{IP[2]}.0")) + "/24"
print(f"--- Target range: {target_range} ---")

#output filename
cwd = os.getcwd() + "/scanning"
fname = "Test" + "_" + str(len(os.listdir(f"{cwd}/scans/"))-1)
fpath = f"{cwd}/scans/{fname}"

os.system(f"mkdir '{fpath}'")
print(f"--- Output files in: {fpath} ---")


# In built nmap scans, saved to specific file in Test dir
def run_scan(range, type, filename):
    if type == "ping":  # Ping scan
        print(f"Running ping scan on {range}")
        nmap_proc = NmapProcess(targets=range, options=f"-sn -oX {fpath}/ping-{filename}.xml", safe_mode=False,)
    elif type == "port":
        print(f"Running port scan on {range}")  # Port Scan
        nmap_proc = NmapProcess(targets=range, options=f"--A -T4 -oX {fpath}/port-{filename}.xml", safe_mode=False,)
    elif type == "smb":
        print(f"Running smb scan on {range}")  # SMB scan
        nmap_proc = NmapProcess(targets=range, options=f"--script smb-enum-shares.nse -p445 -oX {fpath}/smb-{filename}.xml", safe_mode=False,)
    else:
        print("Not a valid scan choice")
        return
    rc = nmap_proc.run()
    if nmap_proc.rc == 0:
        pass
        #print(nmap_proc.stdout)
    else:
        pass
        #print(nmap_proc.stderr)


run_scan(target_range, "ping", idx(target_range))
parsed_report = NmapParser.parse_fromfile(
    f"{fpath}/ping-{idx(target_range)}.xml"
)


host_list = []


for host in parsed_report.hosts:
    if host.status == "up" and host.address != get_ip():
        filename = idx(host.address)
        print(f"Host {host} is up. Running port and smb scans...")
        run_scan(host.address, "port", filename)
        run_scan(host.address, "smb", filename)
        host_info = xml_parser(f'{fpath}/port-{filename}.xml')
        host_info['hostname'] = host.hostnames
        host_list.append(host_info)
        print(f"host list {host_list}")

target_ips = []
for host in host_list:
    print("Writing data...")
    target_ip = idx(host["ip"])
    ip = host["ip"]
    try:
        if host["445"][0] != "closed":
            filename = f'{cwd}/vulnerable_targets/{target_ip}.json'
            target_ips.append(host["ip"])
            print(f"Target IP {host['ip']} found")
        else:
            filename = f'{cwd}/non_vuln_targets/{target_ip}.json'
            print(f"Non target IP {host['ip']} found")
    except KeyError:
        filename = f'{cwd}/non_vuln_targets/{target_ip}.json'
        print(f"Non target IP {host['ip']} found")
    except:
        print("Writing data failed. Not sure why. Please view error log.")
        filename = f'{cwd}/non_vuln_targets/{target_ip}.json'
    write_json(host, filename)

# At this point we should have various files I need to manually analyse so I can script the rest

# Ideally a text file with IPs that are vulnerable to eternal blue, or simply have port 445 open
# We can run the exploit against all vulnerable devices
# Save file as target IPs
