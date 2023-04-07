from internetspeed import InternetSpeedTwitterBot
import time
import os
from dotenv import load_dotenv

load_dotenv("config.env")

PROMISED_DOWN = 200
PROMISED_UP = 200
TWITTER_URL = "https://twitter.com/"
SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_EMAIL = os.getenv('TWITTER_EMAIL')
TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')

##twitter
internet_speed = InternetSpeedTwitterBot()
internet_speed.get_internet_speed(SPEEDTEST_URL)
internet_speed.tweet_at_provider(url=TWITTER_URL, email=TWITTER_EMAIL, username=TWITTER_USERNAME, password=TWITTER_PASSWORD)

time.sleep(30)