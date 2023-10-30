import os


ip_prefix =input("Please enter Ip prefix: ")

def ping_sweep(target_ip):
    command = f"ping -n 1 {target_ip}" 
    response = os.system(command)

    if response == 0:
        print(f"{target_ip} is online")
    else:
        print(f"{target_ip} is offline")

for i in range(0,256):
    target_ip = f"{ip_prefix}.{i}"
    ping_sweep(target_ip)
