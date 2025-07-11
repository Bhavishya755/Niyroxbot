#!/usr/bin/env python3
"""
Create minimal but working __init__.py for telegram package
"""

# Create minimal __init__.py content
init_content = '''#!/usr/bin/env python3
"""
Python Telegram Bot API
"""

__version__ = "20.8"

# Import the essential classes that are definitely needed
from telegram._bot import Bot
from telegram._chat import Chat
from telegram._user import User
from telegram._message import Message
from telegram._update import Update
from telegram._callbackquery import CallbackQuery
from telegram._chatmember import ChatMember
from telegram._messageentity import MessageEntity
from telegram._keyboardbutton import KeyboardButton
from telegram._replykeyboardmarkup import ReplyKeyboardMarkup
from telegram._replykeyboardremove import ReplyKeyboardRemove
from telegram._forcereply import ForceReply
from telegram._menubutton import MenuButton
from telegram._botcommand import BotCommand
from telegram._dice import Dice
from telegram._poll import Poll
from telegram._files.document import Document
from telegram._files.photo import PhotoSize  
from telegram._files.video import Video
from telegram._files.audio import Audio
from telegram._files.voice import Voice
from telegram._files.sticker import Sticker
from telegram._files.animation import Animation
from telegram._files.contact import Contact
from telegram._files.location import Location
from telegram._files.venue import Venue
from telegram._inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram._inline.inlinekeyboardbutton import InlineKeyboardButton

# Import constants
from telegram import constants

__all__ = [
    'Bot',
    'Chat',
    'User',
    'Message', 
    'Update',
    'CallbackQuery',
    'ChatMember',
    'MessageEntity',
    'KeyboardButton',
    'ReplyKeyboardMarkup',
    'ReplyKeyboardRemove',
    'ForceReply',
    'MenuButton',
    'BotCommand',
    'Dice',
    'Poll',
    'Document',
    'PhotoSize',
    'Video',
    'Audio',
    'Voice',
    'Sticker',
    'Animation',
    'Contact',
    'Location',
    'Venue',
    'InlineKeyboardMarkup',
    'InlineKeyboardButton',
    'constants',
]
'''

with open('.pythonlibs/lib/python3.11/site-packages/telegram/__init__.py', 'w') as f:
    f.write(init_content)

print("Created minimal __init__.py")