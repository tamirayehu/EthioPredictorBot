
# ⚽ EthioPredictorBot

> AI-powered Telegram football match prediction bot built with Python.

**Author:** Tamir Ayehu | Ethiopian Python & AI Developer

---

## Overview

EthioPredictorBot is a Telegram-based football prediction system that uses statistical modeling to predict match outcomes. Users simply send a match like Arsenal vs Chelsea and instantly receive win probabilities, likely score, and confidence rating. Fully offline, no paid API required.

---

## Features

- Predict any football match worldwide
- Home / Draw / Away win probabilities
- Confidence score per prediction
- Likely scoreline estimate
- Instant response via Telegram
- Fully offline, no paid API needed
- Deterministic results (same match = same prediction every time)

---

## Tech Stack

- Language: Python 3.10+
- Bot Framework: python-telegram-bot v20+
- Prediction Engine: MD5 seeded statistical modeling
- Deployment: Android Pydroid3 / Linux VPS

---

## Try It Live

Search @EthioPredictorBot on Telegram

Send any match:
- Arsenal vs Chelsea
- Liverpool vs Man City
- Ethiopia vs Egypt

---

## Installation

git clone https://github.com/tamirayehu/EthioPredictorBot
cd EthioPredictorBot
pip install python-telegram-bot
python bot.py

---

## How Prediction Works

1. Match name hashed with MD5 for consistent seeding
2. Team strengths derived from seed value
3. Win probabilities calculated using strength ratios
4. Confidence score reflects margin between probabilities
5. No internet or paid API required

---

## Developer

Tamir Ayehu — Ethiopian Python & AI Developer
- Based in Ethiopia
- Open to remote work and international opportunities
- Telegram: @EthioPredictorBot

---

## License

MIT License