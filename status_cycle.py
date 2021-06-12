
import discord
from discord.ext import commands
from discord.ext.commands import Bot

# update Benne's status

class Status_Cycle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    if ctx.message.author.id in user_list:
        await ctx.send("This will now overwrite your last status request.")
    else:
        await ctx.send("This will now be added to the list.")
        user_list.append(ctx.message.author.id)
    channel = bot.get_channel(853107850217652234) #channel id here
    await channel.send('.activity ' + statustype + " " + status)
