"""
At first: This bot was coded in Replit.
"""
import discord
import os
import json
import random
import asyncio
from discord.ext import commands, tasks
from discord.ext.commands.errors import CommandNotFound
from itertools import cycle
from keep_alive import keep_alive # Importing the keep_alive function out of the keep_alive.py file

bot = commands.Bot(command_prefix='pp!')
bot.remove_command("help")
status = cycle(['Ping', 'Pong']) # The list of the statuses the bot has as its activity

@bot.event
async def on_ready(): # When the bot is ready, online and functional it:
    print("Started Bot")
    change_status.start()
    print('----------------------------')
    print('Logged in as {0.user}'.format(bot))
    print('----------------------------')
    print(f'Bot´s ID: {bot.user.id}')
    print('----------------------------')


@tasks.loop(seconds=5) # Creates a loop every 5 seconds 
async def change_status(): 
  await bot.change_presence(activity=discord.Game(next(status))) # This changes the bots activity status with one of the statuses out of the status list


@bot.event
async def on_message(msg): # When someone posts a messages, the bot procceds the following code
  if msg.author == bot.user: # Checks if the author of the messages is the bot
    return # If the author is the bot, it wont procced with the following code
  
  # If a message start with a certain pharse, it will send a certain messages back and print a certain phrase in the console
  if msg.content.startswith('Ping'):
    await msg.channel.send('Pong')
    print('Played Ping Pong')

  if msg.content.startswith('ping'):
    await msg.channel.send('Pong')
    print('Played ping Pong')

  await bot.process_commands(msg) # this procceds the following commands


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        embed = discord.Embed(title="Unvalid Command",
                              description='**For help: ``pp!help``**',
                              timestamp=ctx.message.created_at,
                              colour=discord.Colour.red())

        embed.set_footer(
            text='🏓Ping Pong  •  Bot by shouzy',
            icon_url=bot.user.avatar_url
        )
        embed.set_author(name='❌Error')

        await ctx.reply(embed=embed)


@bot.command()
async def ping(ctx):
  try:
    embed = discord.Embed(title=f" The ping is: ``{round(bot.latency * 1000)}ms``",
                          description='',
                          timestamp=ctx.message.created_at,
                          colour=discord.Colour.green())
    embed.set_author(name='🏓Ping Pong')
    embed.set_footer(text=f"Requested by {ctx.author}",
                     icon_url=ctx.author.avatar_url)

    await ctx.reply(embed=embed)
    print("Ping was sent")
  
  except:
    embed = discord.Embed(title="Something went wrong",
                              description='**Please try later again**',
                              timestamp=ctx.message.created_at,
                              colour=discord.Colour.red())

    embed.set_footer(
            text='🏓Ping Pong  •  Bot by shouzy',
            icon_url=bot.user.avatar_url
        )
    embed.set_author(name='❌Error')
    await ctx.reply(embed=embed)

@bot.command()
async def stats(ctx):
  try:
    embed = discord.Embed(title='',
                          description=f"**Playing Ping Pong on {len(bot.guilds)} servers.**",
                          timestamp=ctx.message.created_at,
                          colour=discord.Colour.green())
    embed.set_author(name='🏓Ping Pong')
    embed.set_footer(text=f"Requested by {ctx.author}",
                     icon_url=ctx.author.avatar_url)

    await ctx.reply(embed=embed)
    print("Stats were sent")

  except:
    embed = discord.Embed(title="Something went wrong",
                              description='**Please try later again**',
                              timestamp=ctx.message.created_at,
                              colour=discord.Colour.red())

    embed.set_footer(
            text='🏓Ping Pong  •  Bot by shouzy',
            icon_url=bot.user.avatar_url
        )
    embed.set_author(name='❌Error')
    await ctx.reply(embed=embed)

@bot.command()
async def invite(ctx):
  try:
    embed = discord.Embed(
        title="",
        description=
        "**You can invite the bot to your server by** **__[clicking here!](https://discord.com/api/oauth2/authorize?client_id=831066967287791627&permissions=3072&scope=bot)__**",
        timestamp=ctx.message.created_at,
        colour=discord.Colour.green())

    embed.set_author(name='🏓Ping Pong')
    embed.set_footer(text=f"Requested by {ctx.author}",
                     icon_url=ctx.author.avatar_url)

    await ctx.reply(embed=embed)
    print("Invitelink was sent")

  except:
    embed = discord.Embed(title="Something went wrong",
                              description='**Please try later again**',
                              timestamp=ctx.message.created_at,
                              colour=discord.Colour.red())

    embed.set_footer(
            text='🏓Ping Pong  •  Bot by shouzy',
            icon_url=bot.user.avatar_url
        )
    embed.set_author(name='❌Error')
    await ctx.reply(embed=embed)

@bot.command()
async def vote(ctx):
  try:
    embed = discord.Embed(
        title="",
        description=
        "**If you like the bot, you can vote for it on top.gg:**\n**__[Click here to vote!](https://top.gg/bot/831066967287791627/vote)__**",
        timestamp=ctx.message.created_at,
        colour=discord.Colour.green())

    embed.set_author(name='🏓Ping Pong')
    embed.set_footer(text=f"Requested by {ctx.author}",
                     icon_url=ctx.author.avatar_url)

    await ctx.reply(embed=embed)
    print("Votelink was sent")

  except:
    embed = discord.Embed(title="Something went wrong",
                              description='**Please try later again**',
                              timestamp=ctx.message.created_at,
                              colour=discord.Colour.red())

    embed.set_footer(
            text='🏓Ping Pong  •  Bot by shouzy',
            icon_url=bot.user.avatar_url
        )
    embed.set_author(name='❌Error')
    await ctx.reply(embed=embed)

@bot.command()
async def website(ctx):
  try:
    embed = discord.Embed(
        title="",
        description="**You can find the bots website by clicking the link:**\n**__https://ping-pong.shouzy.repl.co/__**",
        timestamp=ctx.message.created_at,
        colour=discord.Colour.green())

    embed.set_author(name='🏓Ping Pong')
    embed.set_footer(text=f"Requested by {ctx.author}",
                     icon_url=ctx.author.avatar_url)

    await ctx.reply(embed=embed)
    print("Websitelink was sent")

  except:
    embed = discord.Embed(title="Something went wrong",
                              description='**Please try later again**',
                              timestamp=ctx.message.created_at,
                              colour=discord.Colour.red())

    embed.set_footer(
            text='🏓Ping Pong  •  Bot by shouzy',
            icon_url=bot.user.avatar_url
        )
    embed.set_author(name='❌Error')
    await ctx.reply(embed=embed)

@bot.command()
async def code(ctx):
  try:
    embed = discord.Embed(
        title="",
        description=
        "**You can find the bots code by** **__[clicking here!](https://github.com/realshouzy/Ping-Pong-Bot)__**",
        timestamp=ctx.message.created_at,
        colour=discord.Colour.green())

    embed.set_author(name='🏓Ping Pong')
    embed.set_footer(text=f"Requested by {ctx.author}",
                     icon_url=ctx.author.avatar_url)

    await ctx.reply(embed=embed)
    print("Codelink was sent")

  except:
    embed = discord.Embed(title="Something went wrong",
                              description='**Please try later again**',
                              timestamp=ctx.message.created_at,
                              colour=discord.Colour.red())

    embed.set_footer(
            text='🏓Ping Pong  •  Bot by shouzy',
            icon_url=bot.user.avatar_url
        )
    embed.set_author(name='❌Error')
    await ctx.reply(embed=embed)


@bot.command()
async def help(ctx):
  try:
    embed = discord.Embed(
          title="Help",
          description=
          "This are all commands and their functions:",
          timestamp=ctx.message.created_at,
          colour=discord.Colour.green())

    embed.set_author(name='🏓Ping Pong')
    embed.add_field(name='``pp!help``', value='Shows this messages', inline=False)
    embed.add_field(name='``pp!info``', value='Shows information about the Bot', inline=False)
    embed.add_field(name='``pp!ping``', value='Shows the bots lantency', inline=False)
    embed.add_field(name='``pp!stats``', value='Shows the bots stats', inline=False)
    embed.add_field(name='``pp!code``', value='Shows the link to bots code', inline=False)
    embed.add_field(name='``pp!website``', value='Shows the link to bots website', inline=False)
    embed.add_field(name='``pp!invite``', value='Shows the bots invitelink', inline=False)
    embed.add_field(name='``pp!vote``', value='Shows the link where you can vote for the bot', inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}",
                      icon_url=ctx.author.avatar_url)
    
    await ctx.reply(embed=embed)
    print("Help was sent")
  
  except:
    embed = discord.Embed(title="Something went wrong",
                              description='**Please try later again**',
                              timestamp=ctx.message.created_at,
                              colour=discord.Colour.red())

    embed.set_footer(
            text='🏓Ping Pong  •  Bot by shouzy',
            icon_url=bot.user.avatar_url
        )
    embed.set_author(name='❌Error')
    await ctx.reply(embed=embed)

@bot.command()
async def info(ctx):
  try:
    embed = discord.Embed(
        title="",
        description=
        f'**So the main function of this bot is to write "Pong" when you write "Ping" (or "ping").\nIt also has a few commands with the prefix "pp!".**',
        timestamp=ctx.message.created_at,
        colour=discord.Colour.green())

    embed.set_author(name='🏓Ping Pong')
    embed.add_field(name="Ping:", value=f"``{round(bot.latency * 1000)}ms``", inline=False)
    embed.add_field(name="Stats:", value=f"{len(bot.guilds)} servers", inline=False)
    embed.add_field(name="Help command:", value="pp!help", inline=False)
    embed.add_field(name="Website:", value="__https://ping-pong.shouzy.repl.co/__", inline=False)
    embed.add_field(name="Invite:", value="__[Click here!](https://discord.com/api/oauth2/authorize?client_id=831066967287791627&permissions=3072&scope=bot)__", inline=False)
    embed.add_field(name="Code:", value="__[Click here!](https://github.com/realshouzy/Ping-Pong-Bot)__", inline=False)
    embed.add_field(name="Vote:", value="__[Click here!](https://top.gg/bot/831066967287791627/vote)__", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}",
                     icon_url=ctx.author.avatar_url)

    await ctx.reply(embed=embed)
    print("Codelink was sent")

  except:
    embed = discord.Embed(title="Something went wrong",
                              description='**Please try later again**',
                              timestamp=ctx.message.created_at,
                              colour=discord.Colour.red())

    embed.set_footer(
            text='🏓Ping Pong  •  Bot by shouzy',
            icon_url=bot.user.avatar_url
        )
    embed.set_author(name='❌Error')
    await ctx.reply(embed=embed)


keep_alive() # Executes the keep_alive function out of the keep_alive.py file
bot.run(os.getenv('TOKEN')) # Gets the bots token from the env file with help of os
