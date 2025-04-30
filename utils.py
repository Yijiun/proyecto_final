#Leer los archivos dentro del folder

import json

def leer_json(nombre_archivo):
       with open(f'{nombre_archivo}.json', encoding="utf-8") as f:
            return json.load(f)
 