#-*- coding: utf-8 -*-

# Imports

from os import listdir, path, getenv, system

from   random    import shuffle, random
from   time      import time
import re
from   pprint    import pp

# from replit import db
# from replit.database.database import ObservedList, OvservedDict

import discord
from   discord.ext import tasks, commands
from   discord_slash import SlashCommand
from   discord_slash.utils.manage_commands import create_option, create_choice

# Pre-settings

# bot instance: core of bot
bot = commands.Bot(
	command_prefix=['!'],
	help_command=None,
	intents=discord.Intents.all()
)

slash = SlashCommand(bot, sync_commands=True)

# Other

def randCol():
	return int(random() * 0xffffff)

def toGen(tmp):
	'''
	if 'ObservedList' in globals().keys():
		if isinstance(tmp, ObservedList):
			return list(tmp)
		elif isinstance(tmp, ObservedDict):
			return dict(tmp)
	'''
	return tmp