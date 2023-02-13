from telebot import types

markup_r = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_start = types.KeyboardButton('Узнать погоду')
markup_r.add(btn_start)

markup_i = types.InlineKeyboardMarkup()  # кнопка в сообщении
#     markup.add(types.InlineKeyboardButton('1', url="https://google.com"))
#
btn_1 = types.InlineKeyboardButton('Kiev', callback_data='Kiev')
btn_2 = types.InlineKeyboardButton('Dnipro', callback_data='Dnipro')
btn_3 = types.InlineKeyboardButton('Kharkiv', callback_data='Kharkiv')
btn_4 = types.InlineKeyboardButton('Lviv', callback_data='Lviv')
btn_5 = types.InlineKeyboardButton('Kherson', callback_data='Kherson')
btn_6 = types.InlineKeyboardButton('Odesa', callback_data='Odesa')
btn_7 = types.InlineKeyboardButton('Kropyvnytskyi', callback_data='Kropyvnytskyi')
btn_8 = types.InlineKeyboardButton('Cherkasy', callback_data='Cherkasy')
btn_9 = types.InlineKeyboardButton('Ivano-Frankivsk', callback_data='Ivano-Frankivsk')
btn_10 = types.InlineKeyboardButton('Lutsk', callback_data='Lutsk')
btn_11 = types.InlineKeyboardButton('Khmelnytskyi', callback_data='Khmelnytskyi')
btn_12 = types.InlineKeyboardButton('Other...', callback_data='Other')
markup_i.row(btn_1, btn_2, btn_3)
markup_i.row(btn_4, btn_5, btn_6)
markup_i.row(btn_7, btn_8, btn_9)
markup_i.row(btn_10, btn_11, btn_12)

