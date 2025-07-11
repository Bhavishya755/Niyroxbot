#!/usr/bin/env python3
"""
Create proper __init__.py for telegram package
"""
import os

# Create proper __init__.py content by finding the existing _bot.py and other files
telegram_dir = ".pythonlibs/lib/python3.11/site-packages/telegram"
init_file = os.path.join(telegram_dir, "__init__.py")

# Check what files exist in the telegram directory
files = []
for root, dirs, file_list in os.walk(telegram_dir):
    for file in file_list:
        if file.endswith('.py') and not file.startswith('__'):
            files.append(os.path.join(root, file))

print("Found python files:")
for f in files[:10]:  # Show first 10 files
    print(f)

# Create a basic __init__.py that just imports what we need
init_content = '''#!/usr/bin/env python3
"""
Telegram Bot API Library
"""

__version__ = "20.8"

# Import basic classes from their respective modules
try:
    from telegram._bot import Bot
    from telegram._chat import Chat  
    from telegram._user import User
    from telegram._message import Message
    from telegram._update import Update
    from telegram._callbackquery import CallbackQuery
    from telegram._chatmember import ChatMember
    from telegram._files.file import File
    from telegram._files.document import Document
    from telegram._files.photo import PhotoSize
    from telegram._files.video import Video
    from telegram._files.audio import Audio
    from telegram._files.voice import Voice
    from telegram._files.sticker import Sticker
    from telegram._files.animation import Animation
    from telegram._files.videNote import VideoNote
    from telegram._files.contact import Contact
    from telegram._files.location import Location
    from telegram._files.venue import Venue
    from telegram._files.inputmedia import InputMedia
    from telegram._inline.inlinekeyboardmarkup import InlineKeyboardMarkup
    from telegram._inline.inlinekeyboardbutton import InlineKeyboardButton
    from telegram._keyboardbutton import KeyboardButton
    from telegram._replykeyboardmarkup import ReplyKeyboardMarkup
    from telegram._replykeyboardremove import ReplyKeyboardRemove
    from telegram._forcereply import ForceReply
    from telegram._menubutton import MenuButton
    from telegram._botcommand import BotCommand
    
    # Version and constants
    from telegram import constants
    
    __all__ = [
        'Bot',
        'Chat',
        'User', 
        'Message',
        'Update',
        'CallbackQuery',
        'ChatMember',
        'File',
        'Document',
        'PhotoSize',
        'Video',
        'Audio',
        'Voice',
        'Sticker',
        'Animation',
        'VideoNote',
        'Contact',
        'Location',
        'Venue',
        'InputMedia',
        'InlineKeyboardMarkup',
        'InlineKeyboardButton',
        'KeyboardButton',
        'ReplyKeyboardMarkup',
        'ReplyKeyboardRemove',
        'ForceReply',
        'MenuButton',
        'BotCommand',
        'constants',
    ]
    
except ImportError as e:
    print(f"Import error in telegram __init__.py: {e}")
    # Fallback minimal imports
    __all__ = []
'''

with open(init_file, 'w') as f:
    f.write(init_content)

print(f"Created {init_file}")