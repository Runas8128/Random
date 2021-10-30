#-*- coding: utf-8 -*-

from rPingSlash import *

# Extra

@slash.slash(
	name='기만',
	description='기만이 감지되었습니다!'
)
async def sc_GIMAN(ctx):
	await ctx.send(f'삐빅! {ctx.author.display_name}님에 의해 기만이 감지되었습니다. 누가 기만함 ㅡㅡ')

@slash.slash(
	name='선동',
	description='선동 멈춰!'
)
async def sc_Sundong(ctx):
	await ctx.send('선동 멈춰!\n... 선동의 강도가 더욱 심해집니다')

@slash.slash(
	name='선',
	description='선넘내'
)
async def sc_Sun(ctx):
	await ctx.send('선넘내..')
