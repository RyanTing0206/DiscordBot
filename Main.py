import discord
from discord.ext import commands


@bot.event
async def on_ready():
    print(">> Bot is online <<")

