#!/usr/bin/python3 
import os
import datetime 
import requests
from telegram.ext import Updater  , CommandHandler

ban ='''

88 88""Yb .dP"Y8 888888 88b 88 8888b.  888888 88""Yb
88 88__dP `Ybo." 88__   88Yb88  8I  Yb 88__   88__dP
88 88"""  o.`Y8b 88""   88 Y88  8I  dY 88""   88"Yb 
88 88     8bodP' 888888 88  Y8 8888Y"  888888 88  Yb



telegram channel : @learninlevels
created by @ArianQaragozlou
'''
print (ban)
token = input("token : ")
psw = input("password : ")
print("proxy syntax is http://url:port")
proxy = input("http proxy (if you haven't , type 'c' ) : ")
if (proxy != "c") :
        proxy = { "proxy_url" : proxy }
        update = Updater(token, request_kwargs=proxy)
else :
    update = Updater(token)
def getip(bot , update , args ):
    
    if (args[0] == psw) :
        ip = requests.get("http://ifconfig.me")
        bot.sendMessage(update.message.chat.id , ip.text)
        os.system("echo %s >> log" % (str(datetime.datetime.now())+" : " +ip.text+" was sent to @"+update.message.chat.username ) )
    else :
        bot.sendMessage(update.message.chat.id , "permission denied !")
get_command = CommandHandler("getip" , getip , pass_args=True ) 
update.dispatcher.add_handler(get_command)
update.start_polling()
print("\n connectd")
os.system("echo %s >> log" % (str(datetime.datetime.now())+" : connected to telegram bot " ) )
