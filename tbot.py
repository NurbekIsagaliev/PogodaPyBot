from email import message
from pyexpat.errors import messages
import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
bot = telebot.TeleBot("5109872744:AAF_MghBrzFtijSi-evC-AIhAKG10l-KfYg", parse_mode=None)
@bot.message_handler(content_types=['text'])
def send_welcome(message):
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = OWM('f21be11cefb7feeeab4509aea53455a3', config_dict)
    owm.supported_languages
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    answer="В  " + message.text +"  сейчас  " + w.detailed_status+"\n"
    answer+="Температура сейчас в районе "+str(temp)+"\n\n"
    bot.send_message(message.chat.id,answer)
bot.polling(non_stop=True)