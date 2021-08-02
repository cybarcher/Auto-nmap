import os
import sys
from multiprocessing.dummy import Pool as ThreadPool 
from netaddr import IPNetwork
import socket
import time 
import nmap

yes = {'yes','y', 'ye', ''}
no = {'no','n'}
if os.path.exists('./scans.log'):
	out=open('scans.log','a')
else:
	out=open('scans.log','w')


def checkInternetConnection():
	host="8.8.8.8"
	port=53
	timeout=3

	try:
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
	except Exception as ex:
		print "Please check your internet......."
		time.sleep(3)
		checkInternetConnection()


def scan(i):

	checkInternetConnection()
	i=i.strip()
	#nm = nmap.PortScanner()
	#nm1=nm.scan(i, '1')
	#u=nm[i].state()
	#print u
	os.system("nmap -sV -v -Pn -oX %s.xml %s"% (str(i),str(i)))
	l=os.path.realpath(str(i)+".xml")
	ll=open(l,'r')
	lll=(ll.read())	
	if "</nmaprun>" in lll :
		fflist=open('scans.log','a')
		fflist.write(i+"\n")
		fflist.close()
		
def htmlReport():
	os.system('mkdir xml html 2>/dev/null')
	replist = open('scans.log','r')
	for i in replist:
		
		os.system('xsltproc %s.xml -o %s.html' % (str(i).strip(),str(i).strip()))
	os.system('mv *.xml xml/ 2>/dev/null')
	os.system('mv *.html html/ 2>/dev/null')
	exit(0) 

	

if __name__ == '__main__':

	if len(sys.argv) < 3:
		print "\nUSAGE: python "+sys.argv[0]+" ipList threads_count \n\n"
		sys.exit(1)
	start = time.time()
	hosts=sys.argv[1]
	threads=sys.argv[2]
	ff= []
	with open(hosts, "r") as hostsFile:
		
		for line in hostsFile: # Reading cidr from file
			#print line.strip()
			for ip in IPNetwork(line.strip()): # resolve cidr
				ip1 = str(ip).strip()
				ff.append(ip1)
		choice = raw_input("Do you want to restore from previous session (y/n): ").lower()
		if choice in no:
			open('scans.log','w').close()

		rd = [line.rstrip('\n') for line in open('scans.log')]
		res = list(set(ff) - set(rd))
		pool = ThreadPool(int(threads))
		results = pool.map(scan, res)
			
		pool.close() 
		pool.join()
	#choice
	
	
	
	htmlReport()
		#for item in res:
		#	results.append(scan(item))

			
	
	exit(0)
