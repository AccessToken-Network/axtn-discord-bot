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
from lib._debug import *

_cls()
load_dotenv()
Token = os.getenv('DISCORD_TOKEN')

intents = Intents.all()
activity = discord.Activity(name='TCP', type=discord.ActivityType.watching)
bot = Bot(command_prefix="$", intents=intents, activity=activity)
client = discord.Client(intents=intents)

_cout("AXTN: Configuration loaded")
_cout("AXTN Awaiting Actions")


