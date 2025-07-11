#!/usr/bin/env python3
"""
Add all the missing imports found in _extbot.py to the telegram __init__.py
"""

# List of imports from _extbot.py that need to be added
missing_imports = [
    'BotShortDescription',
    'GameHighScore', 
    'InlineQueryResultsButton',
    'MaskPosition',
    'ReplyParameters',
    'StickerSet',
    'TelegramObject',
    'UserChatBoosts',
]

# Read current __init__.py
with open('.pythonlibs/lib/python3.11/site-packages/telegram/__init__.py', 'r') as f:
    content = f.read()

# Add the missing imports
additional_imports = '''
from telegram._botdescription import BotShortDescription
from telegram._games.gamehighscore import GameHighScore
from telegram._inline.inlinequeryresultsbutton import InlineQueryResultsButton
from telegram._files.sticker import MaskPosition
from telegram._reply import ReplyParameters
from telegram._files.sticker import StickerSet
from telegram._telegramobject import TelegramObject
from telegram._chatboost import UserChatBoosts'''

# Add to imports section before constants
content = content.replace(
    'from telegram import constants',
    additional_imports + '\nfrom telegram import constants'
)

# Add to __all__ list
content = content.replace(
    "'constants', 'error', 'helpers',",
    "'BotShortDescription', 'GameHighScore', 'InlineQueryResultsButton', 'MaskPosition', 'ReplyParameters', 'StickerSet', 'TelegramObject', 'UserChatBoosts', 'constants', 'error', 'helpers',"
)

# Write back
with open('.pythonlibs/lib/python3.11/site-packages/telegram/__init__.py', 'w') as f:
    f.write(content)

print("Added missing imports to telegram __init__.py")