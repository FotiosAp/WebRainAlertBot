import requests
import os
from dotenv import load_dotenv
#Load environment variables securely from the .env file
load_dotenv()
#COMMENT: SECRETS & API KEYS
bot_token=os.environ.get("TELEGRAM_BOT_TOKEN")
chat_id=os.environ.get("TELEGRAM_CHAT_ID")
weather_api_key=os.environ.get("WEATHER_API_KEY")
LATITUDE=38.9098
LONGITUDE=16.5877
FORECAST_COUNT=4
#STEP 1 - FETCH WEATHER DATA FROM OPENWEATHERMAP
parameters={
    "lat":LATITUDE,
    "lon":LONGITUDE,
    "appid":weather_api_key,
    "cnt":FORECAST_COUNT
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
print(response.json())
data_weather=response.json()
#STEP 2 ADDING ALL THE DATA CODES FOR WEATHER IN A LIST AND ANALYZE WEATHER CONDITIONS
condition_list=[]
for status in data_weather["list"]:
    condition_list.append(status["weather"][0]["id"])
print(condition_list)
is_gonna_rain=False
#In the OpenWeatherMap API, condition codes under 700 indicate rain, snow, or thunderstorms
for i in condition_list:
    if i< 700:
        is_gonna_rain=True
if is_gonna_rain:
    message="🌧️☂️Bring an Umbrella it's gonna rain today!"
else:
    message="There is no rain today!"
#STEP 3 - FORMAT AND SEND TELEGRAM ALERT
url=f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload={
        "chat_id": chat_id,
        "text": message
    }
telegram_message = requests.post(url=url, data=payload)
print(telegram_message.json())
telegram_message.raise_for_status()
print("Telegram message sent")

