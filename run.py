"""
Punto di avvio per produzione su Windows.
Usa Waitress come WSGI server — stabile, multi-thread, zero dipendenze C.

Avvio:
    python run.py

Variabili d'ambiente rilevanti (configurabili in .env):
    HOST     — indirizzo di ascolto (default: 0.0.0.0 = tutte le interfacce)
    PORT     — porta TCP (default: 8080)
"""
import os
import logging
from dotenv import load_dotenv

load_dotenv()

from waitress import serve
from app import app

host = os.getenv("HOST", "0.0.0.0")
port = int(os.getenv("PORT", "8080"))
threads = int(os.getenv("THREADS", "8"))

logging.info("=" * 60)
logging.info(f"RFQ Database in ascolto su http://{host}:{port}")
logging.info(f"Accessibile dalla rete locale — proteggi con Windows Firewall")
logging.info("=" * 60)

serve(app, host=host, port=port, threads=threads)
