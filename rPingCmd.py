#-*- coding: utf-8 -*-

from Parser import *

@bot.command(name='일시정지')
async def RD_Pause(ctx):
	if ctx.message.author.id == 449837429885763584:
		Parser.get(ctx.guild.id).Pause()
		await ctx.send('랜덤핑을 정지했습니다!')
	else:
		await ctx.send('제작자 전용이래요')

@bot.command(name='재시작')
async def RD_Restart(ctx):
	if ctx.message.author.id == 449837429885763584:
		Parser.get(ctx.guild.id).Resume()
		await ctx.send('랜덤핑을 다시 시작할게요')
	else:
		await ctx.send('제작자 전용이래요')

@bot.group(name='화이트', aliases=['화이트리스트', '화리'])
async def RD_WhiteList(ctx):
	if ctx.invoked_subcommand == None:
		parser = Parser.get(ctx.guild.id)
		ls = parser.GetWhiteList()
		if len(ls) == 0:
			await ctx.send(f"현재 {ctx.guild.name}의 화이트리스트가 비어있습니다. 랜덤핑시 서버의 모든 유저가 대상이 되니 주의해주세요!")
		else:
			async with ctx.typing():
				s = ''
				for _id in ls:
					try:
						tmp = (await ctx.guild.fetch_member(_id)).display_name
						s += ('\n' + tmp)
					except discord.errors.NotFound:
						parser.RemWhiteList([_id])
				await ctx.send(f"현재 {ctx.guild.name}의 화이트리스트(총 {len(ls)}명)```{s}```")

@RD_WhiteList.command(name='추가')
async def RD_WhiteList_Add(ctx):
	async with ctx.typing():
		ls = [user.id for user in ctx.message.mentions if not user.bot]
		tot = Parser.get(ctx.guild.id).AddWhiteList(ls)
	await ctx.send(f"{ctx.guild.name}의 화이트리스트에 총 {len(ls)}명을 추가했습니다! (총 {tot}명)")

@RD_WhiteList.command(name='제거')
async def RD_WhiteList_Rem(ctx):
	async with ctx.typing():
		ls = [user.id for user in ctx.message.mentions]
		tot = Parser.get(ctx.guild.id).RemWhiteList(ls)
		await ctx.send(f"{ctx.guild.name}의 화이트리스트에 총 {len(ls)}명을 제거했습니다! (총 {tot}명)")

@bot.command(name='시간제한')
async def RD_TimeLimiter(ctx, seconds: int = None):
	async with ctx.typing():
		if seconds == None:
			await ctx.send(f"현재 시간제한은 {Parser.get(ctx.guild.id).db['limit']}초 입니다!")

		elif ctx.message.author.id == 449837429885763584:
			if not isinstance(seconds, int):
				await ctx.send('정수를 좀 입력해봐요..')
			else:
				if seconds < 0:
					seconds = 0
				Parser.get(ctx.guild.id).setTimeLimit(seconds)
				await ctx.message.add_reaction('👌')	
		else:
			await ctx.send('제작자 전용이래요')