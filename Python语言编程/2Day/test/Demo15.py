import pexpect
import re
import time
import psutil
import threading


def ssh_command(user='khm',host='localhost',password='1qaz@WSX'):
    ssh_newkey="Are you sure want to countine connecting"

    pass


def getCPUInfo():
    child=ssh_command()
    child.sendline("cat /pro/cpuinfo")



