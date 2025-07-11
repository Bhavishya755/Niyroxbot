#!/usr/bin/env python3
"""
Telegram Bot with Flask Keep-Alive Server
Combines the bot functionality with a Flask web server for UptimeRobot monitoring
"""

import os
import sys
import asyncio
import logging
from threading import Thread
from flask import Flask

# Import the main bot functionality
from main import main as run_bot

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

# Flask web server
app = Flask(__name__)

@app.route('/')
def home():
    """Main endpoint - returns bot status"""
    return """
    <html>
        <head>
            <title>Telegram Bot Status</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .status { color: green; font-weight: bold; }
                .info { background: #f0f0f0; padding: 20px; margin: 20px 0; border-radius: 5px; }
            </style>
        </head>
        <body>
            <h1>🤖 Telegram Bot Status</h1>
            <p class="status">✅ Bot is running!</p>
            <div class="info">
                <h3>Bot Information:</h3>
                <p>• Status: Active and monitoring for messages</p>
                <p>• Features: Admin commands, moderation, fun commands, utilities</p>
                <p>• Last update: Bot is continuously polling Telegram API</p>
            </div>
            <p><small>This endpoint is used by UptimeRobot to keep the bot alive 24/7</small></p>
        </body>
    </html>
    """

@app.route('/health')
def health():
    """Health check endpoint for UptimeRobot"""
    import time
    return {
        "status": "ok",
        "message": "Bot is running",
        "timestamp": str(time.time())
    }

@app.route('/stats')
def stats():
    """Bot statistics endpoint"""
    return {
        "bot_name": "Telegram Admin Bot",
        "status": "running",
        "features": [
            "Admin Commands",
            "Moderation Tools", 
            "Fun Commands",
            "Utility Commands",
            "Information Commands"
        ],
        "uptime": "24/7 with UptimeRobot monitoring"
    }

def run_flask():
    """Run Flask server"""
    logger.info("🌐 Starting Flask keep-alive server on port 8080...")
    app.run(host='0.0.0.0', port=8080, debug=False)

def run_bot_async():
    """Run the bot in an async context"""
    logger.info("🚀 Starting Telegram bot...")
    try:
        # Import and run the bot main function directly
        from main import main as bot_main
        bot_main()
    except Exception as e:
        logger.error(f"❌ Error running bot: {e}")

def main():
    """Main function to start both Flask server and bot"""
    logger.info("🚀 Starting Telegram Bot with Flask Keep-Alive...")
    
    # Start Flask server in background thread
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    logger.info("✅ Flask keep-alive server started")
    
    # Start the bot
    try:
        run_bot_async()
    except KeyboardInterrupt:
        logger.info("👋 Bot stopped by user")
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()