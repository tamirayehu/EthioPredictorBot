#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ETHIOPREDICTORBOT - GLOBAL FOOTBALL PREDICTOR
Free Offline Version for Portfolio
"""

import os
import re
import hashlib
import logging
import random

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# CONFIGURATION
TELEGRAM_TOKEN = "7755615804:AAGEoUL6oleIPpTMQ590-uJcF2aP1kHR1GE"
SYSTEM_VERSION = "3.2-Free"

logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)

# PREDICTION ENGINE
class PredictionEngine:
    async def predict(self, home_name: str, away_name: str):
        seed = int(hashlib.md5((home_name + away_name).lower().encode()).hexdigest()[:8], 16)
        random.seed(seed)
        
        home_strength = random.uniform(0.9, 1.8)
        away_strength = random.uniform(0.9, 1.8)
        
        home_win_prob = home_strength / (home_strength + away_strength + 0.4)
        draw_prob = 0.28
        away_win_prob = 1.0 - home_win_prob - draw_prob
        
        if home_win_prob > away_win_prob and home_win_prob > draw_prob:
            winner = home_name
        elif away_win_prob > draw_prob:
            winner = away_name
        else:
            winner = "Draw"

        return {
            "home_team": home_name,
            "away_team": away_name,
            "winner": winner,
            "home_prob": round(home_win_prob * 100, 1),
            "draw_prob": round(draw_prob * 100, 1),
            "away_prob": round(away_win_prob * 100, 1),
            "likely_score": f"{round(home_strength + 0.5)} - {round(away_strength + 0.5)}",
            "confidence": round(55 + abs(home_win_prob - 0.5) * 60, 1)
        }

# TELEGRAM BOT
class PredictorBot:
    def __init__(self):
        self.engine = PredictionEngine()
        self.app = Application.builder().token(TELEGRAM_TOKEN).build()
        self._register_handlers()

    def _register_handlers(self):
        self.app.add_handler(CommandHandler("start", self.cmd_start))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.on_text))

    async def cmd_start(self, update: Update, context: CallbackContext):
        await update.message.reply_text(
            f"⚽ *Ethiopredictorbot v{SYSTEM_VERSION}*\n\n"
            "Send any match like:\n"
            "`Arsenal vs Chelsea`\n"
            "`Liverpool vs Man City`",
            parse_mode="Markdown"
        )

    async def on_text(self, update: Update, context: CallbackContext):
        text = update.message.text.strip()
        parts = re.split(r'\s+vs\.?\s+', text, flags=re.IGNORECASE)
        
        if len(parts) == 2:
            home = parts[0].strip()
            away = parts[1].strip()
            
            msg = await update.message.reply_text(f"🔮 Predicting {home} vs {away}...", parse_mode="Markdown")
            
            result = await self.engine.predict(home, away)
            
            response = f"""
⚽ **{result['home_team']} vs {result['away_team']}**

🏆 **Prediction:** {result['winner']}
🎯 **Confidence:** {result['confidence']}%
📊 **Probabilities:**
• Home: {result['home_prob']}% 
• Draw: {result['draw_prob']}% 
• Away: {result['away_prob']}%
🔢 **Likely Score:** {result['likely_score']}
            """.strip()
            
            await msg.edit_text(response, parse_mode="Markdown")
        else:
            await update.message.reply_text("⚽ Send match like: `Team A vs Team B`")

    def run(self):
        print("🚀 Ethiopredictorbot is running...")
        print("Open Telegram and type a match!")
        self.app.run_polling(drop_pending_updates=True)

# START
if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    bot = PredictorBot()
    bot.run()