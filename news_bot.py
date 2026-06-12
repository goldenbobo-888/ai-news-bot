import requests
import xml.etree.ElementTree as ET
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

RSS_URL = "https://news.google.com/rss/search?q=US+stock+market&hl=en-US&gl=US&ceid=US:en"

response = requests.get(RSS_URL)

if response.status_code == 200:

    root = ET.fromstring(response.content)

    items = root.findall(".//item")

    message = "📈 **US MARKET NEWS**\n\n"

    for item in items[:5]:

        title = item.find("title").text
        link = item.find("link").text

        message += f"• {title}\n{link}\n\n"

    requests.post(
        WEBHOOK_URL,
        json={"content": message}
    )

    print("Success")

else:
    print("Failed")
