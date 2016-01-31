import rarfile,threading

RARNAME = 'a.rar'
rf = rarfile.RarFile(RARNAME)
found = False
mutex = threading.Lock()
def extract(rarfile, password = None):
	try:
		if password:
			rarfile.setpassword(password)		
		for f in rarfile.infolist():
			rf.read(f)
		with mutex:
			print '[+] Found Password : ' + password
		found = True
	except:
		pass

for password in ('a','b','c','a','b','c','a','b','c','a','b','c','a','b','c','a','b','c','a','b','c','a','b','c','a','b','c','viptam','a','b','c'):
	print '[-] Try Password : ' + password
	if found: break
	threading.Thread(target = extract, args = (rf, password)).start()
