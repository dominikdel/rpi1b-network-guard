# Raspberry Pi 1B - Network Guard

<pre>
.~~.  .~~.
'. \ ' ' /.'
.~.~~~..~.
:.~.'~'.~. :
~ (   ) (   ) ~
( : '~'.~.'~' : )
 ~.~ (   ) ~. ~
  (  : '~' :  )
   '~.~~~. ~'
       '~'
Raspberry Pi 1B - Network Guard
</pre>

## 📌 Przegląd Projektu (Overview)
Profesjonalna implementacja systemu monitorowania infrastruktury sieciowej na układzie Raspberry Pi 1B, z wykorzystaniem drastycznej optymalizacji jądra Linux.

![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi_1B-C51A4A?style=for-the-badge&logo=raspberrypi&logoColor=white)
![Debian](https://img.shields.io/badge/Debian_OS_Lite-A81D33?style=for-the-badge&logo=debian&logoColor=white)
![UFW](https://img.shields.io/badge/UFW_Firewall-000000?style=for-the-badge&logo=linux&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram_Bot_API-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![zRAM](https://img.shields.io/badge/zRAM_lz4_Opt-FCC624?style=for-the-badge&logo=linux&logoColor=black)

## 🛠 Topologia Katalogów
Zgodnie z najlepszymi praktykami inżynierii oprogramowania (DRY & Separation of Concerns):
- `src/` - Asynchroniczny agent monitorujący w Pythonie.
- `infrastructure/` - Usługi `systemd` i skrypty zabezpieczające.
- `.github/` - Szablony i automatyzacja CI/CD.

## 🚀 Instrukcja Wdrożenia
1. Klonowanie repozytorium:
   ```bash
   git clone https://github.com/TwojProfil/rpi-network-guard.git
   cd rpi-network-guard
   ```
2. Instalacja zależności ze standardu `pyproject.toml`.
3. Konfiguracja `.env` na bazie `.env.example`.
4. Linkowanie usługi do menedżera systemu:
   ```bash
   sudo ln -s $(pwd)/infrastructure/net-monitor.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable --now net-monitor.service
   ```

## 🔒 Architektura Bezpieczeństwa
System operuje na polityce Zero Trust poprzez firewall UFW (Default Deny Incoming). Dozwolony jest jedynie wychodzący ruch ICMP/TCP w celu raportowania stanu do API Telegrama.