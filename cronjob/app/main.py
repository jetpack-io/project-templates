from jetpack import cron
import requests
import json

@cron.repeat(cron.every(10).minute)
async def bitcoin_cron_test_job():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    r = requests.get(url).text
    data = json.loads(r)
    print("Getting latest BTC Price")
    price = data["bpi"]["USD"]["rate"]
    print("Latest Bitcoin Price:", price)

