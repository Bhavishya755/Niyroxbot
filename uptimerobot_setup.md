# UptimeRobot Setup Guide for Telegram Bot

## Overview
This guide will help you set up UptimeRobot monitoring to keep your Telegram bot running 24/7 on Replit.

## Prerequisites
- Your Telegram bot is running with the Flask keep-alive server
- You have access to your Replit project URL

## Step 1: Get Your Bot's URL

Your bot is currently running at:
```
https://bf1cd8be-20c8-4f99-8083-7e7cba4cb776-00-13j3n5uexl3dy.riker.replit.dev
```

Health check endpoint:
```
https://bf1cd8be-20c8-4f99-8083-7e7cba4cb776-00-13j3n5uexl3dy.riker.replit.dev/health
```

## Step 2: Create UptimeRobot Account

1. Go to [https://uptimerobot.com](https://uptimerobot.com)
2. Click "Sign Up" and create a free account
3. Verify your email address
4. Log in to your dashboard

## Step 3: Add New Monitor

1. In your UptimeRobot dashboard, click "Add New Monitor"
2. Configure the monitor with these settings:

   **Monitor Type:** HTTP(s)
   **Friendly Name:** Telegram Bot Keep-Alive
   **URL:** `https://bf1cd8be-20c8-4f99-8083-7e7cba4cb776-00-13j3n5uexl3dy.riker.replit.dev/health`
   **Monitoring Interval:** 5 minutes
   **HTTP Method:** GET
   **Expected HTTP Status Code:** 200

3. Click "Create Monitor"

## Step 4: Configure Notifications (Optional)

1. Go to "My Settings" → "Alert Contacts"
2. Add your email address or phone number
3. Configure when you want to be notified (e.g., when the bot goes down)

## Step 5: Test Your Setup

1. Wait a few minutes for the first ping
2. Check that the monitor shows "Up" status
3. Your bot should now stay alive 24/7!

## How It Works

- UptimeRobot pings your bot's `/health` endpoint every 5 minutes
- This prevents Replit from putting your project to sleep
- If your bot goes down, UptimeRobot will notify you
- The Flask server runs alongside your Telegram bot, providing the web interface

## Available Endpoints

Your bot provides these endpoints:

1. **Main Status Page:** `/`
   - Shows a nice HTML page with bot status
   - Good for checking if everything is working

2. **Health Check:** `/health`
   - JSON response with bot status
   - Used by UptimeRobot for monitoring

3. **Bot Statistics:** `/stats`
   - JSON response with bot features and info
   - Useful for debugging

## Troubleshooting

### Monitor Shows "Down"
- Check that your Replit project is running
- Verify the URL is correct
- Make sure the Flask server is running on port 8080

### Bot Not Responding to Messages
- Check the bot token in your environment variables
- Look at the bot logs in the Replit console
- Verify the bot is properly started alongside Flask

### Can't Access the URLs
- Make sure your Replit project is public or properly configured
- Check that the Flask server is bound to `0.0.0.0:8080`
- Verify no firewall is blocking the ports

## Current Status

✅ Bot is running successfully
✅ Flask keep-alive server is active
✅ Health endpoint is responding correctly
✅ Bot token is properly configured
✅ All endpoints are accessible

Your bot is now ready for 24/7 operation with UptimeRobot monitoring!