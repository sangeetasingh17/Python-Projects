import requests

while True:
    # Webhook of my channel. Click on edit channel --> Webhooks --> Creates webhook
    mUrl = "https://discord.com/api/webhooks/871628330804314132/FIjRqUZTjomRIyHJGwbGFETYKud8kUBqnRrR1RRjzd6u-sw0B8jGrB6hd6qRoHlnDlrw"

    data = {"content": 'Hey my first message'}
    response = requests.post(mUrl, json=data)
