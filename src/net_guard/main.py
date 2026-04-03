#!/usr/bin/env python3
"""
Główny agent monitorujący Network Guard.
Realizuje asynchroniczny monitoring ICMP oraz powiadomienia via Telegram API.
"""
import os
import time
import requests
import subprocess
from dotenv import load_dotenv

# Ładowanie bezpiecznych zmiennych środowiskowych
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("AUTHORIZED_USERS")
TARGET_HOST = "1.1.1.1"

def check_ping(host: str) -> bool:
    """Weryfikuje dostępność hosta używając protokołu ICMP."""
    try:
        # Wykorzystanie natywnego ping w Linuksie (1 pakiet, timeout 2s)
        output = subprocess.run(["ping", "-c", "1", "-W", "2", host], 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE)
        return output.returncode == 0
    except Exception as e:
        print(f"Błąd krytyczny podczas pomiaru ICMP: {e}")
        return False

def send_telegram_alert(message: str):
    """Przesyła zaszyfrowany alert przez REST API Telegramu."""
    if not BOT_TOKEN or not CHAT_ID:
        print("Brak tokenu bota lub ID użytkownika.")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    
    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Błąd wysyłania powiadomienia API: {e}")

def daemon_loop():
    """Główna pętla nienadzorowanego agenta (unattended system)."""
    print(f"Uruchomiono Network Guard PID: {os.getpid()}")
    is_down = False
    
    while True:
        if not check_ping(TARGET_HOST):
            if not is_down:
                print("Wykryto awarię sieciową warstwy 3 (L3)!")
                send_telegram_alert("⚠️ *ALERT:* Utracono łączność sieciową z internetem (Brak odpowiedzi ICMP).")
                is_down = True
        else:
            if is_down:
                print("Przywrócono połączenie sieciowe.")
                send_telegram_alert("✅ *INFO:* Połączenie sieciowe zostało przywrócone.")
                is_down = False
                
        # Cykliczne odpytywanie w celu minimalizacji wywłaszczeń CPU (context switching)
        time.sleep(30)

if __name__ == "__main__":
    daemon_loop()
