import requests
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from pymongo import MongoClient

token = ''
bot = commands.Bot(command_prefix='')
@bot.remove_command( 'help' )

@bot.event
async def on_ready():
	print("бот работает")
	await bot.change_presence(status = discord.Status.idle, activity= discord.Activity(name=f'на бананы. | аркадий', type= discord.ActivityType.watching))

@bot.command()
async def аркадий(ctx, *, atext):
	if 'хелпай' in ctx.message.content:
		embed = discord.Embed(title="Мои команды", description="Я кста бананы люблю")
		embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
		embed.add_field(name="аркадий (ваш вопрос)", value="Поговорить со мной")
		embed.add_field(name="аркадий статы", value="Увидеть мою статистику")
		embed.add_field(name="аркадий хелпай", value="Увидеть список моих команд")
		embed.add_field(name='Добавить меня', value='[Нажми](https://discord.com/api/oauth2/authorize?client_id=950779877378887760&permissions=414464677888&scope=bot)')
		await ctx.reply(embed=embed)
	elif 'статы' in ctx.message.content:
	#guilds = await bot.fetch_guilds(limit = None).flatten()
		members = 0
		for guild in bot.guilds:
			members = members + guild.member_count
		embed = discord.Embed(title='Статистика Аркадия', description="А почему не бананов..?")
		embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
		embed.add_field(name='Сервера:', value=f'{str(len(bot.guilds))}')
		embed.add_field(name='Сумма участников', value =f'{str(members)}')
		embed.add_field(name='Добавить меня', value='[Нажми](https://discord.com/api/oauth2/authorize?client_id=950779877378887760&permissions=414464677888&scope=bot)')
		await ctx.send(embed=embed)
	else:
		
		text = str(atext)
		payload = {
		'uid': "8cb6c95f-725d-4c89-b9bd-7af4f516e48b",
		'bot': "main",
		'text': text}

		response = requests.post('https://xu.su/api/send', data=payload)
		soup = BeautifulSoup(response.content, 'html.parser')
		res = str(soup).replace('''{
		"ok": true,
		"text": "''', '').replace('''",
		"uid": "8cb6c95f-725d-4c89-b9bd-7af4f516e48b"
		}''', '')
		res = res.split(': "', 1)[1].lstrip()
		res = res.split('"')[0]
		print(f"Сервер: {ctx.guild.name}" + f"\nОтвет бота : {res}" + "\nАргумент : " + str(atext) + f"\nАвтор аргумента : { ctx.author.display_name }\n \n")

		res = res.lower()

		if 'xu su' in res:
			
			res = res.replace('xu su', 'BenBot')
			await ctx.reply(res)
		else:
			await ctx.reply(res)
@аркадий.error
async def inform_error(ctx, error):
        await ctx.reply("> Чо надо, я бананы ем\n> И да, ты ведь не написал аргумент.\n> Команда вызова: аркадий хелпай")
	
bot.run(token)
