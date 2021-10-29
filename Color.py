#-*- coding: utf-8 -*-

from Common import *

@bot.command(name='색깔', aliases=['색', 'color'])
async def color(ctx, color):
	try:
		ch = color.replace('#', '').replace('0x', '')
		
		if ch.upper() in ['랜덤', 'RANDOM']:
			ch = hex(randCol())[2:]

		color = int(ch, 16)
		
		if 0x000000 <= color <= 0xffffff:
			embed = discord.Embed(title=f'#{ch}의 색을 알려드릴게요!', color=color)
			embed.add_field(name='Red',   value=f'{int(ch[0:2], 16)}')
			embed.add_field(name='Green', value=f'{int(ch[2:4], 16)}')
			embed.add_field(name='Blue',  value=f'{int(ch[4:6], 16)}')
			embed.add_field(name='Hex Value',  value=f'0x{ch}', inline=False)
			embed.set_image(url=f'https://www.colorbook.io/imagecreator.php?hex={ch}&width=200&height=200')
			await ctx.send(embed=embed)
		else:
			await ctx.send(f"{ch}이 올바른 16진수 색이 아닙니다")
	except:
		await ctx.send(f"{ch}이 16진수 아닌거같은데요..?")