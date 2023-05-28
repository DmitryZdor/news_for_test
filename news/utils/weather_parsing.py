import json

def pars():
    with open('weather.txt', 'r', encoding='utf-8') as file:
        data = json.load(file)



    print('Населенный пункт {}'.format(data['name']))
    print('Температура воздуха {} С'.format(data['main']['temp']))
    print('Влажность воздуха {} %'.format(data['main']['humidity']))
    print('Атмосферное давление {} мм. рт. с.'.format(round(data['main']['pressure']/1.333, 2)))
    print('Направление ветра {} градусов'.format(data['wind']['deg']))
    print('Скорость ветра {} м/с'.format(data['wind']['speed']))

