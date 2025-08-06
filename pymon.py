import socket
import time
import streamlit as st

# Liste personnalisable de services à surveiller
services = [
    {"host": "google.com", "port": 80, "name": "HTTP Google"},
    {"host": "github.com", "port": 443, "name": "HTTPS GitHub"},
    {"host": "127.0.0.1", "port": 22, "name": "SSH Localhost"}
]

def check_service(host, port):
    try:
        start = time.time()
        sock = socket.create_connection((host, port), timeout=3)
        sock.close()
        duration = round((time.time() - start) * 1000, 2)
        return True, duration
    except Exception:
        return False, None

st.set_page_config(page_title="PyMon", page_icon="📡")
st.title("📡 PyMon – Interface de monitoring réseau")

st.markdown("Clique sur **Analyser** pour vérifier l’état des services réseau.\n")

if st.button("Analyser les services"):
    with st.spinner("Analyse en cours..."):
        for service in services:
            status, duration = check_service(service["host"], service["port"])
            if status:
                st.success(f"✅ {service['name']} est UP ({duration} ms)")
            else:
                st.error(f"❌ {service['name']} est DOWN ({service['host']}:{service['port']})")
