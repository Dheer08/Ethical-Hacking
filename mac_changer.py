import subprocess
import optparse
import re

def get_arguments():
	parser = optparse.OptionParser()
	#The dest is the place where the values will be stored
	parser.add_option("-i","--interface",dest="interface",help="Enter your interface")
	parser.add_option("-m","--mac",dest="new_mac",help="Enter your New MAC address")
	(options,arguments) = parser.parse_args()
	if not options.interface:
		parse.error("[-] please specify an interface,use --help for more info ")
	elif not options.new_mac:
		parse.error("[-] please specify an new MAC address ,use --help for more info")
	else:
		return options

def change_mac_address(interface,new_mac):
	print("[+] Changing MAC address of ",interface," to ",new_mac)
	#subprocess module is used to run the terminal commands in python
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["ifconfig",interface,"up"])

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig",interface])
	mac_address_search_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_result))
	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		 print("[-] could not read MAC address")


options= get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC address :",str(current_mac))
change_mac_address(options.interface,options.new_mac)
if options.new_mac == current_mac:
	print("MAC address had sucessfully altered")
else:
	print("MAC address had not been altered")























