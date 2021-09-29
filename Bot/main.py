import discord
import os
import json
import random
import asyncio
from discord.ext import tasks
from itertools import cycle
from keep_alive import keep_alive

bot = discord.Client()
status = cycle(['Ping', 'Pong'])

@bot.event
async def on_ready():
    change_status.start()
    print('Logged in as {0.user}'.format(bot))


@tasks.loop(seconds=5)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

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
    await message.channel.send('https://Ping-Pong-Bot.shouzy.repl.co')
    print('Websitelink sent')

  if message.content.startswith('pp!code'):
    await message.channel.send('You can finde the code here: https://github.com/realshouzy/Ping-Pong-Bot')
    print('Codelink sent')


keep_alive()
bot.run(os.getenv('TOKEN'))
