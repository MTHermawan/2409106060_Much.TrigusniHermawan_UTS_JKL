#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""  
NIM: 2409106060 | Nama: Much. Trigusni Hermawan 
""" 

import paramiko 
from pysnmp.hlapi.v3arch.asyncio import * 
  
host_vm = "127.0.0.1" 
port_ssh_vm = 2222 
user_ssh = "mthermawan" 
pass_ssh = "2409106060" 
  
  
def cek_ssh(): 
    client = paramiko.SSHClient() 
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    try: 
        client.connect(host_vm, port=port_ssh_vm, username=user_ssh, password=pass_ssh, timeout=5) 
        stdin, stdout, stderr = client.exec_command("hostname") 
        hasil_hostname = stdout.read().decode().strip() 
        stdin, stdout, stderr = client.exec_command("whoami") 
        hasil_whoami = stdout.read().decode().strip() 
        print("[SSH] hostname VM: " + hasil_hostname) 
        print("[SSH] whoami di VM: " + hasil_whoami) 
        return {
            "status": "BERHASIL",
            "username": user_ssh,
            "host": host_vm,
            "error": None,
            "output": {"hostname": hasil_hostname, "whoami": hasil_whoami},
        }
    except Exception as e: 
        print("[SSH] GAGAL: " + str(e))
        return {
            "status": "GAGAL",
            "username": user_ssh,
            "host": host_vm,
            "error": str(e),
            "output": {},
        }
    finally:
        client.close()
