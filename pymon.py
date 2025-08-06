import socket
import time

# Liste des services à surveiller
services = [
    {"host": "google.com", "port": 80, "name": "HTTP Google"},
    {"host": "github.com", "port": 443, "name": "HTTPS GitHub"},
    {"host": "127.0.0.1", "port": 22, "name": "SSH Localhost"}
]

def check_service(host, port, name):
    try:
        start = time.time()
        sock = socket.create_connection((host, port), timeout=3)
        sock.close()
        duration = round((time.time() - start) * 1000, 2)
        print(f"[✅] {name} est UP ({duration} ms)")
    except Exception as e:
        print(f"[❌] {name} est DOWN ({host}:{port})")

if __name__ == "__main__":
    print("📡 PyMon – Monitoring des services\n")
    for service in services:
        check_service(service["host"], service["port"], service["name"])
