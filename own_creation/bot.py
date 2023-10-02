"""__script_writer__ = "Ahmed" 
__copyright__ = "Copyright (C) 2004" 
__license__ = "Free for all" 
__version__ = "1.0"
"""
"""Importing Some Modules"""
try:
	import requests,json,sys,rich
except:
	os.system('pip install requests && pip install rich');os.system('clear')
	import requests
from rich.panel import Panel as panel	
from rich import print as prints

print(' '*5+'[Bot Tool]'+'\nType "exit" to stop the program\n')

def bot(user_text):
	"""Get bot reply using simsimi bot api"""
	bot_reply_scrap = requests.get(f'https://api.simsimi.net/v2/?text={user_text}&lc=en&bn=false').json()
	bot_reply = bot_reply_scrap["success"]
	return bot_reply
	
while True:
	"""User input section"""
	user_text = input('Message : ')
	if 'exit' not in user_text:
		prints(panel('Bot reply : '+bot(user_text),style='green',title='Reply'))
	else:
		sys.exit('Bye.......')
	
