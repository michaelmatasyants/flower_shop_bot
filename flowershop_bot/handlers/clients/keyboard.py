from telegram import (ReplyKeyboardMarkup, KeyboardButton,
                      InlineKeyboardButton, InlineKeyboardMarkup)

from flowershop_bot.handlers.clients.texts import start_button_text


def build_menu(buttons, n_cols,
               header_buttons=None,
               footer_buttons=None):
    print('build_menu')
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


def make_keyboard_for_start_command() -> ReplyKeyboardMarkup:
    print('make_keyboard_for_start_command')
    buttons = [KeyboardButton(button) for button in start_button_text]

    reply_markup = ReplyKeyboardMarkup(
        build_menu(buttons, n_cols=3),
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return reply_markup
