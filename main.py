from const import *
from keybords import *
import telebot
from telebot import types
import requests
import json


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hi, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, reply_markup=markup_r)
    bot.register_next_step_handler(message, get_city)


@bot.message_handler(content_types=['text'])
def menu(message):

    get_message_bot = message.text.strip().lower()
    if get_message_bot == "узнать погоду":
        get_city(message)
    else:
        get_weather(chat_id=message.chat.id, location=message.text)


def get_city(message):
    mess = 'Choose a city'
    bot.send_message(message.chat.id, mess, reply_markup=markup_i)


def get_other_name(message):
    get_weather(chat_id=message.chat.id, location=message.text)


def get_weather(chat_id='', location=''):
    url = WEATHER_URL.format(city=location, token=WEATHER_TOKEN)
    response = requests.get(url)
    if response.status_code != 200:
        mess = f'{location} not found'
        bot.send_message(chat_id, mess)
        repeat(chat_id)
        # bot.register_next_step_handler(message, get_city)
        return False
    data = json.loads(response.content)
    print(data)
    bot.send_message(chat_id, parse_weather_data(data))
    repeat(chat_id)
    return True


def parse_weather_data(data):
    weather_state = data['weather'][0]['description']
    # print(weather_state)
    icon = get_icon(weather_state)
    temp = round(data['main']['temp'] - 273.15, 1)
    feels_like = round(data['main']['feels_like'] - 273.15, 1)
    humidity = data['main']['humidity']
    city = data['name']
    msg = f'The weather in {city}:\nTemp is {temp}\u00b0С, feels like {feels_like}\u00b0С, humidity is {humidity}% ' \
          f'{weather_state} {icon}'
    return msg


def get_icon(status):
    match status:
        case 'clear sky': return '☀'
        case 'overcast clouds': return '🌥'
        case 'broken clouds': return '☁'
        case 'moderate rain': return '🌦'
        case 'mist': return '🌫'
        case 'snow': return '🌨'
        case 'scattered clouds': return '☁️'
        case 'light snow': return '❄️'
        case 'fog': return '🌫'
        case 'drizzle': return '🌧'
        case 'thunderstorm': return '⛈'
        case 'few clouds': return '🌤'
        case 'rain': return '🌧'
        case 'shower rain': return '🌧'
        case _: return ''


def repeat(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Yes', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='No', callback_data='no')
    keyboard.add(key_no)
    msg = 'Another city?'
    bot.send_message(chat_id, text=msg, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.message.text == 'Choose a city')
def handle(call):
    if str(call.data) != 'Other':
        get_weather(chat_id=call.message.chat.id, location=str(call.data))
    else:
        mess = 'Enter city name'
        message = bot.send_message(call.message.chat.id, mess)
        bot.register_next_step_handler(message, get_other_name)
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.message.text == 'Another city?')
def handle(call):
    if str(call.data) == 'yes':
        get_city(call.message)
    elif str(call.data) == 'no':
        bot.send_message(call.message.chat.id, 'Come back later')
    bot.answer_callback_query(call.id)


bot.polling(non_stop=True)
