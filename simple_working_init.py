#!/usr/bin/env python3
"""
Create simple working __init__.py with only essential imports
"""

# Create minimal working __init__.py
init_content = '''#!/usr/bin/env python3
"""
Python Telegram Bot API
"""

__version__ = "20.8"

# Core classes - import only what exists and is needed
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
from telegram._botcommandscope import BotCommandScope
from telegram._dice import Dice
from telegram._poll import Poll
from telegram._messageorigin import MessageOrigin, MessageOriginChannel, MessageOriginChat, MessageOriginUser, MessageOriginHiddenUser
from telegram._files.document import Document
from telegram._files.photosize import PhotoSize
from telegram._files.video import Video
from telegram._files.audio import Audio
from telegram._files.voice import Voice
from telegram._files.sticker import Sticker
from telegram._files.animation import Animation
from telegram._files.contact import Contact
from telegram._files.location import Location
from telegram._files.venue import Venue
from telegram._files.file import File
from telegram._files.videonote import VideoNote
from telegram._files.inputmedia import InputMedia
from telegram._files.inputfile import InputFile
from telegram._files.chatphoto import ChatPhoto
from telegram._inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram._inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram._choseninlineresult import ChosenInlineResult
from telegram._chatinvitelink import ChatInviteLink
from telegram._chatjoinrequest import ChatJoinRequest
from telegram._chatmemberupdated import ChatMemberUpdated
from telegram._chatpermissions import ChatPermissions
from telegram._chatadministratorrights import ChatAdministratorRights
from telegram._proximityalerttriggered import ProximityAlertTriggered
from telegram._videochat import VideoChatStarted, VideoChatEnded, VideoChatParticipantsInvited, VideoChatScheduled
from telegram._loginurl import LoginUrl
from telegram._webappdata import WebAppData
from telegram._webappinfo import WebAppInfo
from telegram._keyboardbuttonpolltype import KeyboardButtonPollType
from telegram._writeaccessallowed import WriteAccessAllowed
from telegram._forumtopic import ForumTopic, ForumTopicCreated, ForumTopicClosed, ForumTopicEdited, ForumTopicReopened, GeneralForumTopicHidden, GeneralForumTopicUnhidden
from telegram._shared import UsersShared, ChatShared
from telegram._story import Story
from telegram._giveaway import Giveaway, GiveawayWinners, GiveawayCompleted, GiveawayCreated
from telegram._linkpreviewoptions import LinkPreviewOptions
from telegram._reaction import ReactionType, ReactionTypeEmoji, ReactionTypeCustomEmoji
from telegram._messagereactionupdated import MessageReactionUpdated, MessageReactionCountUpdated
from telegram._chatboost import ChatBoost, ChatBoostUpdated, ChatBoostRemoved, ChatBoostSource, ChatBoostSourcePremium, ChatBoostSourceGiftCode, ChatBoostSourceGiveaway
from telegram._messageautodeletetimerchanged import MessageAutoDeleteTimerChanged
from telegram._messageid import MessageId
from telegram._userprofilephotos import UserProfilePhotos
from telegram._webhookinfo import WebhookInfo
from telegram import constants
from telegram import error
from telegram import helpers

__all__ = [
    'Bot', 'Chat', 'User', 'Message', 'Update', 'CallbackQuery', 'ChatMember', 'MessageEntity',
    'KeyboardButton', 'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'ForceReply', 'MenuButton',
    'BotCommand', 'BotCommandScope', 'Dice', 'Poll', 'MessageOrigin', 'MessageOriginChannel',
    'MessageOriginChat', 'MessageOriginUser', 'MessageOriginHiddenUser', 'Document', 'PhotoSize',
    'Video', 'Audio', 'Voice', 'Sticker', 'Animation', 'Contact', 'Location', 'Venue', 'File',
    'VideoNote', 'InputMedia', 'InputFile', 'ChatPhoto', 'InlineKeyboardMarkup', 'InlineKeyboardButton',
    'ChosenInlineResult', 'ChatInviteLink', 'ChatJoinRequest', 'ChatMemberUpdated', 'ChatPermissions',
    'ChatAdministratorRights', 'ProximityAlertTriggered', 'VideoChatStarted', 'VideoChatEnded',
    'VideoChatParticipantsInvited', 'VideoChatScheduled', 'LoginUrl', 'WebAppData', 'WebAppInfo',
    'KeyboardButtonPollType', 'WriteAccessAllowed', 'ForumTopic', 'ForumTopicCreated', 'ForumTopicClosed',
    'ForumTopicEdited', 'ForumTopicReopened', 'GeneralForumTopicHidden', 'GeneralForumTopicUnhidden',
    'UsersShared', 'ChatShared', 'Story', 'Giveaway', 'GiveawayWinners', 'GiveawayCompleted',
    'GiveawayCreated', 'LinkPreviewOptions', 'ReactionType', 'ReactionTypeEmoji', 'ReactionTypeCustomEmoji',
    'MessageReactionUpdated', 'MessageReactionCountUpdated', 'ChatBoost', 'ChatBoostUpdated',
    'ChatBoostRemoved', 'ChatBoostSource', 'ChatBoostSourcePremium', 'ChatBoostSourceGiftCode',
    'ChatBoostSourceGiveaway', 'MessageAutoDeleteTimerChanged', 'MessageId', 'UserProfilePhotos',
    'WebhookInfo', 'constants', 'error', 'helpers',
]
'''

with open('.pythonlibs/lib/python3.11/site-packages/telegram/__init__.py', 'w') as f:
    f.write(init_content)

print("Created simple working __init__.py")