import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '/')

@bot.event
async def on_ready():
    
    print(">> Bot is online <<")

    bot.run('ODU0Njg5MzY5MzEzNzcxNTcw.YMnlgQ.8XhVSLVhNi9PlH-B0Ux4E-7eIOs')