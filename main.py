from BotEventHdr import *
from keep_alive import keep_alive
keep_alive()

# Runner

try:
	if __name__ == '__main__':
		bot.run(getenv('TOKEN'))
except RuntimeError:
	bot.logout()
except discord.errors.HTTPException as E:
	system('clear')

	sec = int(E.response.headers['Retry-After'])
	h = sec // 3600
	sec -= h * 3600
	m = sec // 60
	sec -= m * 60
	s = sec

	print(f"Retry-After: {h}h {m}m {s}s")