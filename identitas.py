#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama file : 2409106060_modul.py
Tujuan    : File module yang berisikan fungsi membantu pembuatan program utama.
Pembuat   : Hermawan
"""

kode_cabang = "060"

def buat_id_perangkat(jenis, nomor):
    id_perangkat = f"{jenis}-{kode_cabang}-{nomor:02d}"
    return id_perangkat
