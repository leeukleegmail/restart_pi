import schedule
import time

from pi_restart import restart_pi


schedule.every().day.at("12:00", "Europe/Amsterdam").do(restart_pi())

while True:
    schedule.run_pending()
    time.sleep(60)
