import dialogflow_v2 as dialogflow
import os
import json
from dotenv import load_dotenv
import argparse
import logging



def learn_intent(filename, project_id):
    with open (filename, 'r') as file:
        file_content = file.read()
    expressions = json.loads(file_content)
    for topic, phrases in expressions.items():
        questions = phrases['questions']
        answer = [phrases['answer']]
        create_intent(project_id, topic, questions, answer)
    


def create_intent(project_id, display_name, training_phrases_parts,
                  message_texts):
    intents_client = dialogflow.IntentsClient()

    parent = intents_client.project_agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.types.Intent.Message.Text(text=message_texts)
    message = dialogflow.types.Intent.Message(text=text)

    intent = dialogflow.types.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message])

    intents_client.create_intent(parent, intent)


if __name__ == '__main__':
    load_dotenv()
    google_application_credentials = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    dialogflow_project_id = os.getenv('DIALOG_FLOW_PROJECT_ID')
    
    parser = argparse.ArgumentParser(description='diaogflow intent creation and fitting')
    parser.add_argument('training_file', help='path to the training phrases file')
    args = parser.parse_args()
    training_file = args.training_file


    logger = logging.getLogger('ChatBot_logger')
    
    learn_intent(training_file, dialogflow_project_id)
    



