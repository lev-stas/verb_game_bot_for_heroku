# Verb game chat bots
This project creates bots for Telegram and VK for fictional publisher house "Verb Game". These bots answer popular questions from authors, who want or already work with publisher house.

<img src='demo_gifs/demo_tg_bot.gif' title='demo_tg_bot'/>
<img src='demo_gifs/demo_vk_bot.gif' title='demo_vk_bot'/>

#### Demo
You may try to use this bots:
telegram bot - @stast_devman_talking_bot

vk bot - xkcd_commics_group

### Prepare your work environment
You need Python3 interpreter to use this project. You can check what version or python interpreter typing in your terminal
```
python --version
```
If you see `python2.X` version, check if you have python3 version, typing in your terminal
```
python3 --version
```
If you don't have python3 install it. All necessary information about how to install it on your operating system you can find on [python official page](https://www.python.org)
Also, you need pip packet manager to install python libraries. You can find information about pip and how to install it in [pip documentation](https://pip.pypa.io/en/stable/installing/). 

To prepare work environment open terminal, clone `verb_game_bot_for_heroku` repository and go to the repository directory typing:
```
git clone https://github.com/lev-stas/verb_game_bot_for_heroku.git
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
This script needs some environment variables for correct work. Create file `.env` and specify`GOOGLE_APPLICATION_CREDENTIALS` and `DIALOG_FLOW_PROJECT_ID` variables.
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
##### Chat bot deploy
We will use heroku to deploy our bots. First of all, you need an account on [heroku](https://www.heroku.com/). Create a new app and push the repository to this project. For more information, you may read in [official documentation](https://devcenter.heroku.com/). Before you start using your bots, you should scpecify cofig vars for your aplllication: `DIALOG_FLOW_PROJECT_ID`, `TELEGRAM_CHAT_ID`, `TELEGRAM_TOKEN`, `VK_ACCOUNT_ACCESS_TOKEN`, and set `GOOFLE_APPLICATION_CREDENTIALS` for your dialogflow project (you may read about how to do that on [stackoverflow](https://stackoverflow.com/questions/47446480/how-to-use-google-api-credentials-json-on-heroku) and on [github](https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack)). 

After all preparations are ready, run your bots.

#### Purpose of project
This script was performed as a part of chat bots course by [Devman](https://dvmn.org/modules) 