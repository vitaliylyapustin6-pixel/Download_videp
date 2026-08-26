import aiohttp

class gg:
    def __init__(self,city0):
        self.city0 = city0
        self.url = 'https://geocoding-api.open-meteo.com/v1/search'

    async def city1(self):
        # Создаем сеанс
        async with aiohttp.ClientSession() as s:
            # Запрос на сервер
            async with s.get(url=self.url,params={'name':self.city0,'count':3}) as res:
                # Проверка если города не будет 
                try:
                    # Получаем данные с сервера и конвертируем в json формат
                    data = await res.json()
                    # Достем значение которое нам надо
                    c1 = data['results'][0]['country']
                    return f'Страна: {c1}'
                except Exception as e:
                    return f'Мы не смогли найти страну'

