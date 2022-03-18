#!/usr/bin/python3
# -*- coding: utf-8 -*-

###################
#    This module implements a NetworkScanner.
#    Copyright (C) 2021  Maurice Lambert

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
###################

"""
This module implements a NetworkScanner.

~# python3 NetworkScanner.py -t 172.18.0.1-172.18.0.15

NetworkScanner  Copyright (C) 2021, 2022  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.


PythonToolsKit  Copyright (C) 2022  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.

172.18.0.9
172.18.0.13
172.18.0.14
172.18.0.10

~# python3 NetworkScanner.py -d --noping --hostname --ports 22 80 -p 445 139 443 -T 1 -R -s -t 172.18.0.0/28

NetworkScanner  Copyright (C) 2021, 2022  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.


PythonToolsKit  Copyright (C) 2022  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.

[2016-06-22 05:01:12] DEBUG    (10) {__main__ - NetworkScanner.py:490} Build NetworkScanner...
[2016-06-22 05:01:12] DEBUG    (10) {__main__ - NetworkScanner.py:501} Configure real time...
[2016-06-22 05:01:12] DEBUG    (10) {__main__ - NetworkScanner.py:509} The scan begins...
[2016-06-22 05:01:12] INFO     (20) {__main__ - NetworkScanner.py:295} Run asynchronous scan (without scapy).
[2016-06-22 05:01:12] INFO     (20) {__main__ - NetworkScanner.py:204} Start asynchronous scan without scapy...
[2016-06-22 05:01:12] DEBUG    (10) {__main__ - NetworkScanner.py:350} Check '172.18.0.11' (step 1: PING)...
[2016-06-22 05:01:12] DEBUG    (10) {__main__ - NetworkScanner.py:355} Check '172.18.0.11' (step 2: HOSTNAME)...
[2016-06-22 05:01:21] DEBUG    (10) {__main__ - NetworkScanner.py:365} Check '172.18.0.11' (step 3: TCP connections)...
[2016-06-22 05:01:21] DEBUG    (10) {__main__ - NetworkScanner.py:350} Check '172.18.0.2' (step 1: PING)...
[2016-06-22 05:01:21] DEBUG    (10) {__main__ - NetworkScanner.py:355} Check '172.18.0.2' (step 2: HOSTNAME)...
[2016-06-22 05:01:30] DEBUG    (10) {__main__ - NetworkScanner.py:365} Check '172.18.0.2' (step 3: TCP connections)...
[2016-06-22 05:01:30] DEBUG    (10) {__main__ - NetworkScanner.py:350} Check '172.18.0.3' (step 1: PING)...
[2016-06-22 05:01:30] DEBUG    (10) {__main__ - NetworkScanner.py:355} Check '172.18.0.3' (step 2: HOSTNAME)...
[2016-06-22 05:01:39] DEBUG    (10) {__main__ - NetworkScanner.py:365} Check '172.18.0.3' (step 3: TCP connections)...
[2016-06-22 05:01:39] DEBUG    (10) {__main__ - NetworkScanner.py:350} Check '172.18.0.7' (step 1: PING)...
[2016-06-22 05:01:39] DEBUG    (10) {__main__ - NetworkScanner.py:355} Check '172.18.0.7' (step 2: HOSTNAME)...
[2016-06-22 05:01:48] DEBUG    (10) {__main__ - NetworkScanner.py:365} Check '172.18.0.7' (step 3: TCP connections)...
[2016-06-22 05:01:48] DEBUG    (10) {__main__ - NetworkScanner.py:350} Check '172.18.0.4' (step 1: PING)...
[2016-06-22 05:01:48] DEBUG    (10) {__main__ - NetworkScanner.py:355} Check '172.18.0.4' (step 2: HOSTNAME)...
[2016-06-22 05:01:57] DEBUG    (10) {__main__ - NetworkScanner.py:365} Check '172.18.0.4' (step 3: TCP connections)...
[2016-06-22 05:01:57] DEBUG    (10) {__main__ - NetworkScanner.py:350} Check '172.18.0.13' (step 1: PING)...
[2016-06-22 05:01:57] DEBUG    (10) {__main__ - NetworkScanner.py:355} Check '172.18.0.13' (step 2: HOSTNAME)...
[2016-06-22 05:02:03] DEBUG    (10) {__main__ - NetworkScanner.py:365} Check '172.18.0.13' (step 3: TCP connections)...
[2016-06-22 05:02:03] DEBUG    (10) {__main__ - NetworkScanner.py:350} Check '172.18.0.14' (step 1: PING)...
[2016-06-22 05:02:03] DEBUG    (10) {__main__ - NetworkScanner.py:355} Check '172.18.0.14' (step 2: HOSTNAME)...
[2016-06-22 05:02:07] DEBUG    (10) {__main__ - NetworkScanner.py:365} Check '172.18.0.14' (step 3: TCP connections)...
[2016-06-22 05:02:07] DEBUG    (10) {__main__ - NetworkScanner.py:350} Check '172.18.0.6' (step 1: PING)...
[2016-06-22 05:02:08] DEBUG    (10) {__main__ - NetworkScanner.py:355} Check '172.18.0.6' (step 2: HOSTNAME)...
[2016-06-22 05:02:17] DEBUG    (10) {__main__ - NetworkScanner.py:365} Check '172.18.0.6' (step 3: TCP connections)...
[2016-06-22 05:02:17] DEBUG    (10) {__main__ - NetworkScanner.py:350} Check '172.18.0.10' (step 1: PING)...
[2016-06-22 05:02:17] DEBUG    (10) {__main__ - NetworkScanner.py:355} Check '172.18.0.10' (step 2: HOSTNAME)...
[2016-06-22 05:02:21] DEBUG    (10) {__main__ - NetworkScanner.py:365} Check '172.18.0.10' (step 3: TCP connections)...
[2016-06-22 05:02:21] DEBUG    (10) {__main__ - NetworkScanner.py:350} Check '172.18.0.8' (step 1: PING)...
[2016-06-22 05:02:21] DEBUG    (10) {__main__ - NetworkScanner.py:355} Check '172.18.0.8' (step 2: HOSTNAME)...
[2016-06-22 05:02:26] DEBUG    (10) {__main__ - NetworkScanner.py:365} Check '172.18.0.8' (step 3: TCP connections)...
[2016-06-22 05:02:26] DEBUG    (10) {__main__ - NetworkScanner.py:350} Check '172.18.0.5' (step 1: PING)...
[2016-06-22 05:02:26] DEBUG    (10) {__main__ - NetworkScanner.py:355} Check '172.18.0.5' (step 2: HOSTNAME)...
[2016-06-22 05:02:35] DEBUG    (10) {__main__ - NetworkScanner.py:365} Check '172.18.0.5' (step 3: TCP connections)...
[2016-06-22 05:02:35] DEBUG    (10) {__main__ - NetworkScanner.py:350} Check '172.18.0.9' (step 1: PING)...
[2016-06-22 05:02:35] DEBUG    (10) {__main__ - NetworkScanner.py:355} Check '172.18.0.9' (step 2: HOSTNAME)...
[2016-06-22 05:02:40] DEBUG    (10) {__main__ - NetworkScanner.py:317} Start handle_UP for '172.18.0.9'...
[2016-06-22 05:02:40] DEBUG    (10) {__main__ - NetworkScanner.py:319} Quit handle_UP for '172.18.0.9'.
[2016-06-22 05:02:40] DEBUG    (10) {__main__ - NetworkScanner.py:350} Check '172.18.0.1' (step 1: PING)...
[2016-06-22 05:02:40] DEBUG    (10) {__main__ - NetworkScanner.py:355} Check '172.18.0.1' (step 2: HOSTNAME)...
[2016-06-22 05:02:49] DEBUG    (10) {__main__ - NetworkScanner.py:365} Check '172.18.0.1' (step 3: TCP connections)...
[2016-06-22 05:02:49] DEBUG    (10) {__main__ - NetworkScanner.py:350} Check '172.18.0.12' (step 1: PING)...
[2016-06-22 05:02:49] DEBUG    (10) {__main__ - NetworkScanner.py:355} Check '172.18.0.12' (step 2: HOSTNAME)...
[2016-06-22 05:02:58] DEBUG    (10) {__main__ - NetworkScanner.py:365} Check '172.18.0.12' (step 3: TCP connections)...
[2016-06-22 05:03:02] DEBUG    (10) {__main__ - NetworkScanner.py:381} '172.18.0.14' is probably not up.
[2016-06-22 05:03:02] DEBUG    (10) {__main__ - NetworkScanner.py:381} '172.18.0.6' is probably not up.
[2016-06-22 05:03:02] DEBUG    (10) {__main__ - NetworkScanner.py:381} '172.18.0.3' is probably not up.
[2016-06-22 05:03:02] DEBUG    (10) {__main__ - NetworkScanner.py:381} '172.18.0.13' is probably not up.
[2016-06-22 05:03:02] DEBUG    (10) {__main__ - NetworkScanner.py:381} '172.18.0.11' is probably not up.
[2016-06-22 05:03:02] DEBUG    (10) {__main__ - NetworkScanner.py:381} '172.18.0.4' is probably not up.
[2016-06-22 05:03:02] DEBUG    (10) {__main__ - NetworkScanner.py:381} '172.18.0.7' is probably not up.
[2016-06-22 05:03:02] DEBUG    (10) {__main__ - NetworkScanner.py:381} '172.18.0.5' is probably not up.
[2016-06-22 05:03:02] DEBUG    (10) {__main__ - NetworkScanner.py:381} '172.18.0.8' is probably not up.
[2016-06-22 05:03:02] DEBUG    (10) {__main__ - NetworkScanner.py:381} '172.18.0.2' is probably not up.
[2016-06-22 05:03:02] DEBUG    (10) {__main__ - NetworkScanner.py:381} '172.18.0.10' is probably not up.
[2016-06-22 05:03:02] DEBUG    (10) {__main__ - NetworkScanner.py:381} '172.18.0.1' is probably not up.
[2016-06-22 05:03:03] DEBUG    (10) {__main__ - NetworkScanner.py:381} '172.18.0.12' is probably not up.
[2016-06-22 05:03:03] DEBUG    (10) {__main__ - NetworkScanner.py:215} Start ARP detection...
[2016-06-22 05:03:04] INFO     (20) {__main__ - NetworkScanner.py:227} Scan end.
[2016-06-22 05:03:04] DEBUG    (10) {__main__ - NetworkScanner.py:511} Scan end.
UP: 172.18.0.9
DOWN:

~# python NetworkScanner.py -d -t 172.18.0.0/28

NetworkScanner  Copyright (C) 2021, 2022  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.


PythonToolsKit  Copyright (C) 2022  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.

[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:651} Build NetworkScanner...
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:662} Configure real time...
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:670} The scan begins...
[2016-06-22 05:02:24] INFO     (20) {__main__ - NetworkScanner.py:445} Run scapy scan.
[2016-06-22 05:02:24] INFO     (20) {__main__ - NetworkScanner.py:385} Start AsyncSniffer using Scapy...
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:402} Sending ARP packets...
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:309} Send ARP packet for '172.18.0.6'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:309} Send ARP packet for '172.18.0.9'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:309} Send ARP packet for '172.18.0.8'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:309} Send ARP packet for '172.18.0.5'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:309} Send ARP packet for '172.18.0.10'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:309} Send ARP packet for '172.18.0.13'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:309} Send ARP packet for '172.18.0.14'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:309} Send ARP packet for '172.18.0.4'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:309} Send ARP packet for '172.18.0.7'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:309} Send ARP packet for '172.18.0.3'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:309} Send ARP packet for '172.18.0.12'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:309} Send ARP packet for '172.18.0.11'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:309} Send ARP packet for '172.18.0.1'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:309} Send ARP packet for '172.18.0.2'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:407} Sending ICMP packets...
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:300} Send ICMP packet for '172.18.0.6'
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:369} ARP detected in packet...
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:470} Start handle_UP for '172.18.0.9' (ARPa4:ee:57:35:c0:a8)...
172.18.0.9
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:476} Quit handle_UP for '172.18.0.9'.
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:369} ARP detected in packet...
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:470} Start handle_UP for '172.18.0.10' (ARP62:66:e6:d0:e0:b0)...
172.18.0.10
[2016-06-22 05:02:24] DEBUG    (10) {__main__ - NetworkScanner.py:476} Quit handle_UP for '172.18.0.10'.
[2016-06-22 05:02:26] DEBUG    (10) {__main__ - NetworkScanner.py:300} Send ICMP packet for '172.18.0.9'
[2016-06-22 05:02:26] DEBUG    (10) {__main__ - NetworkScanner.py:300} Send ICMP packet for '172.18.0.8'
[2016-06-22 05:02:28] DEBUG    (10) {__main__ - NetworkScanner.py:300} Send ICMP packet for '172.18.0.5'
[2016-06-22 05:02:30] DEBUG    (10) {__main__ - NetworkScanner.py:300} Send ICMP packet for '172.18.0.10'
[2016-06-22 05:02:32] DEBUG    (10) {__main__ - NetworkScanner.py:300} Send ICMP packet for '172.18.0.13'
[2016-06-22 05:02:34] DEBUG    (10) {__main__ - NetworkScanner.py:300} Send ICMP packet for '172.18.0.14'
[2016-06-22 05:02:36] DEBUG    (10) {__main__ - NetworkScanner.py:300} Send ICMP packet for '172.18.0.4'
[2016-06-22 05:02:38] DEBUG    (10) {__main__ - NetworkScanner.py:300} Send ICMP packet for '172.18.0.7'
[2016-06-22 05:02:40] DEBUG    (10) {__main__ - NetworkScanner.py:300} Send ICMP packet for '172.18.0.3'
[2016-06-22 05:02:42] DEBUG    (10) {__main__ - NetworkScanner.py:300} Send ICMP packet for '172.18.0.12'
[2016-06-22 05:02:44] DEBUG    (10) {__main__ - NetworkScanner.py:300} Send ICMP packet for '172.18.0.11'
[2016-06-22 05:02:46] DEBUG    (10) {__main__ - NetworkScanner.py:300} Send ICMP packet for '172.18.0.1'
[2016-06-22 05:02:48] DEBUG    (10) {__main__ - NetworkScanner.py:300} Send ICMP packet for '172.18.0.2'
[2016-06-22 05:02:50] DEBUG    (10) {__main__ - NetworkScanner.py:414} Sending TCP packets...
[2016-06-22 05:02:50] DEBUG    (10) {__main__ - NetworkScanner.py:420} Packets, are sent. Wait for timeout...
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:426} Get IP addresses down...
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:497} Start handle_DOWN for '172.18.0.1'...
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:499} Quit handle_DOWN for '172.18.0.1'.
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:497} Start handle_DOWN for '172.18.0.8'...
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:499} Quit handle_DOWN for '172.18.0.8'.
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:497} Start handle_DOWN for '172.18.0.11'...
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:499} Quit handle_DOWN for '172.18.0.11'.
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:497} Start handle_DOWN for '172.18.0.5'...
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:499} Quit handle_DOWN for '172.18.0.5'.
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:497} Start handle_DOWN for '172.18.0.14'...
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:499} Quit handle_DOWN for '172.18.0.14'.
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:497} Start handle_DOWN for '172.18.0.4'...
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:499} Quit handle_DOWN for '172.18.0.4'.
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:497} Start handle_DOWN for '172.18.0.7'...
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:499} Quit handle_DOWN for '172.18.0.7'.
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:497} Start handle_DOWN for '172.18.0.13'...
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:499} Quit handle_DOWN for '172.18.0.13'.
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:497} Start handle_DOWN for '172.18.0.12'...
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:499} Quit handle_DOWN for '172.18.0.12'.
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:497} Start handle_DOWN for '172.18.0.3'...
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:499} Quit handle_DOWN for '172.18.0.3'.
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:497} Start handle_DOWN for '172.18.0.6'...
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:499} Quit handle_DOWN for '172.18.0.6'.
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:497} Start handle_DOWN for '172.18.0.2'...
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:499} Quit handle_DOWN for '172.18.0.2'.
[2016-06-22 05:02:53] INFO     (20) {__main__ - NetworkScanner.py:433} Stop AsyncSniffer, scan end.
[2016-06-22 05:02:53] DEBUG    (10) {__main__ - NetworkScanner.py:672} Scan end.

~# python NetworkScanner.py --noping --hostname --ports 22 80 -p 445 139 443 -T 1 -R -s -t 172.18.0.0/28

NetworkScanner  Copyright (C) 2021, 2022  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.


PythonToolsKit  Copyright (C) 2022  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.

UP: 172.18.0.9
UP: 172.18.0.10
DOWN: 172.18.0.13
DOWN: 172.18.0.5
DOWN: 172.18.0.12
DOWN: 172.18.0.14
DOWN: 172.18.0.7
DOWN: 172.18.0.4
DOWN: 172.18.0.11
DOWN: 172.18.0.3
DOWN: 172.18.0.6
DOWN: 172.18.0.2
DOWN: 172.18.0.1
DOWN: 172.18.0.8

~#

>>> from NetworkScanner import NetworkScanner, logger
>>> scanner = NetworkScanner({"172.18.0.1", "172.18.0.3"})
>>> scanner.scan()      # Without scapy
IP: '172.18.0.1' is UP ('ARP', None).
IP: '172.18.0.3' is UP ('ARP', None).
[True, True]
>>> def do_IP_UP(ip, reason, detail = None):
...     print(f"{ip} is UP ({reason} {detail})")
...
>>> scanner.handle_UP = do_IP_UP
>>> scanner.scan(True)  # With scapy
172.18.0.1 is UP (ARP 01:02:03:04:05:06)
172.18.0.3 is UP (ARP FF:EE:DD:CC:BB:AA)
[True, True]
>>> scanner.hosts_up
['172.18.0.3', '172.18.0.1']
>>> scanner.hosts_down
[]
>>> from scapy.all import *
>>> scanner = NetworkScanner({"172.18.0.1"}, False, [22, 80], False, True, False, 1, conf.iface)
>>> scanner.handle_UP = do_IP_UP
>>> scanner.handle_DOWN = print
>>> scanner.scan()
172.18.0.1
[False]
>>> logger.setLevel(10)  # debug mode
>>>
"""

__version__ = "1.0.0"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = "This module implements a NetworkScanner."
license = "GPL-3.0 License"
__url__ = "https://github.com/mauricelambert/NetworkScanner"

copyright = """
NetworkScanner  Copyright (C) 2021, 2022  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
__license__ = license
__copyright__ = copyright

__all__ = ["NetworkScanner", "main"]

print(copyright)

from asyncio import (
    create_subprocess_exec,
    open_connection,
    wait_for,
    gather,
    sleep,
    run,
)
from asyncio.exceptions import TimeoutError as AsyncTimeoutError
from PythonToolsKit.GetType import get_ipv4_addresses
from PythonToolsKit.Logs import get_custom_logger
from subprocess import PIPE, DEVNULL, getoutput
from argparse import ArgumentParser, Namespace
from logging import Logger, DEBUG, WARNING
from typing import List, Set, TypeVar, Any
from socket import gethostbyaddr, herror
from collections.abc import Callable
from functools import partial
from platform import system
from random import randint
from sys import exit

try:
    from scapy.error import log_runtime
    from scapy.sendrecv import sendp, send
    from scapy.layers.l2 import Ether, ARP
    from scapy.interfaces import NetworkInterface
    from scapy.all import Packet, IP, ICMP, AsyncSniffer, TCP
    from PythonToolsKit.ScapyTools import ScapyArguments as ArgumentParser
except ImportError:
    NetworkInterface = TypeVar("NetworkInterface")
    Packet = TypeVar("Packet")
    SCAPY = False
else:
    SCAPY = True

IS_WINDOWS = system() == "Windows"

logger: Logger = get_custom_logger(__name__)
debug: Callable = logger.debug
info: Callable = logger.info
warning: Callable = logger.warning
error: Callable = logger.error
critical: Callable = logger.critical


async def ping_command(
    command: List[str], ip: str, stdout: int = None
) -> bool:

    """
    This function executes ping command and checks for success/response.
    """

    command = command.copy()
    command.append(ip)

    debug(f"Start ping command for {ip}...")
    process = await create_subprocess_exec(
        *command, stdout=stdout, stderr=DEVNULL, stdin=DEVNULL
    )
    stdout, _ = await process.communicate()

    if process.returncode or (IS_WINDOWS and b"TTL" not in stdout):
        debug(f"Ping failed for {ip}.")
        return False

    debug(f"Ping match for {ip}")
    return True


def get_linux_arp_cache() -> bytes:

    """
    This function returns ARP cache on Linux.
    """

    info("Get Linux ARP cache.")
    with open(
        NO_SCAPY_BEHAVIOR.LINUX_ARP_FILE, "r", encoding="latin-1"
    ) as file:
        arp_cache = file.read()

    return arp_cache


class NO_SCAPY_BEHAVIOR:

    """
    This class defines data and function to scan without scapy.
    """

    WINDOWS_PING_COMMAND: List[str] = ["ping", "-n", "1"]
    LINUX_PING_COMMAND: List[str] = ["ping", "-c", "1"]
    WINDOWS_ARP_COMMAND: List[str] = ["arp", "-a"]
    LINUX_ARP_FILE: str = "/proc/net/arp"

    LINUX_GET_ARP_CACHE: Callable = get_linux_arp_cache
    WINDOWS_GET_ARP_CACHE: Callable = partial(getoutput, WINDOWS_ARP_COMMAND)
    WINDOWS_PING: Callable = partial(
        ping_command, WINDOWS_PING_COMMAND, stdout=PIPE
    )
    LINUX_PING: Callable = partial(
        ping_command, LINUX_PING_COMMAND, stdout=DEVNULL
    )

    ERRORS = (OSError, TimeoutError, AsyncTimeoutError)

    if IS_WINDOWS:
        PING: Callable = WINDOWS_PING
        ARP: Callable = WINDOWS_GET_ARP_CACHE
    else:
        ARP: Callable = LINUX_GET_ARP_CACHE
        PING: Callable = LINUX_PING


class NetworkScanner:

    """
    This class implements an asynchronous network scanner.
    """

    def __init__(
        self,
        targets: Set[str],
        ping: bool = True,
        ports: List[int] = [],
        arp: bool = True,
        hostname: bool = True,
        real_time: bool = True,
        timeout: int = 3,
        iface: NetworkInterface = None,
    ):
        self.targets = targets
        self._targets = targets.copy()
        self.ping = ping
        self.ports = ports
        self.arp = arp
        self.hostname = hostname
        self.real_time = real_time
        self.timeout = timeout
        self.hosts_up = []
        self.hosts_down = []
        self.iface = iface
        self.ip = getattr(iface, "ip", None)
        self.mac = getattr(iface, "mac", None)

    def scapy_ping(self, ip: str) -> None:

        """
        This function pings a host with Scapy.
        """

        debug(f"Send ICMP packet for {ip!r}")
        send(IP(dst=ip, src=self.ip) / ICMP(), iface=self.iface, verbose=False)

    def scapy_arp(self, ip: str) -> None:

        """
        This function send an ARP request with Scapy.
        """

        debug(f"Send ARP packet for {ip!r}")
        sendp(
            Ether(dst="ff:ff:ff:ff:ff:ff", src=self.mac)
            / ARP(op=1, psrc=self.ip, pdst=ip),
            iface=self.iface,
            verbose=False,
        )

    def scapy_tcp(self, ip: str, dport: int, sport: int) -> None:

        """
        This function send a TCP packet with Scapy.
        """

        debug(f"Send TCP packet for {ip!r}")
        send(
            IP(src=self.ip, dst=ip)
            / TCP(sport=sport, dport=dport, flags="S", seq=1000),
            iface=self.iface,
            verbose=False,
        )

    def no_scapy_scan(self) -> List[bool]:

        """
        This function starts the scan without scapy.
        """

        async def tasks() -> List[bool]:
            return await gather(
                *[no_scapy_check_ip(target) for target in targets]
            )

        info("Start asynchronous scan without scapy...")
        no_scapy_check_ip = self.no_scapy_check_ip
        hosts_up = self.hosts_up
        targets = self.targets
        results = run(tasks())

        if self.arp:
            debug("Start ARP detection...")
            arp_cache = NO_SCAPY_BEHAVIOR.ARP().split()
        else:
            arp_cache = []

        remove = self.hosts_down.remove
        append = hosts_up.append

        for ip in targets:
            if ip in hosts_up:
                continue

            if ip in arp_cache:
                remove(ip)
                append(ip)
                self._handle_UP(ip, "ARP")
            else:
                self._handle_DOWN(ip)

        info("Scan end.")
        return results

    def scapy_match(self, packet: Packet) -> None:

        """
        This function gets IP address of matching packets with scapy.
        """

        if packet.haslayer(ARP):
            ip = packet[ARP].psrc
            mode = "ARP"
        else:
            ip = packet[IP].src
            mode = "IP"

        debug(f"{mode} detected in packet...")
        targets = self._targets
        if ip in targets:
            targets.remove(ip)
            self._handle_UP(ip, mode, packet[Ether].src)

    def start_scapy_scan(self) -> List[bool]:

        """
        This function starts AsyncSniffer and scapy scan,
        finally stops AsyncSniffer.
        """

        no_error = False
        _targets = self._targets
        info("Start AsyncSniffer using Scapy...")

        sniffer = AsyncSniffer(
            iface=self.iface,
            lfilter=lambda p: (
                (ARP in p and p.psrc in _targets)
                or (IP in p and p.src in _targets)
            ),
            prn=self.scapy_match,
        )
        sniffer.start()

        try:
            results = self.scapy_scan()
        except Exception as e:
            error = e
        else:
            no_error = True
        finally:
            info("Stop AsyncSniffer, scan end.")
            sniffer.stop()

        if no_error:
            return results
        else:
            raise error

    def scapy_scan(self) -> List[bool]:

        """
        This function starts the scapy scan.
        """

        targets = self.targets

        scapy_ping = self.scapy_ping
        scapy_arp = self.scapy_arp
        scapy_tcp = self.scapy_tcp

        targets = self._targets.copy()
        debug("Sending ARP packets...")
        if self.arp:
            for target in targets:
                scapy_arp(target)

        debug("Sending ICMP packets...")
        if self.ping:
            for target in targets:
                scapy_ping(target)

        targets = self._targets.copy()
        sport = randint(1024, 65535)
        debug("Sending TCP packets...")
        for port in self.ports:
            debug(f"Send {port}/TCP packets...")
            for target in targets:
                scapy_tcp(target, port, sport)

        debug("Packets, are sent. Wait for timeout...")
        run(sleep(self.timeout))

        hosts_up = self.hosts_up
        handle_DOWN = self._handle_DOWN

        debug("Get IP addresses down...")
        targets = self._targets.copy()
        results = [
            (handle_DOWN(target) or False) if target not in hosts_up else True
            for target in targets
        ]

        return results

    def scan(self, scapy: bool = False) -> List[bool]:

        """
        This function starts the scan (using scapy
        if available otherwise an asynchronous scanner).
        """

        if scapy and SCAPY:
            info("Run scapy scan.")
            return self.start_scapy_scan()
        else:
            info("Run asynchronous scan (without scapy).")
            return self.no_scapy_scan()

    def handle_UP(self, ip: str, reason: str, detail: Any = None) -> None:

        """
        This function is the default behavior when IP is UP.

        Print the IP address.
        """

        print(f"IP: {ip!r} is UP ({reason!r}, {detail!r}).")

    def _handle_UP(self, ip: str, reason: str, detail: Any = None) -> None:

        """
        This function is the default behavior when IP is UP.

        Store IP address in self.hosts_up and call self.handle_UP.
        """

        self.hosts_up.append(ip)
        debug(
            f"""Start handle_UP for {ip!r} ({reason}{
                '' if detail is None else detail
            })..."""
        )
        self.handle_UP(ip, reason, detail)
        debug(f"Quit handle_UP for {ip!r}.")

    def handle_DOWN(self, ip: str) -> None:

        """
        This function is the default behavior when IP is DOWN.

        Print the IP address.
        """

        print(f"IP: {ip!r} is DOWN.")

    def _handle_DOWN(self, ip: str) -> None:

        """
        This function is the default behavior when IP is DOWN.

        Store IP address in self.hosts_down and call self.handle_DOWN.
        """

        self.hosts_down.append(ip)
        debug(f"Start handle_DOWN for {ip!r}...")
        self.handle_DOWN(ip)
        debug(f"Quit handle_DOWN for {ip!r}.")

    async def no_scapy_check_ip(self, ip: str) -> bool:

        """
        This function checks the IP address to see if it is being used.
        """

        if self.ping and await NO_SCAPY_BEHAVIOR.PING(ip):
            debug(f"Check {ip!r} (step 1: PING)...")
            self._handle_UP(ip, "ping")
            return True

        if self.hostname:
            debug(f"Check {ip!r} (step 2: HOSTNAME)...")
            try:
                hostname = gethostbyaddr(ip)
            except herror:
                pass
            else:
                self._handle_UP(ip, "hostname", hostname)
                return True

        if self.ports:
            debug(f"Check {ip!r} (step 3: TCP connections)...")
            timeout = self.timeout
            ERRORS = NO_SCAPY_BEHAVIOR.ERRORS
            for port in self.ports:
                try:
                    connection = open_connection(ip, port)
                    reader, writer = await wait_for(
                        connection, timeout=timeout
                    )
                except ERRORS:
                    pass
                else:
                    self._handle_UP(ip, "tcp", port)
                    return True

        debug(f"{ip!r} is probably not up.")
        return False


def parse_args() -> Namespace:

    """
    This function parses the command line arguments.
    """

    parser = ArgumentParser(
        description="This program scans networks and IP address ranges."
    )

    add_argument = parser.add_argument
    add_argument(
        "--targets",
        "-t",
        help="Targets from networks and IP address ranges.",
        required=True,
        nargs="+",
        action="extend",
        type=get_ipv4_addresses,
    )
    add_argument(
        "--noping",
        "-P",
        help=(
            "No ping detection. [Without scapy ping "
            "is required for ARP detection]"
        ),
        action="store_false",
    )
    add_argument("--noarp", "-A", help="No arp cache.", action="store_false")
    add_argument(
        "--hostname",
        "-H",
        help="Test the hostname resolution to defined if host is UP (longer).",
        action="store_true",
    )
    add_argument(
        "--ports",
        "-p",
        help="Test the TCP port connections to defined if the host is UP.",
        type=int,
        action="extend",
        nargs="+",
        default=[],
    )
    add_argument(
        "--timeout",
        "-T",
        help="Connections timeout.",
        type=int,
        default=3,
    )
    add_argument(
        "--no-realtime",
        "-R",
        help="Do not print results in real time.",
        action="store_true",
    )
    add_argument(
        "--debug",
        "-d",
        help="Debug mode (logger level debug).",
        action="store_true",
    )
    add_argument(
        "--print-state",
        "-s",
        help="Print IP state (default print IP UP only).",
        action="store_true",
    )

    return parser.parse_args()


def main() -> int:

    """
    This function executes this program from the command line.
    """

    arguments = parse_args()

    if arguments.debug:
        logger.setLevel(DEBUG)

    if SCAPY:
        log_runtime.setLevel(WARNING + 1)

    no_realtime = arguments.no_realtime
    print_state = arguments.print_state

    debug("Build NetworkScanner...")
    scanner = NetworkScanner(
        {str(ip) for addresses in arguments.targets for ip in addresses},
        ping=arguments.noping,
        ports=arguments.ports,
        arp=arguments.noarp,
        hostname=arguments.hostname,
        timeout=arguments.timeout,
        iface=getattr(arguments, "iface", None),
    )

    debug("Configure real time...")
    if no_realtime:
        scanner.handle_UP = lambda *args: None
        scanner.handle_DOWN = lambda x: None
    elif not print_state:
        scanner.handle_UP = lambda *args: print(args[0])
        scanner.handle_DOWN = lambda x: None

    debug("The scan begins...")
    scanner.scan(SCAPY)
    debug("Scan end.")

    if no_realtime and print_state:
        print("UP:", "\nUP: ".join(scanner.hosts_up))
        print("DOWN:", "\nDOWN: ".join(scanner.hosts_down))
    elif no_realtime:
        print("\n".join(scanner.hosts_up))

    return 0


if __name__ == "__main__":
    exit(main())
