import logging

import os

from telegram import Update

from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define command handler

def rename_files(update: Update, context: CallbackContext):

    chat_id = update.effective_chat.id

    message_text = update.message.text

    # Assuming the message is in the format: "/rename old_name new_name"

    command, old_name, new_name = message_text.split()

    try:

        os.rename(old_name, new_name)

        context.bot.send_message(chat_id=chat_id, text="File renamed successfully!")

    except FileNotFoundError:

        context.bot.send_message(chat_id=chat_id, text="File not found.")

    except:

        context.bot.send_message(chat_id=chat_id, text="An error occurred while renaming the file.")

# Set up the bot

def main():

    # Set up the Telegram Bot API token

    bot_token = "6227649599:AAG1b9IY7QOvT-Mo8KlPg8fSm6fz7a99j3U"

    # Create an instance of the Updater class with your bot token

    updater = Updater(token=bot_token, use_context=True)

    # Get the dispatcher to register handlers

    dispatcher = updater.dispatcher

    # Register the rename command handler

    dispatcher.add_handler(CommandHandler('rename', rename_files))

    # Start the bot

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':

    main()

