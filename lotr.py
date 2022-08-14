from collections import Counter
import re
import pandas as pd
import matplotlib.pyplot as plt


# Вытаскиваем все расы, каунтером вытаскиваем ключи и количества.
# Ну и строим график bar по ключам и количествам.
def get_races_pie(data):
    race_data = data['Race'].to_numpy()
    counter = Counter(race_data)
    keys = counter.keys()
    values = counter.values()
    plt.bar(keys, values)
    plt.savefig('races.png')
    plt.show()


# Ставим индекс по расе, засовываем имена хоббитов в список.
def get_hobbit_families_bars(df):
    df = df.set_index(['Race'])
    names = df.loc['Hobbit']['Name'].to_numpy()
    # Тут фильтруем, убираем фамилии в скобочках.
    new_names = []
    for name in names:
        new_name = re.subn(r'\([^()]*\)', '', name)
        new_names.append(new_name[0])
    # Здесь выбираем только фамилии, если они есть.
    second_names = []
    for name in new_names:
        splitted_name = name.split()
        if len(splitted_name) == 2:
            second_names.append(splitted_name[1])
    # Так же, как и в расах, каунтером делаем ключи и количества и выводим пирог.
    counter = Counter(second_names)
    keys = counter.keys()
    values = counter.values()
    plt.figure(figsize=(10, 7))
    plt.pie(values, autopct='%1.0f%%', pctdistance=1.15)
    plt.legend(keys, bbox_to_anchor=(-0.3, 0.5), loc='center left')
    plt.savefig('second_names.png')
    plt.show()


# Делаем индексацию по расе, создаем датафрейм чисто с Эльфами
# сейвим в csv с отсутствием индексов (чтобы не было везде Elf)
def get_new_csv(df):
    df = df.set_index(['Race'])
    elves = df.loc['Elf']
    elves_df = pd.DataFrame(elves)
    elves_df.to_csv('elves.csv', index=False)



link = 'https://raw.githubusercontent.com/MokoSan/FSharpAdvent/master/Data/Characters.csv'
data = pd.read_csv(link)
dataframe = pd.DataFrame(data)
get_races_pie(data)
get_hobbit_families_bars(dataframe)
get_new_csv(dataframe)
