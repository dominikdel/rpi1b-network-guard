# 🖥️ Raspberry Pi 1B — Performance Optimization & Network Guard

<p align="center">
  <img src="https://img.shields.io/badge/Hardware-Raspberry%20Pi%201B-red?style=for-the-badge&logo=raspberrypi&logoColor=white"/>
  <img src="https://img.shields.io/badge/OS-Raspberry%20Pi%20OS%20Lite-green?style=for-the-badge&logo=linux&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Firewall-UFW-orange?style=for-the-badge&logo=linux&logoColor=white"/>
  <img src="https://img.shields.io/badge/Alerts-Telegram%20Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"/>
</p>

---

## 📋 Opis projektu

Celem projektu było **przywrócenie pełnej użyteczności legacy hardware** (Raspberry Pi 1B, 512MB RAM) poprzez głęboką optymalizację systemu **Raspberry Pi OS Lite** oraz implementację autorskiego systemu monitorowania infrastruktury sieciowej z powiadomieniami w czasie rzeczywistym.

> 💡 Projekt udowadnia, że przy odpowiedniej konfiguracji jądra Linux i selektywnym doborze usług, **sprzęt sprzed dekady** może służyć jako stabilne i bezpieczne narzędzie w nowoczesnej infrastrukturze sieciowej.

---

## 🛠️ Wykorzystane technologie

| Kategoria | Szczegóły |
|---|---|
| **Hardware** | Raspberry Pi 1B — Single-core 700MHz, 512MB RAM |
| **System operacyjny** | Raspberry Pi OS Lite (32-bit, Debian Bookworm) |
| **Język** | Python 3.11 |
| **Zabezpieczenia** | UFW (Uncomplicated Firewall) |
| **Integracje** | Telegram Bot API (`requests`) |
| **Zarządzanie pamięcią** | zRAM, Linux Kernel Swap Management |

---

## 🚀 Kluczowe optymalizacje systemu

W celu zapewnienia płynności działania na mocno ograniczonych zasobach, przeprowadzono następujące kroki:

### 1. ⚡ Overclocking CPU
Stabilne podniesienie taktowania procesora z **700MHz do 900MHz** (profil High) bez utraty stabilności systemu.

### 2. 🎮 GPU Memory Split
Redukcja przydzielonej pamięci wideo do **16MB** — tryb Headless (brak wyświetlacza), co oddaje więcej RAM procesom systemowym.

### 3. 🧠 Implementacja zRAM
Zastąpienie fizycznego swapu na karcie SD **skompresowaną przestrzenią w RAM** (algorytm `lz4`).

```bash
sudo systemctl status zramswap
zramctl
```

**Korzyści:**
- Znaczna redukcja opóźnień I/O
- Wydłużenie żywotności karty SD
- Szybszy dostęp do danych swap

### 4. 🧹 System Debloating
Wyłączenie zbędnych usług systemowych zwalniających zasoby CPU:

```bash
sudo systemctl disable --now avahi-daemon
sudo systemctl disable --now triggerhappy
sudo systemctl disable --now ModemManager
```

### 5. 🔒 Hardening — UFW Firewall
Konfiguracja firewalla w modelu **"Default Deny"** — domyślne blokowanie całego ruchu przychodzącego:

```bash
sudo apt update && sudo apt install ufw -y
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw enable
sudo ufw status verbose
```

---

## 🛡️ Network Guard (Strażnik Sieci)

Zaimplementowano autorski skrypt w Pythonie pełniący rolę **lekkiego agenta monitorującego** infrastrukturę sieciową.

### Funkcjonalności

- **📡 Monitoring ICMP** — cykliczne sprawdzanie dostępności bramy domyślnej oraz zewnętrznych serwerów DNS
- **🔍 Detekcja incydentów** — identyfikacja błędnych konfiguracji firewalla oraz awarii warstwy 3 (IP)
- **📲 System alertów** — natychmiastowe powiadomienia przez **Telegram Bot API** o każdym incydencie sieciowym
- **⚙️ Automatyzacja** — skrypt działa jako persystentny daemon zarządzany przez `systemd`

### Uruchomienie jako systemd daemon

```bash
sudo systemctl enable net-monitor.service
sudo systemctl start net-monitor.service
sudo systemctl status net-monitor.service
```

---

## 📈 Wyniki i Diagnostyka

Po przeprowadzeniu optymalizacji, system w stanie spoczynku osiąga następujące parametry:

| Metryka | Wartość |
|---|---|
| **Zużycie RAM** | ~56MB / 428MB (ok. **13%**) |
| **Load Average** | ~0.06 |
| **Temperatura CPU** | ~42°C (pasywne chłodzenie + OC) |

```bash
# Sprawdzenie temperatury
vcgencmd measure_temp

# Podgląd zasobów
htop
```

---

## 💡 Wnioski i plany rozwoju

Projekt potwierdza, że **stary sprzęt ≠ bezużyteczny sprzęt**. Przy odpowiednim tuningu jądra Linux i eliminacji zbędnych usług, Raspberry Pi 1B może pełnić rolę niezawodnego i bezpiecznego węzła sieciowego.

### 🔮 Planowane funkcje
- [ ] **Pi-hole** — sieciowy DNS sinkholing i blokowanie reklam
- [ ] Rozszerzone logowanie zdarzeń sieciowych
- [ ] Dashboard webowy do podglądu metryk w czasie rzeczywistym

---

## 📄 Licencja

Projekt udostępniony na licencji [MIT](LICENSE).

---

<p align="center">
  Wykonane z pasją do Linuksa i cyberbezpieczeństwa 🐧🔐
</p>
