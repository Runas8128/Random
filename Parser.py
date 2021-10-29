#-*- coding: utf-8 -*-

from Common import *

class R_User:
	def __init__(self, Me:int):
		self.Me             = Me
		self.LastRandomPing = 0
		self.PingedLog      = []
		self.TotalPingCnt   = 0

class _Parser:
	def __init__(self, guildID: int):
		self.guild = guildID
		guildID = str(guildID)
		if guildID not in db:
			db[guildID] = {
				'ed': [], 'ing': [], 'time': [],
				'whiteList': [],
				'ghost': False, 'limit': 0, 'paused': False
			}
		self.db = db[guildID]

	def __eq__(self, item: int):
		return item == self.guild
	
	def addDB(self, key, val):
		self.db[key].insert(len(self.db[key]), val)
	
	def remDB(self, key, val):
		self.db[key].remove(val)

	def canPing(self, tarID: int, time: float):
		lrps = [
			self.db['time'][idx] \
			for idx in range(len(self.db['time'])) \
			if self.db['ing'][idx] == tarID
		]
		return (time - (lrps[-1] if lrps else 0)) > self.db['limit']

	def GhostPing(self, OnOff: bool):
		self.db['ghost'] = OnOff

	def Pause(self):
		self.db['paused'] = True
	def Resume(self):
		self.db['paused'] = False

	def AddWhiteList(self, idList: list):
		if 'whiteList' not in self.db:
			self.db['whiteList'] = []
		for id in idList:
			if id not in self.db['whiteList']:
				self.addDB('whiteList', id)
		return len(self.getDB('whiteList'))
	def RemWhiteList(self, idList: list):
		if 'whiteList' not in self.db:
			return 0
		for id in idList:
			if id in self.db['whiteList']:
				self.remDB('whiteList', id)
		return len(self.db['whiteList'])
	def SetWhiteList(self, idList: list):
		self.db['whiteList'] = idList
		return len(self.db['whiteList'])
	def GetWhiteList(self):
		return self.db['whiteList']

	def setTimeLimit(self, newLim: int):
		self.db['limit'] = newLim

	def getRandomPings(self, counts: int):
		tar = []
		tar = self.db.get('whiteList', []) or [
			user.id \
			for user in bot.get_guild(self.guild).members \
			if not user.bot
		]
		shuffle(tar)
		return None if counts > len(tar) else tar[:counts]

	def ping(self, pinging: int, pinged: int):
		self.addDB('ed', pinged)
		self.addDB('ing', pinging)
		self.addDB('time', int(time()))

		return f"<@!{pinged}>"

	def WhoCalledMe(self, pinged: int):
		now = time()
		sliceIdx = self.db['time'].index([x for x in self.db['time'] if now - x <= 3 * 60 * 60][0]) - 1
		
		if sliceIdx != -1:
			self.db['ed'] = self.db['ed'][sliceIdx:]
			self.db['ing'] = self.db['ing'][sliceIdx:]
			self.db['time'] = self.db['time'][sliceIdx:]
		
		return ', '.join([
			bot.get_user(self.db['ing'][idx]).display_name \
			for idx in range(len(self.db['ing'])) \
			if self.db['ed'][idx] == pinged
		])
		
	def HowManyCalledMe(self, pinged: int):
		now = time()
		sliceIdx = self.db['time'].index([x for x in self.db['time'] if now - x <= 3 * 60 * 60][0]) - 1
		
		if sliceIdx != -1:
			self.db['ed'] = self.db['ed'][sliceIdx:]
			self.db['ing'] = self.db['ing'][sliceIdx:]
			self.db['time'] = self.db['time'][sliceIdx:]
		
		return self.db['ed'].count(pinged)

class ParserWrapper:
	def __init__(self):
		self.dict = {}

	def get(self, guildID: int):
		if guildID not in self.dict:
			self.dict[guildID] = _Parser(guildID)
		return self.dict[guildID]

Parser = ParserWrapper()

def AdaptRandomPing(message, time):
	msg = message.content
	atr = message.author
	gd  = message.guild

	ss = msg.split()
	parserObj = Parser.get(gd.id)

	if parserObj.db['paused']:
		return '랜덤핑 정지돼있는데요', False

	if parserObj.canPing(atr.id, time):
		isNTimes = len(ss) == 2 and ss[1].isdigit()
		pingTars = parserObj.getRandomPings(
			int(ss[1]) if isNTimes \
			else msg.count('<@!810020540064333834>') +\
				msg.count('<@810020540064333834>')
		)

		if pingTars == None:
			return '???: 설마 이만큼 랜덤핑을 박겠어 아 ㅋㅋ', False
		
		pings = [parserObj.ping(atr.id, user) for user in pingTars]
		
		if isNTimes:
			return ' '.join(pings), parserObj.db['ghost']
		else:
			while '<@!810020540064333834>' in msg:
				msg = msg.replace('<@!810020540064333834>', pings.pop(), 1)
			while '<@810020540064333834>' in msg:
				msg = msg.replace('<@810020540064333834>', pings.pop(), 1)
			return msg, parserObj.db['ghost']
	else:
		return '시간제한!', False