# NetworkScanner

## Description
This package implement a asynchronous network scanner.

## Requirements
This package require : 
 - python3
 - python3 Standard Library

## Installation
```bash
pip install NetworkScanner 
```

## Examples

### Command lines

```bash
NetworkScan -n 192.168.56.0/24 # Scan all ip in network 192.168.56.0/24
NetworkScan -f 192.168.0.1 -l 192.168.0.50 # Scan ip between 192.168.0.1 and 192.168.0.50
NetworkScan -p 80,443 -P -A -H -R -n 192.168.0.0/24 # Scan all ip in network without ping, arp cache and hostname. This scan check ports 80 and 443 on TCP if one port is opened, host is up. 
```

### Python3

```python
from NetworkScanner import NetworkScanner
from asyncio import run

scanner = NetworkScanner(
	NetworkScanner.get_targets("127.0.0.1", "127.0.0.10")
)
run(scanner.scan())
```

```python
from NetworkScanner import NetworkScanner
from asyncio import run

scanner = NetworkScanner(
	NetworkScanner.get_targets_from_network("127.0.0.1/24"),
	ping=True,
	ports=[80,443],
	arp=True,
	hostname=True,
	real_time=False,
	timeout=3)
run(scanner.scan())
print(scanner.hosts_up)
```

## Link
[Github Page](https://github.com/mauricelambert/NetworkScanner)

## Licence
Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
