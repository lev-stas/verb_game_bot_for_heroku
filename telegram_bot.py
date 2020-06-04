from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import os
import dialogflow_v2 as dialogflow
import logging



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
    
    tg_token = os.environ['TELEGRAM_TOKEN']
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    google_application_credentials = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
    dialogflow_project_id = os.environ['DIALOG_FLOW_PROJECT_ID']

    tg_bot = telegram.Bot(token=tg_token)
    
    class MyLogsHandler(logging.Handler):
        def emit(self, record):
            log_entry = self.format(record)
            tg_bot.send_message(chat_id=telegram_chat_id, text=log_entry)

    t_logger = logging.getLogger('ChatBot_logger')
    t_logger.addHandler(MyLogsHandler())

    main(tg_token)
