#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama/NIM : Much. Trigusni Hermawan / 2409106060
File     : main.py
Tujuan   : Mengintegrasikan semua modul lalu mencetak satu laporan akhir cabang.
Pembuat  : Much. Trigusni Hermawan
"""

import asyncio

import identitas
import netconf_modul
import snmp_modul
import ssh_modul
import telemetry_modul


class LaporanCabang:
    """Menampung identitas cabang dan menampilkan hasil seluruh modul sebagai satu laporan."""

    def __init__(self, nama, nim, id_perangkat):
        self.nama = nama
        self.nim = nim
        self.id_perangkat = id_perangkat

    def tampilkan_laporan(self, hasil_ssh, hasil_snmp, pesan_netconf, hasil_telemetry):
        garis = "=" * 62
        print(f"\n{garis}\nLAPORAN AKHIR CABANG VIRTUAL\n{garis}")
        print(f"Nama / NIM   : {self.nama} / {self.nim}")
        print(f"ID perangkat : {self.id_perangkat}")

        print("\n1. SSH")
        print(f"   Status : {hasil_ssh['status']} ({hasil_ssh['username']}@{hasil_ssh['host']})")
        if hasil_ssh["error"]:
            print(f"   Alasan : {hasil_ssh['error']}")
        for perintah, keluaran in hasil_ssh["output"].items():
            ringkas = keluaran.splitlines()[-1] if keluaran else "-"
            print(f"   $ {perintah:<9}: {ringkas}")

        print("\n2. SNMP")
        print(f"   Status : {hasil_snmp['status']} (OID {hasil_snmp['oid']})")
        if hasil_snmp["status"] == "BERHASIL":
            print(f"   sysName: {hasil_snmp['sysName']}")
        else:
            print(f"   Alasan : {hasil_snmp['error']}")

        print("\n3. NETCONF")
        jumlah_baris = len(pesan_netconf.splitlines())
        print(f"   Pesan <rpc><edit-config> dibuat ({jumlah_baris} baris XML, VLAN ID {int(identitas.kode_cabang)})")

        print("\n4. Telemetry (cpuUsage)")
        for nama_sampel, isi in hasil_telemetry.items():
            print(f"   {nama_sampel}: {isi['cpuUsage']:>3}% -> {isi['status']}")
        print(garis)


def main():
    print("== Memulai pengecekan cabang ==")
    id_perangkat = identitas.buat_id_perangkat("RTR", 1)

    print("\n[1/4] SSH")
    hasil_ssh = ssh_modul.cek_ssh()

    print("\n[2/4] SNMP")
    hasil_snmp = asyncio.run(snmp_modul.cek_snmp())

    print("\n[3/4] NETCONF")
    pesan_netconf = netconf_modul.buat_pesan_netconf()
    print(pesan_netconf)

    print("\n[4/4] Telemetry")
    hasil_telemetry = telemetry_modul.klasifikasi_telemetry()

    LaporanCabang(identitas.nama, identitas.nim, id_perangkat).tampilkan_laporan(
        hasil_ssh, hasil_snmp, pesan_netconf, hasil_telemetry
    )


if __name__ == "__main__":
    main()