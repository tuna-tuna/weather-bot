import discord
import os

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)
TOKEN = os.environ['DISCORD_TOKEN']

@bot.event
async def on_ready():
    print('Ready')

if __name__ == '__main__':
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')
    bot.run(TOKEN)