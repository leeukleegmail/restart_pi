import schedule
import time

from ssh_commands import run_command_via_ssh
from env import user, password, host, reboot_command


schedule.every().day.at("12:00", "Europe/Amsterdam").do(run_command_via_ssh(host, user, password, reboot_command))

while True:
    schedule.run_pending()
    time.sleep(60)
