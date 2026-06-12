import requests
import xml.etree.ElementTree as ET
import os

MARKET_WEBHOOK = os.environ["DISCORD_WEBHOOK"]
TRUMP_WEBHOOK = os.environ["TRUMP_WEBHOOK"]
FED_WEBHOOK = os.environ["FED_WEBHOOK"]
AI_WEBHOOK = os.environ["AI_WEBHOOK"]
SEMI_WEBHOOK = os.environ["SEMI_WEBHOOK"]

RSS_URL = "https://news.google.com/rss/search?q=US+stock+market&hl=en-US&gl=US&ceid=US:en"

TRUMP_KEYWORDS = ["trump", "tariff", "china", "taiwan", "trade war"]

FED_KEYWORDS = [
"fed", "powell", "interest rate",
"inflation", "cpi", "ppi",
"nonfarm", "nfp"
]

AI_KEYWORDS = [
"ai", "openai", "anthropic",
"chatgpt", "claude", "gemini"
]

SEMI_KEYWORDS = [
"nvidia", "nvda", "amd",
"tsmc", "tsm", "intel",
"broadcom", "qualcomm"
]

def send_message(webhook, message):
requests.post(
webhook,
json={"content": message}
)

print("Fetching RSS...")

response = requests.get(RSS_URL)

print("RSS Status:", response.status_code)

if response.status_code == 200:

root = ET.fromstring(response.content)

items = root.findall(".//item")

print("Items found:", len(items))

for item in items[:10]:

    title = item.find("title").text

    if not title:
        continue

    title_lower = title.lower()

    message = f"📰 {title}"

    if any(word in title_lower for word in TRUMP_KEYWORDS):
        send_message(TRUMP_WEBHOOK, f"🚨 TRUMP WATCH\n\n{message}")

    elif any(word in title_lower for word in FED_KEYWORDS):
        send_message(FED_WEBHOOK, f"🏦 FED WATCH\n\n{message}")

    elif any(word in title_lower for word in AI_KEYWORDS):
        send_message(AI_WEBHOOK, f"🤖 AI WATCH\n\n{message}")

    elif any(word in title_lower for word in SEMI_KEYWORDS):
        send_message(SEMI_WEBHOOK, f"💾 SEMICONDUCTOR WATCH\n\n{message}")

    else:
        send_message(MARKET_WEBHOOK, f"📈 MARKET NEWS\n\n{message}")

print("Done")

else:
print("RSS Failed")
