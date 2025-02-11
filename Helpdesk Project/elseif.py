cpu_usage = int(input("Enter CPU Usage: "));

if cpu_usage > 80:
    print("High Usage");
elif cpu_usage < 50:
    print("Low Usage");

else:
    print("Normal Usage");