import discord
from discord.ext import commands
import asyncio

bot = commands.bot(command_prefix='/')

@bot.event
async def on_ready():
    print('Succees login to {0.user}'.format(bot))

async def playing():
    await bot.wait_until_ready()

    status = [' /도움말 로 명령어를 확인해봐!', '{ }SERVERS | { }USERS'.format(len(bot.guilds), len(set(bot.get_all_members()))), '본 봇은 길드 전다'
