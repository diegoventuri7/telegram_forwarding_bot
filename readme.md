# Telegram Message Forwarding Bot

This project is a Telegram bot that automatically forwards messages from a source channel to a destination channel, with optional text substitutions.

## Setup

1. Clone the repository:

```
git clone https://github.com/diegoventuri7/telegram_forwarding_bot.git
cd telegram-bot
```

2. Install the required dependencies:

```
pip3 install python-telegram-bot
```

3. Create a new file named `config.ini` in the project directory and add your configuration settings:

```
[DEFAULT]
API_TOKEN = YOUR_API_TOKEN
SOURCE_CHANNEL_ID = SOURCE_CHANNEL_ID
DESTINATION_CHANNEL_ID = DESTINATION_CHANNEL_ID
SUBSTITUTIONS_FILE = dictonary.txt
```

Replace `YOUR_API_TOKEN` with your Telegram bot token, and `SOURCE_CHANNEL_ID` and `DESTINATION_CHANNEL_ID` with the respective channel IDs. The `SUBSTITUTIONS_FILE` specifies the name of the file containing text substitutions.

4. Create a new file named `dictonary.txt` in the project directory and add your text substitutions, one per line, separated by `>`:

```
value>amount
example>test
```

## Get Channel IDs

To get the channel IDs for your source and destination channels, use the `get_channel_id.py` script.

1. Make sure your bot is a member of the source and destination channels.

2. Start the script:

```
python3 get_channel_id.py
```

3. Send a message to each channel:

```
/get_chat_id
```

4. The bot will reply with the channel ID. Update the `config.ini` file with these IDs.

## Running the Bot

1. Ensure that your bot is a member of both the source and destination channels.

2. Start the bot:

```
python3 telegram_bot.py
```

The bot will now automatically forward messages from the source channel to the destination channel, applying any text substitutions specified in the `dictonary.txt` file.

If you need to stop the bot, press `Ctrl+C` in the terminal.