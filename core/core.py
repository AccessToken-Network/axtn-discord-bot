import os
import dotenv
import discord
import asyncio
import time, datetime


from time import sleep
from discord import Intents
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from discord_slash import SlashCommand

from lib._sys import _sys
from lib._cls import _cls
from lib._cout import _cout
from _reboot import _reboot
from lib._colors import BColors
from lib._debug import _print_debug
from lib._timestamp import *

try:
    
	_cls()
 
	# Intent Setting
	intents = discord.Intents.all()
	intents.typing = True
	intents.presences = True
	intents.members = True
	intents.voice_states = True
 
	load_dotenv()
	Token = os.getenv('DISCORD_TOKEN')
	prefix = '/'
	
	# setting up the bot, with its discritpion etc.
	bot = commands.Bot(command_prefix=prefix, intents=intents)
	slash = SlashCommand(bot, sync_commands=True)

	# deleting default help comand
	bot.remove_command("help")

	_print_debug("AXTN: Configuration loaded")
	_print_debug("AXTN: Awaiting Actions")

	staff_channels = {
		"staff-chat" : 967573966313107456,
		"github" : 967575140701442088,
		"github-audit-log" : 967860766344626257,
		"audit-news" : 967532828940177448,
		"audit-log" : 967612494854123560,
		"super-audit" : 967974412760530954,
		"disboard" : 967617421726863421,
		"join-log" : 967532895067590678,
		"leave-log": 967532916005543996,
		"bot" : 967532965636734996,
		"ot-notes" : 968551862716473466,
		"staff-nodes" : 968550803440816158
	}

	#boot activity event
	@bot.event
	async def on_ready():
		channel_bot = bot.get_channel(967532965636734996)
		await channel_bot.send(f"AXTN: Successfully Booted")
		await bot.change_presence(activity=discord.Game(name="localhost | exploring"))
		_print_debug(f"AXTN: Logged in on Server as {bot.user}!")

	@bot.event
	async def on_member_join(member):
		channel_bot = bot.get_channel(967532895067590678)
		await channel_bot.send(f"AXTN Admin Log: {member} joined!")
		_print_debug(f"AXTN: {member} joined!")

	@bot.event
	async def on_member_remove(member):
		channel_bot = bot.get_channel(967532916005543996)
		await channel_bot.send(f"AXTN Admin Log: {member} left!")
		_print_debug(f"AXTN: {member} joined!")

	@bot.event
	async def on_message(message):
		if message.channel.id == staff_channels["bot"]:
			if message.content == "reboot" or message.content == "Reboot":
				channel_bot = bot.get_channel(staff_channels["bot"])
				await channel_bot.send(f"AXTN: Awaiting Reboot!")
				_print_debug(f"AXTN: Awaiting Reboot!")
				_reboot()
     
		if message.channel.id != staff_channels["staff-chat"] and message.channel.id != staff_channels["github"] and message.channel.id != staff_channels["github-audit-log"] and message.channel.id != staff_channels["audit-news"]:
			if message.channel.id != staff_channels["audit-log"] and message.channel.id != staff_channels["super-audit"] and message.channel.id != staff_channels["disboard"] and message.channel.id != staff_channels["join-log"]:
				if message.channel.id != staff_channels["leave-log"] and message.channel.id != staff_channels["bot"] and message.channel.id != staff_channels["ot-notes"] and message.channel.id != staff_channels["staff-nodes"]:
					if message.content == "ping" or message.content == "Ping":
						channel_local = bot.get_channel(message.channel.id)
						await channel_local.send(f"AXTN: pong")
					elif message.content == "pong" or message.content == "Pong":
						channel_local = bot.get_channel(message.channel.id)
						await channel_local.send(f"AXTN: ping")
					else:
						channel_super_audit = bot.get_channel(staff_channels["super-audit"])
						await channel_super_audit.send(f"{message.author.name}: {message.content}")
  
	bot.run(Token)
 
except KeyboardInterrupt:
    print(BColors.YELLOW + "\nProgram closed by user ( CTRL+C )")
    exit()