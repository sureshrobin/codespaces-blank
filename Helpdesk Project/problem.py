"""
Write a Python script that:

Prompts the user to enter a server response time (in milliseconds).
Uses if-elif-else to classify the server health:
Response time < 100ms → "Server is fast"
100ms ≤ Response time < 300ms → "Server is normal"
300ms ≤ Response time < 600ms → "Server is slow"
600ms or more → "Server is very slow! Needs attention."

"""

latency = int(input("Enter the response time: "))

if latency <= 100:
    print("server is fast");
elif latency <=300:
    print("server is normal");
elif latency <=600:
    print("server is slow");
else:
    print("server is very slow! Needs attention");
