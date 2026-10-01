## Biodata
Nama: Much. Trigusni Hermawan
NIM: 2409106060

## Struktur Project
- `identitas.py`        : identitas cabang dan pembuat ID perangkat
- `ssh_modul.py`        : akses SSH (Paramiko)
- `snmp_modul.py`       : pengambilan sysName lewat SNMPv2c (PySNMP)
- `netconf_modul.py`    : pembuatan pesan NETCONF <rpc><edit-config>
- `telemetry_modul.py`  : klasifikasi sampel cpuUsage
- `main.py`             : integrasi dan laporan akhir
- `.gitignore`          : Mengabaikan file venv untuk di-commit

## Cara Menjalankan
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export JKL_HOST=<IP_VM>
python main.py
```

## Ringkasan Personalisasi
- Username SSH berpola `admin_<kode_cabang>`, community SNMP berpola `comm_<kode_cabang>`.
- VLAN ID diambil dari angka kode_cabang (3 digit terakhir NIM).
- cpuUsage = batas bawah kelas + digit NIM x pengali (rumus di `telemetry_modul.py`).
- Password tidak disimpan di repo; dibaca dari environment variable atau diketik saat dijalankan.