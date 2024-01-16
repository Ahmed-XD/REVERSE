import os,time,sys
STLP="RUN"
log="""\033[1;37m
âââââââââââââââââââââââââââââââââââââââââââââââ
â \033[1;36m   ââ¦âââââ¦ââââ¦ââ¦ â¦ââ â¦   ââââââââ¦ââ¦ â¦âââ \033[1;37m   â
â  \033[1;36m   â ââ£ â â¦âââââ âââ©â¦âââââââââ£  â â ââ ââ  \033[1;37m  â
â  \033[1;36m   â© ââââ©âââ© â©ââââ© ââ   ââââââ â© ââââ©    \033[1;37m  â
â ââââââââââââââââââââââââââââââââââââââââââââââ£
â \033[1;32m   [â] AUTHOR   :   TEAM STLP             \033[1;37m  â
â  \033[1;33m  [â] GITHUB   :   STLP-TEAM            \033[1;37m   â
â   \033[1;35m [â] FACEBOOK :   SPAMMING & TERMUX   \033[1;37m    â
â    \033[1;34m                 LEARNING POINT(STLP)  \033[1;37m  â
âââââââââââââââââââââââââââââââââââââââââââââââ
  """
def logo():
  cl()
  print(log)
  option()
def option():
  print("""\n         \033[46m\033[1;31mTOOLS  OPTIONS\033[0m\033[1;37m
  
 \033[1;32m  [01] GIVE STORAGE PERMISSION
 \033[1;34m  [02] INSTALL BASIC PACKAGE
 \033[1;35m  [03] MAKE TERMUX BANNER(NORMAL)
 \033[1;36m  [04] MAKE TERMUX BANNER(LOGIN SYSTEM)
 \033[1;31m  [05] REMOVE ANY TERMUX BANNER
 \033[1;32m  [06] SET SHORT-KUT KEY
 \033[1;34m  [07] SET TERMUX COLOUR THEME
 \033[1;35m  [08] SET TERMUX FONT
 \033[1;36m  [09] SET CUSTOM TERMUX FONT
 \033[1;31m  [10] REMOVE TERMUX COLOUR THEME
 \033[1;32m  [11] REMOVE ANY TERMUX FONT
 \033[1;34m  [12] SET DEFAULT SHORT-KUT KEY
 \033[1;35m  [13] OUR MORE TOOLS
 \033[1;36m  [14] FIND US ON FB
 \033[1;31m  [15] EXIT TOOLS
  """)
  os.system("xdg-open https://facebook.com/groups/spamming.termux.learning.point/")
  ab=input("\n\033[1;37m   [â¢] YOUR CHOICE : \033[1;32m")
  if ab in ["1","01"]:
    os.system("termux-setup-storage")
    sys.exit()
  elif ab in ["2","02"]:
    install()
    sys.exit()
  elif ab in ["3","03"]:
    banner_normal()
    sys.exit()
  elif ab in ["4","04"]:
    banner_login()
    sys.exit()
  elif ab in ["5","05"]:
    rm_banner()
    sys.exit()
  elif ab in ["6","06"]:
    key()
    sys.exit()
  elif ab in ["7","07"]:
    color()
    sys.exit()
  elif ab in ["8","08"]:
    font()
    sys.exit()
  elif ab in ["9","09"]:
    custom_font()
    sys.exit()
  elif ab in ["10"]:
    del_color()
    sys.exit()
  elif ab in ["11"]:
    del_font()
    sys.exit()
  elif ab in ["12"]:
    del_key()
    sys.exit()
  elif ab in ["13"]:
    os.system("xdg-open https://github.com/STLP-TEAM?tab=repositories")
    sys.exit()
  elif ab in ["14"]:
    os.system("xdg-open https://facebook.com/groups/spamming.termux.learning.point/")
    sys.exit()
  elif ab in ["15"]:
    sys.exit("   EXIT DONE\n")
  else:
    print("   WRONG VALUE ENTERED!")
    time.sleep(0.5)
    print("   TRY AGAIN!\n")
    time.sleep(0.5)
    logo()
def banner_login():
  cl()
  print(log)
  os.system("chsh -s bash")
  os.system("touch ~/.hushlogin")
  name=input("\n\033[1;37mENTER YOUR NAME :\033[1;32m ")
  while True:
    ab=input("\033[1;37mCREATE A NEW PASSWORD :\033[1;32m ")
    mn=input("\033[1;37mCONFIRM PASSWORD : \033[1;32m")
    if ab==mn:
      passw=ab
      break
    else:
      print("\033[1;31mDIDN'T MATCHED,TRY AGAIN\033[1;37m")
      continue
  banner="""#github.com/STLP-TEAM\n#FACEBOOK: Spamming & Termux Learning Point\nshopt -s histappend\nshopt -s histverify\nexport HISTCONTROL=ignoreboth\n\n\nACTUAL="stlp"\nread -p "Password: " enteredpass\necho ""\n[ "$enteredpass" != "$ACTUAL" ] && echo "OPPS!PASSWORD WRONG" && sleep 1 && echo "EXITING...." && sleep 1 && exit || clear\n\necho -e "\e[1;33mâââââââââââââââââââââââââââââââââââââââââ"\necho -e "  \e[1;33m     ââ\e[1;32m  WELLCOME TO TERMUX\e[1;33m ââ "\necho -e "\e[1;37mHACKING IS NOT A CRIME ââ IT's MY PASSION\e[0m"\necho -e "\e[1;33mâââââââââââââââââââââââââââââââââââââââââ\e[1;36m"\nfiglet -f slant NAZMUL\nPROMPT_DIRTRIM=2\nPS1='\n\[\e[1;34m\]ââââ[\[\e[1;31m\]NAZMUL@TERMUX\[\e[1;34m\]\[\e[1;34m\]]ââ\[\e[1;33m\]{\[\e[1;32m\]\w\[\e[0m\]\[\e[1;33m\]}\n\[\e[1;34m\]âââââ\[\e[1;32m\]#\[\e[1;97m\] '\n\nif [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then\n  command_not_found_handle() {\n           /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"\n   }\nfi\n"""
  redy=banner.replace("NAZMUL",name)
  ready=redy.replace("stlp",passw)
  file=open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
  file.write(ready)
  file.close()
  os.system("termux-reload-settings")
  print("\033[1;36mPROCESS COMPLETED\nRESTART YOUR TERMUX\033[1;37m\n")

#github.com/STLP-TEAM\n#FACEBOOK: Spamming & Termux Learning Point\n

def banner_normal():
  cl()
  print(log)
  name=input("\n\033[1;37mENTER YOUR NAME :\033[1;32m ")
  os.system("chsh -s bash")
  os.system("touch ~/.hushlogin")
  banner="""#github.com/STLP-TEAM\n#FACEBOOK: Spamming & Termux Learning Point\nshopt -s histappend\nshopt -s histverify\nexport HISTCONTROL=ignoreboth\necho -e "\e[1;33mâââââââââââââââââââââââââââââââââââââââââ"\necho -e "  \e[1;33m     ââ\e[1;32m  WELLCOME TO TERMUX\e[1;33m ââ "\necho -e "\e[1;37mHACKING IS NOT A CRIME ââ IT's MY PASSION\e[0m"\necho -e "\e[1;33mâââââââââââââââââââââââââââââââââââââââââ\e[1;36m"\nfiglet -f slant NAZMUL\nPROMPT_DIRTRIM=2\nPS1='\n\[\e[1;34m\]ââââ[\[\e[1;31m\]NAZMUL@TERMUX\[\e[1;34m\]\[\e[1;34m\]]ââ\[\e[1;33m\]{\[\e[1;32m\]\w\[\e[0m\]\[\e[1;33m\]}\n\[\e[1;34m\]âââââ\[\e[1;32m\]#\[\e[1;97m\] '\n\nif [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then\n  command_not_found_handle() {\n           /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"\n   }\nfi\n"""
  ready=banner.replace("NAZMUL",name)
  file=open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
  file.write(ready)
  file.close()
  os.system("termux-reload-settings")
  print("\033[1;36mPROCESS COMPLETED\nRESTART YOUR TERMUX\033[1;37m\n")
def rm_banner():
  cl()
  print(log)
  os.system("chsh -s bash")
  os.system("touch ~/.hushlogin")
  os.system("rm ~/.hushlogin")
  motd_file = open("/data/data/com.termux/files/usr/etc/motd","w")
  motd_file.write("Welcome to Termux!\n\nCommunity forum: https://termux.com/community\nGitter chat:     https://gitter.im/termux/termux\nIRC channel:     termux on libera.chat\n\nWorking with packages:\n\n * Search packages:   pkg search <query>\n * Install a package: pkg install <package>\n * Upgrade packages:  pkg upgrade\n\nSubscribing to additional repositories:\n\n * Root:     pkg install root-repo\n * Unstable: pkg install unstable-repo\n * X11:      pkg install x11-repo\n\nReport issues at https://termux.com/issues\n\nThe Google Play version of the Termux app no longer\nreceives updates. For more information, visit:\nhttps://wiki.termux.com/wiki/Termux_Google_Play\n\n")
  motd_file.close()
  bash_file = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
  bash_file.write("""#github.com/STLP-TEAM\n#FACEBOOK: Spamming & Termux Learning Point\nshopt -s histappend\nshopt -s histverify\nexport HISTCONTROL=ignoreboth\nPROMPT_DIRTRIM=2\nPS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '\nif [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then\n	command_not_found_handle() {\n		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"\n	}\nfi""")
  bash_file.close()
  os.system("termux-reload-settings")
  print("\033[1;36mPROCESS COMPLETED\nRESTART YOUR TERMUX\033[1;37m\n")
def install():
  cl()
  print(log)
  print("""
         \033[1;36m REQUIREMENTS\n
   \033[1;35m  [â] 1 GB INTERNET (Minimum)
     [â] 1.5 GB FREE STORAGE (Minimum)
  """)
  ab=input("\033[1;31mSTART INSTALLATION.....[Y/N] ")
  ab=ab.replace(" ","")
  ab=ab.upper()
  if ab=="Y":
    pass
  elif ab=="N":
    print("\033[1;36mINSTALLATION STOPPED BY YOU")
    sys.exit()
  else:
    print("\033[1;36mINSTALLATION STOPPED FOR YOUR WRONG ACTION")
    sys.exit()
  print("\n\033[1;32mPLEASE WAIT A MOMENT...")
  time.sleep(1)
  print("\033[1;35mDON'T EXIT TERMUX BEFORE COMPLETE INSTALLATION")
  time.sleep(1)
  print("\033[1;36mIF IT'S WANT ANY PERMISSION, GIVE THERE \"y\"")
  time.sleep(1)
  input("\n\033[1;31mPRESS ENTER FOR START ")
  print("\033[1;32m")
  os.system("pkg update -y")
  print("\033[1;32m")
  os.system("pkg upgrade -y")
  print("\033[1;32m")
  os.system("pkg install git -y")
  print("\033[1;32m")
  os.system("pkg install python -y")
  print("\033[1;32m")
  os.system("pkg install python2 -y")
  print("\033[1;32m")
  os.system("pkg install wget -y")
  print("\033[1;32m")
  os.system("pkg install figlet -y")
  print("\033[1;32m")
  os.system("pkg install curl -y")
  print("\033[1;32m")
  os.system("pkg install php -y")
  print("\033[1;32m")
  os.system("pkg install cmatrix -y")
  print("\033[1;32m")
  os.system("pkg install sl -y")
  print("\033[1;32m")
  os.system("pkg install ruby -y")
  print("\033[1;32m")
  os.system("gem install lolcat -y")
  print("\033[1;32m")
  os.system("pkg install zip -y")
  print("\033[1;32m")
  os.system("pkg install unzip -y")
  print("\033[1;32m")
  os.system("pkg install openssh -y")
  print("\033[1;32m")
  os.system("pkg install clang -y")
  print("\033[1;32m")
  os.system("pkg install crunch -y")
  print("\033[1;32m")
  os.system("pkg install proot-distro -y")
  print("\033[1;32m")
  os.system("pkg install ncurses-utils -y")
  print("\033[1;32m")
  os.system("python -m pip install --upgrade pip")
  print("\033[1;32m")
  os.system("python2 -m pip install --upgrade pip")
  print("\033[1;32m")
  os.system("pip install requests")
  print("\033[1;32m")
  os.system("pip2 install requests")
  print("\033[1;32m")
  os.system("pip install rich")
  print("\033[1;32m")
  os.system("pip2 install rich")
  print("\033[1;32m")
  os.system("pip install bs4")
  print("\033[1;32m")
  os.system("pip2 install bs4")
  print("\033[1;32m")
  os.system("pip install mechanize")
  print("\033[1;32m")
  os.system("pip2 install mechanize")
  print("\n\n\033[1;36m[â] ALL PACKAGE INSTALLED SUCCESSFULLY [â] \n")
def key():
  cl()
  print(log)
  ab=open("/data/data/com.termux/files/home/.termux/termux.properties","w")
  ab.write("#github.com/STLP-TEAM\n#FACEBOOK: Spamming & Termux Learning Point\nextra-keys = [ \\n    ['ESC', 'ALT', 'CTRL','exit', {key: KEYBOARD, popup: DRAWER},'clear', 'HOME', 'UP', 'END'], \\n    ['TAB', '{}', '()', '[]', '$','/', 'LEFT', 'DOWN', 'RIGHT'] \\n]\n\nterminal-cursor-blink-rate=600\n")
  ab.close()
  os.system("termux-reload-settings")
  print("\033[1;36mPROCESS COMPLETED\nRESTART YOUR TERMUX\033[1;37m\n")
def font():
  cl()
  print(log)
  try:
    check=open("STLP.ttf","r")
    check.close()
  except:
    print("\033[1;31mFONT FILE NOT FOUND!\nPLEASE INSTALL THE LATEST\nVERSION OF THIS TOOLS..!")
    os.system("xdg-open https://facebook.com/groups/spamming.termux.learning.point/")
    sys.exit()
  os.system("cp STLP.ttf /data/data/com.termux/files/home/.termux/font.ttf")
  os.system("termux-reload-settings")
  print("\033[1;36mPROCESS COMPLETED\nRESTART YOUR TERMUX\033[1;37m\n")
def color():
  cl()
  print(log)
  cl1="#github.com/STLP-TEAM\n#FACEBOOK: Spamming & Termux Learning Point\nbackground=#0e1019\nforeground=#fffaf4\ncursor=#808080\n\ncolor0=#232323\ncolor1=#ff000f\ncolor2=#8ce10b\ncolor3=#ffb900\ncolor4=#008df8\ncolor5=#6d43a6\ncolor6=#00d8eb\ncolor7=#ffffff\ncolor8=#444444\ncolor9=#ff2740\ncolor10=#abe15b\ncolor11=#ffd242\ncolor12=#0092ff\ncolor13=#9a5feb\ncolor14=#67fff0\ncolor15=#ffffff\n"
  cl3="#github.com/STLP-TEAM\n#FACEBOOK: Spamming & Termux Learning Point\ncolor0=#2f343f\ncolor1=#fd6b85\ncolor2=#63e0be\ncolor3=#fed270\ncolor4=#67d4f2\ncolor5=#ff8167\ncolor6=#63e0be\ncolor7=#eeeeee\ncolor8=#4f4f5b\ncolor9=#fd6b85\ncolor10=#63e0be\ncolor11=#fed270\ncolor12=#67d4f2\ncolor13=#ff8167\ncolor14=#63e0be\ncolor15=#eeeeee\nbackground=#2a2c3a\n#background=#090d13\nforeground=#eeeeee\ncursor=#808080\n"
  cl2="#github.com/STLP-TEAM\n#FACEBOOK: SPAMMING & TERMUX LEARNING POINT\n\nbackground=#171717\nforeground=#F8F8F8\n# black\ncolor0=#171717\ncolor8=#38252C\n# red\ncolor1=#D81765\ncolor9=#FF0000\n# green\ncolor2=#97D01A\ncolor10=#76B639\n# yellow\ncolor3=#FFA800\ncolor11=#E1A126\n# blue\ncolor4=#16B1FB\ncolor12=#289CD5\n# magenta\ncolor5=#FF2491\ncolor13=#FF2491\n# cyan\ncolor6=#0FDCB6\ncolor14=#0A9B81\n# white\ncolor7=#EBEBEB\ncolor15=#F8F8F8\n"
  print("""\n\033[1;36m    CHOOSE COLOUR\n\033[1;37m
  [01] DARK-1
  [02] DARK-2
  [03] GRAY-BRIGHT [default]
  """)
  ab=input(" \033[1;37m [â¢] SELECT : \033[1;32m")
  if ab in ["1","01"]:
    file=open("/data/data/com.termux/files/home/.termux/colors.properties","w")
    file.write(cl1)
    file.close()
  elif ab in ["2","02"]:
    file=open("/data/data/com.termux/files/home/.termux/colors.properties","w")
    file.write(cl2)
    file.close()
  elif ab in ["3","03"]:
    file=open("/data/data/com.termux/files/home/.termux/colors.properties","w")
    file.write(cl3)
    file.close()
  else:
    file=open("/data/data/com.termux/files/home/.termux/colors.properties","w")
    file.write(cl3)
    file.close()
  os.system("termux-reload-settings")
  print("\033[1;36m  PROCESS COMPLETED\n  RESTART YOUR TERMUX\033[1;37m\n")
def custom_font():
  cl()
  print(log)
  font=input("\n\033[1;37m[â¢] FONT PATH : \033[1;32m")
  try:
    check=open(font,"r")
    check.close()
  except:
    print(f"\033[1;31mFONT [{font}] NOT FOUND !")
    time.sleep(0.5)
    print("\033[1;31mTRY AGAIN..!")
    time.sleep(0.5)
    sys.exit()
  com=f"cp {font} /data/data/com.termux/files/home/.termux/font.ttf"
  os.system(com)
  os.system("termux-reload-settings")
  print("\033[1;36mPROCESS COMPLETED\nRESTART YOUR TERMUX\033[1;37m\n")
def del_color():
  cl()
  print(log)
  no="#github.com/STLP-TEAM\n#FACEBOOK: Spamming & Termux Learning Point"
  file=open("/data/data/com.termux/files/home/.termux/colors.properties","w")
  file.write(no)
  file.close()
  os.system("termux-reload-settings")
  print("\033[1;36mPROCESS COMPLETED\nRESTART YOUR TERMUX\033[1;37m\n")
def del_font():
  cl()
  print(log)
  os.system("touch /data/data/com.termux/files/home/.termux/font.ttf")
  os.system("rm /data/data/com.termux/files/home/.termux/font.ttf")
  os.system("termux-reload-settings")
  print("\033[1;36mPROCESS COMPLETED\nRESTART YOUR TERMUX\033[1;37m\n")
def del_key():
  cl()
  print(log)
  no="#github.com/STLP-TEAM\n#FACEBOOK: Spamming & Termux Learning Point"
  file=open("/data/data/com.termux/files/home/.termux/termux.properties","w")
  file.write(no)
  file.close()
  os.system("termux-reload-settings")
  print("\033[1;36mPROCESS COMPLETED\nRESTART YOUR TERMUX\033[1;37m\n")
def cl():
  os.system("clear")
if STLP=="RUN":
  logo()
