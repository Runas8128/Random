#-*- coding: utf-8 -*-

from rPingCmd import *
from Color import *

# Commands

@bot.command()
async def latency(ctx):
	await ctx.send(f'{round(bot.latency, 2)}ms')

@bot.command()
async def giveAll(ctx, role: discord.Role):
	if ctx.message.author.id != 449837429885763584 and \
		not ctx.message.author.guild_permissions.administrator:
		await ctx.send('관리자/개발자 전용 명령어입니다')
		return

	msg = await ctx.send(f'모두에게 {role.name} 역할을 주는 중...')
	for user in [user for user in ctx.guild.members if not user.bot]:
		try:
			await user.add_roles(role)
		except:
			await ctx.send(f"{user.display_name} 역할 주기 실패: 권한 부족")
	await msg.delete()
	await ctx.send(f'모두에게 {role.name} 역할을 주었습니다!')

@bot.command()
async def cls(ctx):
	system('clear') # for unix
	await ctx.message.add_reaction('👌')

@bot.command(name='기만')
async def GIMAN(ctx):
	await ctx.send("삐빅! 기만이 감지되었습니다")

@bot.command(name='코드보기')
async def ShowCode(ctx):
	await ctx.send('https://github.com/Runas8128/Random')
