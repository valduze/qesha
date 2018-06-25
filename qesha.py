import logging
import random
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

updater = Updater(token='__PUT_YOUR_TOKEN_HERE__')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.DEBUG)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm Jongi, well in a computer version, something like a robot, please talk to me!, I only speak the folowing commands for now: /cv, /qualifications, /matric, /iddoc and /playmusic")

def echo(bot, update):
    #bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    texting =  update.message.text
    errormessage = "I don't understand you now: " + texting + "??? Did you forget to type / (foward slash)??? Hmmm"
    bot.send_message(chat_id=update.message.chat_id, text=errormessage)
    bot.send_photo(chat_id=update.message.chat_id, photo='http://www.jongi.za.net/wp-content/uploads/2015/04/jongi-214x300.jpg')

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command. I only speek /cv, /qualifications, /matric, /iddoc and /playmusic")

def cv(bot, update):
    message = "Please be patient while I am sending you my CV"
    bot.send_message(chat_id=update.message.chat_id, text=message)
    bot.send_document(chat_id=update.message.chat_id, document=open('/home/jongi/python-telegram-bot/docs/JongiCV.pdf', 'rb'))

def qualifications(bot, update):
    message = "Please be patient while I am sending you my qualifications"
    bot.send_message(chat_id=update.message.chat_id, text=message)
    bot.send_document(chat_id=update.message.chat_id, document=open('/home/jongi/python-telegram-bot/docs/Jguma.pdf', 'rb'))

def matric(bot, update):
    message = "I matriculated in 1996 at Ikamvalethu Finishing School, Langa, Cape Town, Western Cape, South Africa"
    bot.send_message(chat_id=update.message.chat_id, text=message)

def iddoc(bot, update):
    message = "Please call me, I do not give my ID to strangers"
    bot.send_message(chat_id=update.message.chat_id, text=message)


def playmusic(bot, update):
    music = ["Bob Marley - No Woman No Cry.mp3",
"Bob Marley - One Love.mp3",
"Bob Marley - Redemption Song.mp3",
"Boney M -  Ma Baker.mp3",
"Freshly Ground - Doo Be Doo.mp3",
"Freshly Ground  - Id Like.mp3",
"Juluka - Impi.mp3"]
    rtext = random.choice(music)
    playing = "Please be patient I am going to play: " + rtext + " for you my friend"
    bot.send_message(chat_id=update.message.chat_id, text=playing)
    #bot.send_audio(chat_id=update.message.chat_id, audio='http://jongi.za.net/old_school/'+rtext)
    bot.send_audio(chat_id=update.message.chat_id, audio=open('/home/jongi/python-telegram-bot/old_school/'+rtext, 'rb'))

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
playmusic_handler = CommandHandler('playmusic', playmusic)
dispatcher.add_handler(playmusic_handler)
id_handler = CommandHandler('iddoc', iddoc)
dispatcher.add_handler(id_handler)
matric_handler = CommandHandler('matric', matric)
dispatcher.add_handler(matric_handler)
qualifications_handler = CommandHandler('qualifications', qualifications)
dispatcher.add_handler(qualifications_handler)
cv_handler = CommandHandler('cv', cv)
dispatcher.add_handler(cv_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
updater.start_polling()
