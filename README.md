# 🖥️ Raspberry Pi 1B — Performance Optimization & Network Guard

<p align="center">
  <img src="https://img.shields.io/badge/Hardware-Raspberry%20Pi%201B-red?style=for-the-badge&logo=raspberrypi&logoColor=white"/>
  <img src="https://img.shields.io/badge/OS-Raspberry%20Pi%20OS%20Lite-green?style=for-the-badge&logo=linux&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Firewall-UFW-orange?style=for-the-badge&logo=linux&logoColor=white"/>
  <img src="https://img.shields.io/badge/Alerts-Telegram%20Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"/>
</p>

---

## 📋 Project Overview

The primary goal of this project was to **restore full operational capability to legacy hardware** (Raspberry Pi 1B, 512MB RAM) through deep optimization of **Raspberry Pi OS Lite**, combined with a custom-built network infrastructure monitoring system featuring real-time Telegram alerting.

> 💡 This project proves that with proper Linux kernel tuning and selective service deployment, **decade-old hardware** can still serve as a reliable and secure asset in modern network infrastructures.

---

## 🛠️ Technologies & Tools

| Category | Details |
|---|---|
| **Hardware** | Raspberry Pi 1B — Single-core 700MHz, 512MB RAM |
| **Operating System** | Raspberry Pi OS Lite (32-bit, Debian Bookworm) |
| **Language** | Python 3.11 |
| **Security** | UFW (Uncomplicated Firewall) |
| **Integrations** | Telegram Bot API (`requests`) |
| **Memory Management** | zRAM, Linux Kernel Swap Management |

---

## 🚀 Key System Optimizations

To ensure smooth operation under severely constrained resources, the following steps were implemented:

### 1. ⚡ CPU Overclocking
Safely increased CPU frequency from **700MHz to 900MHz** (High profile) without any stability loss.

### 2. 🎮 GPU Memory Split
Reduced video memory allocation to **16MB** — Headless mode (no display), freeing more RAM for system processes.

### 3. 🧠 zRAM Implementation
Replaced physical SD card swap with **compressed RAM blocks** (using the `lz4` algorithm).

```bash
sudo systemctl status zramswap
zramctl
```

**Benefits:**
- Significant reduction in I/O latency
- Extended SD card lifespan
- Faster swap data access

### 4. 🧹 System Debloating
Disabled redundant background services to free up CPU cycles:

```bash
sudo systemctl disable --now avahi-daemon
sudo systemctl disable --now triggerhappy
sudo systemctl disable --now ModemManager
```

### 5. 🔒 Hardening — UFW Firewall
Configured firewall using a strict **"Default Deny"** incoming policy:

```bash
sudo apt update && sudo apt install ufw -y
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw enable
sudo ufw status verbose
```

---

## 🛡️ Network Guard (Monitoring Agent)

A custom lightweight Python script acting as a **persistent network monitoring daemon**.

### Features

- **📡 ICMP Monitoring** — cyclic availability checks on the default gateway and external DNS servers
- **🔍 Incident Detection** — identifies firewall misconfigurations and Layer 3 (IP) routing failures
- **📲 Alerting System** — instant notifications via **Telegram Bot API** on every network incident
- **⚙️ Automation** — runs as a persistent background daemon managed by `systemd`

### Setup & Run

1. Clone the repository and configure your bot token in `monitoring.py`:

```bash
git clone https://github.com/dominikdel/rpi1b-network-guard.git
cd rpi1b-network-guard
nano monitoring.py
```

2. Install dependencies:

```bash
pip3 install requests
```

3. Deploy as a systemd daemon:

```bash
sudo systemctl enable net-monitor.service
sudo systemctl start net-monitor.service
sudo systemctl status net-monitor.service
```

---

## 📈 Results & Diagnostics

Post-optimization metrics at system idle:

| Metric | Value |
|---|---|
| **RAM Usage** | ~56MB / 428MB (approx. **13%**) |
| **Load Average** | ~0.06 |
| **CPU Temperature** | ~42°C (passive cooling + OC) |

```bash
# Check CPU temperature
vcgencmd measure_temp

# Resource overview
htop
```

---

## 💡 Conclusions & Future Scope

This project confirms that **old hardware ≠ useless hardware**. With proper Linux kernel tuning and elimination of unnecessary services, the Raspberry Pi 1B can serve as a reliable and secure network node.

### 🔮 Planned Features
- [ ] **Pi-hole** — network-wide DNS sinkholing and ad blocking
- [ ] Extended network event logging
- [ ] Web dashboard for real-time metrics monitoring

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">
  Built with passion for Linux and cybersecurity 🐧🔐
</p>
