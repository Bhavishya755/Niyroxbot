#!/usr/bin/env python3
"""
Simple Telegram Bot Runner
Runs the bot directly without any web server complications
"""
import os
import sys
import asyncio
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Main function to run the bot"""
    try:
        # Get bot token from environment
        bot_token = os.getenv('BOT_TOKEN')
        if not bot_token:
            logger.error("BOT_TOKEN not found in environment variables")
            return
        
        logger.info("🚀 Starting Telegram Bot...")
        logger.info(f"🔑 Token: {bot_token[:10]}...")
        
        # Import and run the bot
        from main import main as bot_main
        bot_main()
        
    except Exception as e:
        logger.error(f"❌ Error starting bot: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()