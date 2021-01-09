#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" This file implement a NetworkScanner. """

###################
#    This file implement a NetworkScanner.
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

__all__ = [ "NetworkScanner", "main" ]

from asyncio import create_subprocess_shell, subprocess, run, wait_for, open_connection, gather, exceptions
from ipaddress import ip_address, ip_network
from socket import gethostbyaddr, herror
from enum import Enum
from platform import system
from os import device_encoding

class Constants (Enum):
	if system() == "Windows":
		ARP_COMMAND = "arp -a"
		PING_COMMAND = "ping -n 1 "
	else:
		ARP_COMMAND = "cat /proc/net/arp"
		PING_COMMAND = "ping -c 1 "


class NetworkScanner:

	""" This class implement an asynchronous network scanner. """

	def __init__ (self, targets, ping=True, ports=None, arp=True, hostname=True, real_time=True, timeout=3):
		self.targets = targets
		self.ping = ping
		self.ports = ports
		self.arp = arp
		self.hostname = hostname
		self.real_time = real_time
		self.timeout = timeout
		
		if not real_time:
			self.hosts_up = []

	@classmethod
	def get_targets (self, first, last):
		""" Function to get targets from first target to last target. """

		first = ip_address(first)
		last = ip_address(last)

		if last < first:
			first, last = last, first

		self.targets = (ip_address(target) for target in range(int(first), int(last) + 1))
		return self.targets

	@classmethod
	def get_targets_from_network (self, network):
		""" Function to get targets from network. """

		self.targets = ip_network(network)
		return self.targets

	async def scan (self):
		""" Function to launch scan on all targets. """

		await gather(*[self.test_ip(str(target)) for target in self.targets])

	def handle_ip (self, ip):
		""" Function to get ip in realtime. """

		print(f"IP: {ip} is up.")

	async def test_ip (self, ip):
		""" This function try to etablished a connection with target. """

		up = False
		hostname = None

		if self.ping:
			process = await create_subprocess_shell(Constants.PING_COMMAND.value + ip, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			stdout, stderr = await process.communicate()
			data = stdout + stderr
			data = data.decode(device_encoding(0)).lower()

			if not process.returncode and "max" in data and "min" in data:
				up = True

		if not up and self.arp:
			process = await create_subprocess_shell(Constants.ARP_COMMAND.value, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			stdout, stderr = await process.communicate()
			data = stdout + stderr
			lines = data.decode(device_encoding(0)).lower().split("\n")

			for line in lines:
				if not process.returncode:
					break
				if ip in line and "00:00:00:00:00:00" not in line:
					up = True
					break

		if not up and self.hostname:
			try:
				hostname = gethostbyaddr(ip)
			except herror:
				pass

		if not up and not hostname and self.ports and self.timeout:
			for port in self.ports:
				try:
					connection = open_connection(ip, port)
					reader, writer = await wait_for(connection, timeout=self.timeout)
				except OSError:
					pass
				except TimeoutError:
					pass
				except exceptions.TimeoutError:
					pass
				else:
					up = True
					break

		if up or hostname:
			if self.real_time:
				self.handle_ip(ip)
			else:
				self.hosts_up.append(ip)

def test ():
	print("Launch little scan...")
	scanner = NetworkScanner(
		NetworkScanner.get_targets("127.0.0.1", "127.0.0.10")
	)
	run(scanner.scan())

	print("Launch network scan...")
	scanner = NetworkScanner(
		NetworkScanner.get_targets_from_network("127.0.0.1/24"),
		ping=False,
		ports=[80,445],
		arp=False,
		hostname=False,
		real_time=False)
	run(scanner.scan())
	print(scanner.hosts_up)

def get_ports (ports_string) -> list:

	""" This function return ports as a list. """

	return [int(port) for port in ports_string.split(",")]

def parse ():
	from argparse import ArgumentParser

	parser = ArgumentParser()

	parser.add_argument("--network-target", "-n", help="Get targets from network. [replace --first-target and --last-target arguments]", default=None)
	parser.add_argument("--first-target", "-f", help="First ip of targets range. [--last-target argument is required]", default=None)
	parser.add_argument("--last-target", "-l", help="Last ip of targets range. [--first-target argument is required]", default=None)
	parser.add_argument("--noping", "-P", help="No ping detection. [recommended for arp cache]", action="store_false")
	parser.add_argument("--noarp", "-A", help="No arp cache.", action="store_false")
	parser.add_argument("--nohostname", "-H", help="No hostname resolution.", action="store_false")
	parser.add_argument("--ports", "-p", help="Ports for TCP connect discovery. Example: 80,443,8080", default=None)
	parser.add_argument("--timeout", "-t", help="Timeout for TCP connect discovery.", type=int, default=3)
	parser.add_argument("--norealtime", "-R", help="No realtime.", action="store_false")

	return parser, parser.parse_args()

def main ():
	_, parser = parse()

	if parser.ports:
		ports = get_ports(parser.ports)
	else:
		ports = parser.ports

	if parser.network_target:
		targets = NetworkScanner.get_targets_from_network(parser.network_target)
	elif parser.first_target and parser.last_target:
		targets = NetworkScanner.get_targets(parser.first_target, parser.last_target)
	else:
		print("ERROR: Targets is required ! (--network-target) or (--first-target and --last-target)\n")
		_.print_help()
		exit(1)

	scanner = NetworkScanner(
		targets,
		ping=parser.noping,
		ports=ports,
		arp=parser.noarp,
		hostname=parser.nohostname,
		real_time=parser.norealtime,
		timeout=parser.timeout)
	run(scanner.scan())

	if not parser.norealtime:
		print(scanner.hosts_up)

if __name__ == "__main__":
	main()
