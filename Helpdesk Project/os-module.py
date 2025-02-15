import os
hosts = ['google.com', 'cnn.com']

for host in hosts:
    print(os.system(f'ping {host} -n 1'))
    
    