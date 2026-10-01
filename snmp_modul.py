#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""  
NIM: 2409106060 | Nama: Much. Trigusni Hermawan 
""" 

import asyncio
import paramiko 
from pysnmp.hlapi.v3arch.asyncio import * 
  
nim = "2409106060" 
host_vm = "127.0.0.1" 
port_ssh_vm = 2222 
port_snmp_vm = 1161 
user_ssh = "mthermawan" 
pass_ssh = "2409106060" 
community = "comm_060" 
  
  
def cek_ssh(): 
    try: 
        client = paramiko.SSHClient() 
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        client.connect(host_vm, port=port_ssh_vm, username=user_ssh, password=pass_ssh, timeout=5) 
        stdin, stdout, stderr = client.exec_command("hostname") 
        hasil_hostname = stdout.read().decode().strip() 
        stdin, stdout, stderr = client.exec_command("whoami") 
        hasil_whoami = stdout.read().decode().strip() 
        print("[SSH] hostname VM: " + hasil_hostname) 
        print("[SSH] whoami di VM: " + hasil_whoami) 
        client.close() 
    except Exception as e: 
        print("[SSH] GAGAL: " + str(e)) 
  
  
async def cek_snmp(): 
    try: 
        errorIndication, errorStatus, errorIndex, varBinds = await get_cmd( 
            SnmpEngine(), 
            CommunityData(community), 
            await UdpTransportTarget.create((host_vm, port_snmp_vm)), 
            ContextData(), 
            ObjectType(ObjectIdentity("1.3.6.1.2.1.1.5.0")) 
        )
        if errorIndication: 
            print("[SNMP] GAGAL: " + str(errorIndication)) 
        elif errorStatus: 
            print("[SNMP] GAGAL: " + errorStatus.prettyPrint()) 
        else: 
            for vb in varBinds: 
                print("[SNMP] sysName VM: " + str(vb[1])) 
    except Exception as e: 
        print("[SNMP] GAGAL: " + str(e)) 
  
  
cek_ssh() 
asyncio.run(cek_snmp()) 
print("Pengecekan selesai untuk NIM " + nim + ".")