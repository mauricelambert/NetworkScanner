![NetworkScanner logo](https://mauricelambert.github.io/info/python/security/NetworkScanner_small.png "NetworkScanner logo")

# NetworkScanner

## Description

This package implements an asynchronous network scanner (using scapy or asyncio).

## Requirements

This package require: 
 - python3
 - python3 Standard Library
 - PythonToolsKit

Optional:
 - Scapy

## Installation

```bash
pip install NetworkScanner 
```

## Usages

### Command lines

```bash
# Python executable
python3 NetworkScanner.pyz -h
# or
chmod u+x NetworkScanner.pyz
./NetworkScanner.pyz --help

# Python module
python3 -m NetworkScanner -t 172.18.0.1-172.18.0.15

# Entry point (console)
NetworkScanner -d --noping --hostname --ports 22 80 -p 445 139 443 -T 1 -R -s -t 172.18.0.0/28
```

### Python3

```python
# Simple usage to print results in your console
from NetworkScanner import NetworkScanner, logger
scanner = NetworkScanner({"172.18.0.1", "172.18.0.3"})
scanner.scan()      # Without scapy

# Custom behaviors

def do_IP_UP(ip, reason, detail = None):
    print(f"{ip} is UP ({reason} {detail})")

scanner.handle_UP = do_IP_UP
scanner.scan(True)  # With scapy

scanner.hosts_up    # List of IP addresses used
scanner.hosts_down  # List of unused IP addresses

from scapy.all import *
scanner = NetworkScanner({"172.18.0.1"}, False, [22, 80], False, True, False, 1, conf.iface)
scanner.handle_UP = do_IP_UP
scanner.handle_DOWN = print
scanner.scan()

logger.setLevel(10) # debug mode

class CustomNetworkScanner(NetworkScanner):
    def handle_UP(self, ip: str, detection_type: str, details = None): # details is a kwarg
        print(f"IP: {ip} is UP (detection type: {detection_type}, details: {details}")
    def handle_DOWN(self, ip: str):
        print(f"IP: {ip} is DOWN")

scanner = NetworkScanner({"172.18.0.1", "172.18.0.3"})
scanner.scan()
```

## Useful usages

With scapy, *hosts discovery (best performances)*:

```bash
NetworkScanner --noping -T 1 -t [targets]
```

```python
from NetworkScanner import NetworkScanner
from scapy.all import conf

scanner = NetworkScanner(
    {},
    ping=False,
    ports=[],
    arp=True,
    hostname=False,
    real_time=False,
    timeout=1,
    iface=conf.iface,
)
scanner.scan(True)
```

Without scapy, *hosts discovery*:

```bash
NetworkScanner -t [targets]
```

```python
from NetworkScanner import NetworkScanner
scanner = NetworkScanner(
    {},
    ping=True,
    ports=[],
    arp=True,
    hostname=False,
    real_time=False,
    timeout=1,
)
scanner.scan()
```

Without scapy, *opened port && hosts discovery*:

```python
from NetworkScanner import NetworkScanner

def host_up(ip: str, method: str, port: int = None):
    if method == 'tcp':
        print(f"{ip}:{port} is open.")
    else:
        print(f"{ip} is UP.")

scanner = NetworkScanner(
    {},
    ping=False,
    ports=[22, 80, 443],
    arp=True,
    hostname=False,
    real_time=False,
    timeout=1,
)
scanner.handle_UP = host_up
scanner.scan(False)
```

## Links

 - [Github Page](https://github.com/mauricelambert/NetworkScanner)
 - [Pypi](https://pypi.org/project/NetworkScanner/)
 - [Documentation](https://mauricelambert.github.io/info/python/security/NetworkScanner.html)
 - [Executable](https://mauricelambert.github.io/info/python/security/NetworkScanner.pyz)

## Help

```text
~# python3 NetworkScanner.py --help
usage: NetworkScanner.py [-h] [--interface INTERFACE] --targets TARGETS [TARGETS ...] [--noping] [--noarp]
                         [--hostname] [--ports PORTS [PORTS ...]] [--timeout TIMEOUT] [--no-realtime] [--debug]
                         [--print-state]

This program scans networks and IP address ranges.

optional arguments:
  -h, --help            show this help message and exit
  --interface INTERFACE, -i INTERFACE
                        Part of the IP, MAC or name of the interface
  --targets TARGETS [TARGETS ...], -t TARGETS [TARGETS ...]
                        Targets from networks and IP address ranges.
  --noping, -P          No ping detection. [Without scapy ping is required for ARP detection]
  --noarp, -A           No arp detection.
  --hostname, -H        Test the hostname resolution to defined if host is UP (longer).
  --ports PORTS [PORTS ...], -p PORTS [PORTS ...]
                        Test the TCP port connections to defined if the host is UP.
  --timeout TIMEOUT, -T TIMEOUT
                        Connections timeout.
  --no-realtime, -R     Do not print results in real time.
  --debug, -d           Debug mode (logger level debug).
  --print-state, -s     Print IP state (default print IP UP only).
```

## Licence

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
