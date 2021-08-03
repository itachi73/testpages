import os
import sys
import subprocess
allfiles = os.listdir(os.getcwd())
for filename in allfiles:
	for i in range(1,3):
   		with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
   			for line in f :
   				if len(line) > 3 :
   					try :  
   						output = subprocess.check_output("dig "+ line, shell=True)
   						out = str(output)
   						if "NXDOMAIN" in out :
   							if "CNAME" in out :
   								print (line)
   								record = subprocess.check_output("dig "+ line +" +short", shell=True)
   								print (record)
   					except : 
   						print ("Error-happened: "+ line )
