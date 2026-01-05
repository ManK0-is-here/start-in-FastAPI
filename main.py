from fastapi import FastAPI
from pydantic import Field, BaseModel, field_validator
from utils import *
import os
from typing import Optional

# Получаем путь к JSON
path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'students.json')


app = FastAPI()

# data = {
# "0": "Камень",
# "1": "Нет",
# "2": "Муравей-прыгун (Myrmecia pilosula, самки)",
# "3": "Нет",
# "4": "Комарик (Cricotopus sylvestris)",
# "5": "Нет",
# "6": "Комар желтой лихорадки (Aedes aegypti)",
# "7": "Индийский мунтжак (Muntiacus muntjak, самцы)",
# "8": "Дрозофила (Drosophila melanogaster)",
# "9": "Нет",
# "10": "Болотный валлаби (Wallabia bicolor, самки)",
# "11": "Болотный валлаби (Wallabia bicolor, самцы)",
# "12": "Домовая муха (Musca domestica)",
# "13": "Нет",
# "14": "Нет",
# "15": "Нет",
# "16": "Голубь (Columbidae)",
# "17": "Чесоточный клещ (Sarcoptes scabiei, самцы)",
# "18": "Чесоточный клещ (Sarcoptes scabiei, самки)",
# "19": "Нет",
# "20": "Красный кенгуру (Macropus rufus)",
# "21": "Нет",
# "22": "Щетинохвостая скальная валлаби (Brush-tailed Rock-wallaby)",
# "23": "Таракан (Periplaneta americana, самцы?)",
# "24": "Улитка (Snail)",
# "25": "Нет",
# "26": "Лягушка (British frog)",
# "27": "Нет",
# "28": "Нет",
# "29": "Нет",
# "30": "Жираф (Giraffa camelopardalis)",
# "31": "Нет",
# "32": "Медоносная пчела (Apis mellifera, самки)",
# "33": "Нет",
# "34": "Красная лисица (Vulpes vulpes)",
# "35": "Нет",
# "36": "Земляной червь (Lumbricus terrestris)",
# "37": "Нет",
# "38": "Кошка (Felis catus)",
# "39": "Нет",
# "40": "Мышь (Mus musculus)",
# "41": "Нет",
# "42": "Крыса (Rattus norvegicus)",
# "43": "Нет",
# "44": "Кролик (Oryctolagus cuniculus)",
# "45": "Нет",
# "46": "Человек (Homo sapiens)",
# "47": "Нет",
# "48": "Шимпанзе (Pan troglodytes)"
# }

# @app.post("/hromo")
# def api_sum(first_value: int, two_value: int) -> str:

#     sum_value = first_value + two_value

#     if str(sum_value) in data and data[str(sum_value)] != "Нет":
#         return data[str(sum_value)]
#     elif sum_value > 48:
#         return "Ты за рамки то не выходи"
    
#     return "Нет животного с таким количетвом хромосом, возможно это ты)"

# @app.post("/grade")
# def pls_grade(grade: int) -> str:
#     if grade == 10:
#         return "Спасибо за оценку"
#     return "Ты даун сам себе ставить заниженную оценку?"


@app.get("/students")
def get_all_students():
    return json_to_dict_list(path_to_json)