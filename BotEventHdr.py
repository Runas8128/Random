#-*- coding: utf-8 -*-

from Commands import *
from Slashes  import *

# 봇이 켜졌을때 실행

@bot.event
async def on_ready():
	# 봇의 활동상태 바꾸기 
	# Playing with Runas를 노린거라 영문판 기준임
	await bot.change_presence(
		activity=discord.Game(name="with Runas")
	)
	
	# 콘솔에 켜진 표시
	print('Random ON')

# 메시지 받았을 때 실행

@bot.event
async def on_message(message):
	if message.type == discord.MessageType.pins_add:
		await message.delete()
		return
	
	# 일단 봇 거름
	if message.author.bot:
		return
	
	# 기본적 변수 선언
	msg = message.content
	ch = message.channel
	name = message.author.display_name

	# 짤방 처리
	if (ch.type != discord.ChannelType.private) and \
		ch.name == "짤" and \
		not (
			len(message.attachments) > 0 or
			(
				(
					'https://twitter.com/' in msg or
					'https://youtu.be/' in msg or
					'https://www.youtube.com/watch?v=' in msg or
					'https://media.discordapp.net/' in msg or
					'https://www.instagram.com/' in msg
				) and
				not re.search(r'[가-힣]', msg)
			)
		):
		await message.delete()
		return

	# 키워드에 반응
	if '!!' in msg:
		await message.add_reaction('<:brilliant:840225769632301066>')
	if '?' in msg:
		if '??' in msg:
			await message.add_reaction('<:blunder:840225769476849674>')
		if msg.count('?!') == 1:
			await message.add_reaction('<:inaccuracy:840225769665724436>')
		if msg == '?':
			await message.add_reaction('<:mistake:840225769656942652>')

	# 랜덤핑 적용
	if '<@!810020540064333834>' in msg or '<@810020540064333834>' in msg:
		await ch.trigger_typing()
		s = AdaptRandomPing(message, time())
		_Msg = await ch.send(s[0])
		if s[1]:
			await _Msg.delete()
	
	# 핑 목록
	elif msg == '누가 나 핑함':
		await ch.trigger_typing()
		s = Parser.get(ch.guild.id).WhoCalledMe(message.author.id)
		if s:
			await ch.send(f'{name}님은 {s} 이 분들에게 랜덤핑 당했습니다!')
		else:
			await ch.send(f'{name}님은 최근 3시간동안 랜덤핑 당하지 않았습니다!')
	
	# 핑 카운트
	elif msg == '나 얼마나 핑당함':
		await ch.trigger_typing()
		cnt = Parser.get(ch.guild.id).HowManyCalledMe(message.author.id)
		await ch.send(f'{name}님은 최근 3시간동안 {cnt}번 랜덤핑 당했습니다!')

	# 반사
	elif msg.replace('!', '') == '<@449837429885763584>' and ch.id == 871408004875059200:
		await ch.send(message.author.mention)

	# 커맨드 실행
	else:
		await bot.process_commands(message)

# :pin: 반응 달렸을때 고정
@bot.event
async def on_reaction_add(reaction, user):
	try:
		if reaction.emoji == '📌':
			await reaction.message.pin()
	except discord.errors.HTTPException as E:
		await reaction.message.channel.send(E, delete_after=5)
		await reaction.message.clear_reaction('📌')
		
@bot.event
async def on_reaction_remove(reaction, user):
	if reaction.emoji == '📌':
		await reaction.message.unpin()

# '!아무거나' 이런식으로 했을때 나오는 잡오류 무시
@bot.event
async def on_command_error(ctx, error):
	if not isinstance(error, commands.CommandNotFound):
		raise error

# 이 파일 주석만 해도 귀찮아서 나머지 안함 엌ㅋㅋ