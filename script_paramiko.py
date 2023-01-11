#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko
from getpass import getpass
import time

ip = raw_input("Por favor ingrese la direccion IP: ")
username = raw_input("Por favor ingrese el nombre de usuario: ")
password = getpass()

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, port=22, username=username,  
                        password=password,
                        look_for_keys=False, allow_agent=False)

remote_conn = remote_conn_pre.invoke_shell()
remote_conn.send("show ip interface brief\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print output


