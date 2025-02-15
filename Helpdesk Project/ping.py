import subprocess

def check_ip(*ip):
    for i in ip:
        stream = subprocess.run(f"ping {i} -n 1", capture_output=True, text=True)
        
        if stream.returncode == 0:
            print(f"{i} is UP")

        else:
            print(f"{i} is DOWN")
    
check_ip('192.168.109.1', '192.168.117.1', '192.168.120.1', '192.168.110.2', '192.168.122.1', '192.168.124.1', '192.168.121.1', '192.168.127.1', '192.168.111.1', '192.168.114.1')