import requests, json
import sqlite3

con = sqlite3.connect("dados_temperatura.db")
cur = con.cursor()

id_cidade = input('Digite o woeid da cidade: ')
request = requests.get("https://api.hgbrasil.com/weather?woeid={0}", id_cidade)
data = json.loads(request.content)

temperatura = data['results']['temp']
date = data['results']['date']
time = data['results']['time']
desc = data['results']['description']
day_night = data['results']['currently']
umidade = data['results']['humidity']
velocidade_vento = data['results']['wind_speedy']
sunset = data['results']['sunset']
sunrise = data['results']['sunrise']

#Media Temperatura Maxima
sab_max = data['results']['forecast'][0]['max']
dom_max = data['results']['forecast'][1]['max']
seg_max = data['results']['forecast'][2]['max']
ter_max = data['results']['forecast'][3]['max']
qua_max = data['results']['forecast'][4]['max']
qui_max = data['results']['forecast'][5]['max']
sex_max = data['results']['forecast'][6]['max']
max_media = (sab_max + dom_max + seg_max + ter_max + qua_max + qui_max + sex_max)/7

#Media Temperatura Minima
sab_min = data['results']['forecast'][0]['min']
dom_min = data['results']['forecast'][1]['min']
seg_min = data['results']['forecast'][2]['min']
ter_min = data['results']['forecast'][3]['min']
qua_min = data['results']['forecast'][4]['min']
qui_min = data['results']['forecast'][5]['min']
sex_min = data['results']['forecast'][6]['min']
min_media = (sab_min + dom_min + seg_min + ter_min + qua_min + qui_min + sex_min)/7

cur.execute("""
    INSERT INTO Clima ('DataHora', 'Temperatura', 'Umidade', 'VelocidadeVento') VALUES
        (DATE('now'),?,?,?)""", (temperatura, umidade, velocidade_vento))

con.commit()

print('Temperatura:',temperatura, 'ºC')
print('Data e Hora:', date, time)
print('Descrição:', desc)
print('Data e Hora:', date, time)
print('Horário:', day_night)
print('Umidade:', umidade)
print('Velocidade do Vento:', velocidade_vento)
print('Nascer do sol:', sunrise)
print('Pôr do sol:', sunset)
print('Media temp. minima na semana:',min_media, 'ºC')
print('Media temp. maxima na semana:',max_media, 'ºC')