import discord
from discord.ext import commands
import asyncio

bot = commands.bot(command_prefix='/')

@bot.event
async def on_ready():
    print('Succees login to {0.user}'.format(bot))

async def playing():
    await bot.wait_until_ready()


