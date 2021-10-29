#-*- coding: utf-8 -*-

from Parser import *

# Utilities

@slash.slash(
	name='고스트핑',
	description='고스트핑을 켜거나 끕니다',
	options=[
		create_option(
			name="nf",
			description="고스트핑을 켤지 끌지 지정합니다",
			option_type=3,
			required=True,
			choices=[
				create_choice(name="켜기", value="On"),
				create_choice(name="끄기", value="Off"),
				create_choice(name="보기", value="View")
			]
		)
	]
)
async def sc_GhostPing(ctx, nf: str):
	guild = Parser.get(ctx.guild.id)
	if nf == 'On':
		guild.GhostPing(True)
		await ctx.send("고스트핑을 켰어요!")
	elif nf == 'Off':
		guild.GhostPing(False)
		await ctx.send("고스트핑을 껐어요!")
	elif nf == 'View':
		await ctx.send(f"지금 고스트핑은 {'켜' if guild.db['ghost'] else '꺼'}져있어요")
	else:
		await ctx.send('옵션이 있지 않나요..?')

@slash.slash(
	name='시간제한',
	description='랜덤핑 쿨타임을 정합니다',
	options=[
		create_option(
			name='tl',
			description='쿨타임',
			option_type=4,
			required=False
		)
	]
)
async def sc_TimeLimiter(ctx, tl: int = None):
	if tl == None:
		await ctx.send(f"현재 시간제한은 {Parser.get(ctx.guild.id).db['limit']}초 입니다!")
	elif isinstance(tl, int):
		if ctx.author.guild_permissions.administrator\
			or ctx.author.id == 449837429885763584:
			if tl < 0:
				tl = 0
			Parser.get(ctx.guild.id).setTimeLimit(tl)
			await ctx.send(f'시간제한을 {tl}초로 지정했어요!')
		else:
			await ctx.send('관리자 전용입니다')
	else:
		await ctx.send('시간제한은 정수로만 지정할 수 있습니다!')

@slash.slash(
	name='핑목록',
	description='최근 3시간동안 나를 핑한 사람을 알려줍니다'
)
async def sc_WhoPingedMe(ctx):
	s = Parser.get(ctx.guild.id).WhoCalledMe(ctx.author.id)
	if s:
		await ctx.send(f'{ctx.author.display_name}님은 {s} 이 분들에게 랜덤핑 당했습니다!')
	else:
		await ctx.send(f'{ctx.author.display_name}님은 최근 3시간동안 랜덤핑 당하지 않았습니다!')

@slash.slash(
	name='핑카운트',
	description='최근 3시간동안 핑당한 횟수를 알려줍니다'
)
async def sc_HowMuchPinged(ctx):
	cnt = Parser.get(ctx.guild.id).HowManyCalledMe(ctx.author.id)
	await ctx.send(f'{ctx.author.display_name}님은 최근 3시간동안 {cnt}번 랜덤핑 당했습니다!')
