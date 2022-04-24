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

_cls()
load_dotenv()
Token = os.getenv('DISCORD_TOKEN')