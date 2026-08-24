import aiohttp
import asyncio

class selff:
    def __init__(self,city):
        self.city = city
        self.url = 'https://geocoding-api.open-meteo.com/v1/search'

    async def get(self):
        async with aiohttp.ClientSession() as s:
            async with s.get(url=self.url,params={'name': self.city,'count': 3}) as res:
                    data = await res.json()
                    c = data['results'][0]['population']
                    return f'Столько людей проживают в {self.city}: {c}'

async def main():
    R = selff('Odesa')
    R1 = selff('Kyiv')
    R2 = selff('Shanghai')

    res = await R.get()
    res1 = await R1.get()
    res2 = await R2.get()

    print(res)
    print(res1)
    print(res2)


asyncio.run(main())