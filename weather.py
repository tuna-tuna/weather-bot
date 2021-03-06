import discord
import aiohttp
from wordlist import WordList

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
            date = date.replace('2022-', '')
            date = date.replace('-', '/')
            if date[:1] == '0':
                date = date.replace('0', '')
            weather: str = dayForecast['telop']
            weatherCode: str = dayForecast['image']['url']
            weatherCode = weatherCode.replace('https://www.jma.go.jp/bosai/forecast/img/', '')
            weatherCode = weatherCode.replace('.svg', '')
            if dayForecast['temperature']['max']['celsius'] == None:
                maxTemp: str = '--'
            else:
                maxTemp: str = dayForecast['temperature']['max']['celsius']
            if dayForecast['temperature']['min']['celsius'] == None:
                minTemp: str = '--'
            else:
                minTemp: str = dayForecast['temperature']['min']['celsius']
            chanceOfRain612: str = dayForecast['chanceOfRain']['T06_12']
            chanceOfRain1218: str = dayForecast['chanceOfRain']['T12_18']
            chanceOfRain1824: str = dayForecast['chanceOfRain']['T18_24']
            svgUrl: str = dayForecast['image']['url']
            dayForecastData = {
                'date': date,
                'weather': weather,
                'weatherCode': weatherCode,
                'maxTemp': maxTemp,
                'minTemp': minTemp,
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
        sunnyCode = ['100', '101', '102', '110']
        cloudyCode = ['200', '201', '202', '210', '212']
        rainyCode = ['300', '302', '313']
        forecastsData = await self.fetchForecasts()
        embed = discord.Embed(title='???????????????')
        weather: str = forecastsData['forecasts'][0]['weather']
        weatherCode: str = forecastsData['forecasts'][0]["weatherCode"]
        maxTemp: str = forecastsData['forecasts'][0]['maxTemp'] + '???'
        cor0612: str = forecastsData['forecasts'][0]['cor0612']
        cor1218: str = forecastsData['forecasts'][0]['cor1218']
        cor1824: str = forecastsData['forecasts'][0]['cor1824']
        thumbnailPath = './assets/' + weatherCode + '.png'
        fileName = weatherCode + '.png'
        attachmentPath = 'attachment://' + fileName
        file = discord.File(thumbnailPath, fileName)
        embed.set_thumbnail(url=attachmentPath)
        embed.add_field(name='```??????```', value=weather, inline=False)
        embed.add_field(name='```????????????```', value=maxTemp, inline=False)
        embed.add_field(name='```????????????```\n6???~12???', value=cor0612, inline=True)
        embed.add_field(name='----------\n12???~18???', value=cor1218, inline=True)
        embed.add_field(name='----------\n18???~24???', value=cor1824, inline=True)
        if weatherCode in sunnyCode:
            weatherStr = await WordList.getRandomMessage('Sunny', weather)
        elif weatherCode in cloudyCode:
            weatherStr = await WordList.getRandomMessage('Cloudy', weather)
        elif weatherCode in rainyCode:
            weatherStr = await WordList.getRandomMessage('Rainy', weather)
        embed.add_field(name='```?????????????????????```', value=f'{weatherStr}')
        return embed, file

    async def create3DaysEmbed(self):
        forecastsData = await self.fetchForecasts()
        embed = discord.Embed(title='3???????????????')
        for forecast in forecastsData['forecasts']:
            date: str = forecast['date']
            weather: str = forecast['weather']
            weatherCode: str = forecast['weatherCode']
            maxTemp: str = forecast['maxTemp'] + '???'
            minTemp: str = forecast['minTemp'] + '???'
            cor0612: str = forecast['cor0612']
            if cor0612 == '0%': cor0612 = ' 0%'
            cor1218: str = forecast['cor1218']
            if cor1218 == '0%': cor1218 = ' 0%'
            cor1824: str = forecast['cor1824']
            if cor1824 == '0%': cor1824 = ' 0%'
            embed.add_field(name=date, value=f'```??????: {weather}\n????????????: {minTemp}    ????????????: {maxTemp}\n????????????\n| 6~12???|12~18???|18~24???|\n|-------|-------|-------|\n|  {cor0612}  |  {cor1218}  |  {cor1824}  |```', inline=False)
        return embed
