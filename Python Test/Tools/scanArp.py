from scapy.all import *
from threading import Thread,BoundedSemaphore

# Init Values
network = '192.168.40'
maxThread = 20
mutex = BoundedSemaphore(maxThread)

def sendArp(ip):
	arpRequest = Ether(dst = 'ff:ff:ff:ff:ff:ff')/ \
				 ARP(pdst = ip , hwdst = 'ff:ff:ff:ff:ff:ff')	
	arpResponse = srp1(arpRequest , iface = 'wlan0' , timeout = 3 , verbose = False)
	if arpResponse:
		try:
			print '\n[+] IP : ' + arpResponse.psrc + ', MAC : ' + arpResponse.hwsrc + '\n'
		except:
			print arpResponse.show()
	mutex.release()

def scanArp(network):
	for i in range(1,255):
		mutex.acquire()
		ip = network + '.' + str(i)
		print '[*] Scan ' + ip
		Thread(target = sendArp, args = (ip,)).start()

def main():
	print '[*] SCANING : Max Thread = %d'%(maxThread)
	scanArp(network)
	print '[*] SCAN COMPLELE'
if __name__ == '__main__':
	main()