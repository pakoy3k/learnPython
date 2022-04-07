import telepot
import sys
import time
import os
from pprint import pprint
reload(sys)
sys.setdefaultencoding('utf-8')
bot = telepot.Bot('01234567:PAK_00112358132133') # token


def handle(msg):
    pprint(msg)


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pprint(msg['text'])
    cmd = msg['text']
    print cmd
    if cmd == "/start":
        bot.sendMessage(chat_id, "Server cmd TelegramBot")
    if cmd == "/ls":
        f = os.popen('ls')
        cmd = f.read()
        bot.sendMessage(chat_id, cmd)


bot.message_loop({'chat': on_chat_message})

print('Listening ...')

while 1:
    time.sleep(10)
