# #ЛР_2
# #Общее задание
# #1
# #линейный способ
# from sympy import*
# k,T,C,L = symbols('k C T L')
# C_ost=100000
# Am_lst=[]
# C_ost_lst=[]
# for i in range(5):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C: 100000, T:5, L:0})
#   Am_lst.append(round(Am.subs({C: 100000, T:5, L:0}), 2))
#   C_ost_lst.append(round(C_ost, 2))
# print( 'Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #2
# #способ уменьшаемого остатка
# Aj=0
# C_ost=100000
# Am_lst_2=[]
# C_ost_lst_2=[]
# for i in range(5):
#   Am = k * 1/T * (C - Aj)
#   C_ost -= Am.subs({C: 100000, T:5, k:2})
#   Am_lst_2.append(round(Am.subs({C: 100000, T:5, k:2}), 2))
#   Aj += Am
#   C_ost_lst_2.append(round(C_ost, 2))
# print ('Am_lst_2:', Am_lst_2)
# print ('C_ost_lst_2', C_ost_lst_2)

# #Контейнер табличного вывода
# import pandas as pd
# Y = range(1, 6)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# #3
# #линейный способ
# from sympy import *
# k, T, C, L = symbols('k T C L')
# C_ost = 30000
# Am_lst =[]
# C_ost_lst=[]
# for i in range(8):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C:30000, T:8, L:0})
#   Am_lst.append(round(Am.subs({C: 30000, T:8, L:0}),2))
#   C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #способ уменьшаемого остатка
# Aj=0
# C_ost = 30000
# Am_lst_2=[]
# C_ost_lst_2=[]
# for i in range(8):
#   Am = k*1/T*(C - Aj)
#   C_ost -= Am.subs({C:30000, T:8, k:2})
#   Am_lst_2.append(round(Am.subs({C:30000, T:8, k:2}), 2))
#   Aj += Am 
#   C_ost_lst_2.append(round(C_ost,2))
# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер табличного вывода
# import pandas as pd
# Y = range(1, 9)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# #визуализация
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
# plt.savefig('chart1.png')
# plt.figure()
# plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am2')
# plt.savefig('chart2.png')
# plt.figure()

# vals = Am_lst
# labels = [str(x) for x in range(1,9)]
# explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart3.png')
# plt.figure()

# vals =  Am_lst_2
# labels = [str(x) for x in range(1,9)]
# explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart4.png')
# plt.clf()
# plt.figure()


# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tframe = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
# tframe2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig('chart5.jpeg')
# plt.figure()
# plt.bar(tfame2['Y'], tfame2['Am_lst_2'])
# plt.savefig('chart6.jpeg')
# plt.figure()


# #ИНДИВИДУАЛЬНОЕ_ЗАДАНИЕ
# #линейный способ
# from sympy import *
# k, T, C, L = symbols('k T C L')
# C_ost = 40000
# Am_lst =[]
# C_ost_lst=[]
# for i in range(10):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C:40000, T:10, L:0})
#   Am_lst.append(round(Am.subs({C: 40000, T:10, L:0}),2))
#   C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #способ уменьшаемого остатка
# Aj=0
# C_ost = 40000
# Am_lst_2=[]
# C_ost_lst_2=[]
# for i in range(10):
#   Am = k*1/T*(C - Aj)
#   C_ost -= Am.subs({C:40000, T:10, k:2})
#   Am_lst_2.append(round(Am.subs({C:40000, T:10, k:2}), 2))
#   Aj += Am 
#   C_ost_lst_2.append(round(C_ost,2))
# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер табличного вывода
# import pandas as pd
# Y = range(1, 11)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# #визуализация
# plt.figure()
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
# plt.savefig('chart7.png')
# plt.figure()
# plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am2')
# plt.savefig('chart8.png')
# plt.figure()

# plt.figure()
# vals = Am_lst
# labels = [str(x) for x in range(1,11)]
# explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart9.png')
# plt.figure()

# plt.figure()
# vals =  Am_lst_2
# labels = [str(x) for x in range(1,11)]
# explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart10.png')
# plt.figure()
# plt.clf()


# plt.figure()
# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tframe = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
# tframe2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig('chart11.jpeg')
# plt.figure()
# plt.bar(tfame2['Y'], tfame2['Am_lst_2'])
# plt.savefig('chart12.jpeg')
# plt.figure()



#ЛР_3
#Общее задание
import os 
my_secret=os.environ['MY_SECRET']
print(my_secret)



#Задание_1_секреты_делала_с_Малаховой
import os 
my_secret=os.environ['SEC_Kuznetsova_1']
print(my_secret)

import os 
my_secret=os.environ['SEC_Kuznetsova_2']
print(my_secret)

import os 
my_secret=os.environ['SEC_Kuznetsova_3']
print(my_secret)

#Задание_2_берем код из индивидуальной части лр_2
#вариант 2 
#линейный способ
from sympy import *
k, T, C, L = symbols('k T C L')
C_ost = 70000 # изменение1 50000 на 70000 
Am_lst =[]
C_ost_lst=[]
for i in range(9):
  Am = (C-L)/T
  C_ost -= Am.subs({C:50000, T:9, L:0})
  Am_lst.append(round(Am.subs({C: 50000, T:9, L:0}),2))
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

#способ уменьшаемого остатка
Aj=0
C_ost = 50000
Am_lst_2=[]
C_ost_lst_2=[]
for i in range(9):
  Am = k*1/T*(C - Aj)
  C_ost -= Am.subs({C:50000, T:9, k:2})
  Am_lst_2.append(round(Am.subs({C:50000, T:9, k:2}), 2))
  Aj += Am 
  C_ost_lst_2.append(round(C_ost,2))
print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер табличного вывода
import pandas as pd
Y = range(1, 10)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
print(tfame)
print(tfame2)

#визуализация

import numpy as np
import matplotlib.pyplot as plt #что это значит? Ответ: это стандартный способ подключить инструменты для рисования графиков в Python. 
plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
plt.savefig('chart7.png')
plt.figure()
plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am2')
plt.savefig('chart8.png') # что это значит? Ответ: это команда для сохранения текущего графика в файл с именем 'chart8.png'. 
plt.figure()

plt.figure()
vals = Am_lst
labels = [str(x) for x in range(1,10)] # что это значит? Ответ:  это генератор списка, который создает список строковых представлений чисел от 1 до 9. 
explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
ax.axis("equal")
plt.savefig('chart9.png')
plt.figure()

plt.figure()
vals =  Am_lst_2
labels = [str(x) for x in range(1,10)]
explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
ax.axis("equal")
plt.savefig('chart10.png')
plt.figure()
plt.clf()


plt.figure()
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tframe = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
tframe2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])
plt.bar(tfame['Y'], tfame['Am_lst'])
plt.savefig('chart11.jpeg')
plt.figure()
plt.bar(tfame2['Y'], tfame2['Am_lst_2'])
plt.savefig('chart12.jpeg')
plt.figure()

# Проверил: Икрамов. Все верно.

#Задание 4 выполняла с Малаховой Дарьей.
#(что это значит?)
# На вопросы Малахова Д.С. ответила верно, 5/5. 



#ИНДИВИДУАЛЬНАЯ ЧАСТЬ ЛР_3

#КОНТЕЙНЕР РАСЧЁТА (микросервис защиты от несанкционированного доступа через сторонние сервисы)

import random
import pandas as pd
import matplotlib.pyplot as plt

# Список сторонних сервисов 
external_services = [
    "Google OAuth",
    "Facebook Login",
    "Payment Gateway",
    "Cloud Storage API",
    "CRM System",
    "Telegram Bot API",
    "Apple ID",
    "GitHub OAuth"
]

n = len(external_services)

# Генерация исходных данных
requests_count = []
token_valid = []
suspicious_ip = []
oauth_anomaly = []
rate_exceeded = []
token_reuse = []

for _ in range(n):
    requests_count.append(random.randint(1, 200))
    token_valid.append(random.choice([0, 1]))
    suspicious_ip.append(random.choice([0, 1]))
    oauth_anomaly.append(random.choice([0, 1]))
    rate_exceeded.append(random.choice([0, 1]))
    token_reuse.append(random.choice([0, 1]))

# Расчёт уровня риска НСД
risk_level = []
decision = []

for i in range(n):
    risk = 0
    if requests_count[i] > 100:
        risk += 1
    if token_valid[i] == 0:
        risk += 2
    if suspicious_ip[i] == 1:
        risk += 1
    if oauth_anomaly[i] == 1:
        risk += 2
    if rate_exceeded[i] == 1:
        risk += 1
    if token_reuse[i] == 1:
        risk += 2
    risk_level.append(risk)
    if risk >= 3:
        decision.append("BLOCK")
    else:
        decision.append("ALLOW")


# КОНТЕЙНЕР ТАБЛИЧНОГО ВЫВОДА

data = list(zip(
    range(1, n+1),
    external_services,
    requests_count,
    token_valid,
    suspicious_ip,
    oauth_anomaly,
    rate_exceeded,
    token_reuse,
    risk_level,
    decision
))

df = pd.DataFrame(data, columns=[
    "ID", "Сторонний сервис", "Запросы", "Токен валиден",
    "Подозрит. IP", "OAuth-аномалия", "Превышение частоты",
    "Повтор токена", "Риск НСД", "Решение"
])

#print("\n" + "="*80)
print("РЕЗУЛЬТАТЫ РАБОТЫ КОНТЕЙНЕРА БЕЗОПАСНОСТИ (защита от НСД через сторонние сервисы)")
#print("="*80)
print(df.to_string(index=False))
print("\nСтатистика решений:")
print(df["Решение"].value_counts())

# ==================================================
# КОНТЕЙНЕР ВИЗУАЛИЗАЦИИ (каждый график в отдельном файле)
# ==================================================
plt.style.use('ggplot')

# 1. Линейный график – количество запросов по сервисам
plt.figure(figsize=(10, 6))
plt.plot(df["ID"], df["Запросы"], marker='o', linestyle='-', color='blue')
plt.title("Запросы к сторонним сервисам")
plt.xlabel("ID сервиса")
plt.ylabel("Количество запросов")
plt.grid(True)
plt.savefig("chart_requests.png")
#plt.show()
plt.close()

# 2. Линейный график – уровень риска НСД
plt.figure(figsize=(10, 6))
plt.plot(df["ID"], df["Риск НСД"], marker='s', linestyle='-', color='red')
plt.title("Уровень риска несанкционированного доступа")
plt.xlabel("ID сервиса")
plt.ylabel("Риск (баллы)")
plt.grid(True)
plt.savefig("chart_risk.png")
#plt.show()
plt.close()

# 3. Круговая диаграмма решений (ALLOW / BLOCK)
plt.figure(figsize=(8, 8))
decision_counts = df["Решение"].value_counts()
labels = ["Разрешить (ALLOW)", "Заблокировать (BLOCK)"]
sizes = [decision_counts.get("ALLOW", 0), decision_counts.get("BLOCK", 0)]
colors = ['#66b3ff', '#ff6666']
explode = (0.05, 0.1)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
        shadow=True, explode=explode, colors=colors)
plt.title("Распределение решений контейнера")
plt.savefig("chart_pie.png")
#plt.show()
plt.close()

# 4. Гистограмма – риск по сервисам
plt.figure(figsize=(10, 6))
plt.bar(df["ID"], df["Риск НСД"], color='orange', edgecolor='black')
plt.title("Риск НСД для каждого стороннего сервиса")
plt.xlabel("ID сервиса")
plt.ylabel("Уровень риска")
plt.xticks(df["ID"])
plt.grid(axis='y')
plt.savefig("chart_risk_bars.png")
#plt.show()
plt.close()

# 5. Дополнительная гистограмма: суммарные срабатывания факторов риска
plt.figure(figsize=(10, 6))
risk_factors = df[["Токен валиден", "Подозрит. IP", "OAuth-аномалия",
                   "Превышение частоты", "Повтор токена"]].sum()
risk_factors.plot(kind='bar', color=['green', 'red', 'purple', 'orange', 'brown'])
plt.title("Суммарные срабатывания факторов риска по всем сервисам")
plt.ylabel("Количество случаев")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("risk_factors_sum.png")
#plt.show()
plt.close()

# print(" - chart_requests.png (запросы)")
# print(" - chart_risk.png (линия риска)")
# print(" - chart_pie.png (круговая диаграмма решений)")
# print(" - chart_risk_bars.png (гистограмма риска)")
# print(" - risk_factors_sum.png (факторы риска)")