import requests
import xml.etree.ElementTree as ET
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

RSS_URL = "https://news.google.com/rss/search?q=US+stock+market&hl=en-US&gl=US&ceid=US:en"

print("Fetching RSS...")

response = requests.get(RSS_URL)

print("RSS Status:", response.status_code)

if response.status_code == 200:

root = ET.fromstring(response.content)

items = root.findall(".//item")

print("Items found:", len(items))

message = "📈 US MARKET NEWS\n\n"

for item in items[:3]:
    title = item.find("title").text

    message += f"📰 {title[:120]}\n\n"

message = message[:1900]

r = requests.post(
    WEBHOOK_URL,
    json={"content": message}
)

print("Discord Status:", r.status_code)
print("Discord Response:", r.text)
```

else:
print("RSS Failed")
