# rpi_luma_oled

Scripts for SH1106 display module

## Installation

### 1. enable i2c interface using `sudo raspi-config`

### 2. Update python3 version

```bash
sudo apt-get update
sudo apt-get install python3-dev build-essential
```

### 3. Then follow [Luma OLED Project](https://luma-oled.readthedocs.io/en/latest/intro.html)

### 4. Enable cron service

```bash
crontab -e
```

Add the following line to the end of the file (check username and path)

```bash
@reboot sleep 10 && /home/pi/luma-env/bin/python /home/pi/rpi_luma_oled/stats.py
```

Add cron service to startup

```bash
sudo systemctl enable cron.service
```
