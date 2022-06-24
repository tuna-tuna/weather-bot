import discord
from discord.commands import slash_command
from discord.ext import commands
from weather import Weather

weatherInst = Weather()

class Weather(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @slash_command()
    async def weather(self, ctx:discord.ApplicationContext):
        await ctx.defer(ephemeral=True)
        embed, file = await weatherInst.createTodaysEmbed()
        await ctx.respond(file=file, embed=embed)

def setup(bot: discord.Bot):
    bot.add_cog(Weather(bot))