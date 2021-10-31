"""
At first: This bot was coded in Replit.
About "keep_alive":
It uses Flask to keep the bot online
The code is from: https://gist.github.com/beaucarnes/51ec37412ab181a2e3fd320ee474b671
After that go on uptimerobot and create a new monitor with the url the keep_alive.py file created.
Then the bot will stay then online for ever.
"""
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is online"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
