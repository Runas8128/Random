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
	system('cls')
	await ctx.message.add_reaction('👌')

@bot.command(name='기만')
async def GIMAN(ctx):
	await ctx.send("삐빅! 기만이 감지되었습니다")

@bot.command(name='db')
async def _db(ctx, *, var:str='All'):
	if var == 'All':
		if not db.keys():
			await ctx.send('Empty')
		else:
			for key in db.keys():
				s = f'{key}: {toGen(db[key])}'
				for i in range(0, len(s), 1000):
					await ctx.send(s[i:i+1000])
	elif var.lower() == 'key':
		await ctx.send(db.keys() or 'No key in DB')
	else:
		await ctx.send(db.get(var, 'Not in DB'))

@bot.command()
async def clearDB(ctx):
	if ctx.message.author.id == 449837429885763584:
		for key in db.keys():
			del db[key]
		await ctx.send('done')
	else:
		await ctx.send('개발자용 디버깅 명령어입니다')

@bot.command(name='코드보기')
async def ShowCode(ctx):
	await ctx.send('https://replit.com/@Runas8128/Random')

@bot.command(name='계산')
async def _eval(ctx, *expr):
	await ctx.send(f"계산값: {eval(' '.join(expr))}")
	