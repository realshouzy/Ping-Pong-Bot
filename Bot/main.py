import discord
import os
import json
import random
import asyncio
from discord.ext import tasks
from itertools import cycle
from keep_alive import keep_alive # Importing the keep_alive function out of the keep_alive.py file

bot = discord.Client()
status = cycle(['Ping', 'Pong']) # The list of the statuses the bot has as its activity

@bot.event
async def on_ready(): # When the bot is ready, online and functionat it:
    change_status.start() # starts the change_status function  
    print('Logged in as {0.user}'.format(bot)) # and it prints "Logged in as [bots name + bots tag]" in the console


@tasks.loop(seconds=5) # Creates a loop every 5 seconds 
async def change_status(): # Defines the change_status function
  await bot.change_presence(activity=discord.Game(next(status))) # This changes the bots activity status with one of the statuses out of the status list


@bot.event
async def on_message(message): # When someone posts a messages, the bot procceds the following code
  if message.author == bot.user: # Checks if the author of the messages is the bot
    return # If the author is the bot, it wont procced with the following code

  if message.content.startswith('Ping'):
    await message.channel.send('Pong')
    print('Played Ping Pong')

  if message.content.startswith('ping'):
    await message.channel.send('Pong')
    print('Played ping Pong')

  if message.content.startswith('pp!help'):
    await message.channel.send('So the main function of this bot is to write "Pong" when you write "Ping"(or "ping"). It also has a few commands with the prefix "pp!", like "pp!ping" for the latency, "pp!invite" to get the invite link of the bot and "pp!vote" to get the vote link of the bot. You can also read the code if you want with "pp!code".')
    print('Stats sent')

  if message.content.startswith('pp!ping'):
    await message.channel.send(f'The ping is {round(bot.latency * 1000)}ms')
    print('Ping sent')
    
  if message.content.startswith('pp!invite'):
    await message.channel.send('Invite the bot to other server: https://discord.com/api/oauth2/authorize?client_id=831066967287791627&permissions=3072&scope=bot')
    print('Invitelink sent')

  if message.content.startswith('pp!stats'):
    await message.channel.send(f'Playing Ping Pong on {len(bot.guilds)} servers.')
    print('Stats sent')

  if message.content.startswith('pp!vote'):
    await message.channel.send('You can vote for the bot here: https://top.gg/bot/831066967287791627/vote')
    print('Votelink sent')

  if message.content.startswith('pp!website'):
    await message.channel.send('https://ping-pong.shouzy.repl.co/')
    print('Websitelink sent')

  if message.content.startswith('pp!code'):
    await message.channel.send('You can finde the code here: https://github.com/realshouzy/Ping-Pong-Bot')
    print('Codelink sent')


keep_alive() # Executes the keep_alive function out of the keep_alive.py file
bot.run(os.getenv('TOKEN')) # Gets the bots token from the env file with help of os
