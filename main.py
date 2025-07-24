import requests
import os, dotenv
import send_email

dotenv.load_dotenv()
api_key = os.getenv("API_KEY")

topic = "tesla"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2025-06-23&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "language=en"

request = requests.get(url)

content = request.json()

body = ""
for article in content["articles"][:5]:
      if article["title"] and article["description"] is not None:
            body = "Subject: Today's news!" + "\n" \
                  + body + article["title"] + 2*"\n" \
                  + article["description"] + "\n" \
                  + article["url"] + 3*"\n"

body = body.encode("utf-8")
send_email.send_email(body)