from bs4 import BeautifulSoup
from dotenv import load_dotenv
import datetime
import json
import os
import requests

load_dotenv()
DISCORD_CHANNEL_ID = os.environ["DISCORD_CHANNEL_ID"]
DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]

res = requests.get("https://atcoder.jp/contests/?lang=ja")
soup = BeautifulSoup(res.text, "html.parser")

for contest in soup.select("#contest-table-upcoming tbody tr"):
  start_at_text = contest.select_one("time").get_text()
  start_at = datetime.datetime.strptime(start_at_text, "%Y-%m-%d %H:%M:%S%z")
  contest_url = contest.select_one('a[href^="/contests"]').get("href")

  JST = datetime.timezone(datetime.timedelta(hours=9))
  today = datetime.datetime.now(JST)
  tomorrow = today + datetime.timedelta(days=1)
  if "abc" in contest_url and start_at > today and start_at < tomorrow:
    url = f"https://discord.com/api/channels/{DISCORD_CHANNEL_ID}/messages"
    headers = {"Authorization": f"Bot {DISCORD_BOT_TOKEN}", "Content-Type": "application/json"}
    data = {"content": f"https://atcoder.jp{contest_url}"}
    res = requests.post(url, headers=headers, data=json.dumps(data))
    res.raise_for_status()
    break
