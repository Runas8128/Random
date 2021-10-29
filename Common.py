#-*- coding: utf-8 -*-

# Imports

from os import listdir, path, getenv, system

from   random    import shuffle, random
from   time      import time
import re
from   pprint    import pp

import discord
from   discord.ext import tasks, commands
from   discord_slash import SlashCommand
from   discord_slash.utils.manage_commands import create_option, create_choice

db = {}

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
	return tmp