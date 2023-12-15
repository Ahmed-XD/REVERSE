#       › reversed by exotic-hridoy ‹
import requests, re, os, time, random, sys
from bs4 import BeautifulSoup as parser
list = 0
hc = {}
banner = f"""
                     _____.__         
  ____  ____   _____/ ____\__| ____   
_/ ___\/  _ \ /    \   __\|  |/ ___\  
\  \__(  <_> )   |  \  |  |  / /_/  > All custom http \x1b[1;92mconfig\x1b[0m
 \___  >____/|___|  /__|  |__\___  /  
     \/           \/        /_____/   

             \033[4;37mhttps://github.com/Xenzi-XN1/ConfigHc\x1b[0m
"""

path = "/storage/emulated/0/config-http-custom"
try:os.mkdir(path)
except:pass

def Animasi(teks, second):
	war = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m"])
	bar = [
		"[\x1b[1;91m■\x1b[0m     ] {} detik  ",
		"[\x1b[1;92m■■\x1b[0m    ] {} detik  ",
		"[\x1b[1;93m■■■\x1b[0m   ] {} detik  ",
		"[\x1b[1;94m■■■■\x1b[0m  ] {} detik  ",
		"[\x1b[1;95m■■■■■\x1b[0m ] {} detik  "
	]
	put = [
		f"[\x1b[1;90m--\x1b[0m]",
		f"[{war}>\x1b[1;90m-\x1b[0m]",
		f"[\x1b[1;90m-{war}>\x1b[0m]"
	]
	i = 0
	while True:
		print(f"\r{put[i % len(put)]} {teks} {bar[i % len(bar)].format(str(second - i))}", end="\r")
		time.sleep(1)
		i += 1
		if i == second + 1:
			break

def Config():
	global list
	os.system("clear");print (banner)
	a = parser(requests.get("https://sfile.mobi/loads/6/Config.html").text, 'html.parser')
	for b in a.find_all("div", {"class":"list"}):
		for c in re.findall('<a href="(.*?)">(.*?)</a>', str(b)):
			list += 1
			d = re.search("<small>(.*?), Uploaded: (.*?), Download: (.*?)</small>", str(b))
			hc.update({
				f'{list}':{
					"name": c[1],
					"url": c[0],
					"upload": d.group(2),
					"total": d.group(3),
					"size": d.group(1)
				}
			})
			print (f"[\x1b[1;92m{list}\x1b[0m]. {c[1]}")

	chs = input("\n[•>] Pilih config: ")
	try:e = hc[chs]
	except KeyError:
		exit("[!>] Pilih dengan benar")
	print (f"\n[+>] Nama           : \x1b[1;92m{e['name']}\x1b[0m")
	print (f"[+>] Code url       : \x1b[1;90m{str(e['url']).replace('https://sfile.mobi/', '')}\x1b[0m")
	print (f"[+>] Tanggal upload : \x1b[1;92m{e['upload']}\x1b[0m")
	print (f"[+>] Ukuran file    : \x1b[1;92m{e['size']}\x1b[0m")
	print (f"[+>] Total download : \x1b[1;92m{e['total']}\x1b[0m")
	dwk = input("[?>] inggin melanjutkan download? y/t: ")
	if dwk.lower() in ["y"]:
		with requests.Session() as com:
			try:
				f = com.get(e['url']).text
				# Get url file
				link = re.search('<a class="w3-button w3-blue w3-round" id="download" href="(.*?)" onclick="location.href=this.href+'"(.*?)"'+'"(.*?)"';return false;" rel="nofollow">(.*?)</a>', str(f))
				g = str(link.group(3)).split("+")[1].replace("'", "")
				key = str(link.group(3)).split("+")[2].replace("'", "")
				url = f"{str(link.group(1))}{g}{key}"
				nama_file = e['name'].replace(" ", "-")
				# Download file
				run = com.get(url).content
				with open(f"{path}/{nama_file}", "wb") as sv:
					sv.write(run)
				print ()
				Animasi("Tunggu sebentar sedang mendownload", 5)
				print (f"[√>] Download File (\x1b[1;90m{nama_file}\x1b[0m) \x1b[1;92mberhasil\x1b[0m      ")
				print (f"[√>] Tersimpan di folder : \x1b[1;92m{path}/{nama_file}\x1b[0m")
			except:exit("\n[!>] Download gagal/error")
				
	else:exit("\n[#>] Download tidak di lanjutkan :)")
if __name__=='__main__':
	os.system("clear");print (banner)
	with requests.Session() as com:
		new_url = com.get("https://pastebin.com/raw/hSdE4XVG").json()
		if 'on' in new_url["Status"]:
			try:
				key = open('.Login.key','r').read()
				if new_url["Key"] in key:
					Config()
				else:os.remove(".Login.key");os.system(f"python {sys.argv[0]}")
			except FileNotFoundError:
				url_key = com.post("https://api.biturl.top/short",data={"url":new_url["url"]},headers={'user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'}).json()['short']
				print (f"[+>] Link Download Key: \033[4;32m{url_key}\x1b[0m")
				key = input("[?>] Key:\x1b[1;92m ")
				print ("\x1b[0m")
				Animasi("Tunggu sebentar sedang mengecek key", 5)
				if new_url["Key"] in key:
					open(".Login.key", "w").write(key)
					print ("[√>] Selamat login \x1b[1;92mkey\x1b[0m berhasil >_<                       ")
					time.sleep(3)
					Config()
				else:exit(f"[!>] Login gagal, silahkan cek kembali key anda !!!      ")
		else:exit(f"[!>] Mohon maaf script sedang di \x1b[1;93mperbaiki\x1b[0m, silahkan hubungi admin >_<")
