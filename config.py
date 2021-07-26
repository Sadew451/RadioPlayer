"""
RadioPlayerV2, Telegram Voice Chat Userbot
Copyright (C) 2021  Sadew Jayasekara <https://t.me/Darkridersslk>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", "1803810116 1221558981")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 6775322))
    CHAT = int(os.environ.get("CHAT", "-1001311942992"))
    LOG_GROUP = os.environ.get("LOG_GROUP", "-1001311942992")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = os.environ.get("STREAM_URL", "https://radioindia.net/radio/hungamanow/icecast.audio")
    API_HASH = os.environ.get("API_HASH", "89ca2ba997c610e24f82bf4f6c3e777b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1911917540:AAFe-i9h9sOB4erAxk5NhBXz9xEgzRbvJI8") 
    SESSION = os.environ.get("SESSION_STRING", "BAAo9iBSkC1vIhki5uuwwDBhrX7_XWUB-k0Ui_QUXvzU64Nk24wVqE2zam9-oAUMiqKNfV-SHdWMcoaYogxqYu94aRWvEcCTaMt1F7Og3ju0IyFEaR0uwHI6rJ3w8OgJyvX7lFSJ0gYbpIfedArstzJsdbsufsGfQuFCsj_2Q4hlmNKOgbPgJDPSIF0xme36r0cZF9hNv3vbmTMrRRJnFZdLoCeyfceVhX5eBF7tlZXCDSWUrE2O5xwDUVuSUEd8mHBPZH0N5LWWHeO1YkMjEA_x4-WOguxrLHlLLvzBI3OzRbxvWJ31Cys3doMqGQ3C2ZZI3VZBT8ELP5zKk-qHRezka4P1RAA")

