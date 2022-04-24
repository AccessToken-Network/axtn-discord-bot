import os
import dotenv
import discord

from time import sleep
from discord import Intents
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot

from lib._sys import *
from lib._cls import *
from lib._cout import *
from lib._colors import BColors
from lib._debug import *
from lib._timestamp import *

try:
	_cls()
	load_dotenv()
	Token = os.getenv('DISCORD_TOKEN')

	intents = Intents.all()
	activity = discord.Activity(name='TCP', type=discord.ActivityType.watching)
	bot = Bot(command_prefix="$", intents=intents, activity=activity)
	client = discord.Client(intents=intents)

	_cout("AXTN: Configuration loaded")
	_cout("AXTN Awaiting Actions")

	#listener on on_ready
	@bot.event
	async def on_ready():
		channel_sudo = bot.get_channel(967532965636734996)
		await channel_sudo.send(f"AXTN: Successfully Booted")

	bot.run(TOKEN)
 
except KeyboardInterrupt:
    print(BColors.YELLOW + "\nProgram closed by user (CTRL+C)")
    exit()