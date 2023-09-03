import discord
from discord.ext import commands
from logic import detect_cat
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')


@bot.command()
async def check_cat(ctx):
    if ctx.message.attachments:
        await ctx.send(f'Фото получено.')
        for attachment in ctx.message.attachments:
            name = attachment.filename
            await attachment.save(f"img/{name}")
            class_name = detect_cat(f"img/{name}", 'keras_model.h5', 'labels.txt')[0]
            await ctx.send(f'Это порода: {class_name}')
    else:
        await ctx.send(f'Фото НЕ получено. Попробуйте прикрепить фото и попробовать снова.')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        await ctx.send(f'Фото получено.')
        for attachment in ctx.message.attachments:
            name = attachment.filename
            await attachment.save(f"img/{name}")
    else:
        await ctx.send(f'Фото НЕ получено. Попробуйте прикрепить фото и попробовать снова.')
bot.run("ВАШ ТОКЕН")




