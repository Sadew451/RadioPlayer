# Telegram Radio Player V2

![GitHub](https://img.shields.io/github/license/Sadew451/FM)



- An Telegram Bot to Play Radio/Music in Channel or Group Voice Chats.

This is also the source code of the bot which is being used for playing
Radio in [SDBOTs Inifinity](https://t.me/SDBOTs_inifinity) Channel & Music in [SDBOTs](https://t.me/SDBOTz) Group.

## Special Features

- Playlist, queue, 24x7 radio stream
- Loop one track when there is only one track in the playlist
- Automatically downloads audio for the first two tracks in the playlist to ensure smooth playing
- Show current playing position of the audio
- Control with buttons and commands
- Download songs from youtube as audio

## Deploy to Heroku (The Easy Way)

<p><a href="https://heroku.com/deploy?template=https://github.com/sadew451/RadioPlayer"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200""/></a></p>
NOTE: Make Sure You Have Started A Voice Chat In Your Channel/Group Before Deploying!

## Heroku Vars:
1. `API_ID` : Get From my.telegram.org
2. `API_HASH` : Get From my.telegram.org
3. `BOT_TOKEN` : Get it From @Botfather
4. `SESSION_STRING` : Generate From [@SDStringSessonGenbot](http://t.me/SDStringSessonGenbot).
5. `CHAT` : ID of Channel/Group where the bot plays Music/Radio.
6. `LOG_GROUP` : Group to send Playlist, if CHAT is a Group.
7. `ADMINS` : ID of users who can use admin commands.
8. `STREAM_URL` : Stream URL of radio station to stream when the bot starts or with /radio command.

- Enable the worker after deploy the project to Heroku.
- Bot will starts radio automatically in given `CHAT` with given `STREAM_URL` after deploy. 
- 24x7 Music even if heroku restarts, radio stream restarts automatically.  
- To play a song just send the audio file to Bot or reply to an audio with `/play` to start playing it in the voice chat.
- To download audio you can use [@TheNatsukiBot](http://t.me/TheNatsukiBot) or `/song` command to the bot.
- Use `/help` to know about other commands & its usage.

## Requirements

- Python 3.6 or higher.
- A
  [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api)
  and a Telegram account.
- [FFmpeg Python](https://www.ffmpeg.org/)
- Telegram [String Session](http://t.me/genStr_robot) of the account.
- Userbot Needs To Be Admin In The Channel or Group.
- Must Start A Voice Chat In Channel/Group Before Running The Bot.

## Run On VPS (The Hard Way)

```sh
$ git clone https://github.com/AsmSafone/RadioPlayerV2
$ cd RadioPlayerV2
$ sudo apt-get install python3-pip ffmpeg
$ pip3 install -U pip
$ pip3 install -U -r requirements.txt
```
Edit **config.py** with your own values.

```sh
$ python3 main.py
```

## Credits

- [Asm Safone](https://github.com/AsmSafone) 
- [Dash Eclipse](https://github.com/dashezup) 
- [Il'ya](https://github.com/MarshalX) [For tgcalls]
- [Subin](https://github.com/subinps) [For bot support]
