#!/usr/bin/python3

import urllib.request
import re

template = """
Actor "ACSUtils_CF_{flag}_0" : CustomInventory
{{
	states
	{{
	Pickup:
		TNT1 A 0 A_ChangeFlag("{flag}", false)
		stop
	}}
}}

Actor "ACSUtils_CF_{flag}_1" : CustomInventory
{{
	states
	{{
	Pickup:
		TNT1 A 0 A_ChangeFlag("{flag}", true)
		stop
	}}
}}

"""

def main():
	flags = open('flags.txt', 'r').read().splitlines()
	out = open('dist/decorate.acsutils', 'a')

	out.write('// Supported flags:\n')
	for flag in flags:
		out.write('// ' + flag + '\n')
	
	for flag in flags:
		out.write(template.format(flag=flag))
		if '.' in flag:
			flag = flag.split('.')[1]
			out.write(template.format(flag=flag))
		
if __name__ == '__main__':
	main()
