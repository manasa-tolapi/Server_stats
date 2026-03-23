import psutil
import json
import datetime
import os
import time

# LOG_HEALTH = "health_logs.json"
LOG_REPORTS = "health_reports.txt"

def server_health_check():
    # while True:
    # for i in range(10):
    #     cpu = psutil.cpu_percent(interval = 1)
    #     ram = psutil.virtual_memory().percent
    #     disk = psutil.disk_usage('/').percent
    #     curr_time = datetime.datetime.now().isoformat()
    #     report = f"CPU: {cpu}%, RAM: {ram}%, DISK: {disk}, at {curr_time} \n"
    #     print(report)
    #     with open(LOG_REPORTS, "a") as f:
    #         f.write(report)
    #     time.sleep(2)

    cpu = psutil.cpu_percent(interval = 1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    curr_time = datetime.datetime.now().isoformat()
    report = f"CPU: {cpu}%, RAM: {ram}%, DISK: {disk}, at {curr_time} \n"
    return report

# server_health_check()
