#!/usr/bin/env python3
"""
Script to fix the telegram import issue by removing the conflicting package
"""
import os
import shutil
import sys

def fix_telegram_import():
    """Remove the conflicting telegram package"""
    site_packages = ".pythonlibs/lib/python3.11/site-packages"
    
    # Remove the conflicting telegram package
    conflicting_files = [
        f"{site_packages}/telegram/__init__.py",
        f"{site_packages}/telegram-0.0.1.dist-info"
    ]
    
    for file_path in conflicting_files:
        if os.path.exists(file_path):
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Removed directory: {file_path}")
            else:
                os.remove(file_path)
                print(f"Removed file: {file_path}")
    
    # Create the correct __init__.py for telegram package
    telegram_init = f"{site_packages}/telegram/__init__.py"
    telegram_init_content = '''"""
Python Telegram Bot Library
"""

__version__ = "20.8"
__author__ = "python-telegram-bot"

# Import all the main classes
from telegram._bot import Bot
from telegram._application import Application
from telegram._chat import Chat
from telegram._user import User
from telegram._message import Message
from telegram._update import Update
from telegram._callbackquery import CallbackQuery
from telegram._chatmember import ChatMember
from telegram._chatmemberowner import ChatMemberOwner
from telegram._chatmemberadministrator import ChatMemberAdministrator
from telegram._chatmembermember import ChatMemberMember
from telegram._chatmemberrestricted import ChatMemberRestricted
from telegram._chatmemberleft import ChatMemberLeft
from telegram._chatmemberbanned import ChatMemberBanned

# Import constants
from telegram import constants

__all__ = [
    "Bot",
    "Application", 
    "Chat",
    "User",
    "Message",
    "Update",
    "CallbackQuery",
    "ChatMember",
    "ChatMemberOwner",
    "ChatMemberAdministrator",
    "ChatMemberMember",
    "ChatMemberRestricted",
    "ChatMemberLeft",
    "ChatMemberBanned",
    "constants",
]
'''
    
    os.makedirs(os.path.dirname(telegram_init), exist_ok=True)
    with open(telegram_init, 'w') as f:
        f.write(telegram_init_content)
    print(f"Created correct __init__.py: {telegram_init}")

if __name__ == "__main__":
    fix_telegram_import()
    print("Fixed telegram import issue")