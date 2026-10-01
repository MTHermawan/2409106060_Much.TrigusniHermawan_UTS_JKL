#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama/NIM : Nama Lengkap Kamu / 2409106060
File     : netconf_modul.py
Tujuan   : Membangun pesan NETCONF <rpc><edit-config> untuk membuat VLAN (ID = kode_cabang).
Pembuat  : Nama Lengkap Kamu
"""

from identitas import kode_cabang

NS_NETCONF = "urn:ietf:params:xml:ns:netconf:base:1.0"
NS_NATIVE = "http://cisco.com/ns/yang/Cisco-IOS-XE-native"
NS_VLAN = "http://cisco.com/ns/yang/Cisco-IOS-XE-vlan"


def buat_pesan_netconf(message_id="101"):
    """Membangun string XML <rpc><edit-config> pembuat VLAN lalu mengembalikannya."""
    vlan_id = int(kode_cabang)
    if not 1 <= vlan_id <= 4094:
        raise ValueError(f"VLAN ID {vlan_id} di luar rentang 1-4094")

    baris = [
        "<!-- MESSAGES LAYER -->",
        f'<rpc message-id="{message_id}" xmlns="{NS_NETCONF}" xmlns:nc="{NS_NETCONF}">',
        "  <!-- OPERATIONS LAYER -->",
        "  <edit-config>",
        "    <target><running/></target>",
        "    <!-- CONTENT LAYER -->",
        "    <config>",
        f'      <native xmlns="{NS_NATIVE}">',
        "        <vlan>",
        f'          <vlan-list xmlns="{NS_VLAN}" nc:operation="create">',
        f"            <id>{vlan_id}</id>",
        f"            <name>CABANG_{kode_cabang}</name>",
        "          </vlan-list>",
        "        </vlan>",
        "      </native>",
        "    </config>",
        "  </edit-config>",
        "</rpc>",
    ]
    return "\n".join(baris)


if __name__ == "__main__":
    print(buat_pesan_netconf())