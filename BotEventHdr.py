#-*- coding: utf-8 -*-

from Commands import *
from Slashes  import *
from random import random

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
async def on_message(message: discord.Message):
	if message.type == discord.MessageType.pins_add:
		await message.delete()
		return
	
	# 일단 봇 거름
	if message.author.bot:
		return
	
	# 기본적 변수 선언
	msg = message.content
	ch = message.channel

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
		await message.add_reaction('<:brilliant:864664970799874120>')
	if '?' in msg:
		if '??' in msg:
			if random()<0.96:
				await message.add_reaction('<:blunder:864664935631683614>')
			else:
				await ch.send('<:mia:882839095653568533>')
		if msg.count('?!') == 1:
			await message.add_reaction('<:inaccuracy:864664944644718653>')
		if msg == '?':
			if random()<0.98:
				await message.add_reaction('<:mistake:864664953537167380>')
			else:
				await ch.send('<:mia:882839095653568533>')

	if ('원신' in msg) and (random()<0.5):
		await message.add_reaction('<:genshin:864823001869451284>')
	if (('저런' in msg) or ('절너' in msg)) and (random()<0.1):
		await ch.send('<:wjfsj:902174408448286741>')
	if '흥.' == msg and ch.id == 864541135585673228:
		await ch.send('https://cdn.discordapp.com/attachments/853207469987594283/907241951273836574/a83bc7fe05d7b6ad.jpg')

	# 랜덤핑 적용
	if '<@!810020540064333834>' in msg or '<@810020540064333834>' in msg:
		await ch.trigger_typing()
		await ch.send(AdaptRandomPing(message, time()))

	# 반사
	elif msg.replace('!', '') == '<@449837429885763584>' and ch.id == 871408004875059200:
		await ch.send(message.author.mention)

	# 핑크색 양 스폰
	elif random() < 0.001558:
		await ch.send('https://cdn.discordapp.com/attachments/903552936511148082/903571862884339712/Pink_Sheep_JE4__.png')

	# 커맨드 실행
	else:
		await bot.process_commands(message)

# :pin: 반응 달렸을때 고정
@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    if payload.emoji == '📌':
        ch: discord.TextChannel = bot.get_channel(payload.channel_id)
        msg = await ch.fetch_message(payload.message_id)
        await msg.pin()

@bot.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    if payload.emoji == '📌':
        ch: discord.TextChannel = bot.get_channel(payload.channel_id)
        msg = await ch.fetch_message(payload.message_id)
        await msg.unpin()

@bot.event
async def on_command_error(ctx: commands.Context, error: discord.DiscordException):
    if isinstance(error, commands.CommandNotFound):
        return
        
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("관리자 전용 명령어입니다!")
        return
        
    elif isinstance(error, commands.NotOwner):
        await ctx.send("개발자 전용 명령어입니다!")
        return
        
    elif isinstance(error, commands.errors.UserNotFound):
        await ctx.send("유저는 멘션으로 전달해주세요!")
        return
        
    elif isinstance(error, discord.errors.HTTPException):
        if error.code != 429:   # Too Many Requests
            return

    embed = discord.Embed(title="Bug report", timestamp=now())
    embed.add_field(name="error string", value=str(error), inline=False)
    embed.add_field(name="error invoked with", value=ctx.invoked_with, inline=False)
    embed.add_field(name="full context", value=ctx.message.content, inline=False)
    
    await bot.get_channel(863719856061939723).send(embed=embed)
