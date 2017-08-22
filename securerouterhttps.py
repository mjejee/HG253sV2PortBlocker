#!/usr/bin/env python
from nmap import PortScanner
from subprocess import call
import time
import os
import logging

HOST = "" # Your router local ip address
PORT = 443
arg = "-sS -n"
interval = 15
routernohttps_path = "" # Path to the expect script

logging.basicConfig(filename="/var/log/https_disable.log", level=logging.INFO)

def isHTTPSopen ():
    try:
        scanner = PortScanner()
        scanner.scan(HOST, str(PORT), sudo=True, arguments=arg)
        return scanner[HOST]['tcp'][PORT]['state'] == "open"
    except KeyError:
        logging.warning("{} - nmap Key error. Probably the router is off".format(time.asctime()))
    except:
        logging.error("{} - nmap Scan error".format(time.asctime()))

def closeHTTPS():
    call(["expect", routernohttps_path])


def store_pid():
    pid = str(os.getpid())
    with open('/tmp/srh_pid', 'w') as f:
        f.write(pid)


store_pid()
logging.info("{} - Daemon started".format(time.asctime()))

while (True):
    if isHTTPSopen():
        logging.warning("{} - HTTPS state check: OPEN".format(time.asctime()))
        closeHTTPS()
    time.sleep(interval)
