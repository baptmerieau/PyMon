# PyMon 

PyMon est un outil léger de monitoring réseau écrit en Python. Il permet de surveiller l’état de plusieurs services (HTTP, SSH, FTP...) en temps réel.

##  Fonctionnalités

- Vérifie la disponibilité d’un service réseau (host:port)
- Affiche le statut UP/DOWN et le temps de réponse
- Utilise les sockets Python (pas de dépendance externe)

## Lancer PyMon

```bash
git clone https://github.com/baptmerieau/PyMon.git
cd PyMon
python pymon.py
