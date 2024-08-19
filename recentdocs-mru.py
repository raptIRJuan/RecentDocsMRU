#recentdocsmru.py
#v1.0 (2016-06-05)
#Parses the RecentDocs key in the NTUSER.dat registry file

#Copyright (C) 2016  Juan Aranda (raptir.juan@gmail.com)

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from Registry import Registry
import argparse
import struct
import sys

class FileEntry(object):
	def __init__(self, fname):
		self.fname = fname
		self.ftimestamp = " "*26
		
def parse_MRUListEx(mrulist):
	size = (len(mrulist) - 4) // 4
	struct_arg = "%sI" % (size)
	return struct.unpack(struct_arg, mrulist.rstrip(b'\xff\xff\xff\xff'))

def main():
	parser = argparse.ArgumentParser(description = 'Parses the RecentDocs key')
	parser.add_argument('-f', '--file', help = 'path to NTUser.dat', required = True)
	parser.add_argument('-o', '--output', help = 'Output File Name')
	args = parser.parse_args()

	reg = Registry.Registry(args.file)

	try:
		key = reg.open("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RecentDocs")
	except Registry.RegistryKeyNotFoundException as e:
		print("Couldn't find the RecentDocs key.")
		sys.exit(1)

	MRUListEx = parse_MRUListEx(key.value('MRUListEx').value())
	recent = []
	for r in MRUListEx:
		recent += [FileEntry(key.value(str(r)).value().split(b'\x00\x00')[0])]
	
	if recent:
		recent[0].ftimestamp = key.timestamp()
	else: 
		print("RecentDocs MRUListEx is empty")
		sys.exit(1)
	
	for subkey in key.subkeys():
		timestamp = subkey.timestamp()
		try:
			subMRUListEx = parse_MRUListEx(subkey.value('MRUListEx').value())
			if subMRUListEx:
				mru0 = str(subMRUListEx[0])
				for i in recent:
					if i.fname == subkey.value(mru0).value().split(b'\x00\x00')[0]:
						i.ftimestamp = timestamp
			else:
				print("The MRUListEx for subkey %s is empty." % (subkey.name()))
		except Registry.RegistryValueNotFoundException as e:
			print("Couldn't find the MRUListEx in the %s subkey." % (subkey.name()))

	if args.output:
		with open(args.output, 'wb') as outputfile:
			for i in recent:
				if len(i.fname) % 2 != 0:
					i.fname += b'\x00'
				line = str(i.ftimestamp) + ' ' + i.fname.decode('utf-16') + '\r\n'
				outputfile.write(line.encode('utf-16'))
	else:
		for i in recent:
			print(str(i.ftimestamp) + ' ' + str(i.fname.replace(b'\x00', b'')))
			
if __name__ == '__main__':
	main()
