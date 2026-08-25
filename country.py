import aiohttp

class gg:
    def __init__(self,city0):
        self.city0 = city0
        self.url = 'https://geocoding-api.open-meteo.com/v1/search'

    async def city1(self):
        async with aiohttp.ClientSession() as s:
            async with s.get(url=self.url,params={'name':self.city0,'count':3}) as res:
                data = await res.json()
                c1 = data['results'][0]['country']
                return f'Страна: {c1}'


