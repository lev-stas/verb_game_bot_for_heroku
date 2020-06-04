from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import os
import dialogflow_v2 as dialogflow
import logging
from logging.handlers import RotatingFileHandler
import argparse


def detect_intent_text(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text


def start (bot, update):
    update.message.reply_text('Добро пожаловать в чат "Игры глаголов"')

def reply_message (bot, update):
    users_text = update.message.text
    session_id = update.message.chat['id']
    reply = detect_intent_text(dialogflow_project_id, session_id, users_text, 'ru')
    update.message.reply_text(reply)    


def main(token, params=None):
    if params:
        updater = Updater(token, request_kwargs=params)
    else:
        updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, reply_message))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    logs_dir = 'logs'
    os.makedirs(logs_dir, exist_ok=True)
    logs_path = os.path.join(logs_dir, 'telegram_bot.log')

    telegram_logger = logging.getLogger('telegram_logger')
    logs_handler = RotatingFileHandler(logs_path, maxBytes=1024, backupCount=5)
    telegram_logger.addHandler(logs_handler)

    load_dotenv()
    tg_token = os.getenv('TELEGRAM_TOKEN')
    google_application_credentials = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    dialogflow_project_id = os.getenv('DIALOG_FLOW_PROJECT_ID')

    parser = argparse.ArgumentParser(description='Check project status on devman resource')
    parser.add_argument('-u', '--socks5_url', help='enter yor proxy server url')
    parser.add_argument('-l', '--socks5_login', help='enter your login on socks5 server')
    parser.add_argument('-p', '--socks5_passwd', help='enter your password on socks5 server')

    script_args = parser.parse_args()

    if script_args.socks5_url and script_args.socks5_login and script_args.socks5_passwd:
        proxy_params = {
            'proxy_url': f'socks5h://{script_args.socks5_url}', 
            'urllib3_proxy_kwargs': {
                'username': script_args.socks5_login,
                'password': script_args.socks5_passwd
            }
        }
        main(tg_token, params=proxy_params)
    else:
        main(tg_token)
