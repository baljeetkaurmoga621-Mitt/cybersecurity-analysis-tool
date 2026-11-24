# Cybersecurity Log Analysis Tool
# Detect repeated failed login attempts

sample_logs = [
    "Failed login from 192.168.1.10",
    "Successful login from 192.168.1.20",
    "Failed login from 192.168.1.10",
    "Failed login from 192.168.1.15",
    "Failed login from 192.168.1.10",
    "Failed login from 192.168.1.15"
]

failed_attempts = {}

for log in sample_logs:
    if "Failed login" in log:
        ip_address = log.split("from ")[1]
        failed_attempts[ip_address] = failed_attempts.get(ip_address, 0) + 1

print("=== Security Log Analysis ===")

for ip_address, count in failed_attempts.items():
    print(f"IP Address: {ip_address} | Failed Attempts: {count}")

    if count >= 3:
        print("WARNING: Multiple failed login attempts detected!")
      
