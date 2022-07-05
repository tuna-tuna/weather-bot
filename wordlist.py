import random

class WordList():
    @staticmethod
    async def getRandomMessage(weatherGenre: str, weather: str) -> str:
        randNum = random.randint(1, 3)
        if weatherGenre == 'Sunny':
            if randNum == 1:
                weatherStr = f'泣かないで、@ぼーたん。君が泣くと僕も悲しい。ほら、空をご覧。今日は{weather}。こんなにもいい天気だよ。'
            elif randNum == 2:
                weatherStr = f'ただ身を焦がすような日々。そこに残るは漠然とした危機。理由を求めて進むこの道。分かったことは、{weather}。\n@ぼーたん「そうか、今日は晴れか」'
            elif randNum == 3:
                weatherStr = f'太陽に手をかざす@ぼーたん。そこに見えるは、真っ赤に流れる血潮。今この瞬間、{weather}。\nみんな生きている。友達なんだ。'
        elif weatherGenre == 'Cloudy':
            if randNum == 1:
                weatherStr = f'もやもやが胸の一面を埋め尽くす。0か100かはっきりしろ。中途半端だと何もなせない。{weather}。そう言って@ぼーたんは、大きいものを乾燥機にかけ、小さいものは部屋に干した。'
            elif randNum == 2:
                weatherStr = f'曇り空を指差して@ぼーたん はたった一言。「お皿だ。」{weather}。これは、空を消した男の話。'
            elif randNum == 3:
                weatherStr = f'@ぼーたん、俯いたままじゃくもりのままだよ。前を向いて、君は太陽なんだから。本日はそんなぼーたんについてです。表面は6000°、中心部は1600万°、直径139万km、距離1億5000万km。君は…こんなにも遠いんだね…'
        elif weatherGenre == 'Rainy':
            if randNum == 1:
                weatherStr = f'@ぼーたんは大いなる事をされるかたで、測り知れない、その不思議なみわざは数えがたい。{weather}。彼は世界を分かち、グラビティウェルをした。(旧約青書5章9節)'
            elif randNum == 2:
                weatherStr = f'あの日。そう{weather}の日。@ぼーたんは人の悪意を憂い涙した。涙は地を這い、大きな奔流となり、大洪水を起こした。これが本当の『創青記』である。'
            elif randNum == 3:
                weatherStr = f'そんな装備で大丈夫か？\n@ぼーたん「大丈夫だ問題ない」\n{weather}\n@ぼーたん「1番いい傘を頼む」'
        return weatherStr