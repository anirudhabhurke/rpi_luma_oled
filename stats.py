from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from time import sleep
import subprocess
from PIL import ImageFont
from pathlib import Path

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)


def make_font(name, size):
    font_path = str(Path(__file__).resolve().parent.joinpath("fonts", name))
    return ImageFont.truetype(font_path, size)


font = make_font("FiraCode-Regular.ttf", 11)

while True:
    with canvas(device) as draw:
        cmd = "hostname -I | cut -d' ' -f1"
        IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = 'cut -f 1 -d " " /proc/loadavg'
        CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB\", $3,$2 }'"
        MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
        Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")
        ip_text = "IP: " + IP
        cpu_text = "CPU load: " + CPU
        mem_text = MemUsage
        disk_text = Disk
        draw.text((0, 0), ip_text, fill="white", font=font)
        draw.text((0, 15), cpu_text, fill="white", font=font)
        draw.text((0, 30), mem_text, fill="white", font=font)
        draw.text((0, 45), disk_text, fill="white", font=font)
    sleep(5)
