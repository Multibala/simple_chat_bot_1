import random
import utils
from utils import *
import numpy as np
import pandas as pd
import warnings 
from config import SAMPLE_RESPONSES_LINK, API_KEY
warnings.filterwarnings('ignore')

import nltk



nltk.download('punkt',quiet=True)
sentence_list = []

df = pd.read_excel(SAMPLE_RESPONSES_LINK)

bot_responses = np.array(df['bot_response']).flatten()


user_inputs = df['user_input']
sentence_list = []
for sentence in user_inputs:
  sentence_list.append(sentence)




exit_words = ['quit','bye','good bye','see you soon','exit']




# from telegram.ext import *

def start_command(update,context):
  update.message.reply_text('Type hello to get start!')
def handle_message(update,context):
  text = str(update.message.text).lower()
  response = bot_response(text,sentence_list,bot_responses)
  update.message.reply_text(response)

def main():
  updater = Updater(API_KEY,use_context=True)
  dp = updater.dispatcher

  dp.add_handler(CommandHandler('start',start_command))
  dp.add_handler(MessageHandler(Filters.text,handle_message))

  updater.start_polling(timeout=600)
  updater.idle()

# main()


while True:
  user_input = input()
  if user_input in exit_words:
    print(random.choice(exit_words[:-1]))
    break
  print(bot_response(user_input,sentence_list,bot_responses))

