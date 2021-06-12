import asyncio

import discord
from discord.ext import commands
from discord.ext import Bot
from discord import activity, tasks


# update Benne's status

class Status_Cycle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    status_list = []
    statustype_list = []
    user_list = []

    @Bot.command
    async def bennestatus(ctx):
        ctx.send(user_list)
        if ctx.message.author.id in user_list:
                
            ctx.send("What status type would you like? Options being: `Watching`, `Playing`, `Listening` and `Competing`")

        statustype_list.append()
        status_list.append()


    @tasks.loop(seconds=10.0)
    async def cycle(self):
        
        activity = discord.Activity(type=discord.ActivityType.statustype)
        bot = commands.Bot(activity=activity)

    
    
    
    def setup(bot):
        bot.add_cog(Status_Cycle(bot))
