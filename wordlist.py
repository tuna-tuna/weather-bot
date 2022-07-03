import random

class WordList():
    @staticmethod
    async def getRandomMessage(weatherGenre: str, weather: str):
        randNum = random.randint(1, 3)
        if weatherGenre == 'Sundy':
            if randNum == 1:
                weatherStr = f'泣かないで、@ぼーたん。君が泣くと僕も悲しい。ほら、空をご覧。今日は{weather}。こんなにもいい天気だよ。'
                return weatherStr
            elif randNum == 2:
                weatherStr = f'ただ身を焦がすような日々。そこに残るは漠然とした危機。理由を求めて進むこの道。分かったことは、{weather}。\n@ぼーたん「そうか、今日は晴れか」'
                return weatherStr
            elif randNum == 3:
                weatherStr = f'太陽に手をかざす@ぼーたん。そこに見えるは、真っ赤に流れる血潮。今この瞬間、{weather}。\nみんな生きている。友達なんだ。'
                return weatherStr
        elif weatherGenre == 'Cloudy':
            if randNum == 1:
                weatherStr = f'もやもやが胸の一面を埋め尽くす。0か100かはっきりしろ。中途半端だと何もなせない。{weather}。そう言って@ぼーたんは、大きいものを乾燥機にかけ、小さいものは部屋に干した。'
                return weatherStr
            elif randNum == 2:
                weatherStr = f'曇り空を指差して@ぼーたん はたった一言。「お皿だ。」{weather}。これは、空を消した男の話。'
                return weatherStr
            elif randNum == 3:
                weatherStr = f''