#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama/NIM : Nama Lengkap Kamu / 2409106060
File     : telemetry_modul.py
Tujuan   : Mengklasifikasikan sampel cpuUsage (mirip hasil decode GPB) menjadi NORMAL/WASPADA/KRITIS.
Pembuat  : Nama Lengkap Kamu
"""

from identitas import nim

digit = [int(d) for d in nim]

# Nilai diturunkan dari 3 digit terakhir NIM: batas_bawah_kelas + digit * pengali
data_telemetry = {
    "sampel_1": {"waktu": "10:00:00", "cpuUsage": 10 + digit[-1] * 4},  # 10..46 -> NORMAL
    "sampel_2": {"waktu": "10:00:05", "cpuUsage": 50 + digit[-2] * 3},  # 50..77 -> WASPADA
    "sampel_3": {"waktu": "10:00:10", "cpuUsage": 81 + digit[-3] * 2},  # 81..99 -> KRITIS
}


def _klasifikasi(nilai):
    """Di atas 80 = KRITIS, 50-80 = WASPADA, di bawah 50 = NORMAL."""
    if nilai > 80:
        return "KRITIS"
    if nilai >= 50:
        return "WASPADA"
    return "NORMAL"


def klasifikasi_telemetry():
    """Iterasi data_telemetry, cetak dan kembalikan hasil klasifikasi (dict)."""
    hasil = {}
    for nama_sampel, isi in data_telemetry.items():
        status = _klasifikasi(isi["cpuUsage"])
        hasil[nama_sampel] = {"cpuUsage": isi["cpuUsage"], "status": status}
        print(f"[TELEMETRY] {nama_sampel} ({isi['waktu']}) cpuUsage={isi['cpuUsage']}% -> {status}")
    return hasil


if __name__ == "__main__":
    klasifikasi_telemetry()