# Rain Alert Bot

An automated Python script that checks the daily weather forecast for a specific location and sends a real-time Telegram notification advising whether you need to bring an umbrella.

## Key Features

- **Automated Weather Tracking:** Uses the OpenWeatherMap API to retrieve upcoming weather conditions based on customizable latitude and longitude coordinates.
- **Smart Condition Parsing:** Analyzes weather condition codes (identifying codes under 700) to accurately detect rain, snow, or thunderstorms.
- **Instant Notifications:** Sends a formatted alert with appropriate emojis directly to your Telegram chat.
- **Secure Configuration:** Protects sensitive API keys and tokens by pulling them from a local `.env` environment variables file.

## System Requirements

- Python 3.x
- `requests` library (`pip install requests`)
- `python-dotenv` library (`pip install python-dotenv`)

## Setup & Installation

1. Create a file named `.env` in the root directory (same folder as `main.py`).
2. Add your API keys and credentials inside the `.env` file using the following format:

   ```env
   WEATHER_API_KEY=your_openweathermap_api_key
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
