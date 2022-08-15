#!/usr/bin/python3
import speech_recognition as sr 
import os
import subprocess
import threading
import time
import mycommands
import argparse

def EchoIt(txt):
    if debug == 1:
      print(txt)
 
def ExecuteCommand(cmd):
    os.system(cmd)

def Speak(text):
    os.system('espeak "'+text+'"')

def CleanTxt(text):
    txt='+'.join(text)
    return txt

def FilterCommand(commands,cmd):
    cmd=cmd.lower().split(' ')
    base_cmd=cmd[0]
    sub_cmd=''
    if len(cmd) > 1:
      sub_cmd=cmd[1]

    txt=CleanTxt(cmd)


    finalcmd=commands['default_browser_search']+txt

    if base_cmd in commands:
        txt=''
        if sub_cmd in commands[base_cmd]:
            if len(cmd) > 2:
              txt=CleanTxt(cmd[2:])
            finalcmd=commands[base_cmd][sub_cmd]
        elif 'default' in commands[base_cmd]:
            if len(cmd) > 1:
              txt=CleanTxt(cmd[1:])
            finalcmd=commands[base_cmd]['default']

        if txt != '':
          finalcmd=finalcmd+txt+"'"

    EchoIt(finalcmd)
    ExecuteCommand(finalcmd)

commands=mycommands.yamlObj()
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug",action='store_true', required=False, help='to help debug and print')
parser.add_argument("-c", "--commandslist", action='store_true', required=False, help='to list the commands')

args=parser.parse_args()
debug=args.debug

if args.commandslist:
  for cmd in commands:
      for subcmd in commands[cmd]:
        if len(subcmd) == 1: continue
        print(cmd +" "+subcmd)
  exit()

mic_name = 'MacBook Pro Microphone'
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer() 

mic_list = sr.Microphone.list_microphone_names() 
EchoIt(mic_list)
device_id=0
while 1:
    with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source: 
	    r.adjust_for_ambient_noise(source,duration=0.5) 
	    EchoIt(".")
	    audio = r.listen(source) 
	    text=''
	    try: 
		    text = r.recognize_google(audio) 
		    EchoIt(text)
		    if text == 'rocket':
		       Speak('Yes, sir')
		       src = r.listen(source)
		       text = r.recognize_google(src) 
		       EchoIt(text)
		       if text != '':
		         Speak('Launching your command')		  
		    else:
		       continue

		    if text == 'goodbye':
		       Speak('Talk to you later. Bye!')
		       exit()
		       quit()
		    else:
		       threading.Thread(target=FilterCommand,args=(commands,text,)).start()
	    
	    except sr.UnknownValueError: 
		    pass                    
	    
	    except sr.RequestError as e: 
		    pass
