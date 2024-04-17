import subprocess
import re
import threading

def get_ping(ip_address):
    # Adjust command based on your operating system
    # For Linux/Unix based systems
    command = ["ping", "-c", "1", ip_address]


    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        # Regex to extract the time from the output
        match = re.search(r'time=(\d+\.?\d*)\s*ms', stdout.decode())
        if match:
            return float(match.group(1))
    else:
        print(f"Error pinging {ip_address}: {stderr}")
        return None

def ping_client(ip_address):
    ping_time = get_ping(ip_address)
    if ping_time is not None:
        print(f"Ping time to {ip_address}: {ping_time} ms")
    else:
        print(f"Failed to get ping time for {ip_address}")

# Example usage
client_ip = "8.8.8.8"  # Replace with actual client IP
ping_thread = threading.Thread(target=ping_client, args=(client_ip,))
ping_thread.start()
