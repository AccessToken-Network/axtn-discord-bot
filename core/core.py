import time
import datetime
clock_t0 = time.time()
t0 = time.process_time()

import os
import re
import sys
import uuid
import socket
import psutil
import dotenv
import random
import discord
import asyncio
import platform
import importlib
import sysconfig

from time import sleep
from asyncio import sleep
from discord import Intents
from datetime import datetime
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

from Notes import Notes
from helpers import getPath
from lib._sys import _sys
from lib._cls import _cls
from lib._cout import _cout
from _reboot import _reboot
from lib._timestamp import *
from lib._colors import BColors
from lib._debug import _print_debug

print(f"Successfully all imports imported")

try:
	_cls()
	load_dotenv()
	Token = os.getenv('DISCORD_TOKEN')
	
	print(f'Clock-t0: {clock_t0}, CPU-t0: {t0}')
		
	intents = discord.Intents.all()
	intents.typing = True
	intents.presences = True
	intents.members = True
	intents.voice_states = True
	prefix = '!'
	bot = commands.Bot(command_prefix=prefix, intents=intents)
	slash = SlashCommand(bot, sync_commands=True)
	bot.remove_command("help")
	_print_debug("AXTN: Configuration loaded")
		
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
		info['ram']=psutil.virtual_memory().percent
		print(f"System Info Loaded")
	except Exception as e:
		_print_debug(e)

	# -START- Categorizing ID's
	staff_channels = {
		"staff-chat" : 967573966313107456,
		"github" : 967575140701442088,
		"github-audit-log" : 967860766344626257,
		"audit-news" : 967532828940177448,
		"audit-log" : 967612494854123560,
		"join-log" : 967532895067590678,
		"leave-log": 967532916005543996,
		"bot" : 967532965636734996,
		"ot-notes" : 968551862716473466,
		"staff-nodes" : 968550803440816158,
		"super-audit" : 967974412760530954,
		"disboard" : 967617421726863421
	}

	guild_ids = {}
	guild_ids["axtn"] = 967529432745132082

	user_channels = {}
	user_channels["chat"] = 967529433433006173

	admin_list = {}
	admin_list["daemon"] = 250648489220898817
	admin_list["exodus"] = 644590202030915594

	# -END- Categorizing ID's
	# -START- Core Event Handling

	@bot.event
	async def on_ready():
		print(f"@bot.event on_ready() triggered!")
		channel_bot = bot.get_channel(staff_channels["bot"])
		now = time.localtime()
		current_time = time.strftime("%H:%M:%S", now)
		t1 = time.process_time()
		clock_t1 = time.time()
		cpu_result = t1 - t0
		clock_result = clock_t1 - clock_t0
		presence_name = f"Boot Time: {cpu_result:.4f}s"
		await channel_bot.send("```js\n"
					f"AXTN: Logged in on Server as {bot.user}!\n"
					f"Current Time Stamp	 	: [{current_time}]\n"
					f"----------------------------------------\n"
					f"Cpu Boot      |			: [{cpu_result:.4f}s]\n"
					f"Clock Boot    |			: [{clock_result:.4f}s]\n"
					f"Member Count  |			: [{len(bot.users)}]\n"
					f"Presence      |			: [{presence_name}]\n"
					f"System		|			: [{platform.system()}]\n"
					f"Release	   |			: [{info['platform-release']}]\n"
					f"Guilds		|			: [{len(bot.guilds)}]\n"
					f"Latency	   |			: [{bot.latency:.4f}]\n"
					f"Ram Usage	 |			: [{info['ram']}%]\n"
					f"SysConfig	 |			: [{sysconfig.get_platform()}]\n"
					f"Processor     |			: [{info['processor']}]\n"
					f"Architecture  |			: [{info['architecture']}]\n"
					f"-----------------------------------------\n"
					f"/git pull - for updates\n"
					"```")
		
		await bot.change_presence(activity=discord.Game(name=presence_name))
		try:
			_print_debug(f"AXTN: Logged in on Server as {bot.user}!")
			_print_debug(f"Current Time : [{current_time}]")
			_print_debug(f"CPU Boot Time : [{cpu_result:.4f}]")
			_print_debug(f"CLOCK Boot Time: [{clock_result:.4f}]")
			_print_debug(f"Member Count : [{len(bot.users)}]")
			_print_debug(f"Presence : [{presence_name}]")
			_print_debug(f"System : [{platform.system()}]")
			_print_debug(f"Guilds : [{len(bot.guilds)}]")
			_print_debug(f"Latency : [{bot.latency}]")
			_print_debug(f"Ram Usage : [{info['ram']}%]")
			_print_debug(f"SysConfig : [{sysconfig.get_platform()}]")
			_print_debug(f"Processor : [{info['processor']}]")
			_print_debug(f"Hostname : [{info['hostname']}]")
			_print_debug(f"Architecture : [{info['architecture']}]")
		except:
			_print_debug("AXTN: Couldn't load a string in axtn/info")

	@bot.command()
	async def help(ctx):
		print(f"@bot.command help() triggered!")
		await ctx.send("```py\n"
			"Notes System:\n"
			"\n"
			"  !notes                      - show list\n"
			"  !note <name>                - read note\n"
			"  !writenote <name> <content> - write <content> to note <name>, replacing.\n"
			"  !deletenote <name>          - delete note\n"
			"\n"
			"```")

	@bot.command()
	async def notes(ctx):
		if ctx.message.author.id == admin_list["daemon"] or ctx.message.author.id == admin_list["exodus"]:
    
		# TODO: Done! Make this an embed so commands to read each note can be embedded in
		#      	notes names (not sure that's possible)
		# TODO: Done!" Numerical Order"

			notes = Notes(getPath(ctx)).getAll()
			if notes:
				message = "Here are the notes available to read:\n\n"
				i = 0
				for name in notes.keys():
					i += 1
					message += f" {i} - {name} \n"

				message += "\nUse `!note <name>` to read a note!"
			else:
				message = "There are no notes! You can add one with `!writenote <name> <content>`."
			#message
			await ctx.send("```js\n" 
							f"{message}"
							"```")

	# TODO: multiple aliases for this command (readnote, getnote)

	@bot.command()
	async def note(ctx, name):
		if ctx.message.author.id == admin_list["daemon"] or ctx.message.author.id == admin_list["exodus"]:
			name = name.lower().replace(" ", "-")
			content = Notes(getPath(ctx)).get(name)
			if content:
				#content = content of message
				message = content
			else:
				message = f"Note “{name}” does not exist.\nUse `!notes` to get a list of available notes."
			#message = content
			await ctx.send("```js\n"
							f"{name}: \n"
							f"{message}"
							"```")


	@note.error
	async def note_error(ctx, error):
		await ctx.send("Usage: `!note <name>`\nUse `!notes` to get a list of available notes.")

	# TODO: multiple aliases for this command (addnote, createnote, newnote?)
	@bot.command()
	async def writenote(ctx, *, args):
		if ctx.message.author.id == admin_list["daemon"] or ctx.message.author.id == admin_list["exodus"]:
			try:
				(name, content) = args.split(maxsplit=1)
			except ValueError:
				await ctx.send("You must provide a content for the note.\nUsage: `!writenote <name> <content>`")
				return

			if not name.replace("-", "").replace("_", "").isalpha():
				await ctx.send("Note name can only contain letters, “-” and “_”.")
				return

			name = name.lower().replace(" ", "-")
			content = content.strip()
			if len(name) > 30:
				await ctx.send("Note name cannot exceed 30 characters.")
				return

			# Write notes to file
			notes = Notes(getPath(ctx))
			notes.write(name, content)
			print(f"Wrote note “{name}” on server “{ctx.guild.name}” ({ctx.guild.id}): {content}")

			await ctx.send(f"Successfully wrote note “{name}”, use `!note {name}` to read it!")


	@writenote.error
	async def writenote_error(ctx, error):
		print(f"Error on !writenote: {error}")
		await ctx.send("Usage: `!writenote <name> <content>`")


	@bot.command()
	async def deletenote(ctx, name):
		if ctx.message.author.id == admin_list["daemon"] or ctx.message.author.id == admin_list["exodus"]:
			name = name.lower().replace(" ", "-")
			notes = Notes(getPath(ctx))

			if not name.replace("-", "").replace("_", "").isalpha():
				await ctx.send("Note name can only contain letters, “-” and “_”.")
				return

			if notes.delete(name):
				message = f"Note “{name}” successfully deleted!"
				print(f"Deleted note “{name}” on server “{ctx.guild.name}” ({ctx.guild.id})")
			else:
				message = f"Note {name} does not exist.\nUse `!notes to get a list of available notes."

			await ctx.send(message)


	@deletenote.error
	async def deletenote_error(ctx, error):
		print(f"Error on !deletenote: {error}")
		await ctx.send("Usage: `!deletenote <name>`\nUse `!notes` to get a list of available notes.")

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
		try:
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
				elif message.content == "/init bump" or message.content == "/Init Bump":
					channel_disboard = bot.get_channel(staff_channels["disboard"])
					await asyncio.sleep(5)
					await channel_disboard.send("/bump")
					_print_debug("AXTN: /bump send in #Disboard, Timer now on 02:00 Hours!")
					await asyncio.sleep(7200)
	
			elif message.channel.id == user_channels["chat"]:
				if message.author.id == admin_list["daemon"] or message.author.id == admin_list["exodus"]:
					if message.content == "axtn/info":
						channel_chat = bot.get_channel(user_channels["chat"])
						now = time.localtime()
						current_time = time.strftime("%H:%M:%S", now)
						presence_name = f"Boot Time : {cpu_result:.4f}"
						await channel_chat.send("```js\n"
							f"AXTN: Logged in on Server as {bot.user}!\n"
							f"Current Time Stamp	 	: [{current_time}]\n"
							f"----------------------------------------\n"
							f"Cpu Boot      |			: [{cpu_result:.4f}s]\n"
							f"Clock Boot    |			: [{clock_result:.4f}s]\n"
							f"Member Count  |			: [{len(bot.users)}]\n"
							f"Presence      |			: [{presence_name}]\n"
							f"System		|			: [{platform.system()}]\n"
							f"Release	   |			: [{info['platform-release']}]\n"
							f"Guilds		|			: [{len(bot.guilds)}]\n"
							f"Latency	   |			: [{bot.latency:.4f}]\n"
							f"Ram Usage	 |			: [{info['ram']}%]\n"
							f"SysConfig	 |			: [{sysconfig.get_platform()}]\n"
							f"Processor     |			: [{info['processor']}]\n"
							f"Architecture  |			: [{info['architecture']}]\n"
							f"-----------------------------------------\n"
							f"/git pull - for updates\n"
							"```")
					if message.content == "/reboot" or message.content == "/Reboot":
						channel_chat = bot.get_channel(user_channels["chat"])
						await channel_chat.send(f"AXTN: Awaiting Reboot!")
						_print_debug(f"AXTN: Awaiting Reboot!")
						_reboot()
					if message.channel.id not in staff_channels:
						if message.content == "ping" or message.content == "Ping":
							channel_local = bot.get_channel(message.channel.id)
							await channel_local.send(f"AXTN: pong")
						elif message.content == "pong" or message.content == "Pong":
							channel_local = bot.get_channel(message.channel.id)
							await channel_local.send(f"AXTN: ping")
						else:
							channel_super_audit = bot.get_channel(staff_channels["super-audit"])
							await channel_super_audit.send(f"{message.author.name}: {message.content}")
		except Exception as exc:
			_print_debug(f"Error: in {exc}")

		await bot.process_commands(message)

	# -END- Core Event Handling

	bot.run(Token)

except KeyboardInterrupt:
	print(BColors.YELLOW + "\nProgram closed by user ( CTRL+C )")
	exit()