# End-to-end Telegram bot development and deployment

## Download Telegram Desktop
Navigate to https://desktop.telegram.org/ to download Telegram Desktop.

## BotFather
### Create a new bot with BotFather
Search for `@BotFather` Telegram bot and click `START` button:
![botfather_newbot_0001.png](img/botfather_newbot_0001.png "BotFather. Start")

Send `/newbot` command:
![botfather_newbot_0002.png](img/botfather_newbot_0002.png "BotFather. '/newbot' command")

Send bot name (e.g., `PyConPLBot`):
![botfather_newbot_0003.png](img/botfather_newbot_0003.png "BotFather. Name")

Send bot username (e.g., `PyConPLBot`). It must end with `bot`:
![botfather_newbot_0004.png](img/botfather_newbot_0004.png "BotFather. Username")

Copy and save the token (e.g., `5741693832:AAFyfYpqWRHaGVhTt9CO4edV7bTlNR7bvaA`):
![botfather_newbot_0005.png](img/botfather_newbot_0005.png "BotFather. Token")

### Turn on inline mode
Navigate to `@BotFather` Telegram bot and send `/mybots` command:
![botfather_edit_bot_0001.png](img/botfather_edit_bot_0001.png "BotFather. '/mybots' command")

Choose a bot from the list (e.g., `@PyConPLBot`):
![botfather_edit_bot_0002.png](img/botfather_edit_bot_0002.png "BotFather. Choose a bot")

Click `Bot Settings` button:
![botfather_edit_bot_0003.png](img/botfather_edit_bot_0003.png "BotFather. Bot Settings")

Click `Inline Mode` button:
![botfather_edit_bot_0004.png](img/botfather_edit_bot_0004.png "BotFather. Inline Mode")

Click `Turn on` button:
![botfather_edit_bot_0005.png](img/botfather_edit_bot_0005.png "BotFather. Turn on")

### Add inline placeholder
Click `Edit inline placeholder` button:
![botfather_edit_bot_0006.png](img/botfather_edit_bot_0006.png "BotFather. Edit inline placeholder")

Send placeholder:
![botfather_edit_bot_0007.png](img/botfather_edit_bot_0007.png "BotFather. Send placeholder")

Success! Inline setting updated:
![botfather_edit_bot_0008.png](img/botfather_edit_bot_0008.png "BotFather. Success")

## Host Telegram bot locally
### Hello world bot with pyTelegramBotAPI
Lets start with "Hello, World!" with pyTelegramBotAPI.
```sh
$ git clone https://github.com/korniichuk/telegram-pycon-pl-2022.git
$ cd telegram-pycon-pl-2022
```

Install requirements:
```sh
$ pip install -r requirements.txt
```

Create .env file with token:
```sh
$ touch .env
```

Copy and past token to .env file:
```sh
$ echo TOKEN=<TOKEN> > .env

```

Example:
```sh
$ echo TOKEN=5741693832:AAFyfYpqWRHaGVhTt9CO4edV7bTlNR7bvaA > .env
```

Start "Hello, World!" bot:
```sh
$ python3 bot1.py
```

### Synchronous NBP bot with pyTelegramBotAPI
```sh
$ python3 bot2.py
```

### Asynchronous NBP bot with pyTelegramBotAPI
```sh
$ python3 bot3.py
```

### Asynchronous NBP bot with python-telegram-bot
```sh
$ python3 bot4.py
```

### Asynchronous NBP bot with aiogram
```sh
$ python3 bot5.py
```

## Deploy on AWS with Elastic Beanstalk
Install AWS CLI:
```sh
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install

$ aws --version
```

**Source:** https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions

Install EB CLI:
```sh
$ pip install awsebcli

$ eb --version
```

**Source:** https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-advanced.html

## Deploy on AWS with SAM
```ssh
$ cd aws-elastic-beanstalk
$ eb init
```

To delete bot from AWS cloud, terminate the environment:
```ssh
$ eb terminate
```
