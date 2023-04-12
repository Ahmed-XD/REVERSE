"""__script_writer__ = "Ahmed" 
__copyright__ = "Copyright (C) 2004"
__tool_type__ = "Useragent Dumping"
__license__ = "Free for all" 
__version__ = "1.0"
"""
import os
try:
    import fake_useragent
except:
    os.system('pip install fake_useragent')
def ua():
    user_agent = fake_useragent.UserAgent()
    random_user_agent = user_agent.random
    return random_user_agent
def main():
    usr_input = int(input('How many useragents you want to genarate : '))
    usr_input2 = input('You want to see useragents on screen? y/n : ')
    for x in range(usr_input):
        agent = str(ua())
        if 'y' in usr_input2:
            print(agent)
        else:pass
        open('useragents.txt','a').write(agent+'\n')
    print('useragents saved in useragents.txt')
main()
