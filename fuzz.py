import os
import sys
import subprocess

domain = sys.argv[1]
list = sys.argv[2]

lines = [line.rstrip('\n') for line in open(list)]

subdomains = []


for x in lines: 
	subdomains.append(x+'.'+domain)

for y in subdomains : 
	try :  
		output = subprocess.check_output("dig "+ y, shell=True)
		out = str(output)

		if "NXDOMAIN" in out :
			if "CNAME" in out :
				print (y)
				record = subprocess.check_output("dig "+ y +" +short", shell=True)
				print (record)
				with open('vulx.txt', 'a') as vul:
        				vul.write("%s\n" % y)
        				vul.write("%s\n" % record)
	except : 
		print ("Error-happened: "+ y )

	

