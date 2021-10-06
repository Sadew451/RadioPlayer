from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "👋🏻 **Hi [{}](tg://user?id={})**,\n\nI'm **Radio Player Bot** \nI Can Play Radio/Stream Music In Channels & Groups 24x7 Nonstop. Made with ❤️ By @Darkridersslk!"
HELP = """🏷️ **Need Help?** 🤔
__(Join @SDBOTz For Support)__

🏷️ **Common Commands**:
\u2022 `/play` reply to an audio to play or queue it
\u2022 `/help` shows help for commands
\u2022 `/playlist` shows the playlist
\u2022 `/current` shows playing time of current track
\u2022 `/song` [song name] download the song as audio

🏷️ **Admin Commands**:
\u2022 `/skip` [n] skip current or n where n >= 2
\u2022 `/join` join voice chat of current group
\u2022 `/leave` leave current voice chat
\u2022 `/vc` check which VC is joined
\u2022 `/stop` stop playing music
\u2022 `/radio` start radio stream
\u2022 `/stopradio` stop radio stream
\u2022 `/replay` play from the beginning
\u2022 `/clean` remove unused RAW PCM files
\u2022 `/pause` pause playing music
\u2022 `/resume` resume playing music
\u2022 `/mute` mute the VC userbot
\u2022 `/unmute` unmute the VC userbot
\u2022 `/restart` restart the bot

🏷️ **Developer: @Darkridersslk** 👑
"""


@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('SDBOTs Channel', url='https://t.me/SDBOTs_inifinity'),
        InlineKeyboardButton('BOT Support', url='https://t.me/SDBOTz'),
    ],
    [
        InlineKeyboardButton('MORE BOTS', url='https://t.me/SDBOTs_inifinity/441'),
        InlineKeyboardButton('Scource Code 💾', url='https://github.com/sadew451/FM'),
    ],
    [
        InlineKeyboardButton('Commands Help ❓', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
