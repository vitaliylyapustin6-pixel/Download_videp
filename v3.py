import requests

# Специальная ссылка на простое погодное API для города Измаил (формат JSON)
url = "https://wttr.in/Izmail?format=j1"

# Делаем запрос к сайту
response = requests.get(url)

# Проверяем, всё ли прошло успешно
if response.status_code == 200:
    # Превращаем ответ сервера в удобный словарь Python
    data = response.json()
    
    # Достаем текущую температуру из словаря
    # В этом API текущая погода лежит в ключе 'current_condition'
    current_temp = data['current_condition'][0]['temp_C']
    
    print(f"Сейчас в Измаиле: {current_temp} °C")
else:
    print("Не удалось получить погоду :(")