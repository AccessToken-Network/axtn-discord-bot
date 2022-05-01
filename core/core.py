import time
boot = time.process_time()

import os
import re
import sys
import uuid
import socket
import psutil
import dotenv
import discord
import asyncio
import platform
import datetime
import sysconfig

from time import sleep
from discord import Intents
from datetime import datetime
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

from lib._sys import _sys
from lib._cls import _cls
from lib._cout import _cout
from _reboot import _reboot
from lib._timestamp import *
from lib._colors import BColors
from lib._debug import _print_debug

try:
    
    try:
		_cls()
		_cout(boot)
		load_dotenv()
 
		intents = discord.Intents.all()
		intents.typing = True
		intents.presences = True
		intents.members = True
		intents.voice_states = True
		Token = os.getenv('DISCORD_TOKEN')
		prefix = '/'
		bot = commands.Bot(command_prefix=prefix, intents=intents)
		slash = SlashCommand(bot, sync_commands=True)
		bot.remove_command("help")
		_print_debug("AXTN: Configuration loaded")
	except:
		_print_debug("AXTN: Couldn't load Configuration in core.py")

	try:
		info={}
		info['platform']=platform.system()
		info['platform-release']=platform.release()
		info['platform-version']=platform.version()
		info['architecture']=platform.machine()
		info['hostname']=socket.gethostname()
		info['ip-address']=socket.gethostbyname(socket.gethostname())
		info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
		info['processor']=platform.processor()
		info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
	except Exception as e:
		_print_debug(e)
		
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

	user_channels = {
		"chat" : 967529433433006173
	}

	@bot.event
	async def on_ready():
		channel_bot = bot.get_channel(967532965636734996)
		now = time.localtime()
		current_time = time.strftime("%H:%M:%S", now)
		presence_name = f"Boot Time: {(time.process_time() - boot):.4f}s"
		await channel_bot.send("```js\n"
                	f"AXTN: Logged in on Server as {bot.user}!\n"
                	f"Current Time Stamp	 	: [{current_time}]\n"
                	f"----------------------------------------\n"
                	f"Boot Time     |			: [{(time.process_time() - boot):.4f}]\n"
					f"Member Count  |			: [{len(bot.users)}]\n"
        			f"Presence      |			: [{presence_name}]\n"
					f"System		|			: [{platform.system()}]\n"
					f"Release	   |			: [{info['platform-release']}]\n"
					f"Guilds		|			: [{len(bot.guilds)}]\n"
					f"Latency	   |			: [{bot.latency:.4f}]\n"
					f"Ram Usage	 |			: [{info['ram']}]\n"
					f"SysConfig	 |			: [{sysconfig.get_platform()}]\n"
					f"Processor     |			: [{info['processor']}]\n"
					f"Hostname      |			: [{info['hostname']}]\n"
					f"Architecture  |			: [{info['architecture']}]\n"
					f"-----------------------------------------\n"
					f"/git pull - test message\n"
                   	"```")
  
		await bot.change_presence(activity=discord.Game(name=presence_name))
		_print_debug(f"AXTN: Logged in on Server as {bot.user}!")
		_print_debug(f"Current Time : [{current_time}]")
		_print_debug(f"Boot Time : [{time.process_time() - boot}]")
		_print_debug(f"Member Count : [{len(bot.users)}]")
		_print_debug(f"Presence : [{presence_name}]")
		_print_debug(f"System : [{platform.system()}]")
		_print_debug(f"Guilds : [{len(bot.guilds)}]")
		_print_debug(f"Latency : [{bot.latency}]")
		_print_debug(f"Ram Usage : [{info['ram']} MB]")
		_print_debug(f"SysConfig : [{sysconfig.get_platform()}]")

	@bot.event
	async def on_member_join(member):
		channel_bot = bot.get_channel(967532895067590678)
		await channel_bot.send(f"AXTN Admin Log: {member} joined!")
		_print_debug(f"AXTN: {member} joined!")

	@bot.event
	async def on_member_remove(member):
		channel_bot = bot.get_channel(967532916005543996)
		await channel_bot.send(f"AXTN Admin Log: {member} left!")
		_print_debug(f"AXTN: {member} joined !")

	@bot.event
	async def on_message(message):
		if message.channel.id == staff_channels["bot"]:
			if message.content == "/reboot" or message.content == "/Reboot":
				channel_bot = bot.get_channel(staff_channels["bot"])
				await channel_bot.send(f"AXTN: Awaiting Reboot!")
				_print_debug(f"AXTN: Awaiting Reboot!")
				_reboot()
			elif message.content == "/exit" or message.content == "/close":
				channel_bot = bot.get_channel(staff_channels["bot"])
				await channel_bot.send(f"AXTN: Awaiting Shutdown!")
				_print_debug(f"AXTN: Awaiting Shutdown!")
				sys.exit()
			elif message.content == "/git pull" or message.content == "/gpull":
				channel_bot = bot.get_channel(staff_channels["bot"])
				await channel_bot.send(f"AXTN: Pulling!")
				_print_debug(f"AXTN: Pulling!")
				_sys("python3 core/gpull.py")
    
		elif message.channel.id == user_channels["chat"]:
			if message.author.id == 250648489220898817 or message.author.id == 644590202030915594:
				if message.content == "axtn/info":
					channel_chat = bot.get_channel(user_channels["chat"])
					now = time.localtime()
					current_time = time.strftime("%H:%M:%S", now)
					presence_name = f"Boot Time : {(time.process_time() - boot):.4f}"
					await channel_chat.send("```js\n"
                	f"AXTN: Logged in on Server as {bot.user}!\n"
                	f"Current Time Stamp	 	: [{current_time}]\n"
                	f"----------------------------------------\n"
                	f"Boot Time     |			: [{(time.process_time() - boot):.4f}]\n"
					f"Member Count  |			: [{len(bot.users)}]\n"
        			f"Presence      |			: [{presence_name}]\n"
					f"System		|			: [{platform.system()}]\n"
					f"Release	   |			: [{info['platform-release']}]\n"
					f"Guilds		|			: [{len(bot.guilds)}]\n"
					f"Latency	   |			: [{bot.latency:.4f}]\n"
					f"Ram Usage	 |			: [{info['ram']}]\n"
					f"SysConfig	 |			: [{sysconfig.get_platform()}]\n"
					f"Processor     |			: [{info['processor']}]\n"
					f"Hostname      |			: [{info['hostname']}]\n"
					f"Architecture  |			: [{info['architecture']}]\n"
					f"-----------------------------------------\n"
					f"/git pull - for updates\n"
                   	"```")
				if message.content == "/reboot" or message.content == "/Reboot":
					channel_chat = bot.get_channel(user_channels["chat"])
					await channel_chat.send(f"AXTN: Awaiting Reboot!")
					_print_debug(f"AXTN: Awaiting Reboot!")
					_reboot()
     
		elif message.channel.id != staff_channels["staff-chat"] and message.channel.id != staff_channels["github"] and message.channel.id != staff_channels["github-audit-log"] and message.channel.id != staff_channels["audit-news"]:
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