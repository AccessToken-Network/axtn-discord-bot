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

	intents = Intents.all()
	activity = discord.Activity(name='TCP', type=discord.ActivityType.watching)
	Token = os.getenv(DISCORD_TOKEN)
	client = discord.Client(intents=intents)
	bot = Bot(command_prefix="$", intents=intents, activity=activity)

	_cout("AXTN: Configuration loaded")
	_cout("AXTN Awaiting Actions")

	#listener on on_ready
	@bot.event
	async def on_ready():
		channel_bot = bot.get_channel(967532965636734996)
		await channel_sudo.send(f"AXTN: Fuck You!")

	bot.run(Token)
 
except KeyboardInterrupt:
    print(BColors.YELLOW + "\nProgram closed by user (CTRL+C)")
    exit()