#!/usr/bin/env python3
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from requests import post as rpost
from markdown import markdown
from random import choice
from datetime import datetime
from calendar import month_name
from pycountry import countries as conn
from urllib.parse import quote as q
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)

# Bot configuration
api_id = 123456  # Replace with your Telegram API ID
api_hash = "your_api_hash_here"  # Replace with your Telegram API hash
bot_token = "your_bot_token_here"  # Replace with your bot token

# Initialize the bot
bot = Client("anime_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Bot commands class
class BotCommands:
    AniListCommand = "anime"
    AnimeHelpCommand = "animehelp"

# Correct custom filter implementation
def authorized_filter(_, __, ___):
    return True

def blacklisted_filter(_, __, ___):
    return False

# Create filter objects
authorized = filters.create(authorized_filter, "AuthorizedFilter")
not_blacklisted = filters.create(lambda _, __, ___: not blacklisted_filter(_, __, ___), "NotBlacklistedFilter")

# [Keep all your existing helper functions, ButtonMaker class, GENRES_EMOJI dict, etc.]

# [Keep all your existing handler functions: anilist, setAnimeButtons, character, etc.]

def register_handlers():
    # Command handlers - using the proper filter combination
    bot.add_handler(MessageHandler(
        anilist, 
        filters.command(BotCommands.AniListCommand) & authorized & not_blacklisted
    ))
    
    bot.add_handler(MessageHandler(
        character,
        filters.command("character") & authorized & not_blacklisted
    ))
    
    bot.add_handler(MessageHandler(
        manga,
        filters.command("manga") & authorized & not_blacklisted
    ))
    
    bot.add_handler(MessageHandler(
        anime_help,
        filters.command(BotCommands.AnimeHelpCommand) & authorized & not_blacklisted
    ))
    
    # Callback handlers remain unchanged
    bot.add_handler(CallbackQueryHandler(
        setAnimeButtons, 
        filters.regex(r"^anime")
    ))
    
    bot.add_handler(CallbackQueryHandler(
        setCharacButtons, 
        filters.regex(r"^cha")
    ))

if __name__ == "__main__":
    LOGGER.info("Starting Anime Bot...")
    register_handlers()
    bot.run()
