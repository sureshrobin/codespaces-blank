import psutil

print(f'{psutil.cpu_percent(interval=1)}%')
print(f'{psutil.cpu_count(logical=False)}%')