import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
import os
import random
import dialogflow_v2 as dialogflow
import logging
from logging.handlers import RotatingFileHandler

def detect_intent_text(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    if not response.query_result.intent.is_fallback:
        return response.query_result.fulfillment_text

def send_message(event, vk_api, project_id):
    question = event.text
    user_id = event.user_id
    answer = detect_intent_text(project_id, user_id, question, 'ru')
    if answer:
        vk_api.messages.send(
            user_id=user_id,
            message=answer,
            random_id=random.randint(1,1000)
        )

if __name__ == '__main__':
    load_dotenv()
    vk_token = os.getenv('VK_ACCOUNT_ACCESS_TOKEN')
    google_application_credentials = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    dialogflow_project_id = os.getenv('DIALOG_FLOW_PROJECT_ID')

    logs_dir = 'logs'
    os.makedirs(logs_dir, exist_ok=True)
    logs_path = os.path.join(logs_dir, 'vk_bot.log')

    vk_logger = logging.getLogger('vk_logger')
    logs_handler = RotatingFileHandler(logs_path, maxBytes=1024, backupCount=5)
    vk_logger.addHandler(logs_handler)

    vk_session = vk_api.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            send_message(event, vk_api, dialogflow_project_id)