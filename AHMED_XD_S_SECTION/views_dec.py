# Reversed by Exotic Hridoy
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
	import threading, ctypes
	from urllib.parse import urlparse, unquote, quote
	from string import ascii_letters, digits
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
file = ".__sanz_login_token_script_zefbot__.json"
path = "/data/data/com.termux/files/usr/.sanz"
try:
	os.mkdir(path)
except:
	pass
try:
	sys.stdout.write('\x1b]2;Script Auto Views TikTok by Sanz - Yt : FREE TUTORIAL\x07')
except:
	pass

clear = lambda : os.system("cls" if os.name == "nt" else "clear")
m = "\x1b[0;31m"
h = "\x1b[0;32m"
h3 = "\x1b[3;32m"
k = "\x1b[0;33m"
b = "\x1b[0;34m"
u = "\x1b[0;35m"
p = "\x1b[0m"
hx = "\x1b[1;30m"
bx = "\x1b[0;36m"
hx2 = "\x1b[0;30m"
hx3 = "\x1b[30m"
px = "\x1b[0m"
kx = "\x1b[0;33m"
hx4 = "\x1b[0;32m"
pp = "\x1b[7m"
dlt = "\x1b[K"
km = "\n %s[%s!%s]" % (p,m,p)
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
	exit("%s %sThe program is stopped\n" % (km,p))
except requests.exceptions.ConnectionError:
	hapus();sleep(0.5)
	exit(f"%s %sInternet connection error\n" % (km,p))
except Exception as lol:
	hapus();sleep(0.5)
	to = "%s %sError : %s" % (km,p,m)
	exit("%s%s\n" % (to,lol))

clear()
try:
	uax = {
		"user-agent": agent
	}
	url_user = [
		"https://sfile.mobi/6OdaxPzX7UW",
		"https://sfile.mobi/3tn8HsVw0gZ",
		"https://sfile.mobi/37d8v3t4RGn"
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
	exit("%s %sThe program is stopped\n" % (km,p))
except requests.exceptions.ConnectionError:
	hapus();sleep(0.5)
	exit(f"%s %sInternet connection error\n" % (km,p))
except Exception as lol:
	hapus();sleep(0.5)
	to = "%s %sError : %s" % (km,p,m)
	exit("%s%s\n" % (to,lol))

banner = "  %s_______        ___ __          __\n |   _   .-----.'  _|  |--.-----|  |_\n |___|   |  -__|   _|  _  |  _  |   _|\n  /  ___/|_____|__| |_____|_____|____|\n |:  1  \\\n |::.. . | %s❬ %sauto view video tiktok %s❭%s\n `-------'\n\n %s[%s•%s] Creator : %sSanz\n %s[%s•%s] Youtube : %sFREE TUTORIAL\n %s▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n %s[%s•%s] Your ip : %s%s\n %s[%s•%s] Total user : %s%s %speople" % (h,p,k,p,h,p,h,p,h,p,h,p,h,hx,p,bx,p,bx,sanz_ip,p,bx,p,k,sanz_user,p)
menu = " %s[%s1%s] Start auto view tiktok\n %s[%s2%s] Support admin\n %s[%s3%s] Exit" % (p,h,p,p,h,p,p,h,p)

class animasi:
	def __init__(self):
		try:
			user = open("%s/%s" % (path,file),"r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file("%s/%s" % (path,file));hapus();sleep(0.5)
			exit("%s %sThe token has expired, please log in again%s..\n" % (km,k,m))
		pass

	def teks(self,sanz):
		try:
			for free_tutorial in sanz + "\n":
				sys.stdout.write(free_tutorial)
				sys.stdout.flush()
				sleep(0.009)

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit("\n%s %sThe program is stopped\n" % (km,p))
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"%s %sInternet connection error\n" % (km,p))
		except Exception as lol:
			hapus();sleep(0.5)
			to = "\n%s %sError : %s" % (km,p,m)
			exit("%s%s\n" % (to,lol))

	def teks2(self,sanz):
		try:
			for free_tutorial in sanz + "\n":
				sys.stdout.write(free_tutorial)
				sys.stdout.flush()
				sleep(0.001)

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit("\n%s %sThe program is stopped\n" % (km,p))
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n%s %sInternet connection error\n" % (km,p))
		except Exception as lol:
			hapus();sleep(0.5)
			to = "\n%s %sError : %s" % (km,p,m)
			exit("%s%s\n" % (to,lol))

	def jeda(self):
		try:
			sleep(0.5);print();sleep(0.5)
		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit("%s %sThe program is stopped\n" % (km,p))
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"%s %sInternet connection error\n" % (km,p))
		except Exception as lol:
			hapus();sleep(0.5)
			to = "%s %sError : %s" % (km,p,m)
			exit("%s%s\n" % (to,lol))

class subrek:
	def __init__(self):
		try:
			user = open("%s/%s" % (path,file),"r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file("%s/%s" % (path,file));hapus();sleep(0.5)
			exit("%s %sThe token has expired, please log in again%s..\n" % (km,k,m))

		self.sanz = subrek_yt_free_tutorial
		self.main()

	def main(self):
		try:
			clear();sleep(0.5)
			menu2 = " %s[%s1%s] Support with donations\n %s[%s2%s] Support with subscribe yt\n %s[%s3%s] Return to the home menu\n %s[%s4%s] Exit" % (p,h,p,p,h,p,p,h,p,p,h,p)
			animasi().teks2(banner)
			animasi().jeda()
			animasi().teks(menu2)
			animasi().jeda()
			sxp = input(" %s[%s?%s] Choose : %s" % (p,m,p,h));sleep(2)
			if sxp in ["1","01"]:
				self.sawer()
			elif sxp in ["2","02"]:
				self.sub_yete()
			elif sxp in ["4","04"]:
				hapus();sleep(0.5)
				exit("%s %sThank you bro, don't forget to come back again..\n" % (km,p))
			elif sxp in [""]:
				hapus();sleep(0.5)
				exit("%s %sDon't be empty bro..\n" % (km,p))
			elif sxp in ["3","03"]:
				Sanz()
			else:
				hapus();sleep(0.5)
				exit("%s %sOption %s%s %sdoesn't exist bro..\n" % (km,p,h,sxp,p))

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit("%s %sThe program is stopped\n" % (km,p))
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"%s %sInternet connection error\n" % (km,p))
		except Exception as lol:
			hapus();sleep(0.5)
			to = "%s %sError : %s" % (km,p,m)
			exit("%s%s\n" % (to,lol))

	def sawer(self):
		try:
			sleep(1);print();sleep(1)
			animasi().teks(" %s[%s!%s] Thanks for those who want to share :D" % (p,m,p));sleep(1)
			animasi().teks(" %s[%s*%s] Not forcing it, just doing what you want ^_^" % (p,k,p));sleep(2)
			os.system("xdg-open https://saweria.co/SanzXp");sleep(3);print();sleep(1)
			input(" %s[%s>%s] Click enter to return " % (p,m,p));sleep(3)
			subrek()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit("%s %sThe program is stopped\n" % (km,p))
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"%s %sInternet connection error\n" % (km,p))
		except Exception as lol:
			hapus();sleep(0.5)
			to = "%s %sError : %s" % (km,p,m)
			exit("%s%s\n" % (to,lol))

	def sub_yete(self):
		try:
			sleep(1);print();sleep(1)
			animasi().teks(" %s[%s!%s] Subscribe to youtube admin woke" % (p,m,p));sleep(2)
			os.system(f"xdg-open {self.sanz}");sleep(3)
			animasi().teks(" %s[%s*%s] Thank you to those who have subscribed ^_^" % (p,k,p));sleep(2);print();sleep(1)
			input(" %s[%s>%s] Click enter to return " % (p,m,p));sleep(3)
			subrek()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit("%s %sThe program is stopped\n" % (km,p))
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"%s %sInternet connection error\n" % (km,p))
		except Exception as lol:
			hapus();sleep(0.5)
			to = "%s %sError : %s" % (km,p,m)
			exit("%s%s\n" % (to,lol))

class Zefbot:
	def __init__(self):
		try:
			user = open("%s/%s" % (path,file),"r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file("%s/%s" % (path,file));hapus();sleep(0.5)
			exit("%s %sThe token has expired, please log in again%s..\n" % (km,k,m))

		self.base_url = "https://zefoy.com/"
		self.headers = {"user-agent": agent}
		self.session = requests.Session()
		self.captcha_1 = None
		self.captcha_ = {}
		self.service = "Views"
		self.video_key = None
		self.services = {}
		self.services_ids = {}
		self.services_status = {}
		self.text = "Sanz x FREE TUTORIAL"
		_url = input(" %s[%s?%s] Enter url : %s" % (p,m,p,h));sleep(2)
		if "https://vt.tiktok.com/" in _url:
			conv_url = requests.get(_url, headers=self.headers).url
			uname_vid = re.findall(r'(@[a-zA-z0-9]*)\/?',conv_url)[0]
			id_vid = re.findall(r'.*\/([\d]*)?',conv_url)[0]
			url1 = "https://www.tiktok.com/%s/video/%s" % (uname_vid,id_vid)
		elif "https://www.tiktok.com/" in _url:
			url1 = _url
		elif "" in _url:
			hapus();sleep(0.5)
			exit("%s %sDon't be empty bro..\n" % (km,p))
		else:
			hapus();sleep(0.5)
			exit("%s %sInvalid URL\n" % (km,p))

		self.username = uname_vid
		self.id = id_vid
		self.url = url1
		animasi().jeda()

	def get_captcha(self):
		if os.path.exists("Data/session"):
			self.session.cookies.set("PHPSESSID", open("Data/session",encoding="utf-8").read(), domain="zefoy.com")
		request = self.session.get(self.base_url, headers=self.headers)
		if "Enter Video URL" in request.text:
			self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]
			return True
		try:
			for x in re.findall(r'<input type="hidden" name="(.*)" value="(.*)">', request.text):
				self.captcha_[x[0]] = x[1]
			self.captcha_1 = request.text.split('type="text" name="')[1].split('" oninput="this.value=this.value.toLowerCase()"')[0]
			captcha_url = request.text.split('<img src="')[1].split('" onerror="imgOnError()" class="')[0]
			request = self.session.get(f"{self.base_url}{captcha_url}",headers=self.headers)
			open("Data/captcha.png", "wb").write(request.content)
			animasi().teks(" %s[%s*%s] Solving captcha%s.." % (p,k,p,m))
			return False
		except Exception as e:
			print("%s %sCan't get captcha : %s%s" % (km,p,m,e))
			sleep(2)
			self.get_captcha()

	def send_captcha(self, new_session = False):
		if new_session:
			self.session = requests.Session()
			os.remove("Data/session")
			sleep(2)
		if self.get_captcha():
			animasi().teks(" %s[%s*%s] Connected to session" % (p,k,p))
			return (True, "The session already exists")
		captcha_solve = self.solve_captcha("Data/captcha.png")[1]
		self.captcha_[self.captcha_1] = captcha_solve
		request = self.session.post(self.base_url, headers=self.headers, data=self.captcha_)
		if "Enter Video URL" in request.text:
			animasi().teks(" %s[%s✓%s] Session was created" % (p,h,p))
			open("Data/session","w",encoding="utf-8").write(self.session.cookies.get("PHPSESSID"))
			self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]
			return (True, captcha_solve)
		else:
			return (False, captcha_solve)

	def solve_captcha(self, path_to_file = None, b64 = None, delete_tag = ["\n","\r"]):
		if path_to_file:
			task = path_to_file
		else:
			open("Data/temp.png","wb").write(base64.b64decode(b64))
			task = "Data/temp.png"
		request = self.session.post("https://api.ocr.space/parse/image?K87899142388957", headers={"apikey":"K87899142388957"}, files={"task":open(task,"rb")}).json()
		solved_text = request["ParsedResults"][0]["ParsedText"]
		for x in delete_tag:
			solved_text = solved_text.replace(x,"")
		return (True, solved_text)

	def get_status_services(self):
		request = self.session.get(self.base_url, headers=self.headers).text
		for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+\n.+', request):
			self.services[x.split('<h5 class="card-title">')[1].split("<")[0].strip()] = x.split('d-sm-inline-block">')[1].split("</small>")[0].strip()
		for x in re.findall(r'<h5 class="card-title mb-3">.+</h5>\n<form action=".+">', request):
			self.services_ids[x.split('title mb-3">')[1].split("<")[0].strip()] = x.split('<form action="')[1].split('">')[0].strip()
		for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+<button .+', request):
			self.services_status[x.split('<h5 class="card-title">')[1].split("<")[0].strip()] = False if "disabled class" in x else True
		sleep(1.5);animasi().jeda()
		return (self.services, self.services_status)

	def find_video(self):
		if self.service is None:
			return (False, "You didn't choose the service")
		while True:
			if self.service not in self.services_ids:
				self.get_status_services()
				sleep(1)
			request = self.session.post(f"{self.base_url}{self.services_ids[self.service]}", headers={"content-type":"multipart/form-data; boundary=----WebKitFormBoundary0nU8PjANC8BhQgjZ", "user-agent":self.headers["user-agent"], "origin":"https://zefoy.com"}, data=f'------WebKitFormBoundary0nU8PjANC8BhQgjZ\r\nContent-Disposition: form-data; name="{self.video_key}"\r\n\r\n{self.url}\r\n------WebKitFormBoundary0nU8PjANC8BhQgjZ--\r\n')
			try:
				self.video_info = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
			except:
				sleep(3)
				continue
			if "Session expired. Please re-login" in self.video_info:
				print(" %s %sSession expired. Reloging%s..." % (km,p,m))
				self.send_captcha()
				return
			elif "service is currently not working" in self.video_info:
				return (True, "Service is currently not working, try again later. | You can change it in config.")
			elif """onsubmit="showHideElements""" in self.video_info:
				self.video_info = [self.video_info.split('" name="')[1].split('"')[0],self.video_info.split('value="')[1].split('"')[0]]
				return (True, request.text)
			elif "Checking Timer..." in self.video_info:
				try:
					t = int(re.findall(r'ltm=(\d*);', self.video_info)[0])
					sanz = int(re.findall(r'ltm=(\d*);', self.video_info)[0])
				except:
					return (False,)
				if sanz == 0:
					self.find_video()
				elif sanz >= 1000:
					print("%s %sYour IP was banned" % (km,p))
				_ = time.time()
				while time.time()-2<_+sanz:
					t -= 1
					sleep(0.5)
					sys.stdout.write("\r %s[%s•%s] Countdown : %s%s %ssec " % (p,k,p,k,t,p))
					sys.stdout.flush()
					sleep(1)
				sys.stdout.write("\r%s" % dlt);sleep(0.5)
				continue
			elif "Too many requests. Please slow" in self.video_info:
				sleep(3)
			else:
				print("%s %s%s" % (km,m,self.video_info))

	def use_service(self):
		if self.find_video()[0] is False:
			return False
		self.token = "".join(random.choices(ascii_letters+digits, k=16))
		request = self.session.post(f"{self.base_url}{self.services_ids[self.service]}", headers={"content-type": f"multipart/form-data; boundary=----WebKitFormBoundary{self.token}", "user-agent":self.headers["user-agent"], "origin":"https://zefoy.com"}, data=f'------WebKitFormBoundary{self.token}\r\nContent-Disposition: form-data; name="{self.video_info[0]}"\r\n\r\n{self.video_info[1]}\r\n------WebKitFormBoundary{self.token}--\r\n')
		try:
			res = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
		except:
			sleep(3)
			return ""
		if "Session expired. Please re-login" in res:
			print("%s %sSession expired. Reloging%s..." % (km,p,m))
			self.send_captcha()
			return ""
		elif "Too many requests. Please slow" in res:
			sleep(3)
		elif "service is currently not working" in res:
			return ("Service is currently not working, try again later. | You can change it in config.")
		else:
			sanz_views = re.findall("<span style='font-size:110%;font-weight:bold;font-family:Arial, Helvetica, sans-serif;text-align:center;color:green;'>Successfully (.*?) views sent.</span>",res)[0]
			animasi().teks(" %s[%s✓%s] Successfully %s%s %sviews sent." % (p,h,p,h,sanz_views,p))
			sleep(0.5)

	def get_video_info(self):
		request = self.session.get(f"https://tiktok.livecounts.io/video/stats/{urlparse(self.url).path.rpartition('/')[2]}",headers={"authority":"tiktok.livecounts.io","origin":"https://livecounts.io","user-agent":self.headers["user-agent"]}).json()
		if "viewCount" in request:
			return request
		else:
			return {"viewCount": 0, "likeCount": 0, "commentCount": 0, "shareCount": 0}

	def get_video_id(self, url_ = None, set_url=True):
		if url_ is None:
			url_ = self.url
		if url_[-1] == "/":
			url_=url_[:-1]
		url = urlparse(url_).path.rpartition("/")[2]
		if url.isdigit():
			self.url = url_; return url_
		request = requests.get(f"https://api.tokcount.com/?type=videoID&username=https://vm.tiktok.com/{url}", headers={"origin": "https://tokcount.com","authority": "api.tokcount.com","user-agent": agent})
		if request.text == "":
			print("%s %sInvalid URL" % (km,p))
			return False
		else:
			json_=request.json()
		if 'author' not in json_:
			print("%s %s%s %s| Invalid URL" % (km,h,self.url,p))
			return False
		if set_url:
			self.url = "https://www.tiktok.com/%s/video/%s" % (self.username,self.id)
			print("%s %sFormated video url %s-> %s%s" % (km,p,m,h,self.url))
		return request.text

	def check_config(self):
		while True:
			try:
				last_url = self.url
				if last_url != self.url:
					self.get_video_id()
			except Exception as e:
				print("%s %s" % (km,e))
			sleep(4)

	def update_name(self):
		while True:
			try:
				ctypes.windll.kernel32.SetConsoleTitleA(self.text.encode())
				video_info = self.get_video_info()
				self.text = " %s[%s✓%s] Successfully %s%s %sviews sent." % (p,h,p,h,video_info["viewCount"],p)
			except: pass
			sleep(5)

class Sanz:
	def __init__(self):
		try:
			user = open("%s/%s" % (path,file),"r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			hapus_file("%s/%s" % (path,file));hapus();sleep(0.5)
			exit("%s %sThe token has expired, please log in again%s..\n" % (km,k,m))

		self.Main()

	def Main(self):
		try:
			clear();sleep(0.5)
			animasi().teks2(banner)
			animasi().jeda()
			animasi().teks(menu)
			animasi().jeda()
			sxp = input(" %s[%s?%s] Choose : %s" % (p,m,p,h));sleep(2)
			if sxp in ["1","01"]:
				clear();sleep(0.5)
				animasi().teks2(banner)
				animasi().jeda()
				animasi().teks(" %s[%s!%s] Enter url video tiktok %s↴\n     %shttps://vt.tiktok.com/xxxxxxx/%s  %sor%s\n     %shttps://www.tiktok.com/@xxxxxx/video/xxxxxx%s" % (p,m,p,m,h3,px,hx,p,h3,px))
				animasi().jeda()
				Z = Zefbot()
				threading.Thread(target=Z.check_config).start()
				threading.Thread(target=Z.update_name).start()
				Z.send_captcha()
				while True:
					try:
						if "Service is currently not working, try again later" in str(Z.use_service()):
							print("%s %sService is currently not working, try again later." % (km,p))
							sleep(5)
					except Exception as e:
						print("%s %sCritical ERROR | retrying in 10 seconds. | %s%s" % (km,p,m,e))
						sleep(10)
			elif sxp in ["2","02"]:
				subrek()
			elif sxp in ["3","03"]:
				hapus();sleep(0.5)
				exit("%s %sThank you bro, don't forget to come back again..\n" % (km,p))
			elif sxp in [""]:
				hapus();sleep(0.5)
				exit("%s %sDon't be empty bro.." % (km,p))
			else:
				hapus();sleep(0.5)
				exit("%s %sOption %s%s %sdoesn't exist bro..\n" % (km,p,h,sxp,p))

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit("%s %sThe program is stopped\n" % (km,p))
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"%s %sInternet connection error\n" % (km,p))
		except Exception as lol:
			hapus();sleep(0.5)
			to = "%s %sError : %s" % (km,p,m)
			exit("%s%s\n" % (to,lol))

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
					sys.stdout.write("\r%s[%s•%s] Memverifikasi token, tunggu %s[%s" % (p,h,p,k,h) + sxp[i % len(sxp)]+"%s] " % k)
					sys.stdout.flush()

			sys.stdout.write("\r\033[K");sleep(1)

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			sys.stdout.write("\r\033[K")
			exit("%s[%s!%s] Program Dihentikan\n" % (p,m,p))
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			sys.stdout.write("\r\033[K")
			exit("%s[%s!%s] Koneksi Internet Error\n" % (p,m,p))
		except Exception as lol:
			hapus();sleep(0.5)
			sys.stdout.write("\r\033[K")
			to="%s[%s!%s] Error %s: %s" % (p,m,p,m,p)
			exit("%s%s\n" % (to,lol))

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
			user = open("%s/%s" % (path,file),"r").read()
			___user___ = json.loads(user)["data"]["token"]
		except:
			clear()
			url = "https://pastebin.com/raw/84nxVehv" # url link + pass random mode
			req = get(url,headers={"user-agent":agent}).text
			index_link = req.split("Link: ")[1].split("\r\n")[0].split("|")
			index_pass = req.split("Pass: ")[1].split("\r\n")[0].split("|")
			_link1 = index_link[0];_link2 = index_link[1];_link3 = index_link[2]
			_pass1 = index_pass[0];_pass2 = index_pass[1];_pass3 = index_pass[2]
			_acak1 = "%s|%s" % (_link1,_pass1);_acak2 = "%s|%s" % (_link2,_pass2);_acak3 = "%s|%s" % (_link3,_pass3)
			index1 = random.choice([_acak1.split("|"),_acak2.split("|"),_acak3.split("|")]);index2 = index1[0].split(";")
			_link_a = get("https://tinyurl.com/api-create.php?url="+index2[0],headers={"user-agent":agent}).text
			_link_b = get("https://tinyurl.com/api-create.php?url="+index2[1],headers={"user-agent":agent}).text
			_pass = get(index1[1],headers={"user-agent":agent}).text
			# -- Sanz Ganz -- #
			banner = "[bold red]● [bold yellow]● [bold green]●[/]\n[bold red]     __             _        ___\n    / /  ___  ___ _(_)__    / _ \___ ____ ____\n   / /__/ _ \/ _ `/ / _ \  / ___/ _ `/ _ `/ -_)\n[bold white]  /____/\___/\_, /_/_//_/ /_/   \_,_/\_, /\__/\n            /___/                   /___/[/]\n\n   [bold white on red] Created by Sanz - Youtube : FREE TUTORIAL [/]"
			printer(Panel(banner,title="[bold red]• [bold white]Selamat %s [bold red]•[/]" % self.sxp_waktu(),width=53,style="color(8)"));print()
			print("%s[%s¤%s] Tanggal %s: %s%s, %s %s %s" % (p,m,p,m,p,hari,tanggal,bulan,tahun))
			print("%s[%s¤%s] Waktu   %s: %s%s" % (p,m,p,m,p,_waktu))
			print("%s-------------" % hx2)
			print("%s[%s•%s] Link token %s: %s%s%s" % (p,m,p,m,hg,_link_a,px));print()
			print("%s[%s!%s] Jika link diatas error atau tidak bisa dilewati,\n    silahkan gunakan link dibawah %s↓" % (p,m,p,m));print()
			print("%s[%s•%s] Link token %s: %s%s%s" % (p,m,p,m,hg,_link_b,px));print()
			print("%s[%s!%s] Silahkan ambil dulu %s↑%s token nya lalu" % (p,m,p,m,p))
			print("    pastekan dibagian input dibawah %s↓" % m);print()
			sanz_pw = input("%s[%s?%s] Input Token %s: %s" % (p,m,p,m,hx2))
			sleep(2);print();sleep(1)
			if sanz_pw == _pass:
				self.animasi(int(rd))
				sleep(0.5)
				save = open("%s/%s" % (path,file),"w").write('{\n  "data": {\n  "token": "%s",\n  "creator": "Sanz",\n  "youtube": "FREE TUTORIAL"\n }\n}' % sanz_pw)
				print("\a%s[%s✓%s] Token Benar" % (p,h,p))
				sleep(2)
				clear()
			elif sanz_pw == "":
				sleep(0.5)
				print("\a%s[%s!%s] Jangan Kosong Ngab" % (p,m,p))
				sleep(2)
				self.log_pewe()
			else:
				self.animasi(int(rd))
				sleep(0.5)
				print("\a%s[%sx%s] Token Salah" % (p,m,p))
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
			print("%sSubrek dulu channel %sYT Aing cuk%s!!" % (bx,p,bx));sleep(1)
			os.system("xdg-open %s" % subrek_yt_free_tutorial);sleep(10)
			Sanz()

		except KeyboardInterrupt:
			hapus();sleep(0.5)
			exit("\n%s[%s!%s] Program Dihentikan\n" % (p,m,p))
		except requests.exceptions.ConnectionError:
			hapus();sleep(0.5)
			exit(f"\n%s[%s!%s] Koneksi Internet Error\n" % (p,m,p))
		except KeyError:
			hapus();sleep(0.5)
			exit("\n%s[%s!%s] Server Error\n%s[%s>%s] Silahkan Coba Lagi%s..\n" % (p,m,p,p,m,p,m))
		except json.decoder.JSONDecodeError:
			hapus();sleep(0.5)
			exit("\n%s[%s!%s] Server Error\n%s[%s!%s] Silahkan Coba Lagi%s..\n" % (p,m,p,p,m,p,m))
		except Exception as lol:
			hapus();sleep(0.5)
			to="\n%s[%s!%s] Error %s: %s" % (p,m,p,m,p)
			exit("%s%s\n" % (to,lol))


if __name__ == "__main__":
	try:
		___free_tutorial___ = "Script termux auto view video tiktok by Sanz"
		_____sanz_ganz_____ = open("Sanz","w").write(___free_tutorial___)
		__sanz_login__()
	except KeyboardInterrupt:
		hapus();sleep(0.5)
		exit("%s %sThe program is stopped\n" % (km,p))
	except requests.exceptions.ConnectionError:
		hapus();sleep(0.5)
		exit(f"%s %sInternet connection error\n" % (km,p))
	except Exception as lol:
		hapus();sleep(0.5)
		to = "%s %sError : %s" % (km,p,m)
		exit("%s%s\n" % (to,lol))
