#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama file : 2409106060_modul.py
Tujuan    : File module yang berisikan fungsi membantu pembuatan program utama.
Pembuat   : Hermawan
"""

nim = "2409106060"
nama = "Hermawan"
kode_cabang = nim[-3:]

def buat_id_perangkat(jenis, nomor):
    id_perangkat = f"{jenis}-{kode_cabang}-{nomor:02d}"
    return id_perangkat
