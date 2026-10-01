#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""  
NIM: 2409106060 | Nama: Much. Trigusni Hermawan 
""" 

from pysnmp.hlapi.v3arch.asyncio import * 
  
host_vm = "127.0.0.1" 
port_snmp_vm = 1161 
community = "comm_060" 
  
async def cek_snmp(): 
    oid = "1.3.6.1.2.1.1.5.0"
    try: 
        errorIndication, errorStatus, errorIndex, varBinds = await get_cmd( 
            SnmpEngine(), 
            CommunityData(community), 
            await UdpTransportTarget.create((host_vm, port_snmp_vm)), 
            ContextData(), 
            ObjectType(ObjectIdentity(oid)) 
        )
        if errorIndication: 
            error = str(errorIndication)
            print("[SNMP] GAGAL: " + error)
            return {"status": "GAGAL", "oid": oid, "sysName": None, "error": error}
        elif errorStatus: 
            error = errorStatus.prettyPrint()
            print("[SNMP] GAGAL: " + error)
            return {"status": "GAGAL", "oid": oid, "sysName": None, "error": error}
        else: 
            sys_name = str(varBinds[0][1]) if varBinds else ""
            for vb in varBinds: 
                print("[SNMP] sysName VM: " + str(vb[1])) 
            return {"status": "BERHASIL", "oid": oid, "sysName": sys_name, "error": None}
    except Exception as e: 
        error = str(e)
        print("[SNMP] GAGAL: " + error)
        return {"status": "GAGAL", "oid": oid, "sysName": None, "error": error}