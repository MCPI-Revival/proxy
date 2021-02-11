#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  proxy.py
#  
#  Copyright 2021 Alvarito050506 <donfrutosgomez@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; version 2 of the License.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
import socket
import threading

class Proxy:
	def __init__(self):
		self.__options = {
			"src_addr": None,
			"src_port": 19132,
			"dst_port": 19133
		};
		self.__running_lock = threading.Lock();
		self.__running = 0;

	def set_option(self, name, value):
		if name in self.__options:
			self.__options[name] = value;
		else:
			raise NameError(name);
		return self.__options;

	def get_options(self):
		return self.__options;

	def run(self):
		dst_addr = ("0.0.0.0", self.__options["dst_port"]);
		try:
			proc_addr = socket.gethostbyname_ex(self.__options["src_addr"])[2][0]
		except socket.gaierror:
			print("Error: Invalid address.");
			return 1;
		src_addr = (proc_addr, self.__options["src_port"]);
		client_addr = None;

		self.__running_lock.acquire();
		self.__running += 1;
		self.__running_lock.release();

		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP);
		self.__socket.bind(dst_addr);
		self.__socket.setblocking(False);

		while True:
			self.__running_lock.acquire();
			condition = self.__running < 1;
			self.__running_lock.release();
			if condition:
				# End Loop
				break;

			try:
				data, addr = self.__socket.recvfrom(4096);
				if addr == src_addr:
					self.__socket.sendto(data, client_addr);
				else:
					if client_addr is None or client_addr[0] == addr[0]:
						client_addr = addr;
						self.__socket.sendto(data, src_addr);
			except:
				# No Data Available
				pass

		self.__socket.close();
		return 0;

	def stop(self):
		self.__running_lock.acquire();
		self.__running -= 1;
		self.__running_lock.release();
		return 0;

if __name__ == '__main__':
	args = sys.argv;
	if len(args) < 2:
		print("Error: You must provide a source address.");
		print("Usage: " + args[0] + " src_addr [src_port [dst_port]]");
		print("Where src_addr is a valid internet address and src_port and dst_port are valid internet ports.")
		sys.exit(1);

	proxy = Proxy();
	proxy.set_option("src_addr", args[1]);
	if len(args) > 2:
		proxy.set_option("src_port", int(args[2]));
	if len(args) > 3:
		proxy.set_option("dst_port", int(args[3]));
	options = proxy.get_options();
	print(options["src_addr"] + ":" + str(options["src_port"]) + " --> 0.0.0.0:" + str(options["dst_port"]));
	try:
		proxy.run();
	except KeyboardInterrupt:
		proxy.stop();
		print("");
		sys.exit(0);
