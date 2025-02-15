import psutil
import time
'''
disk = psutil.disk_usage('/')
print(f'Used Percentage: {disk.percent}%')
print(f'Total Space: {disk.total//(1024**3)} GB')
print(f'Free Space: {disk.free//(1024**3)} GB')
print(f'Used Space: {disk.used//(1024**3)} GB')

'''
boot_time = psutil.boot_time()

uptime = time.time() - boot_time

print(uptime // 3600)