import telepot
from googletrans import Translator
import time
import os
from dotenv import load_dotenv
TRANSLATOR_TOKEN = os.getenv('TRANSLATOR_TOKEN')
print(TRANSLATOR_TOKEN)

def on_chat_message(msg):
  content_type, _, chat_id = telepot.glance(msg)
  if content_type == 'text':
    command = msg.get('text')
    if '!' in command:
      if command == '!help':
        mess = '1. Ogni comando deve essere preceduto da ! \n'
        mess = mess + '2. A seguito del ! devi inserire il nome del comando, minuscolo e senza spazi \n'
        mess = mess + '3. Il comando !toit cat traduce la parola o frase da inglese a italiano\n'
        mess = mess + '4. Il comando !toen gatto traduce la parola o frase da italiano a inglese\n'
        bot.sendMessage(chat_id, mess)
      elif 'toit' in command:
        splitted = command.split('!toit')
        word = splitted[len(splitted)-1]
        translator = Translator()
        translation = translator.translate(word, dest = 'it')
        bot.sendMessage(chat_id, translation.text)
      elif 'toen' in command:
        splitted = command.split('!toen')
        word = splitted[len(splitted)-1]
        translator = Translator()
        translation = translator.translate(word, dest = 'en')
        bot.sendMessage(chat_id, translation.text)
      else:
        bot.sendMessage(chat_id, 'Comando non presente')
    else:
      bot.sendMessage(chat_id, 'Comando non valido, prova con !help')

bot = telepot.Bot(TRANSLATOR_TOKEN)
bot.message_loop(on_chat_message)

print('Listening ...')

while 1:
    time.sleep(10)

