import os
import requests
api_url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/"
response = requests.get(api_url)
estados=response.json() 
data_dict = {}
for estado in estados: 
    if estado["regiao"]["nome"] not in data_dict:
        data_dict[estado["regiao"]["nome"]]=0
    data_dict[estado["regiao"]["nome"]]+=1
    
print(data_dict) 

os.mkdir("csv") 

f = open("csv/regioes.csv", "w")
f.write("Regiao|Qtd. Estados")
for key, value in data_dict.items(): 
    f.write(f"\n{key}|{value}") 
   
f.close()