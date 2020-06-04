# Verb game chat bots
This project creates bots for Telegram and VK for fictional publisher house "Verb Game". These bots answer popular questions from authors, who want or already work with publisher house.
### Prepare your work environment
You need Python3 interpreter to use this script. You can check what version or python interpreter typing in your terminal
```
python --version
```
If you see `python2.X` version, check if you have python3 version, typing in your terminal
```
python3 --version
```
If you don't have python3 install it. All necessary information about how to install it on your operating system you can find on [python official page](https://www.python.org)
Also, you need pip packet manager to install python libraries. You can find information about pip and how to install it in [pip documentation](https://pip.pypa.io/en/stable/installing/). 

To prepare work environment open terminal, clone `devman_verb_game_bot` repository and go to the repository directory typing:
```
git clone https://github.com/lev-stas/devman_verb_game_bot
cd devman_verb_game_bot
```
It is good practice to use virtual environment for your project. It will save you from libraries versions conflicts. To make virtual environment you should install `virtualenv` library, if you don't have it:
```
pip3 install virtualenv
```
Then create and activate virtual environment typing in your terminal
```
python3 -m virtualenv .venv
source .venv/bin/activate
```
All needed dependencies are included in requirements.txt file. To install them, type in your terminal 
```
pip install -r requirements.txt
```
This script needs some environment variables for correct work. Create file `.env` in the same directory, where `telegram_bot.py`, `dialogflow_learning.py` and `vk_bot.py` scripts are located and specify `TELEGRAM_TOKEN`, `GOOGLE_APPLICATION_CREDENTIALS`, `VK_ACCOUNT_ACCESS_TOKEN` and `DIALOG_FLOW_PROJECT_ID` variables.
### Usage
##### DilaogFlow intent creation
To make your bot able to communicate with customers, first of all you should create and train DialogFlow intents, if you haven't done it yet. You can find how to create your DialogFlow project in [official documentation page] (https://cloud.google.com/dialogflow/docs/).

First of all, prepare your train dialog file. It should be in `.txt` format and should match a certain syntax. There is an example of training phrases:
```
{
    "The topic_1 of your dialog": {
        "questions": [
            "Customer phrase",
            "Customer phrase "
        ],
        "answer": "Your bots answer"
    },
    "The topic_2 of your dialog": {
        "questions": [
            "Customer phrase",
            "Customer phrase "
        ],
        "answer": "Your bots answer"
    }
}
```
You can add as many dialog topics in one file as you need.

To create and train DilofFlow intent run `dialogflow_learning.py` script with path to the training phreases file. Type in your terminal
```
python dialogflow_learning.py phrases.txt
```
##### Telegram bot
To run telegram bot, type in your terminal
```
python telegram_bot.py &
```
When you run `telegram_bot.py`, it will work until your server power off or until you'll kill a process.
The bot will answer every question or phrase from the customer according to dialogflow intent. If the bot gets unknown question, it will propose to rephrase a question.

This script allows to use telegram bot even in case telegram is blocked in your country. If you have credentials from socks5 server, run `telegram_bot.py` and give to it socks5 server url with port number, your login and password on this socks5 server as arguments:
```
python telegram_bot.py -u XXX.XXX.XXX.XXX:1080 -l login -p password &
```
##### VK bot
To run your vk bot, type in your terminal
```python vk_bot.py &
```
When you run `vk_bot.py`, it will work until your server power off or until you'll kill a process.
The bot will answer the same way as telegram bot, described above.

#### Purpose of project
This script was performed as a part of chat bots course by [Devman](https://dvmn.org/modules) 