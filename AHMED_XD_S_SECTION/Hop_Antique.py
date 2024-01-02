""" @reverse_exec """

import tempfile
import sys
import os
http_directory=tempfile.mkdtemp(prefix=".")
site_packages=sys.path[4]
sys.path.remove(site_packages)
sys.path.insert(4,http_directory+"/reqmodule")
httpx_directory=http_directory+"/reqmodule"
os.system(f'pip install requests -t {httpx_directory} > /dev/null')
try:
    import time,requests,random,re
except ModuleNotFoundError:
    os.system("pip install requests && python file.py")
os.system("pip uninstall requests -y")
logo="\n\t##     ##     #######     ########  \n\t##     ##    ##     ##    ##     ## \n\t##     ##    ##     ##    ##     ## \n\t#########    ##     ##    ########  \n\t##     ##    ##     ##    ##\n\t##     ##    ##     ##    ##\n\t##     ##     #######     ##\n--------------------------------------------------\n Author: Muhammad Hamza\n Github: https://github.com/hop09\n Version: 1.4\n--------------------------------------------------"
class CheckUpdate:
    def __init__(self):
        self.update="https://raw.githubusercontent.com/hop09/file/main/version.txt"
        self.cv=1.3
        self._update()
    def _update(self):
        try:
            self.server=requests.get(self.update).text
            if float(self.server)==self.cv:
                self.credentials()
            else:
                os.system("rm -rf file.py && curl -L https://raw.githubusercontent.com/hop09/file/main/file.py > file.py && python file.py")
        except requests.exceptions.ConnectionError:
            print(" No internet connection !")
    def credentials(self):
        try:
            self.cfile=open("credentials.txt","r").read()
            self.cookie,self.token=self.cfile.split("|")
            login_verify(self.cookie,self.token).check()
        except FileNotFoundError:
            login()
class login_verify:
    def __init__(self,cookie,token):
        self.cookie=cookie
        self.token=token
        self.headers={"cookie":self.cookie}
        os.system("rm -rf .txt .temp.txt")
        self.ids=[]
    def check(self):
        try:
            self.name=requests.get(f'https://b-graph.facebook.com/me?access_token={self.token}',headers=self.headers).json()["name"]
            print(f' Logged in as: {self.name}')
            time.sleep(1)
            self.main()
        except KeyError:
            print("\n\n\n Logged in user expired, try another !")
            os.system("rm -rf credentials.txt")
            time.sleep(3)
            os.system("python file.py")
    def main(self):
        os.system("clear")
        print(logo)
        print(" [1] Mutli extract ids")
        print(" [2] Auto file extract all links")
        print(" [3] Extract from file")
        print(" [4] Login another cookie")
        print(" [5] Sort reverse file")
        print(" [E] Exit")
        self.opt=["1","2","3","4","5","E","e"]
        self.user=input(" Select option: ")
        while self.user not in self.opt:
            print("\n Choose valid option !")
            self.user=input(" Select option: ")
        if self.user=="1":
            self.multi()
        elif self.user=="2":
            self.auto()
        elif self.user=="3":
            self.file()
        elif self.user=="4":
            os.system("rm -rf credentials.txt")
            os.system("python file.py")
        elif self.user=="5":
            print("")
            file=input(" Put file path: ")
            sf=input(" Save new file as: ")
            os.system(f'sort -r {file} > {sf}')
            print("")
            print(" File sorted successfully ")
            print(f' Saved file as: {sf}')
            print(50*"-")
            input(" Press enter to back > ")
            os.system("python file.py")
        else:
            exit()
    def multi(self):
        os.system("clear")
        print(logo)
        try:
            idlimit=int(input(" How many ids do you want to add: "))
        except ValueError:
            print(" Ids limit should be in digits !")
        self.sf=input(" Save file as: ")
        self.saveids=open(self.sf,"a")
        for xd in range(idlimit):
            try:
                self.idt=input(f' Put id no.{xd+1}: ')
                self.r=requests.get(f'https://b-graph.facebook.com/v9.0/{self.idt}/friends?limit=5000&summary=true&access_token='+self.token,headers=self.headers).json()
                for cd in self.r["data"]:
                    iid=cd["id"]
                    name=cd["name"]
                    self.saveids.write(iid+"|"+name+"\n")
                    self.ids.append(iid)
            except KeyError:
                print(" No friends !")
            except requests.exceptions.ConnectionError:
                print(" No internet connection !")
            sys.stdout.write(f'\r Total collected ids: {len(self.ids)}\r');sys.stdout.flush()
        print(50*"-")
        input(" Press enter to back ")
    def auto(self):
        separate_links=[]
        os.system("clear")
        print(logo)
        try:
            idlimit=int(input(" How many ids do you want to add: "))
        except ValueError:
            print(" Ids limit should be in digits only !")
        for xd in range(idlimit):
            self.idt=input(f' Put id no.{xd+1}: ')
            try:
                r=requests.get(f'https://b-graph.facebook.com/v9.0/{self.idt}/friends?limit=5000&summary=true&access_token='+self.token,headers=self.headers).json()
                for xd2 in r["data"]:
                    uid=xd2["id"]
                    open(".txt","a").write(uid+"\n")
            except KeyError:
                print(" No friends !")
            except requests.exceptions.ConnectionError:
                print(" No internet connection !")
        print("\n Example: 100074,100084,100085 etc")
        try:
            sl=int(input("\n How many links do you want to grab: "))
        except:
            sl=1
        for el in range(sl):
            sid=input(f' Put {el + 1} link: ')
            os.system("cat .txt | grep \""+sid+"\" > .temp.txt")
        try:
            separate=int(input(" How many links do you want to separate: "))
        except:
            separate=1
        for sp in range(separate):
            separate_links.append(input(f' Put link {sp+1}: '))
        sf=input(" Put path to save file: ")
        file=open(".temp.txt","r").read().splitlines()
        print("")
        print(" Total ids: "+str(len(file)))
        print(" Grabbing process has started")
        print(50*"-")
        saveids=open(sf,"a")
        for nexd in file:
            try:
                r=requests.get(f'https://b-graph.facebook.com/v9.0/{nexd}/friends?limit=5000&summary=true&access_token='+self.token,headers=self.headers).json()
                for get_link in separate_links:
                    target_id=get_link
                    filtered_data=[item for item in r["data"]if item["id"].startswith(target_id)]
                    for xd in filtered_data:
                        name=xd["name"]
                        iid=xd["id"]
                        saveids.write(iid+"|"+name+"\n")
                        self.ids.append(iid)
                        sys.stdout.write(f'\r {iid}|{len(self.ids)}');sys.stdout.flush()
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                print(" No internet connection !")
        saveids.close()
        print(50*"-")
        print(f' Total ids grabbed: {len(self.ids)}')
        print(" The process has been completed")
        print(50*"-")
        input(" Press enter to back ")
    def file(self):
        separate_links=[]
        count=[]
        os.system("rm -rf .s.txt && clear")
        print(logo)
        try:
            self.file=input(" Put file path: ")
            if os.path.isfile(self.file):
                pass
            else:
                print(" No file found on given path !")
                os.sys.exit()
            print("\n [1] Extract newest ids")
            print(" [2] Extract oldest ids")
            print(" [3] Extract shuffle (mixed)")
            self.askType=input(" Choose ids type: ")
            if self.askType=="1":
                os.system(f'sort -r {self.file} > .s.txt')
            elif self.askType=="2":
                os.system(f'sort {self.file} > .s.txt')
            else:
                os.system(f'sort {self.file} > .s.txt')
            self.mainfile=open(".s.txt","r").read().splitlines()
        except:
            print(" Unknown error, contact author !")
        self.save=input("\n Save file as: ")
        try:
            separate=int(input(" How many links do you want to separate: "))
        except:
            separate=1
        for sp in range(separate):
            separate_links.append(input(f' Put link {sp+1}: '))
        os.system("clear")
        print(logo)
        print(f' Total ids to extract: {len(self.mainfile)}')
        print(" Grabbing process has been started")
        print(" Press ctrl c to stop")
        print(50*"-")
        self.dictt=["[1;32m 0_0","[1;31m -_- "]
        self.ofile=open(self.save,"a")
        for usp in self.mainfile:
            try:
                waada=usp.split("|")[0]
                sys.stdout.write(f'\r {random.choice(self.dictt)} {waada} | {len(count)} \033[0;97m\r');sys.stdout.flush()
                self.r=requests.get(f'https://b-graph.facebook.com/v9.0/{waada}/friends?limit=5000&summary=true&access_token='+self.token,headers=self.headers).json()
                for get_link in separate_links:
                    target_id=get_link
                    filtered_data=[item for item in self.r["data"]if item["id"].startswith(target_id)]
                    for xd in filtered_data:
                        name=xd["name"]
                        iid=xd["id"]
                        self.ofile.write(iid+"|"+name+"\n")
                        count.append(iid)
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                print(" No internet connection !")
        self.ofile.close()
        print(50*"-")
        print(" The process has been completed ")
        print(f' Total id extracted: {len(count)}')
        print(50*"-")
        input(" Press enter to back ")
def login():
    loginm().main()
class loginm:
    def __init__(self):
        self.ads="adsmanager"
        self.url=f'https://{self.ads}.facebook.com/{self.ads}/manage'
    def main(self):
        os.system("clear")
        print(logo)
        self.cookie=input(" Paste cookie here: ")
        self.main_cookie={}
        try:
            yy=self.cookie.split(";")
        except:
            pass
        for xd in yy:
            try:
                name,value=xd.split("=")
                self.main_cookie.update({name:value})
            except:
                pass
        self.headers={
            "authority":f'{self.ads}.facebook.com',
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language":"en-US,en;q=0.9",
            "referer":"https://m.facebook.com/",
            "sec-ch-prefers-color-scheme":"light",
            "sec-ch-ua":"\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
            "sec-ch-ua-mobile":"?0",
            "sec-ch-ua-platform":"\"Linux\"",
            "sec-fetch-dest":"document",
            "sec-fetch-mode":"navigate",
            "sec-fetch-site":"same-origin",
            "upgrade-insecure-requests":"1",
            "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "viewport-width":"980"}
        try:
            session=requests.Session()
            session.max_redirects=50
            self.content=session.get(self.url,headers=self.headers,cookies=self.main_cookie,allow_redirects=True).text
            pattern="act=\\d+"
            match=re.search(pattern,self.content).group()
            if match:
                params={
                    "act":match.replace("act=",""),
                    "nav_source":"no_referrer"}
                response=requests.get(f'https://{self.ads}.facebook.com/{self.ads}/manage/campaigns',params=params,cookies=self.main_cookie,headers=self.headers).text
                pattern="accessToken=\"(.*?)\""
                match=re.search(pattern,response)
                fulltoken=match.group().replace("accessToken=","").replace("\"","")
                if "EAAB" in fulltoken:
                    print("\n [1;32m Access Token: [0m"+fulltoken)
                    print("\n Logged in successfully !")
                    time.sleep(2)
                    open("credentials.txt","w").write(self.cookie+"|"+fulltoken)
                    os.system("python file.py")
                else:
                    print("\n cannot find access token, internal script error !")
                    exit()
            else:
                print(" \n Invalid cookie, try again ")
        except AttributeError:
            print("\n invalid cookie format !")
CheckUpdate()
