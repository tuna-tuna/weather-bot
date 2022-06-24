import discord
import aiohttp
import ssl

class Weather():
    def __init__(self) -> None:
        self.session = aiohttp.ClientSession(headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}, connector=aiohttp.TCPConnector(verify_ssl=False))

    async def fetchForecasts(self):
        #Only For Task
        #Call 5:50
        baseUrl = 'https://weather.tsukumijima.net/api/forecast/city/'
        areaCode = '140010'
        url = baseUrl + areaCode
        async with self.session.get(url=url) as r:
            data = await r.json()
        updateTime: str = data['publicTimeFormatted']
        forecastsData = {}
        forecastsData['updateTime'] = updateTime
        forecasts = []
        for dayForecast in data['forecasts']:
            date: str = dayForecast['date']
            weather: str = dayForecast['telop']
            weatherCode: str = dayForecast['image']['url']
            weatherCode = weatherCode.replace('https://www.jma.go.jp/bosai/forecast/img/', '')
            weatherCode = weatherCode.replace('.svg', '')
            if dayForecast['temperature']['max']['celsius'] == None:
                maxTemp: str = '--'
            else:
                maxTemp: str = dayForecast['temperature']['max']['celsius']
            chanceOfRain612: str = dayForecast['chanceOfRain']['T06_12']
            chanceOfRain1218: str = dayForecast['chanceOfRain']['T12_18']
            chanceOfRain1824: str = dayForecast['chanceOfRain']['T18_24']
            svgUrl: str = dayForecast['image']['url']
            dayForecastData = {
                'date': date,
                'weather': weather,
                'weatherCode': weatherCode,
                'maxTemp': maxTemp,
                'cor0612': chanceOfRain612,
                'cor1218': chanceOfRain1218,
                'cor1824': chanceOfRain1824,
                'svgUrl': svgUrl
            }
            forecasts.append(dayForecastData.copy())
        forecastsData['forecasts'] = forecasts
        return forecastsData

    async def createTodaysEmbed(self):
        #Only For Task
        forecastsData = await self.fetchForecasts()
        embed = discord.Embed(title='今日の天気')
        weather: str = forecastsData['forecasts'][0]['weather']
        weatherCode: str = forecastsData['forecasts'][0]["weatherCode"]
        maxTemp: str = forecastsData['forecasts'][0]['maxTemp'] + '℃'
        cor0612: str = forecastsData['forecasts'][0]['cor0612']
        cor1218: str = forecastsData['forecasts'][0]['cor1218']
        cor1824: str = forecastsData['forecasts'][0]['cor1824']
        thumbnailPath = './assets/' + weatherCode + '.png'
        fileName = weatherCode + '.png'
        attachmentPath = 'attachment://' + fileName
        file = discord.File(thumbnailPath, fileName)
        embed.set_thumbnail(url=attachmentPath)
        embed.add_field(name='天気', value=weather, inline=False)
        embed.add_field(name='最高気温', value=maxTemp, inline=False)
        embed.add_field(name='降水確率\n6時~12時', value=cor0612, inline=True)
        embed.add_field(name='----------\n12時~18時', value=cor1218, inline=True)
        embed.add_field(name='----------\n18時~24時', value=cor1824, inline=True)
        return embed, file

    async def create3DaysEmbed(self):
        return
