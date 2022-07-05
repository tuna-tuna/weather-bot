import os
import discord
from discord.ext import commands, tasks
from weather import Weather
import datetime

# Asia/Tokyo
class JST(datetime.tzinfo):
    def __repr__(self):
        return self.tzname(self)

    def utcoffset(self, dt):
        # ローカル時刻とUTCの差分に等しいtimedeltaを返す
        return datetime.timedelta(hours=9)

    def tzname(self, dt):
        # タイムゾーン名を返す
        return 'Asia/Tokyo'

    def dst(self, dt):
        # 夏時間を返す。有効でない場合はtimedelta(0)を返す
        return datetime.timedelta(0)

tasktime = datetime.time(hour=6, minute=0, second=0, microsecond=0, tzinfo=JST())

class WeatherTask(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot
        self.weather = Weather()
        self.weatherTask.start()

    def cog_unload(self) -> None:
        self.weatherTask.cancel()

    async def weatherMorning(self):
        weatherChannel = self.bot.get_channel(int(os.environ['DISCORD_CHANNEL_ID']))
        embed, file = await self.weather.createTodaysEmbed()
        await weatherChannel.send(embed=embed, file=file)

    @tasks.loop(time=tasktime)
    async def weatherTask(self):
        await self.weatherMorning()
    
    @weatherTask.before_loop
    async def beforeWeatherTask(self):
        await self.bot.wait_until_ready()

def setup(bot: discord.Bot):
    bot.add_cog(WeatherTask(bot=bot))

