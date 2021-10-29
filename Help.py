from Common import *

def EmbedMaker(title, desc, ):
	pass

embedList = {
	'색': None,
	'color': None,
	
	'고스트핑': None,
	'일시정지': None,
	'재시작': None,
	'시간제한': None,
	
	'화이트': None,
	'화이트 추가': None,
	'화이트 제거': None,
	
	'latency': None,
	'giveAll': None,
	'db': None,
	'clearDB': None,
	
	'지워': None,
	'코드보기': None,
	'계산': None,
	'도움말': None
}

default = discord.Embed(
	title='랜덤핑 명령어',
	description='수많은 노가다가 들어간 도움말임미다 :carrot:'
)
default.add_field(
	name='랜덤핑 관련',
	value='고스트핑, 일시정지/재시작, 시간제한, 화이트리스트[화이트]'
)
default.add_field(
	name='기타 명령어',
	value='색깔[색, color], 코드보기, 계산, latency'
)
default.add_field(
	name='관리자/개발자용 명령어',
	value='일시정지/재시작, 시간제한, giveAll, 지워, clearDB'
)

@bot.command(name='도움말')
async def Help(ctx, *, cmd):
	cmd = cmd.replace('색깔', '색').replace('화이트리스트', '화이트')
	await ctx.send(embed=embedList.get(cmd, default))