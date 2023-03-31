"""
__script_writer__ = "Ahmed" 
__copyright__ = "Copyright (C) 2004" 
__license__ = "Free for all" 
__version__ = "1.0"
"""
import os,sys
option = []
try:
	import googletrans
except:
	os.system('pip3 install googletrans==3.1.0a0');os.system('clear')
	
	
	
def string_to_binary(n):
	"""Convert string into binary"""
	converter = ''.join(format(ord(i), '08b') for i in n)
	print("Binary : " + str(converter))
	
	
def binary_to_string(n):
	"""Convert binary to string"""
	converter = "".join([chr(int(binary, 2)) for binary in n.split(" ")])
	print("String : "+converter)
	
	
	
def translation(n):
	"""Translate any language"""
	from googletrans import Translator, constants
	from pprint import pprint
	translator = Translator()
	translation = translator.translate(n)
	print(f'Translated Text : {translation.text}')
	
	
	
def get_text():
	input_text = input('Paste the text/string/binary code : ')
	if '1' in option:
		string_to_binary(input_text)
	if '2' in option:
		try:
			binary_to_string(input_text)
		except:
			sys.exit('Binary must be integer')
	if '3' in option:
		translation(input_text)
		
	
input_user = input('\n\n    [HelloWorld]\n\n [1]String to binary\n [2]Binary to string\n [3]Convert any language to English\n\n Choose : ')
option.append(input_user)
if '1' or '2' or '3' in input_user:
	get_text()
else:
	sys.exit('choose the right one')
