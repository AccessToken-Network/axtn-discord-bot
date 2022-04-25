import os
import dotenv
import discord

from time import sleep
from discord import Intents
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot

from lib._sys import _sys
from lib._cls import _cls
from lib._cout import _cout
from lib._colors import BColors
from lib._debug import _print_debug
from lib._timestamp import *

try:
	_cls()
	load_dotenv()
	Token = os.getenv('DISCORD_TOKEN')
	prefix = 'axtn/'

	intents = discord.Intents.all()
	#client = discord.Client()
 
	bot = commands.Bot(command_prefix=prefix, intents=intents)

	_print_debug("AXTN: Configuration loaded")
	_print_debug("AXTN: Awaiting Actions")

	#listener on on_ready
	@bot.event
	async def on_ready():
		channel_bot = bot.get_channel(967532965636734996)
		await channel_bot.send(f"AXTN: Successfully Booted")

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

	bot.run(Token)
 
except KeyboardInterrupt:
    print(BColors.YELLOW + "\nProgram closed by user (CTRL+C)")
    exit()