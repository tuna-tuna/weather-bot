import discord
import aiohttp

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
        forecastsData = await self.fetchForecasts()
        embed = discord.Embed(title='3日間の天気')
        for forecast in forecastsData['forecasts']:
            date: str = forecast['date']
            weather: str = forecast['weather']
            weatherCode: str = forecast['weatherCode']
            maxTemp: str = forecast['maxTemp'] + '℃'
            minTemp: str = forecast['minTemp'] + '℃'
            cor0612: str = forecast['cor0612']
            if cor0612 == '0%': cor0612 = ' 0%'
            cor1218: str = forecast['cor1218']
            if cor1218 == '0%': cor1218 = ' 0%'
            cor1824: str = forecast['cor1824']
            if cor1824 == '0%': cor1824 = ' 0%'
            embed.add_field(name=date, value=f'```天気: {weather}\n最低気温: {minTemp}    最高気温: {maxTemp}\n降水確率\n| 6~12時|12~18時|18~24時|\n|-------|-------|-------|\n|  {cor0612}  |  {cor1218}  |  {cor1824}  |```', inline=False)
        return embed
