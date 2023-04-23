import paramiko
from env import user, password, host, reboot_command


def restart_pi():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password, timeout=10)
    stdin, stdout, stderr = ssh.exec_command(reboot_command)
    for line in iter(stdout.readline, ""):
        print(line, end="")
    ssh.close()
