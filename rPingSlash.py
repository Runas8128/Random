#-*- coding: utf-8 -*-

from Parser import *

# Utilities

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
